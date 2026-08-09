# E009 image prompts – Hemlig blinkkod

## Övergripande stil

Följ komponentbiblioteket från v68 och bildreglerna från v69/v78:

- ljus bakgrund,
- korta etiketter,
- tydliga LED-tillstånd,
- konsekvent pilstil,
- inga långa instruktioner i bilden.

## E009-A – Dagens delar

Visa ESP32 DevKit, breadboard, en LED-lampa, ett motstånd 220–330 Ω, kopplingskablar och USB-kabel. Bilden visar delar, inte färdig koppling.

## E009-B – Kopplingsöversikt

Visa en separat ljusväg:

- GPIO 23 till LED-lampans långa ben,
- LED-lampans korta ben via motstånd till GND.

Bilden ska följa v78-standarden och v86-lärdomen: motståndsledare ska visuellt nå LED-benet.

## E009-C – Hemlig blinksekvens

Visa sekvensen:

1. KORT – 180 ms
2. LÅNG – 550 ms
3. KORT – 180 ms
4. PAUS – 900 ms
5. börja om

Texten HEJ kan stå tydligt som betydelsen.

## E009-D – Blinkkodtabell

Visa fyra enkla hemliga koder:

- kort kort = JA
- lång lång = NEJ
- kort lång kort = HEJ
- lång kort lång = KOM

Använd visuella prickar för kort blink och avlånga symboler för lång blink.
