# Steg 2 – Färdighetskarta

## Syfte

Färdighetskartan beskriver vilka kunskaper boken ska bygga upp genom experimenten. Den fungerar som en läroplan, men ska användas praktiskt: varje experiment ska kunna kopplas till ett fåtal tydliga färdigheter.

Målet är inte att barnet ska läsa en teorikurs, utan att färdigheterna ska växa fram genom att bygga, testa och förbättra saker.

---

# Färdighetsområden

Bokens färdigheter delas in i fyra huvudområden:

| Område | Innehåll |
|---|---|
| Elektronik | komponenter, kopplingar, signaler och ström |
| Programmering | kod, logik, variabler och struktur |
| Maker/felsökning | bygga, testa, mäta och förbättra |
| Tillämpningar | spel, smarta prylar, robotik och IoT |

---

# A. Elektronik

| ID | Färdighet | Introduceras ungefär | Kommentar |
|---|---|---|---|
| EL01 | Förstå plus, minus och jord | Baslåda tidigt | Absolut grundfärdighet |
| EL02 | Använda breadboard | Baslåda tidigt | Måste övas många gånger |
| EL03 | Koppla LED med motstånd | Baslåda tidigt | Första konkreta kretsen |
| EL04 | Förstå digital output | Baslåda tidigt | Tända/släcka LED |
| EL05 | Förstå digital input | Baslåda tidigt | Knappar och sensorer |
| EL06 | Använda pullup/pulldown | Baslåda | Kan först döljas via `INPUT_PULLUP` |
| EL07 | Läsa analog signal | Baslåda | Potentiometer och LDR |
| EL08 | Spänningsdelare på enkel nivå | Baslåda | LDR och vissa sensorer |
| EL09 | PWM som “låtsas-analog” output | Baslåda | Dimma LED, styra ljud/servo |
| EL10 | Toner och frekvens | Baslåda | Buzzer och musik |
| EL11 | Avståndsmätning med ultraljud | Baslåda | HC-SR04 |
| EL12 | Magnetisk brytare | Baslåda | Reedkontakt |
| EL13 | Lutning/skakning som digital signal | Baslåda | Tilt-sensor |
| EL14 | I²C på introduktionsnivå | Baslåda/Pluslåda | OLED och senare moduler |
| EL15 | Temperatur och luftfuktighet | Pluslåda | DHT22/DS18B20 |
| EL16 | Rörelsedetektering | Pluslåda | PIR |
| EL17 | Kapacitiv touch | Pluslåda | Touchpanel |
| EL18 | Programmerbara RGB-LED | Pluslåda | NeoPixel |
| EL19 | LED-matris | Pluslåda | MAX7219 |
| EL20 | Servostyrning | Pluslåda | SG90 |
| EL21 | Motorstyrning via drivare | Makerlåda | DC-motor, L9110S |
| EL22 | Stegmotorprincip | Makerlåda | 28BYJ-48 |
| EL23 | RFID på konceptnivå | Makerlåda | RC522 |
| EL24 | IR-fjärrstyrning | Makerlåda | IR-kit |
| EL25 | Tid med RTC | Makerlåda | DS3231 |
| EL26 | Dataloggning till fil | Makerlåda | MicroSD |

---

# B. Programmering

| ID | Färdighet | Introduceras ungefär | Kommentar |
|---|---|---|---|
| PR01 | Förstå `setup()` och `loop()` | Första experimentet | Huvudmönster i Arduino |
| PR02 | Använda `pinMode()` | Första experimentet | Kopplar kod till pinnar |
| PR03 | Använda `digitalWrite()` | Första experimentet | Styra LED |
| PR04 | Använda `delay()` | Första experimentet | Enkel tid |
| PR05 | Variabler | Tidigt | Spara pin-nummer och värden |
| PR06 | Läsa knapp med `digitalRead()` | Tidigt | Digital input |
| PR07 | `if`-satser | Tidigt | Reagera på knapp/sensor |
| PR08 | Booleska värden | Tidigt | På/av, sant/falskt |
| PR09 | Räkna poäng eller tryck | Baslåda | Spel och räknare |
| PR10 | Slumptal | Baslåda | Tärning och spel |
| PR11 | Funktioner | Baslåda | Återanvänd kod |
| PR12 | `for`-loopar | Baslåda | LED-sekvenser, melodier |
| PR13 | Arrayer | Baslåda/Pluslåda | Melodier, färger, spel |
| PR14 | `analogRead()` | Baslåda | Potentiometer, LDR |
| PR15 | `analogWrite()`/PWM | Baslåda | Dimning och styrning |
| PR16 | `millis()` utan blockering | Baslåda/Pluslåda | Viktigt för spel och flera saker samtidigt |
| PR17 | Enkla tillstånd | Pluslåda | Start, spel, slut |
| PR18 | Tillståndsmaskin | Pluslåda | Trafikljus, spel, larm |
| PR19 | Bibliotek | Pluslåda | OLED, DHT, NeoPixel |
| PR20 | Seriell monitor | Baslåda | Felsökning och mätvärden |
| PR21 | Strängar och text | Pluslåda | OLED och webb |
| PR22 | Enkel grafik | Pluslåda | OLED/matris |
| PR23 | Enkel datalogik | Makerlåda | Mätningar över tid |
| PR24 | WiFi-anslutning | Maker/IoT | Internetprojekt |
| PR25 | Enkel webbserver | Maker/IoT | Styra via mobil |
| PR26 | Skicka/läsa data över nätverk | Maker/IoT | Senare IoT-projekt |

