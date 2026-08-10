#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ACTIVE_CHAPTERS = [
    ("Kapitel 1", "07-experimentutkast/kapitel-01", [
        "E001-Forsta-blinket.md",
        "E002-LED-med-egen-rytm.md",
        "E003-Tva-LED-turas-om.md",
        "E005-Polisljus.md",
        "E004-Mini-trafikljus.md",
    ]),
    ("Kapitel 2", "07-experimentutkast/kapitel-02", [
        "E007-LED-stafett.md",
        "E008-Rinnande-ljus.md",
        "E011-RGB-tre-farger-i-en-LED.md",
        "E012-Fargblandaren.md",
        "E013-Regnbagslampan.md",
        "E014-Humorlampan.md",
        "E015-Dimbar-LED.md",
        "E016-Andande-ljus.md",
    ]),
]

REQUIRED_PATHS = [
    "README.md",
    "00-projektstyrning/00-START-HAR-VID-FORTSATT-PRODUKTION.md",
    "00-projektstyrning/02-Status-och-beslutslogg.md",
    "04-experimentbank/01-Experimentbank-E001-E025.csv",
    "06-kapitelstruktur/10-Kapitel-01-Kom-igang.md",
    "06-kapitelstruktur/11-Kapitel-02-LED-och-PWM.md",
    "08-illustrationer-och-kopplingar/generated",
    "publishing/metadata.yaml",
    "publishing/epub.css",
    "scripts/build_book.py",
]

MARKERS = [
    "TODO",
    "FIXME",
    "XXX",
    "<<",
    ">>",
    "[[",
    "]]",
]


def error(errors: list[str], message: str) -> None:
    errors.append(message)
    print(f"ERROR: {message}", file=sys.stderr)


def parse_simple_yaml(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        values[key.strip()] = value
    return values


def validate_image_links(root: Path, md_path: Path, errors: list[str]) -> None:
    text = md_path.read_text(encoding="utf-8")
    for match in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", text):
        target = match.group(1).split("#", 1)[0]
        if re.match(r"^[a-z]+://", target):
            continue
        path = (md_path.parent / target).resolve()
        try:
            path.relative_to(root.resolve())
        except ValueError:
            error(errors, f"{md_path.relative_to(root)} har bildlänk utanför projektet: {target}")
            continue
        if not path.exists():
            error(errors, f"{md_path.relative_to(root)} saknar bildfil: {target}")


def validate_markdown_links(root: Path, errors: list[str]) -> None:
    for md_path in root.rglob("*.md"):
        text = md_path.read_text(encoding="utf-8")
        for match in re.finditer(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
            target = match.group(1).split("#", 1)[0]
            if not target or re.match(r"^[a-z]+://", target) or target.startswith("mailto:"):
                continue
            # Skip generated sandbox-like references in notes if any.
            if target.startswith("sandbox:"):
                continue
            path = (md_path.parent / target).resolve()
            try:
                path.relative_to(root.resolve())
            except ValueError:
                continue
            if not path.exists():
                error(errors, f"{md_path.relative_to(root)} saknar länkad fil: {target}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors: list[str] = []

    for rel in REQUIRED_PATHS:
        path = root / rel
        if not path.exists():
            error(errors, f"Obligatorisk sökväg saknas: {rel}")

    metadata_path = root / "publishing/metadata.yaml"
    if metadata_path.exists():
        metadata = parse_simple_yaml(metadata_path)
        for key in ["title", "author", "language"]:
            if not metadata.get(key):
                error(errors, f"publishing/metadata.yaml saknar värde för '{key}'.")
        if metadata.get("title") != "ESP32 Experimentbok":
            error(errors, "Metadatafältet title matchar inte projektets fastställda titel.")
        if metadata.get("author") != "Erland Lindmark":
            error(errors, "Metadatafältet author matchar inte projektets fastställda författare.")

    active_ids: list[str] = []
    for chapter_name, folder_rel, files in ACTIVE_CHAPTERS:
        folder = root / folder_rel
        if not folder.exists():
            error(errors, f"{chapter_name}: katalog saknas: {folder_rel}")
            continue
        for filename in files:
            path = folder / filename
            if not path.exists():
                error(errors, f"{chapter_name}: aktivt manus saknas: {folder_rel}/{filename}")
                continue
            text = path.read_text(encoding="utf-8")
            stripped = text.strip()
            if not stripped:
                error(errors, f"{path.relative_to(root)} är tom.")
                continue
            first_line = stripped.splitlines()[0].strip()
            id_match = re.match(r"^(E\d{3})-", filename)
            expected_id = id_match.group(1) if id_match else filename[:4]
            active_ids.append(expected_id)
            if not re.match(rf"^#\s+{expected_id}\s+[–-]\s+.+", first_line):
                error(errors, f"{path.relative_to(root)} har fel H1-format; väntat '# {expected_id} – Titel'.")
            for marker in MARKERS:
                if marker in text:
                    error(errors, f"{path.relative_to(root)} innehåller arbetsmarkören {marker}.")
            validate_image_links(root, path, errors)

    # E009/E010 får finnas som arkiv/bonus, men ska inte vara aktiva i exportordningen.
    for inactive in ["E009", "E010"]:
        if inactive in active_ids:
            error(errors, f"{inactive} är markerat som aktivt trots att experimentet är parkerat.")

    validate_markdown_links(root, errors)

    if errors:
        print(f"\nValidation failed: {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(
        "OK: projektvalidering godkänd. "
        f"{len(active_ids)} aktiva experiment: {', '.join(active_ids)}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
