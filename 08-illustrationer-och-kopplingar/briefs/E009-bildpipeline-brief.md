# E009 bildpipeline-brief – Hemlig blinkkod

## Status

Skapad i v91 som första fullständiga E009-utkast.

## Klassning

E009 produceras som **bonusprojekt**, inte som huvudexperiment.

Det följer Kapitel 2-strukturen där E009 är markerat som bonus. Det följer också v83-principen: E009 är pedagogiskt användbart, men ligger nära tidigare blinkexperiment och ska därför inte konkurrera med huvudprogressionen mot RGB/PWM.

## Teknisk sanningskälla

- `08-illustrationer-och-kopplingar/circuits/E009-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E009-diagram.json`
- Manus: `07-experimentutkast/kapitel-02/E009-Hemlig-blinkkod.md`

## Progressionsbedömning enligt v83

E009 tillför ett nytt tänkesätt: blinkning som meddelande.

Men kopplingen och blinkprincipen är nära E002/E006-liknande rytmexperiment. Därför är den bästa placeringen bonus/utmaning, inte huvudspår.

E009 får finnas som fullständigt bonusmaterial eftersom det:

- förstärker funktioner från E007,
- ger mening åt kort/lång/pause,
- förbereder E010 Morse med LED,
- men inte behövs för att fortsätta mot RGB/PWM.

## Bildprincip

Följ komponentbiblioteket från v68/v69 och v78-standarden för kopplingsöversikter:

- kort text i bilder,
- tydliga LED-tillstånd,
- varje LED ska ha eget motstånd,
- signaltråd ska visuellt gå till LED-lampans långa ben,
- motståndsledare ska visuellt gå från LED-lampans korta ben till motståndet,
- blinksekvensen ska visa kort/lång/paus tydligt.

## Bilder

| ID | Fil | Syfte | Status |
|---|---|---|---|
| E009-A | `generated/E009/E009-A-dagens-delar.svg` | Dagens delar | Utkast |
| E009-B | `generated/E009/E009-B-kopplingsoversikt.svg` | Förenklad enkel LED-koppling | Utkast |
| E009-C | `generated/E009/E009-C-blinkkodsekvens.svg` | Kort → lång → kort → paus | Utkast |
| E009-D | `generated/E009/E009-D-blinkkodtabell.svg` | Enkel hemlig kodtabell | Utkast |

## Layoutgranskning som återstår

- Kontrollera att E009-C inte blir för bred i PDF.
- Kontrollera att E009-D blir läsbar i boklayout.
- Kontrollera att bonusklassningen syns tydligt i textflödet.
