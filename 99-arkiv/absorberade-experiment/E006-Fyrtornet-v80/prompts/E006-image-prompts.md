# E006 image prompts – Fyrtornet

## Övergripande stil

Följ komponentbiblioteket från v68 och bildreglerna från v69/v78:

- ljus bakgrund,
- korta etiketter,
- tydliga LED-tillstånd,
- konsekvent pilstil,
- inga långa instruktioner i bilden,
- sekvensbilder visar tillstånd över tid.

## E006-A – Dagens delar

Visa ESP32 DevKit, breadboard, en LED-lampa, ett motstånd 220–330 Ω, kopplingskablar och USB-kabel. Bilden visar delar, inte färdig koppling.

## E006-B – Kopplingsöversikt

Visa en enkel ljusväg:

- GPIO 23 till LED-lampans långa ben,
- LED-lampans korta ben via motstånd till GND.

Kopplingen ska följa v78-standarden och vara visuellt konsekvent med E002-B, E003-B och E005-B.

## E006-C – Fyrsekvens

Visa sekvensen:

1. PÅ – 500 ms
2. AV – 250 ms
3. PÅ – 180 ms
4. AV – 1400 ms
5. börja om

Korta etiketter kan användas för "långt blink", "kort blink" och "lång paus".

## E006-D – Fyrvariationer

Visa att samma LED kan kännas olika beroende på rytm:

- lugn,
- fyrtorn,
- snabb.
