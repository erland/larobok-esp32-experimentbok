# E012 bildpipeline-brief – Färgblandaren

## Status

Skapad i v95 som första fullständiga E012-utkast.

## Teknisk sanningskälla

- `08-illustrationer-och-kopplingar/circuits/E012-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E012-diagram.json`
- Manus: `07-experimentutkast/kapitel-02/E012-Fargblandaren.md`

## Progressionskontroll enligt v83

E012 är motiverat som eget huvudexperiment.

Det återanvänder E011-kopplingen men tillför en tydlig ny huvudidé:

- PWM/0–255-ljusstyrka,
- färgrecept med tre värden,
- blandning av RGB-kanaler.

Det är därför ett nytt kod- och förståelsesteg, inte bara en ny färgordning.

## Bildprincip

- E012-A och E012-B återanvänder E011-standard eftersom kopplingen är samma.
- E012-C ska visa färgrecept med tre tal på ett barnnära sätt.
- E012-D ska förklara PWM som snabb blinkning som ser ut som svagare/starkare ljus.
- Undvik avancerade termer som frekvens, duty cycle och timer i bilderna.

## Bilder

| ID | Fil | Syfte | Status |
|---|---|---|---|
| E012-A | `generated/E012/E012-A-dagens-delar.svg` | Dagens delar | Utkast, återanvänder E011 |
| E012-B | `generated/E012/E012-B-kopplingsoversikt.svg` | RGB-kopplingsöversikt | Utkast, återanvänder E011 |
| E012-C | `generated/E012/E012-C-fargrecept.svg` | Färgrecept med RGB-värden | Utkast |
| E012-D | `generated/E012/E012-D-pwm-snabb-blinkning.svg` | PWM som snabb blinkning | Utkast |

## Layoutgranskning som återstår

- Kontrollera att E012-C blir läsbar i PDF.
- Kontrollera att E012-D inte blir för teoritung.
- Kontrollera att `analogWrite()`-koden inte bryts dåligt över sidor.

## v96-notis – lätt pedagogisk/bildmässig puts

E012 putsades lätt efter analys:

- `0` beskrivs nu som "inget ljus" i stället för "nästan inget ljus".
- `setColor()` introduceras tidigare som huvudbegrepp/färgrecept.
- `analogWrite()` beskrivs som implementation inuti färgreceptet.
- Vuxenrutorna förtydligar att projektet behöver ett tekniskt beslut om `analogWrite()` kontra LEDC/PWM bakom kulisserna.
- E012-D fick mer barnnära bildspråk: "lite på", "mer på", "mest på".
