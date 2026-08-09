# 5A.3 – Komponentintroduktion per kapitel

## Syfte

Denna vy visar vilka komponenter som bör introduceras eller få ny huvudroll i varje kapitel. Målet är att undvika att ett kapitel introducerar för många nya saker samtidigt.

| Kapitel | Nya huvudkomponenter | Återkommande komponenter | Kommentar |
|---:|---|---|---|
| 1 | ESP32, breadboard, LED, motstånd | – | Första fungerande kretsen |
| 2 | RGB-LED, PWM som princip | LED, motstånd | Färg och ljusstyrka |
| 3 | tryckknapp | LED, RGB | Barnet styr systemet |
| 4 | passiv buzzer | knapp, LED, RGB | Ljud och spel |
| 5 | LDR, HC-SR04 | LED, RGB, buzzer | Första mätinstrumenten |
| 6 | reedkontakt, tilt, PIR | RGB, buzzer | Händelsesensorer och larm |
| 7 | DHT22, DS18B20, jordfukt, mikrofon | OLED, RGB | Miljö och kalibrering |
| 8 | OLED som huvudkomponent | sensorer, knapp | Användargränssnitt |
| 9 | LED-matris, NeoPixel | knapp, buzzer | Animation och ljuseffekter |
| 10 | servo | sensorer, OLED, RGB | Fysisk rörelse |
| 11 | DC-motor, motordrivare, stegmotor | HC-SR04, potentiometer | Robotik och säkerhet |
| 12 | RFID, IR | RGB, buzzer, servo | Identifiering och fjärrstyrning |
| 13 | RTC, MicroSD, WiFi | OLED, DHT22 | Tid, data och nätverk |
| 14 | inga nya krav | alla tidigare | Eget skapande |

---

# Kapiteldesignregel

Om ett kapitel introducerar fler än två nya komponentfamiljer bör experimenten delas upp så att varje komponent först testas ensam innan den kombineras.

Särskilt viktigt för:

- Kapitel 7
- Kapitel 11
- Kapitel 13
