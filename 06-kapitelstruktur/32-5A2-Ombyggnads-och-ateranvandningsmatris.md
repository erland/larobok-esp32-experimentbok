# 5A.2 – Ombyggnads- och återanvändningsmatris

## Syfte

Den här matrisen visar hur mycket ombyggnad som bör krävas mellan kapitel och större experimentblock.

| Från | Till | Ombyggnadsnivå | Kommentar |
|---|---|---|---|
| Kapitel 1 | Kapitel 2 | Låg | LED-koppling byggs vidare med fler LED/RGB |
| Kapitel 2 | Kapitel 3 | Låg | LED/RGB behålls, knapp läggs till |
| Kapitel 3 | Kapitel 4 | Låg | knapp + LED behålls, buzzer läggs till |
| Kapitel 4 | Kapitel 5 | Medel | output behålls, sensorer läggs till |
| Kapitel 5 | Kapitel 6 | Låg/Medel | RGB/buzzer behålls, input-sensor byts |
| Kapitel 6 | Kapitel 7 | Medel | miljösensorer kräver nya moduler |
| Kapitel 7 | Kapitel 8 | Låg | OLED återanvänds/förstärks |
| Kapitel 8 | Kapitel 9 | Medel | LED-matris/NeoPixel bör kopplas separat |
| Kapitel 9 | Kapitel 10 | Medel | servo introduceras som ny output |
| Kapitel 10 | Kapitel 11 | Hög | motorer kräver separat säkerhetsblock |
| Kapitel 11 | Kapitel 12 | Medel | tillbaka till signal/identifiering, output återanvänds |
| Kapitel 12 | Kapitel 13 | Medel/Hög | RTC/SD/WiFi kräver separata block |
| Kapitel 13 | Kapitel 14 | Varierar | barnet väljer projektspår |

## Ombyggnadsnivåer

| Nivå | Betydelse |
|---|---|
| Låg | Barnet kan behålla större delen av kopplingen |
| Medel | Några komponenter byts, men layoutprincipen är samma |
| Hög | Ny typ av koppling eller särskild säkerhetsnivå |

## Rekommenderad regel

Efter ett kapitel med hög ombyggnadsnivå bör nästa experiment börja mycket enkelt så att barnet inte möter både ny koppling och ny kod samtidigt.

---

# Standardkopplingar att återkomma till

## A – LED-output

Används i Kapitel 1–6.

Består av:

- ESP32-pin
- seriemotstånd
- LED
- GND

## B – Status-output

Används i Kapitel 2–14.

Består av:

- RGB-LED eller NeoPixel
- eventuell buzzer
- statuslogik i kod

## C – Knapp-input

Används i Kapitel 3–14.

Består av:

- knapp till GND
- intern `INPUT_PULLUP`
- knapphantering i kod

## D – Sensor-input

Används i Kapitel 5–14.

Består av:

- sensor
- läsning via analog/digital/bibliotek
- tröskelvärde eller tolkning

## E – Display-output

Används i Kapitel 8–14.

Består av:

- OLED via I²C
- korta textrader
- status- eller mätvärdesvisning

## F – Rörelse-output

Används i Kapitel 10–14.

Består av:

- servo eller motor
- tydlig strömnotering
- enkel mekanisk rörelse
