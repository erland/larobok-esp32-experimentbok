# v107 – Fix för WeasyPrint/pydyf i GitHub Actions

Preview-flödet i v106 kom vidare till PDF-genereringen men föll med:

```text
AttributeError: 'super' object has no attribute 'transform'
```

## Orsak

WeasyPrint 62.3 kan fallera med nyare pydyf-versioner. I GitHub Actions installerades WeasyPrint via pip utan att pydyf låstes, vilket gjorde att en inkompatibel pydyf-version kunde väljas.

## Ändring

Uppdaterade:

- `.github/workflows/02-build-preview.yml`
- `.github/workflows/03-release.yml`
- `scripts/build_book.py`
- `publishing/build-notes.md`

## Ny installation

Workflows installerar nu:

```bash
pip install "weasyprint==62.3" "pydyf==0.11.0"
```

Workflows skriver också ut:

- WeasyPrint-version,
- pydyf-version.

## Byggscript

`scripts/build_book.py` försöker inte längre falla tillbaka till systemets `python -m weasyprint` om `WEASYPRINT_BIN` är satt men misslyckas. Då blir felorsaken tydligare i loggen.

## Kvar att verifiera

- Kör Build Preview igen i GitHub Actions.
- Kontrollera att PDF skapas.
- Kontrollera att artifactet innehåller både EPUB och PDF.
