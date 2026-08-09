# E008 image prompts – Rinnande ljus

## Övergripande stil

Följ komponentbiblioteket från v68 och bildreglerna från v69/v78:

- ljus bakgrund,
- korta etiketter,
- tydliga LED-tillstånd,
- konsekvent pilstil,
- inga långa instruktioner i bilden,
- sekvensbilder visar rörelse över tid.

## E008-A – Dagens delar

Visa ESP32 DevKit, breadboard, fyra LED-lampor, fyra motstånd 220–330 Ω, kopplingskablar och USB-kabel. Bilden visar delar, inte färdig koppling.

## E008-B – Kopplingsöversikt

Visa fyra separata ljusvägar:

- GPIO 23 till LED 1:s långa ben,
- LED 1:s korta ben via motstånd till GND,
- GPIO 22 till LED 2:s långa ben,
- LED 2:s korta ben via motstånd till GND,
- GPIO 21 till LED 3:s långa ben,
- LED 3:s korta ben via motstånd till GND,
- GPIO 19 till LED 4:s långa ben,
- LED 4:s korta ben via motstånd till GND.

Bilden ska följa v78-standarden och v86-lärdomen: motståndsledare ska visuellt nå LED-benen.

## E008-C – Rinnande ljussekvens

Visa sekvensen:

1. LED 1
2. LED 2
3. LED 3
4. LED 4
5. LED 3
6. LED 2
7. börja om

Det ska kännas som en ljusorm som går fram och tillbaka.

## E008-D – Lista och loop

Visa `ledPins[] = {23, 22, 21, 19}` som fyra rutor.

Visa att `i` flyttar sig från ruta till ruta.

Bilden ska hjälpa barnet förstå idén "loopen pekar på en pinne i taget", inte bli en programmeringstabell.

# v88 – Förenklad lista/loop-bild

E008-D ska vara barnnära och lugn.

Prioritera:

- listan som fyra rutor i rad,
- LED-symbol eller färg i varje ruta,
- tydlig pekare för "loopen är här nu",
- kort text: "loopen flyttar sig en ruta i taget".

Undvik att göra bilden till en programmeringstabell med för många indexrader eller för mycket teknisk notation.

# v89 – ytterligare förenkling av E008-D

E008-D ska vara mycket lugn visuellt.

Behåll:
- fyra rutor i rad,
- en aktiv ruta,
- en enkel pekare ovanför aktiv ruta,
- en kort rad längst ned: "loopen går vidare en ruta i taget".

Ta bort:
- stora böjda pilar,
- onödig konkurrerande text nära rutorna,
- allt som får bilden att kännas som ett tekniskt programmeringsdiagram.
