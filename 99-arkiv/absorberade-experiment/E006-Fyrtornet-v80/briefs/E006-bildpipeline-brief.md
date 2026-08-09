# E006 bildpipeline-brief – Fyrtornet

## Status

Skapad i v79 som första fullständiga E006-utkast.

## Teknisk sanningskälla

- `08-illustrationer-och-kopplingar/circuits/E006-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E006-diagram.json`
- Manus: `07-experimentutkast/kapitel-01/E006-Fyrtornet.md`

## Bildprincip

Följ komponentbiblioteket från v68/v69 och bildstandarden från v78:

- ljus bakgrund,
- kort text i bilder,
- tydlig LED-polaritet när kopplingsbilden visar LED-ben,
- signaltråden ska gå till LED-lampans långa ben,
- LED-lampans korta ben ska gå vidare till motstånd,
- motståndet ska gå vidare till GND,
- sekvensbilder ska visa tillstånd över tid,
- loop-pil ska gå från högersidan av sista steget till vänstersidan av första steget.

## Bilder

| ID | Fil | Syfte | Status |
|---|---|---|---|
| E006-A | `generated/E006/E006-A-dagens-delar.svg` | Dagens delar | Utkast |
| E006-B | `generated/E006/E006-B-kopplingsoversikt.svg` | Förenklad kopplingsöversikt | Utkast |
| E006-C | `generated/E006/E006-C-fyrsekvens.svg` | Sekvens för långt blink, kort blink och lång paus | Utkast |
| E006-D | `generated/E006/E006-D-fyrvariationer.svg` | Visuell jämförelse av olika rytmkänslor | Utkast |

## Layoutgranskning som återstår

- Kontrollera att E006-C är tydlig i PDF.
- Kontrollera att E006-B känns konsekvent med E003 och E005-B v77+.
- Kontrollera att E006-D inte blir för tät i mindre skala.

## v80-notis

E006 fick bildputs i v80.

- `E006-B-kopplingsoversikt.svg` putsades för att bättre följa den visuella standarden från v78.
- `E006-C-fyrsekvens.svg` ritades om med renare kortlayout och tydligare loop-pil.
- `E006-D-fyrvariationer.svg` förenklades kraftigt så att rytmjämförelsen blir lättare att läsa i boklayout.
- PNG-renderingar skapades för B, C och D för enklare granskning.
