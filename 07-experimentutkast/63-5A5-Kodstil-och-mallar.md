# 5A.5 – Kodstil och mallar

## Grundstil

Kod ska vara:

- kort,
- konsekvent,
- barnvänligt kommenterad,
- lätt att ändra,
- uppbyggd i små steg.

---

# Namnstandard

| Typ | Exempel |
|---|---|
| pinne | `ledPin`, `buttonPin`, `buzzerPin` |
| sensorvärde | `lightValue`, `soundValue`, `moistureValue` |
| status | `isOn`, `alarmActive`, `isLocked` |
| tid | `startTime`, `reactionTime`, `lastBlinkTime` |
| funktion | `turnLedOn()`, `playBeep()`, `showStatus()` |

---

# Experimentkodens mall

```cpp
// Experiment E0XX – Namn
// Kort mening om vad programmet gör.

const int ledPin = 5;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Här händer experimentets huvudidé.
}
```

---

# När funktioner introduceras

Funktioner bör introduceras när samma kod upprepas flera gånger.

De ska inte introduceras bara för att koden ska bli "snygg" för vuxna.

---

# När arrayer introduceras

Arrayer bör introduceras i lekfulla sammanhang:

- LED-sekvenser,
- melodier,
- Simon Says,
- LED-matris,
- NeoPixel.

---

# När `millis()` introduceras

`millis()` bör introduceras när `delay()` begränsar vad projektet kan göra:

- blink utan delay,
- reaktionsspel,
- flera saker samtidigt,
- larm som återställs efter en stund.

---

# Kodblock i boken

Varje längre kodexempel bör följas av:

1. Testa detta först
2. Ändra detta
3. Vad händer?
4. Vanliga fel

Det gör att barnet inte bara kopierar kod utan experimenterar.
