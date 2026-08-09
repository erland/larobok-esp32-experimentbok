# E005 image prompts – Polisljus

## Övergripande stil

Följ komponentbiblioteket från v68 och bildreglerna från v69:

- ljus bakgrund,
- korta etiketter,
- tydliga LED-tillstånd,
- konsekvent pilstil,
- inga långa instruktioner i bilden,
- sekvensbilder visar tillstånd över tid.

## E005-A – Dagens delar

Visa ESP32 DevKit, breadboard, två LED-lampor röd/blå, två motstånd 220–330 Ω, kopplingskablar och USB-kabel. Bilden visar delar, inte färdig koppling. Antal visas i markdown-tabellen, inte i bilden.

## E005-B – Kopplingsöversikt

Visa två separata ljusvägar:

- GPIO 23 till röd LED:s långa ben,
- röd LED:s korta ben via motstånd till GND,
- GPIO 22 till blå LED:s långa ben,
- blå LED:s korta ben via motstånd till GND.

Signalkablarna ska visuellt gå till LED-benen/raderna vid benen, inte till LED-huvudet.

## E005-C – Polisljussekvens

Visa sekvensen:

1. RÖD – 150 ms
2. AV – 100 ms
3. RÖD – 150 ms
4. AV – 250 ms
5. BLÅ – 150 ms
6. AV – 100 ms
7. BLÅ – 150 ms
8. AV – 250 ms
9. börja om

Loop-pilen ska börja vid sista rutan och gå tillbaka till första rutan.

## E005-D – Vanliga ledtrådar

Visa visuellt:

- bara röd blinkar → följ blå väg,
- bara blå blinkar → följ röd väg,
- inget blinkar → kontrollera GND.
