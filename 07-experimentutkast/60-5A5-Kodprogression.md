# 5A.5 – Kodprogression

## Syfte

Detta dokument beskriver hur programmeringsinnehållet ska utvecklas genom boken. Målet är att barnet gradvis ska känna igen kodmönster, förstå varför koden behövs och kunna ändra små delar själv.

Kodprogressionen ska säkerställa att:

- kodexempel inte blir för långa för tidigt,
- nya begrepp introduceras i rätt ordning,
- bibliotek inte används innan de behövs,
- återkommande kodmönster känns bekanta,
- senare projekt kan bygga vidare på tidigare kod.

---

# Grundprinciper

## 1. Kod ska följa byggandet

Barnet ska först se vad kretsen gör, sedan förstå koden.

```text
Bygg
  ↓
Kör kod
  ↓
Se effekt
  ↓
Ändra ett värde
  ↓
Förstå principen
```

## 2. En ny kodidé per experiment

Ett experiment får gärna repetera tidigare idéer, men bör bara introducera en ny huvudidé.

## 3. Kort kod först

Tidiga kodexempel ska vara mycket korta och hellre repetitiva än abstrakta. Funktioner, arrayer och mer strukturerad kod introduceras senare.

## 4. Kommentarer ska förklara avsikt

Kommentarer ska förklara varför något görs, inte bara översätta kodraden.

## 5. Samma namn ska återkomma

| Sak | Rekommenderat namn |
|---|---|
| LED-pin | `ledPin` |
| knapp-pin | `buttonPin` |
| buzzer-pin | `buzzerPin` |
| sensorvärde | `sensorValue` |
| ljusvärde | `lightValue` |
| avstånd | `distanceCm` |
| temperatur | `temperatureC` |
| tillstånd | `isOn`, `isLocked`, `alarmActive` |

---

# Kodens fyra utvecklingsfaser

## Fas 1 – Kommandon

- `setup()`
- `loop()`
- `pinMode()`
- `digitalWrite()`
- `delay()`

## Fas 2 – Beslut

- `digitalRead()`
- `if`
- `else`
- booleska värden
- tillståndsvariabler

## Fas 3 – Mönster och mätning

- variabler
- `for`
- arrayer
- `analogRead()`
- tröskelvärden
- Seriell monitor
- `millis()`

## Fas 4 – System

- bibliotek
- funktioner
- skärmlägen
- tillståndsmaskiner
- filskrivning
- WiFi
- enkel webbserver

---

# Kodlängd

| Del av boken | Rekommenderad kodlängd |
|---|---|
| Kapitel 1–2 | 10–30 rader |
| Kapitel 3–4 | 20–60 rader |
| Kapitel 5–7 | 30–80 rader |
| Kapitel 8–10 | 50–120 rader |
| Kapitel 11–13 | 70–160 rader |
| Kapitel 14 | varierar, helst byggt i små moduler |

Om koden blir längre än rekommenderat ska experimentet delas upp eller introducera en förenklad första version.
