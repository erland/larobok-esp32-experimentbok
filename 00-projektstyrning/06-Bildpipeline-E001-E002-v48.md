# v48 – Bild- och layoutpipeline för E001–E002

## Sammanfattning

v48 etablerar en strukturerad bildpipeline för E001 och E002.

Syftet är att kunna skapa kompletta PDF-previewversioner med bilder utan att tekniska kopplingsbilder bygger på fria AI-gissningar.

## Tillagt

- `08-illustrationer-och-kopplingar/circuits/E001-circuit.yaml`
- `08-illustrationer-och-kopplingar/circuits/E002-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E001-diagram.json`
- `08-illustrationer-och-kopplingar/wokwi/E002-diagram.json`
- `08-illustrationer-och-kopplingar/prompts/E001-image-prompts.md`
- `08-illustrationer-och-kopplingar/prompts/E002-image-prompts.md`
- `08-illustrationer-och-kopplingar/generated/E001/E001-C-connection-map.svg`
- `08-illustrationer-och-kopplingar/generated/E002/E002-C-rhythm-timeline.svg`
- `08-illustrationer-och-kopplingar/briefs/E001-bildpipeline-brief.md`
- `08-illustrationer-och-kopplingar/briefs/E002-bildpipeline-brief.md`

## Beslut

Tekniska kopplingsbilder ska utgå från strukturerade kopplingsspecifikationer och validerbara diagram, inte från fria AI-prompter.

AI-prompter får användas för dekorativa bilder och stämningsbilder, men inte som sanningskälla för kopplingar.

## Nästa steg

1. Kontrollera Wokwi-diagrammen i Wokwi.
2. Justera eventuella pin-alias/partnamn.
3. Skapa faktiska breadboardbilder.
4. Rendera komplett PDF-preview för E001–E002 med tekniska bilder och rytm-SVG.
