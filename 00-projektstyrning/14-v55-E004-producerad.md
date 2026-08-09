# v55 – E004 producerad

## Sammanfattning

E004 – Mini-trafikljus har skapats som nästa experiment efter E003.

E004 bygger vidare på progressionen:

- E001: första blinket
- E002: egen rytm
- E003: två LED turas om
- E004: tre LED bildar ett igenkännbart mini-system

## Skapade/uppdaterade filer

- `07-experimentutkast/kapitel-01/E004-Mini-trafikljus.md`
- `08-illustrationer-och-kopplingar/circuits/E004-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E004-diagram.json`
- `08-illustrationer-och-kopplingar/briefs/E004-bildpipeline-brief.md`
- `08-illustrationer-och-kopplingar/prompts/E004-image-prompts.md`
- `08-illustrationer-och-kopplingar/generated/E004/E004-A-dagens-delar.svg`
- `08-illustrationer-och-kopplingar/generated/E004/E004-B-kopplingsoversikt.svg`
- `08-illustrationer-och-kopplingar/generated/E004/E004-C-trafikljussekvens.svg`
- `08-illustrationer-och-kopplingar/generated/E004/E004-D-vanliga-ledtradar.svg`

## Designbeslut

- E004 följer 5B.6-inriktningen: upptäckarbok, konkret uppdrag, tidig effekt, wow-kurva och trygg felsökning.
- E004 använder diskreta `Insikt:`-rader i löptexten och sparar färgade rutor till vuxenkoll, byggtips och mikrokoll.
- Kopplingsordningen är konsekvent med E001–E003: GPIO → långt LED-ben → kort LED-ben → motstånd → GND.
- GPIO 23, 22 och 21 används för röd, gul och grön LED.

## Återstår

E004 är markerad som utkast/pågår. Följande återstår innan färdigstatus:

- fysisk breadboardtest,
- teknisk granskning,
- pedagogisk granskning,
- PDF-layoutgranskning,
- eventuell bildputs efter PDF-preview.
