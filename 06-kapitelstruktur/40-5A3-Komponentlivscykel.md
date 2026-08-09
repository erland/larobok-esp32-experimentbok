# 5A.3 – Komponentlivscykel

## Syfte

Detta steg beskriver när varje komponent introduceras, hur den återkommer, när den bör sitta kvar på breadboarden och om den hör hemma i huvudspår, bonus eller fördjupning.

Komponentlivscykeln kompletterar breadboard-progressionen. Där 5A.2 svarade på frågan:

> Hur utvecklas kopplingarna?

svarar 5A.3 på frågan:

> När kommer varje komponent in i barnets verktygslåda, och hur länge är den relevant?

---

# Livscykelprinciper

## 1. Komponenter ska bli bekanta

En komponent som används ofta bör introduceras tidigt, få ett namn och återkomma i många olika sammanhang. Barnet ska känna igen den och förstå att den är ett verktyg, inte bara en engångsgrej.

## 2. Nya komponenter ska ha ett uppdrag

En ny komponent bör helst introduceras genom ett experiment där dess funktion är tydlig och rolig.

Exempel:

- LED: första blinket
- knapp: barnet styr lampan
- LDR: nattlampa
- HC-SR04: parkeringssensor
- servo: skattkista eller visare
- RFID: hemlig nyckel

## 3. Makerkomponenter ska inte bära huvudboken

Komponenter i Makerlådan bör i första hand användas i senare kapitel, bonusprojekt eller fördjupning. De ska inte vara nödvändiga för att barnet ska förstå bokens grundprogression.

## 4. Output-komponenter bör återkomma ofta

Följande komponenter bör behandlas som återkommande språk i boken:

- LED
- RGB-LED
- buzzer
- OLED
- NeoPixel
- servo

De hjälper barnet att se resultat från olika sensorer.

## 5. Sensorer bör kopplas till handling

Sensorer ska inte bara visa värden. Efter en ren mätning bör komponenten återkomma i ett experiment där den styr något.

---

# Rekommenderade komponentroller

| Roll | Beskrivning | Exempel |
|---|---|---|
| Permanent bas | Används nästan alltid | ESP32, breadboard, kablar, motstånd |
| Standard-output | Återkommer för synlig/hörbar feedback | LED, RGB, buzzer, OLED |
| Standard-input | Återkommer som styrning | knapp, potentiometer |
| Sensorblock | Introduceras i tematiska block | LDR, HC-SR04, DHT22, PIR |
| Fysisk output | Skapar rörelse | servo, DC-motor |
| Fördjupning | Avancerad eller mer specialiserad | RFID, IR, RTC, SD, WiFi |
| Bonus | Rolig men inte nödvändig | stegmotor, touchsensor |

---

# Pedagogisk rekommendation

Varje komponent bör få tre tydliga ögonblick:

1. **Möt komponenten** – vad gör den?
2. **Använd komponenten** – bygg något konkret.
3. **Återanvänd komponenten** – kombinera den med något tidigare.

Exempel:

```text
HC-SR04
  ↓
Möt: visa avstånd i Seriell monitor
  ↓
Använd: parkeringssensor
  ↓
Återanvänd: robot undviker hinder
```
