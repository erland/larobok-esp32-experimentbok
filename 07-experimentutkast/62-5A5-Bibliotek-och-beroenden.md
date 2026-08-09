# 5A.5 – Bibliotek och externa beroenden

## Syfte

Detta dokument listar vilka bibliotek och externa kodberoenden som kan behövas, och när de bör introduceras.

Målet är att undvika att bibliotek blir magiska hinder. Varje bibliotek ska introduceras först när det behövs och med ett mycket litet första exempel.

---

# Rekommenderade bibliotek

| Område | Komponent | Exempel på bibliotek | Introduktion |
|---|---|---|---|
| OLED | D01 | Adafruit SSD1306 / Adafruit GFX | Kapitel 8 |
| DHT | S05 | DHT sensor library | Kapitel 7 |
| DS18B20 | S06 | OneWire + DallasTemperature | Kapitel 7 |
| NeoPixel | L03 | Adafruit NeoPixel | Kapitel 9 |
| LED-matris | D02 | LedControl / MD_MAX72XX | Kapitel 9 |
| Servo | M01 | ESP32Servo eller Servo-kompatibelt bibliotek | Kapitel 10 |
| RFID | C01 | MFRC522 | Kapitel 12 |
| IR | C02 | IRremote / IRremoteESP8266 | Kapitel 12 |
| RTC | D03 | RTClib | Kapitel 13 |
| MicroSD | D04 | SD / SPI | Kapitel 13 |
| WiFi | ESP32 | WiFi.h / WebServer.h | Kapitel 13 |

---

# Introduktionsprincip

Varje bibliotek bör introduceras i tre steg:

1. Installera/inkludera – kort vuxenstöd.
2. Minsta exempel – kontrollera att komponenten svarar.
3. Använd i projekt – koppla till bokens logik.

Exempel:

```text
OLED
  ↓
visa "Hej"
  ↓
visa sensorvärde
  ↓
bygg instrumentpanel
```

---

# Biblioteksrisker

| Risk | Motåtgärd |
|---|---|
| Olika bibliotek har olika API | välj ett standardspår |
| Exempel från nätet är för långa | skriv egna minimala exempel |
| Installation varierar | ha vuxenruta |
| Versioner ändras | håll koden enkel och dokumentera bibliotek |
| WiFi och SD kan krångla | lägg som avancerat block |

---

# Regel för kodexempel

Kodexempel i boken ska inte bara vara kopierade från bibliotekens exempel. De ska vara omskrivna till bokens stil:

- korta namn,
- få rader,
- barnvänliga kommentarer,
- tydlig koppling till experimentet.
