# 5A.4 – Breadboardbilder och standardkopplingar

## Syfte

Detta dokument listar de breadboardbilder som bör fungera som standardkopplingar genom boken.

---

# Standardbilder

| ID | Namn | Används i kapitel | Kommentar |
|---|---|---|---|
| BB-A01 | ESP32 på breadboard | 1–14 | basbild |
| BB-A02 | LED + motstånd | 1–6 | första standard-output |
| BB-A03 | flera LED | 1–4 | ljusmönster |
| BB-A04 | RGB-LED | 2–14 | statusfärg |
| BB-A05 | knapp + LED | 3–14 | standard-input |
| BB-A06 | knapp + LED + buzzer | 4–14 | spel/larm-output |
| BB-A07 | LDR-spänningsdelare | 5–14 | analog sensor |
| BB-A08 | HC-SR04 | 5, 10, 11 | avstånd |
| BB-A09 | reedkontakt | 6, 12, 14 | larm |
| BB-A10 | PIR | 6, 10, 14 | närvaro |
| BB-A11 | DHT22 | 7, 13, 14 | miljö |
| BB-A12 | OLED I²C | 8–14 | display |
| BB-A13 | NeoPixel | 9–14 | ljuseffekt |
| BB-A14 | servo | 10, 12, 14 | rörelse |
| BB-A15 | DC-motor + drivare | 11, 14 | motor/säkerhet |
| BB-A16 | RFID | 12, 14 | identifiering |
| BB-A17 | RTC + OLED | 13, 14 | tid |
| BB-A18 | MicroSD | 13, 14 | loggning |

---

# Lägg-till-bilder

Lägg-till-bilder bör skapas för följande progressioner:

| Från | Till | Bildsyfte |
|---|---|---|
| LED | LED + knapp | visa input läggs till |
| knapp + LED | knapp + LED + buzzer | visa ljud läggs till |
| LED/RGB | LDR + LED/RGB | visa sensor läggs till |
| HC-SR04 + buzzer | HC-SR04 + RGB | visa annan output |
| OLED ensam | OLED + sensor | visa display + mätvärde |
| servo ensam | servo + sensor | visa fysisk output styrs av input |
| RFID ensam | RFID + servo/RGB | visa identifiering styr output |
| RTC + OLED | RTC + sensor + SD | visa loggningssystem |

---

# Teknisk kontroll

Varje breadboardbild ska kontrolleras mot:

- ESP32 3,3V-logik,
- rätt GND,
- rätt motstånd,
- rimlig pinne,
- ingen motor direkt på GPIO,
- I²C/SPI-pinnar konsekventa,
- inga oavsiktliga kortslutningar på breadboard.

Teknisk kontroll bör göras innan bilden markeras som slutbild.
