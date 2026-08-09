# v79 – E006 Fyrtornet

Denna version skapar första fullständiga utkastet till E006.

## Skapade filer

- `07-experimentutkast/kapitel-01/E006-Fyrtornet.md`
- `08-illustrationer-och-kopplingar/generated/E006/E006-A-dagens-delar.svg`
- `08-illustrationer-och-kopplingar/generated/E006/E006-B-kopplingsoversikt.svg`
- `08-illustrationer-och-kopplingar/generated/E006/E006-C-fyrsekvens.svg`
- `08-illustrationer-och-kopplingar/generated/E006/E006-D-fyrvariationer.svg`
- `08-illustrationer-och-kopplingar/circuits/E006-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E006-diagram.json`
- `08-illustrationer-och-kopplingar/briefs/E006-bildpipeline-brief.md`
- `08-illustrationer-och-kopplingar/prompts/E006-image-prompts.md`

## Pedagogiskt syfte

E006 fungerar som ett berättande kapitelprojekt i slutet av Kapitel 1. Experimentet bygger vidare på E002 genom att återanvända en enkel LED-koppling men ge den en lugnare och mer berättande rytm.

## Viktiga val i denna version

- Kopplingen återanvänder en LED på GPIO23 för att hålla tröskeln låg.
- Fyrrytmen definieras som långt blink → kort paus → kort blink → lång paus.
- Bildspråket följer v78-standarden för kopplingsöversikter.
- E006-D används som stöd för Utforska-delen och visar att känslan förändras när tiderna ändras.

## Kvar att göra

- Fysisk breadboardtest.
- Kompilera/verifiera koden i vald ESP32-miljö.
- Teknisk granskning.
- Pedagogisk granskning.
- Eventuell PDF-layoutgranskning när preview byggs.
