# E004 image prompts – Mini-trafikljus

## Övergripande stil

Barnvänlig teknisk SVG-stil enligt E001–E003:

- ljus bakgrund,
- blå rubriker,
- tydliga etiketter,
- förenklade komponenter,
- inga fotorealistiska breadboardbilder,
- inga stora förklarande textrutor som stör läsflödet,
- korta etiketter direkt i bilden.

## E004-A – Dagens delar

Visa ESP32 DevKit, breadboard, tre LED-lampor röd/gul/grön, tre motstånd 220–330 ohm, kopplingskablar och USB-kabel. Bilden visar delar, inte färdig koppling.

## E004-B – Kopplingsöversikt

Visa förenklad teknisk kopplingsväg:

- GPIO 23 till röd LED:s långa ben,
- röd LED:s korta ben via motstånd till GND,
- GPIO 22 till gul LED:s långa ben,
- gul LED:s korta ben via motstånd till GND,
- GPIO 21 till grön LED:s långa ben,
- grön LED:s korta ben via motstånd till GND.

Viktigt: signalkablarna ska gå till LED-benen/raderna vid benen, inte till LED-huvudet.

## E004-C – Trafikljussekvens

Visa tidslinje med fyra steg:

1. RÖTT – 2000 ms – stanna
2. GULT – 700 ms – vänta
3. GRÖNT – 2000 ms – kör
4. GULT – 700 ms – vänta

Visa att sekvensen börjar om.

## E004-D – Vanliga ledtrådar

Visa tre små felsökningskort:

- Fel färg? Kontrollera röd 23, gul 22, grön 21.
- En färg saknas? Följ den färgens väg till GND.
- Två lyser? Läs HIGH/LOW-raderna.

Lägg till en enkel ruta: Bra ordning: välj en färg, följ vägen, kontrollera koden.
