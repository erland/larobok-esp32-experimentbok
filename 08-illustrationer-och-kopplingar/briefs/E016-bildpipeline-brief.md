# E016 bildpipeline-brief – Andande ljus

## Status

Skapad i v103 som första fullständiga E016-utkast.

## Teknisk sanningskälla

- `08-illustrationer-och-kopplingar/circuits/E016-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E016-diagram.json`
- Manus: `07-experimentutkast/kapitel-02/E016-Andande-ljus.md`

## Progressionskontroll enligt v83

E016 bedöms fungera som eget huvudexperiment och kapitelavslutande effekt.

Det återanvänder E015-kopplingen men tillför en tydlig ny huvudidé:

- PWM-värdet räknas upp och ned,
- `for`-loop används som långsam förändring,
- ljuset blir en visuell effekt,
- Kapitel 2 sammanfattas i en enkel men stark observation.

## Bildprincip

- E016-A och E016-B återanvänder E015-standard eftersom kopplingen är samma.
- E016-C visar andningssekvensen: av/svag/mellan/stark/svag och loop tillbaka.
- E016-D visar två loopar: en som räknar upp och en som räknar ned.
- Bilderna ska visa känsla och rörelse, inte avancerad PWM-teori.

## Bilder

| ID | Fil | Syfte | Status |
|---|---|---|---|
| E016-A | `generated/E016/E016-A-dagens-delar.svg` | Dagens delar | Utkast, återanvänder E015 |
| E016-B | `generated/E016/E016-B-kopplingsoversikt.svg` | Enkel LED-koppling | Utkast, återanvänder E015 |
| E016-C | `generated/E016/E016-C-andningssekvens.svg` | Andningssekvens | Utkast |
| E016-D | `generated/E016/E016-D-loop-upp-och-ned.svg` | Loop upp/ned-begrepp | Utkast |

## Layoutgranskning som återstår

- Kontrollera att E016-C inte känns för tät i PDF.
- Kontrollera att E016-D förklarar looparna tydligt utan att bli för kodtung.
- Kontrollera Kapitelavslutningens flöde i PDF.

## v104-notis – lätt puts

E016 putsades lätt efter analys:

- texten mildrades så "andas" tydligare beskrivs som en upplevd effekt,
- E016-C fick en lugnare loop-pil som stör färg-/ljusstyrkekorten mindre,
- E016-C:s looptext ändrades till "Sedan börjar ljuset om",
- E016-D fick mer luft mellan talraden och kurvan på högerkortet,
- E016-D:s nedräkningsrad kortades något.
