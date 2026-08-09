# E013 bildpipeline-brief – Regnbågslampan

## Status

Skapad i v97 som första fullständiga E013-utkast.

## Teknisk sanningskälla

- `08-illustrationer-och-kopplingar/circuits/E013-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E013-diagram.json`
- Manus: `07-experimentutkast/kapitel-02/E013-Regnbagslampan.md`

## Progressionskontroll enligt v83

E013 bedöms fungera som eget huvudexperiment.

Det återanvänder E011/E012-kopplingen men tillför en tydlig ny huvudidé:

- längre färgsekvens,
- många små steg i RGB-värden,
- mjukare färgövergångar,
- känslan av levande/regnbågsliknande ljus.

Det är därför ett nytt upplevelse- och kodsteg, inte bara en ny lista färger.

## Bildprincip

- E013-A och E013-B återanvänder E011/E012-standarden eftersom kopplingen är samma.
- E013-C ska visa regnbågssekvensen som flera färgkort/tillstånd i rad med loop tillbaka till början.
- E013-D ska förklara huvudidén "små steg ger mjukare färg".
- Undvik långa tekniska förklaringar i bilderna; markdown-texten bär teorin.

## Bilder

| ID | Fil | Syfte | Status |
|---|---|---|---|
| E013-A | `generated/E013/E013-A-dagens-delar.svg` | Dagens delar | Utkast, återanvänder E012 |
| E013-B | `generated/E013/E013-B-kopplingsoversikt.svg` | RGB-kopplingsöversikt | Utkast, återanvänder E012 |
| E013-C | `generated/E013/E013-C-regnbagssekvens.svg` | Regnbågssekvens med loop | Utkast |
| E013-D | `generated/E013/E013-D-sma-steg-ger-mjuk-farg.svg` | Begreppsbild för små färgsteg | Utkast |

## Layoutgranskning som återstår

- Kontrollera att E013-C blir läsbar i PDF och att färgnamnen inte känns trånga.
- Kontrollera att E013-D inte blir för kodtung.
- Kontrollera att det är tydligt att E013 återanvänder samma koppling som E012.

## v98-notis – lätt puts

E013 putsades lätt efter analys:

- texten mildrades från absolut "mjuk övergång" till "kan kännas mjukare",
- `glider` ersattes på ett par ställen med `vandrar` för att bättre matcha den stegvisa koden,
- texten förtydligar att fler små steg gör färgresan mjukare,
- E013-C fick lugnare loop-pil,
- E013-D fick kortare förklaringsrad.
