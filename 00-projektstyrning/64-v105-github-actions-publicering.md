# v105 – GitHub Actions för validering, preview och release

Denna version inför GitHub Actions-konceptet från det bifogade publiceringskitet, anpassat till ESP32 Experimentbokens faktiska struktur.

## Tillagda kataloger och filer

`.github/` ligger i repositoryroten, på samma nivå som `README.md`.

Tillagt:

- `.github/workflows/01-validate.yml`
- `.github/workflows/02-build-preview.yml`
- `.github/workflows/03-release.yml`
- `scripts/validate_project.py`
- `scripts/build_book.py`
- `publishing/metadata.yaml`
- `publishing/epub.css`
- `publishing/build-notes.md`

## Workflow-koncept

### Validate

Körs på pull request och push till `main` när relevanta projektfiler ändras.

Kontrollerar bland annat:

- obligatoriska projektfiler,
- aktiv experimentordning,
- H1-format,
- saknade bildreferenser,
- parkerade E009/E010 som inte ska vara aktiva,
- metadata.

### Build Preview

Körs manuellt med `workflow_dispatch`.

Bygger:

- `esp32-experimentbok.epub`
- `esp32-experimentbok.pdf`

Laddar upp båda i ett gemensamt artifact:

- `esp32-experimentbok-preview`

### Release

Körs på taggar `v*`.

Bygger EPUB och PDF och laddar upp dem som separata GitHub Release assets.

## Anpassning från referenskitet

Referenskitet kom från ett romanprojekt. Detta projekt är en illustrerad experimentbok. Därför är byggscriptet anpassat så att:

- aktiv experimentordning används i stället för romanens numeriska kapitelmönster,
- PDF byggs via Pandoc HTML + WeasyPrint för att hantera SVG-bilder, tabeller och kodblock,
- EPUB byggs via Pandoc EPUB3,
- E009 och E010 hålls parkerade och exporteras inte som aktiva experiment.

## Kvar att verifiera i GitHub

- Att `actions/checkout@v6`, `actions/upload-artifact@v7` och Pandoc setup fungerar i valt repository.
- Att Ubuntu-runnerns `python3-weasyprint` räcker för PDF-exporten.
- Att PDF/EPUB får önskad layout även i GitHub Actions-miljön.
