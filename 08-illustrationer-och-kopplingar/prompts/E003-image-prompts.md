# E003 – bildprompter och bildkrav

## Teknisk sanningskälla

- `08-illustrationer-och-kopplingar/circuits/E003-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E003-diagram.json`

## Obligatorisk kopplingslogik

- GPIO 23 → LED 1 långt ben → LED 1 kort ben → R1 → GND
- GPIO 22 → LED 2 långt ben → LED 2 kort ben → R2 → GND
- Varje LED ska ha eget motstånd.
- Inga två GPIO-pinnar får visuellt kopplas ihop.

## E003-A – Dagens delar

Visa ESP32, breadboard, två LED-lampor, två motstånd, kopplingskablar och USB.

## E003-B – Kopplingsöversikt

Förenklad teknisk bild, inte fysisk breadboardplacering. Visa två parallella kopplingsvägar från ESP32 till varsin LED och varsin resistor till GND. Märk LED-ben diskret med `Långt ben` och `Kort ben`.

## E003-C – Tidslinje

Visa att LED 1 är PÅ medan LED 2 är AV, sedan LED 1 AV medan LED 2 är PÅ. Detta ska tydliggöra sekvensen och ljusrörelsen.

## E003-D – Vanliga ledtrådar

Visa felsökningskort för: en LED lyser inte, båda lyser samtidigt, motstånd saknas, rätt GPIO.
