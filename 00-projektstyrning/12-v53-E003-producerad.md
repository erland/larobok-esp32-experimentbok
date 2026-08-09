# v53 – E003 producerad från v52

## Sammanfattning

E003 – Två LED turas om har skapats som nästa experiment efter v52. Arbetet fortsätter direkt från E001/E002 som guldstandard och gör inga nya designbeslut.

## Tillagda filer

- `07-experimentutkast/kapitel-01/E003-Tva-LED-turas-om.md`
- `08-illustrationer-och-kopplingar/circuits/E003-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E003-diagram.json`
- `08-illustrationer-och-kopplingar/prompts/E003-image-prompts.md`
- `08-illustrationer-och-kopplingar/briefs/E003-bildpipeline-brief.md`
- `08-illustrationer-och-kopplingar/generated/E003/E003-A-dagens-delar.svg`
- `08-illustrationer-och-kopplingar/generated/E003/E003-B-kopplingsoversikt.svg`
- `08-illustrationer-och-kopplingar/generated/E003/E003-C-turas-om-tidslinje.svg`
- `08-illustrationer-och-kopplingar/generated/E003/E003-D-vanliga-ledtradar.svg`

## Tekniska val

- LED 1 använder GPIO 23, enligt E001/E002.
- LED 2 använder GPIO 22.
- Varje LED har eget motstånd 220–330 ohm till GND.
- Kodens huvudidé är två pinnar och sekvens: LED 1 på/LED 2 av, sedan LED 1 av/LED 2 på.

## Status

E003 är ett 5B.6-anpassat manusutkast med kod, circuit.yaml, Wokwi-diagram, bildbrief och SVG-bilder. Det är inte markerat som färdigt experiment eftersom fysisk breadboardtest, teknisk granskning, pedagogisk granskning och layoutgranskning återstår.
