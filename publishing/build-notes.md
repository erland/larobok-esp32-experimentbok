# Build notes

GitHub Actions-konceptet infördes i v105 med samma övergripande upplägg som referenskitet:

- snabb validering vid PR/push till `main`,
- manuell Build Preview,
- preview bygger både EPUB och PDF,
- preview publicerar ett gemensamt artifact: `esp32-experimentbok-preview`,
- release på `v*`-taggar publicerar EPUB och PDF som separata release assets,
- Pandoc är låst till 3.1.11.1,
- validerings- och bygglogik ligger i `scripts/`.

## Projektspecifik anpassning

Det här ESP32-projektet är inte ett romanprojekt. Därför är byggscriptet anpassat till projektets faktiska kapitelstruktur:

- Kapitel 1: E001, E002, E003, E005, E004
- Kapitel 2: E007, E008, E011, E012, E013, E014, E015, E016

PDF byggs via Pandoc HTML + WeasyPrint eftersom boken innehåller många SVG-bilder, tabeller, kodblock och instruktionslayout. EPUB byggs via Pandoc EPUB3.

E009 och E010 är parkerade och ingår inte i aktiv bokexport.

## v106 – WeasyPrint-installation på Ubuntu Noble

GitHub Actions-previewen föll på Ubuntu Noble eftersom paketet `python3-weasyprint` saknar installationskandidat.

Åtgärd:

- workflows installerar systembibliotek via apt,
- skapar en temporär Python-venv i `${RUNNER_TEMP}/weasyprint-venv`,
- installerar `weasyprint==62.3` via pip,
- skickar sökvägen till binären via `WEASYPRINT_BIN`,
- `scripts/build_book.py` använder `WEASYPRINT_BIN` om variabeln finns.

Detta undviker beroendet till ett distributionspaket som inte finns i runnerns apt-källor.

## v107 – pydyf pin för WeasyPrint 62.3

Preview-flödet kom vidare till PDF-steget men föll i WeasyPrint med:

```text
AttributeError: 'super' object has no attribute 'transform'
```

Felet beror på en känd inkompatibilitet i kombinationen WeasyPrint 62.3 och nyare pydyf-versioner.

Åtgärd:

- workflows installerar nu `weasyprint==62.3` tillsammans med `pydyf==0.11.0`,
- workflows skriver ut installerade versioner av WeasyPrint och pydyf,
- `scripts/build_book.py` försöker inte längre falla vidare till systemets `python -m weasyprint` om explicit `WEASYPRINT_BIN` misslyckas.
