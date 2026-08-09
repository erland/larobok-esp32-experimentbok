# Steg 1 – Kostnadsöversikt v1

## Antaganden

Priserna är ungefärliga och baseras på lågprisinköp från internationella komponentbutiker eller marknadsplatser. Svenska återförsäljare kan ofta vara 2–4 gånger dyrare, men ger snabbare leverans och enklare reklamation.

Kostnaderna ska ses som planeringsvärden, inte exakta inköpspriser.

---

# Kostnad per nivå

| Nivå | Tilläggskostnad | Ackumulerad kostnad |
|---|---:|---:|
| Baslåda | ca 450–600 kr | ca 450–600 kr |
| Pluslåda | ca 250–350 kr | ca 700–950 kr |
| Makerlåda | ca 200–300 kr | ca 900–1 250 kr |

---

# Baslåda

| Komponentgrupp | Ca-pris |
|---|---:|
| 2 × ESP32 DevKit | 140–200 kr |
| 2 × breadboard | 50–90 kr |
| Jumperkablar | 40–70 kr |
| Motstånd, LED, RGB-LED | 50–80 kr |
| Knappar, potentiometrar, buzzer | 50–80 kr |
| LDR, tilt, reed | 30–60 kr |
| 2 × HC-SR04 | 40–70 kr |
| OLED I²C | 40–70 kr |

**Summa:** ca 450–600 kr

---

# Pluslåda

| Komponentgrupp | Ca-pris |
|---|---:|
| Temperatur- och miljösensorer | 80–120 kr |
| PIR, mikrofon, jordfuktighet | 60–90 kr |
| NeoPixel-ring | 40–80 kr |
| MAX7219 LED-matris | 40–70 kr |
| 2 × SG90 servo | 50–80 kr |
| TTP229 touch-sensor | 20–40 kr |

**Summa:** ca 250–350 kr

---

# Makerlåda

| Komponentgrupp | Ca-pris |
|---|---:|
| RFID RC522 | 35–70 kr |
| IR-mottagare + fjärrkontroll | 25–50 kr |
| DS3231 RTC | 25–50 kr |
| MicroSD-modul | 25–50 kr |
| Stegmotor + ULN2003 | 35–70 kr |
| DC-motorer + L9110S | 40–80 kr |

**Summa:** ca 200–300 kr

---

# Kostnadsdrivare

De största kostnadsdrivarna är:

1. ESP32-korten
2. OLED/LED-matris/NeoPixel
3. servon och motorer
4. sensorer där man köper flera exemplar

## Möjlig besparing

Om man bara köper **ett** ESP32-kort i stället för två kan Baslådan minska med ungefär 70–100 kr.

Rekommendationen är ändå att ha två kort om budgeten tillåter, eftersom det ger reserv, enklare felsökning och möjlighet till framtida experiment med två enheter.
