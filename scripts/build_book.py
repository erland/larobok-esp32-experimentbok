#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PANDOC_VERSION = "3.1.11.1"

ACTIVE_CHAPTERS = [
    ("Kapitel 1 – Kom igång", "07-experimentutkast/kapitel-01", [
        "E001-Forsta-blinket.md",
        "E002-LED-med-egen-rytm.md",
        "E003-Tva-LED-turas-om.md",
        "E005-Polisljus.md",
        "E004-Mini-trafikljus.md",
    ]),
    ("Kapitel 2 – LED, PWM och färg", "07-experimentutkast/kapitel-02", [
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

CALLOUT_LABELS = {
    "Vuxenkoll", "Byggtips", "Mikrokoll", "Första kontrollen", "Titta noga", "OBS", "Tips"
}

PDF_CSS = r"""
@page {
  size: A4;
  margin: 17mm 17mm 19mm 18mm;
  @bottom-center {
    content: counter(page);
    font-family: "DejaVu Sans", Arial, sans-serif;
    font-size: 9pt;
    color: #666;
  }
}
html, body {
  font-family: "DejaVu Sans", Arial, sans-serif;
  font-size: 12.8pt;
  line-height: 1.48;
  color: #222;
  background: white;
}
.cover {
  page-break-after: always;
  min-height: 235mm;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  border: 3px solid #1f6688;
  border-radius: 14px;
  padding: 20mm;
  background: #f5fbff;
}
.cover h1 {
  font-size: 38pt;
  line-height: 1.1;
  margin: 0 0 12mm 0;
  color: #164c67;
}
.subtitle {
  font-size: 20pt;
  font-weight: 700;
  margin: 0 0 8mm 0;
}
.cover-meta {
  font-size: 15pt;
  margin: 0 0 8mm 0;
}
.cover-small {
  font-size: 10.5pt;
  color: #555;
  max-width: 140mm;
  margin: 0 auto;
}
.pagebreak {
  page-break-after: always;
}
.experiment-start {
  page-break-before: always;
}
h1, h2, h3, h4 {
  color: #173f56;
  line-height: 1.22;
  margin-top: 1.3em;
  margin-bottom: 0.55em;
  page-break-after: avoid;
}
h1 {
  font-size: 28pt;
  border-bottom: 3px solid #1f6688;
  padding-bottom: 4mm;
  margin-top: 0;
}
h2 {
  font-size: 18pt;
  border-bottom: 1px solid #b7d7e5;
  padding-bottom: 2mm;
}
h3 {
  font-size: 15pt;
}
p {
  margin: 0 0 0.8em 0;
}
ul, ol {
  margin-top: 0.2em;
  margin-bottom: 0.9em;
}
li {
  margin-bottom: 0.2em;
}
img {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 5mm auto 2.5mm auto;
  page-break-inside: avoid;
}
em {
  color: #555;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin: 5mm 0 7mm 0;
  font-size: 10.5pt;
  page-break-inside: avoid;
}
th, td {
  border: 1.4px solid #8aaebe;
  padding: 2.4mm 2.2mm;
  vertical-align: top;
}
th {
  background: #eaf5fa;
  font-weight: 700;
}
pre, code {
  font-family: "DejaVu Sans Mono", "Courier New", monospace;
}
pre {
  background: #f3f3f3;
  border: 1px solid #cfcfcf;
  border-left: 5px solid #1f6688;
  border-radius: 5px;
  padding: 3mm 3.2mm;
  font-size: 9.5pt;
  line-height: 1.35;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  page-break-inside: avoid;
}
code {
  background: #f1f1f1;
  border-radius: 3px;
  padding: 0.2mm 0.8mm;
  font-size: 0.92em;
}
pre code {
  background: transparent;
  padding: 0;
}
.callout, .insight {
  border-radius: 8px;
  margin: 4mm 0 5mm 0;
  padding: 3.2mm 4mm;
  page-break-inside: avoid;
}
.callout {
  border-left: 6px solid #2e7d32;
  background: #eef8ef;
}
.callout-title {
  font-weight: 700;
  color: #215a25;
  margin-bottom: 1mm;
}
.insight {
  border-left: 6px solid #7b519d;
  background: #f5eef9;
  font-weight: 700;
}
.chapter-intro {
  font-size: 13pt;
  background: #eef8ff;
  border-left: 5px solid #1f6688;
  padding: 4mm;
  margin: 4mm 0 6mm 0;
}
hr {
  border: none;
  border-top: 1px solid #c8dbe3;
  margin: 7mm 0;
}
"""


def simple_metadata(path: Path) -> dict[str, str]:
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


def pandoc_version() -> str:
    result = subprocess.run(["pandoc", "--version"], text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError("Pandoc finns inte i PATH.")
    first = result.stdout.splitlines()[0]
    match = re.search(r"pandoc\s+([0-9][^\s]*)", first)
    return match.group(1) if match else first


def transform_markdown(md: str, root: Path) -> str:
    md = md.replace("../../08-illustrationer-och-kopplingar/", str(root / "08-illustrationer-och-kopplingar") + "/")

    lines = md.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^> \*\*([^:*]+):\*\*\s*(.*)$", line)
        if m and m.group(1) in CALLOUT_LABELS:
            label = m.group(1)
            body_lines = [m.group(2).strip()]
            i += 1
            while i < len(lines) and lines[i].startswith(">"):
                body_lines.append(lines[i].lstrip("> ").strip())
                i += 1
            body = "\n".join([x for x in body_lines if x])
            out.append(f'<div class="callout"><div class="callout-title">{label}</div><div class="callout-body">{body}</div></div>')
            continue
        if line.startswith("> "):
            quote_lines = [line[2:].strip()]
            i += 1
            while i < len(lines) and lines[i].startswith("> "):
                quote_lines.append(lines[i][2:].strip())
                i += 1
            body = " ".join([x for x in quote_lines if x])
            out.append(f'<div class="insight">{body}</div>')
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def build_combined(root: Path, metadata: dict[str, str], *, for_pdf: bool) -> str:
    title = metadata.get("title", "ESP32 Experimentbok")
    subtitle = metadata.get("subtitle", "")
    author = metadata.get("author", "Erland Lindmark")

    if for_pdf:
        parts = [f"""---
title: "{title}"
author: "{author}"
lang: sv-SE
---

<div class="cover">
  <h1>{title}</h1>
  <p class="subtitle">{subtitle or "Preview"}</p>
  <p class="cover-meta">Kapitel 1 och Kapitel 2</p>
  <p class="cover-small">Automatiskt genererad PDF från projektets kanoniska Markdown-filer.</p>
</div>

<div class="pagebreak"></div>

# Innehåll i denna export

**Kapitel 1 – Kom igång**

- E001 – Första blinket
- E002 – LED med egen rytm
- E003 – Två LED turas om
- E005 – Polisljus
- E004 – Mini-trafikljus

**Kapitel 2 – LED, PWM och färg**

- E007 – LED-stafett
- E008 – Rinnande ljus
- E011 – RGB: tre färger i en LED
- E012 – Färgblandaren
- E013 – Regnbågslampan
- E014 – Humörlampan
- E015 – Dimbar LED
- E016 – Andande ljus

<div class="pagebreak"></div>
"""]
    else:
        parts = [f"""---
title: "{title}"
author: "{author}"
lang: sv-SE
---

# {title} {{.unnumbered}}

<div class="title-page">
  <p class="book-title">{title}</p>
  <p class="subtitle">{subtitle}</p>
  <p class="author">{author}</p>
</div>
"""]

    for chapter_title, folder_rel, filenames in ACTIVE_CHAPTERS:
        parts.append(f"\n# {chapter_title}\n")
        if for_pdf:
            parts.append('<div class="chapter-intro">Detta kapitel ingår i den automatiska bokexporten.</div>\n')
        for filename in filenames:
            src = root / folder_rel / filename
            if for_pdf:
                parts.append('\n<div class="experiment-start"></div>\n')
            parts.append(transform_markdown(src.read_text(encoding="utf-8"), root))
            parts.append("\n")
    return "\n\n".join(parts)


def run_weasyprint(html: Path, pdf: Path) -> None:
    explicit = os.environ.get("WEASYPRINT_BIN")
    candidates: list[list[str]] = []
    if explicit:
        candidates.append([explicit, str(html), str(pdf)])
    candidates.extend([
        ["weasyprint", str(html), str(pdf)],
        ["/opt/pyvenv/bin/weasyprint", str(html), str(pdf)],
        [sys.executable, "-m", "weasyprint", str(html), str(pdf)],
    ])

    last_error: Exception | None = None
    for cmd in candidates:
        try:
            if shutil.which(cmd[0]) or Path(cmd[0]).exists() or cmd[0] == sys.executable:
                subprocess.run(cmd, check=True)
                return
        except Exception as exc:
            last_error = exc
    raise RuntimeError(
        "WeasyPrint kunde inte köras. I GitHub Actions installeras WeasyPrint i en venv "
        "och sökvägen skickas via WEASYPRINT_BIN."
    ) from last_error


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--formats", default="epub,pdf")
    parser.add_argument("--name", default="esp32-experimentbok")
    parser.add_argument("--allow-pandoc-version-mismatch", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    actual_pandoc = pandoc_version()
    if actual_pandoc != PANDOC_VERSION and not args.allow_pandoc_version_mismatch:
        raise RuntimeError(
            f"Pandoc-version {actual_pandoc} matchar inte låst version {PANDOC_VERSION}. "
            "Använd --allow-pandoc-version-mismatch lokalt om du bara vill provbygga."
        )

    metadata = simple_metadata(root / "publishing/metadata.yaml")
    formats = {f.strip().lower() for f in args.formats.split(",") if f.strip()}

    with tempfile.TemporaryDirectory(prefix="esp32-book-build-") as tmp_str:
        tmp = Path(tmp_str)

        if "epub" in formats:
            epub_md = tmp / "book_epub.md"
            epub_md.write_text(build_combined(root, metadata, for_pdf=False), encoding="utf-8")
            epub_out = output_dir / f"{args.name}.epub"
            cmd = [
                "pandoc",
                str(epub_md),
                "--from", "markdown+pipe_tables+fenced_code_blocks+raw_html",
                "--to", "epub3",
                "--standalone",
                "--toc",
                "--toc-depth", "2",
                "--css", str(root / "publishing/epub.css"),
                "--metadata-file", str(root / "publishing/metadata.yaml"),
                "-o", str(epub_out),
            ]
            subprocess.run(cmd, check=True)
            print(f"OK: EPUB skapad: {epub_out}")

        if "pdf" in formats:
            pdf_md = tmp / "book_pdf.md"
            html = tmp / "book_pdf.html"
            css = tmp / "pdf.css"
            css.write_text(PDF_CSS, encoding="utf-8")
            pdf_md.write_text(build_combined(root, metadata, for_pdf=True), encoding="utf-8")
            subprocess.run([
                "pandoc",
                str(pdf_md),
                "--from", "markdown+pipe_tables+fenced_code_blocks+raw_html",
                "--to", "html5",
                "--standalone",
                "--metadata", f"title={metadata.get('title', 'ESP32 Experimentbok')}",
                "--css", str(css),
                "-o", str(html),
            ], check=True)
            pdf_out = output_dir / f"{args.name}.pdf"
            run_weasyprint(html, pdf_out)
            print(f"OK: PDF skapad: {pdf_out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
