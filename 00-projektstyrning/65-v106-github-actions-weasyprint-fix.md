# v106 – Fix för WeasyPrint i GitHub Actions

Preview-flödet i v105 föll på steget:

```bash
sudo apt-get install -y --no-install-recommends python3-weasyprint
```

På Ubuntu Noble i GitHub Actions saknas paketet `python3-weasyprint` i apt-källorna.

## Ändring

Uppdaterade:

- `.github/workflows/02-build-preview.yml`
- `.github/workflows/03-release.yml`
- `scripts/build_book.py`
- `publishing/build-notes.md`

## Ny installation

Workflows gör nu:

1. Installerar systembibliotek via apt:
   - `python3-pip`
   - `python3-venv`
   - `libcairo2`
   - `libpango-1.0-0`
   - `libpangocairo-1.0-0`
   - `libgdk-pixbuf-2.0-0`
   - `libffi-dev`
   - `shared-mime-info`
2. Skapar venv:
   - `${RUNNER_TEMP}/weasyprint-venv`
3. Installerar:
   - `weasyprint==62.3`
4. Skickar binärsökvägen till byggscriptet via:
   - `WEASYPRINT_BIN`

## Varför

Det gör preview/release mindre beroende av om Ubuntu-runnern råkar ha ett färdigt `python3-weasyprint`-paket.

## Kvar att verifiera

- Kör `Build Preview` igen i GitHub Actions.
- Kontrollera att artifactet `esp32-experimentbok-preview` innehåller både EPUB och PDF.