---

# C. Maker, felsökning och arbetssätt

| ID | Färdighet | Introduceras ungefär | Kommentar |
|---|---|---|---|
| MK01 | Läsa komponent-ID och plocka rätt delar | Direkt | Stärker självständighet |
| MK02 | Följa en breadboardbild | Direkt | Central praktisk färdighet |
| MK03 | Kontrollera polaritet | Direkt | LED, matning, moduler |
| MK04 | Färgkoda kablar | Direkt | Gör felsökning enklare |
| MK05 | Testa en sak i taget | Tidigt | Undviker stora fel |
| MK06 | Använda felsökningsruta | Tidigt | Normaliserar fel |
| MK07 | Läsa värden i Seriell monitor | Baslåda | Förstå sensorer |
| MK08 | Ändra ett värde och observera skillnaden | Baslåda | Experimentellt tänkande |
| MK09 | Kalibrera tröskelvärden | Baslåda/Pluslåda | LDR, ljud, jordfukt |
| MK10 | Dokumentera vad som fungerade | Pluslåda | Förbereder datalogger |
| MK11 | Kombinera två tidigare projekt | Pluslåda | Uppfinnarnivå |
| MK12 | Designa egen variant | Pluslåda/Maker | Mästarnivå |
| MK13 | Bedöma strömbehov | Makerlåda | Motorer och LED |
| MK14 | Dela upp problem i mindre delar | Genom hela boken | Viktig ingenjörsfärdighet |
| MK15 | Förklara sin lösning för någon annan | Genom hela boken | Fördjupar förståelsen |

---

# D. Tillämpningar

| ID | Färdighet | Introduceras ungefär | Kommentar |
|---|---|---|---|
| AP01 | Bygga signaler och indikatorer | Baslåda | LED, buzzer |
| AP02 | Bygga enkla spel | Baslåda | Reaktion, tärning, Simon |
| AP03 | Bygga larm | Baslåda | Reed, tilt, PIR |
| AP04 | Bygga mätinstrument | Baslåda/Pluslåda | Ljus, avstånd, temperatur |
| AP05 | Bygga interaktiva displayer | Baslåda/Pluslåda | OLED/matris |
| AP06 | Bygga ljud- och musikprojekt | Baslåda | Buzzer |
| AP07 | Bygga rörelseprojekt | Pluslåda | Servo |
| AP08 | Bygga smarta hem-liknande projekt | Pluslåda/Maker | larm, ljus, växter |
| AP09 | Bygga robotliknande projekt | Makerlåda | motorer och sensorer |
| AP10 | Bygga IoT-projekt | Makerlåda | WiFi |
| AP11 | Bygga uppdrag/escape-room-mekanik | Makerlåda | RFID, kodlås, sensorer |
| AP12 | Kombinera mätning, beslut och handling | Pluslåda/Maker | smarta uppfinningar |

---

# Användning i nästa steg

När Experimentbanken skapas bör varje experiment märkas med:

- 1–3 elektronikfärdigheter,
- 1–3 programmeringsfärdigheter,
- 1–2 maker/felsökningsfärdigheter,
- eventuell tillämpningskategori.

Exempel:

| Experiment | Färdigheter |
|---|---|
| Blinkande LED | EL01, EL02, EL03, EL04, PR01, PR02, PR03, PR04, MK02 |
| Reaktionsspel | EL05, PR06, PR07, PR09, PR16, AP02 |
| Smart blomkruka | EL07, EL15, MK09, PR14, AP08 |
