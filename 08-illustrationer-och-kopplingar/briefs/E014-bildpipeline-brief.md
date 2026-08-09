# E014 bildpipeline-brief – Humörlampan

## Status

Skapad i v99 som första fullständiga E014-utkast.

## Teknisk sanningskälla

- `08-illustrationer-och-kopplingar/circuits/E014-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E014-diagram.json`
- Manus: `07-experimentutkast/kapitel-02/E014-Humorlampan.md`

## Progressionskontroll enligt v83

E014 bedöms fungera som eget huvudexperiment.

Det återanvänder RGB-LED-kopplingen och 0–255-modellen, men tillför en tydlig ny huvudidé:

- färg som betydelse,
- funktionsnamn som uttrycker humör/status,
- statuslampa som teknikidé,
- brygga mot senare sensor- och smarta prylar.

Det är därför inte bara en ny färgsekvens utan ett nytt användningssätt för färg.

## Bildprincip

- E014-A och E014-B återanvänder RGB-standardbilderna eftersom kopplingen är samma.
- E014-C ska visa en enkel humörsekvens: glad, lugn, fokus, varning, magi.
- E014-D ska visa färg som status: grön okej, gul vänta, röd varning, blå lugn.
- Undvik att säga att färger alltid betyder samma sak. Poängen är att färg kan fungera som snabbt meddelande.

## Bilder

| ID | Fil | Syfte | Status |
|---|---|---|---|
| E014-A | `generated/E014/E014-A-dagens-delar.svg` | Dagens delar | Utkast, återanvänder E013 |
| E014-B | `generated/E014/E014-B-kopplingsoversikt.svg` | RGB-kopplingsöversikt | Utkast, återanvänder E013 |
| E014-C | `generated/E014/E014-C-humorsekvens.svg` | Humörsekvens | Utkast |
| E014-D | `generated/E014/E014-D-farg-som-status.svg` | Färg som status/betydelse | Utkast |

## Layoutgranskning som återstår

- Kontrollera att E014-C inte blir för texttung i PDF.
- Kontrollera att E014-D:s statuskort är tydliga i boklayout.
- Kontrollera att E014:s övergång till E015 blir pedagogiskt rimlig.

## v100-notis – lätt pedagogisk/bildmässig puts

E014 putsades lätt efter analys:

- `magi` ersattes av `favorit`/`favoritläge` för att göra status-/läge-idén tydligare.
- Texten förtydligar att färger kan visa både humör och läge.
- E014-C fick rubriken "olika lägen" och mer generell signaltext.
- E014-D gjordes mer symmetrisk med fyra lika stora statuskort.
