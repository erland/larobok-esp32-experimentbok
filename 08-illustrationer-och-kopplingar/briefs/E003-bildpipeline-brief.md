# E003 – bildpipeline-brief

## Experiment

E003 – Två LED turas om

## Bildmål

E003 ska visa första steget från en ensam blinkande LED till flera styrda outputs. Bildspråket ska därför kännas som en naturlig fortsättning på E001/E002, inte som en helt ny koppling.

## Bilder

| ID | Fil | Syfte |
|---|---|---|
| E003-A | `generated/E003/E003-A-dagens-delar.svg` | Visa att en andra LED och ett andra motstånd tillkommer |
| E003-B | `generated/E003/E003-B-kopplingsoversikt.svg` | Visa två separata GPIO-vägar i parallella rader utan korsande linjer |
| E003-C | `generated/E003/E003-C-turas-om-tidslinje.svg` | Visa sekvensen LED 1 på / LED 2 på |
| E003-D | `generated/E003/E003-D-vanliga-ledtradar.svg` | Arkiverad/ej refererad från manus från v57; ledtrådar hanteras som text/tabell |

## Kontrollpunkter

- GPIO 23 går endast till LED 1:s långa ben.
- GPIO 22 går endast till LED 2:s långa ben.
- Varje LED har eget motstånd till GND.
- Bilden får inte antyda att LED-lamporna delar samma motstånd.
- Bildtexterna ska följa v52-principen med explicita markdown-referenser.
