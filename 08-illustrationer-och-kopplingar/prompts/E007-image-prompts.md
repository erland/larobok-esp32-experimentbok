# E007 image prompts – LED-stafett

## Övergripande stil

Följ komponentbiblioteket från v68 och bildreglerna från v69/v78:

- ljus bakgrund,
- korta etiketter,
- tydliga LED-tillstånd,
- konsekvent pilstil,
- inga långa instruktioner i bilden,
- sekvensbilder visar tillstånd över tid.

## E007-A – Dagens delar

Visa ESP32 DevKit, breadboard, tre LED-lampor röd/gul/grön, tre motstånd 220–330 Ω, kopplingskablar och USB-kabel. Bilden visar delar, inte färdig koppling.

## E007-B – Kopplingsöversikt

Visa tre separata ljusvägar:

- GPIO 23 till röd LED:s långa ben,
- röd LED:s korta ben via motstånd till GND,
- GPIO 22 till gul LED:s långa ben,
- gul LED:s korta ben via motstånd till GND,
- GPIO 21 till grön LED:s långa ben,
- grön LED:s korta ben via motstånd till GND.

Bilden ska följa v78-standarden.

## E007-C – LED-stafettsekvens

Visa sekvensen:

1. RÖD – 400 ms
2. GUL – 400 ms
3. GRÖN – 400 ms
4. GUL – 400 ms
5. börja om

Loop-pilen ska börja vid sista rutan och gå tillbaka till första rutan.

## E007-D – Kodrecept

Visa `lightOne(pin)` som ett kodrecept i tre steg:

1. släck alla,
2. tänd vald,
3. vänta.

Bilden ska hjälpa barnet förstå funktionens idé, inte visa all kod.

# v85 – Förenklad kodreceptbild

E007-D ska undvika att bli kodtung.

Prioritera barnnära text:

- släck alla,
- tänd vald,
- vänta.

Kod kan visas sparsamt längst ned som exempel på anrop:

- `lightOne(redPin);`
- `lightOne(yellowPin);`
- `lightOne(greenPin);`

Undvik att lägga in `digitalWrite(pin, HIGH);` i bilden eftersom det gör bilden mer abstrakt än nödvändigt.
