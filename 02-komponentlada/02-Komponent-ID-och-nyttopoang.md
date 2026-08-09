# Komponent-ID och nyttopoäng
## Poängmodell
Nyttopoängen anger hur central komponenten är för boken.
| Poäng | Betydelse |
|---:|---|
| 5 | Mycket hög återanvändning, bör prioriteras |
| 4 | Hög nytta, bra att köpa tidigt |
| 3 | Rolig men mer specialiserad |
| 2 | Användbar i färre experiment |
| 1 | Bör normalt undvikas i grundlådan |
## Komponentkatalog
| ID | Komponent | Nivå | Antal | Nyttopoäng | Kort motivering |
|---|---|---|---:|---:|---|
| E01 | ESP32 DevKit | Baslåda | 2 | ★★★★★ | Hjärnan i nästan alla experiment. Har WiFi, Bluetooth, många pinnar och programmeras via USB. |
| B01 | Breadboard 830 punkter | Baslåda | 2 | ★★★★★ | Kopplingsplattan där experimenten byggs utan lödning. |
| B02 | Jumperkablar hane-hane | Baslåda | 65 | ★★★★★ | Kablar för kopplingar mellan ESP32, breadboard och komponenter. |
| B03 | Jumperkablar hane-hona | Baslåda | 30 | ★★★★☆ | Kablar för moduler och sensorer med färdiga stift. |
| R01 | Motståndssats | Baslåda | 1 | ★★★★★ | Skyddar lysdioder och används i enkla sensorkretsar. |
| L01 | LED blandade färger | Baslåda | 25 | ★★★★★ | Små lysdioder för första experimenten, signaler och spel. |
| L02 | RGB-LED | Baslåda | 5 | ★★★★☆ | En lysdiod som kan blanda rött, grönt och blått. |
| K01 | Tryckknapp | Baslåda | 10 | ★★★★★ | Barnets enklaste sätt att styra programmet. |
| K02 | Potentiometer 10kΩ | Baslåda | 3 | ★★★★★ | Ett vred som ger ett analogt värde. |
| A01 | Passiv buzzer | Baslåda | 2 | ★★★★★ | Liten högtalarliknande komponent som kan spela toner. |
| S01 | LDR fotomotstånd | Baslåda | 5 | ★★★★★ | Sensor vars motstånd ändras med ljus. |
| S02 | HC-SR04 avståndssensor | Baslåda | 2 | ★★★★★ | Mäter avstånd med ultraljud. |
| S03 | Tilt-sensor | Baslåda | 2 | ★★★☆☆ | Känner av lutning eller skakning. |
| S04 | Reedkontakt + magnet | Baslåda | 2 | ★★★★☆ | En brytare som påverkas av magnetfält. |
| D01 | OLED 0,96 tum I²C | Baslåda | 1 | ★★★★★ | Liten skärm för text, symboler och enkla spel. |
| S05 | DHT22 temperatur/fukt | Pluslåda | 1 | ★★★★☆ | Mäter temperatur och luftfuktighet. |
| S06 | DS18B20 temperatursensor | Pluslåda | 2 | ★★★★☆ | Robust temperatursensor som även kan användas med vattentät kapsling. |
| S07 | PIR-rörelsesensor | Pluslåda | 1 | ★★★★☆ | Känner av rörelse från varma kroppar. |
| S08 | Kapacitiv jordfuktighetssensor | Pluslåda | 1 | ★★★★☆ | Mäter ungefär hur fuktig jorden är. |
| S09 | Mikrofonmodul | Pluslåda | 1 | ★★★☆☆ | Känner av ljudnivå eller klapp. |
| L03 | NeoPixel-ring 16 LED | Pluslåda | 1 | ★★★★★ | Programmerbara RGB-lysdioder i ringform. |
| D02 | MAX7219 LED-matris 8x8 | Pluslåda | 1 | ★★★★☆ | Rutnät med 64 lysdioder för symboler och spel. |
| M01 | SG90 mikroservo | Pluslåda | 2 | ★★★★★ | Motor som går till en viss vinkel. |
| K03 | TTP229 touch-sensor | Pluslåda | 1 | ★★★★☆ | Flera touchknappar på en modul. |
| C01 | RFID RC522 | Makerlåda | 1 | ★★★☆☆ | Läser RFID-kort och taggar. |
| C02 | IR-mottagare + fjärrkontroll | Makerlåda | 1 | ★★★☆☆ | Tar emot signaler från fjärrkontroll. |
| D03 | DS3231 RTC | Makerlåda | 1 | ★★☆☆☆ | Håller reda på tid även när ESP32 startas om. |
| D04 | MicroSD-modul | Makerlåda | 1 | ★★☆☆☆ | Sparar mätdata på minneskort. |
| M02 | 28BYJ-48 stegmotor + ULN2003 | Makerlåda | 1 | ★★★☆☆ | Motor som kan röra sig i små steg. |
| M03 | DC-motor | Makerlåda | 2 | ★★★☆☆ | Enkel motor som snurrar när den får ström. |
| M04 | L9110S motordrivare | Makerlåda | 1 | ★★★☆☆ | Låter ESP32 styra DC-motorer åt båda håll. |
