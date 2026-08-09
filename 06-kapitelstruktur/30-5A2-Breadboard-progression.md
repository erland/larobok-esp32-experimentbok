# 5A.2 – Breadboard-progression

## Syfte

Detta dokument beskriver hur breadboard-kopplingarna bör utvecklas genom boken för att minska onödig ombyggnad, stärka progressionen och göra arbetet mer barnvänligt.

Målet är att barnet så ofta som möjligt ska känna:

> "Jag bygger vidare på det jag redan har."

i stället för:

> "Jag måste riva allt och börja om."

---

# Grundprinciper

## 1. Återanvänd output-sidan

Många experiment kan använda samma grundläggande outputs:

- LED
- RGB-LED
- buzzer
- OLED
- NeoPixel
- servo

När en ny sensor introduceras bör output-delen helst vara bekant.

## 2. Byt en sak i taget

Ett experiment bör helst ändra endast en av följande:

- ny sensor,
- ny output,
- ny kodidé,
- ny mekanisk konstruktion.

## 3. Separera ingång och utgång

Boken bör tänka i två halvor:

```text
Input/sensor  →  ESP32  →  output/reaktion
```

Det gör det enklare att byta LDR mot PIR eller knapp mot RFID utan att hela kopplingen ändras.

## 4. Skapa återkommande standardkopplingar

Följande standardkopplingar bör återkomma:

| Standardkoppling | Används i |
|---|---|
| LED + motstånd | Kapitel 1–6 |
| RGB-LED status | Kapitel 2–14 |
| Knapp med INPUT_PULLUP | Kapitel 3–14 |
| Buzzer | Kapitel 4–14 |
| OLED I²C | Kapitel 8–14 |
| Sensor + statusfärg | Kapitel 5–14 |
| Servo som lås/visare | Kapitel 10–14 |

## 5. Håll breadboard-layouten konsekvent

Rekommenderad layout:

| Zon | Placering | Innehåll |
|---|---|---|
| Vänster | Input | knappar och sensorer |
| Mitten | ESP32 | styrenhet |
| Höger | Output | LED, buzzer, servo, display |
| Överkant | Ström | 3,3V och GND |
| Nederkant | Tillfälliga moduler | experiment-specifika komponenter |

Detta gör bilder och instruktioner mer konsekventa.

---

# Övergripande progression

```text
Tom breadboard
  ↓
ESP32 + LED
  ↓
Flera LED
  ↓
RGB-LED
  ↓
Knapp
  ↓
Knapp + LED + buzzer
  ↓
Sensor + LED/RGB/buzzer
  ↓
Sensor + OLED
  ↓
Sensor + NeoPixel/matris
  ↓
Sensor + servo
  ↓
Motor/robot
  ↓
RFID/IR/tid/loggning/WiFi
  ↓
Eget makerprojekt
```

---

# Komponenter som bör sitta kvar länge

| Komponent | Rekommendation |
|---|---|
| LED + motstånd | Behåll ofta i Kapitel 1–6 |
| RGB-LED | Kan bli standardstatus från Kapitel 2 och framåt |
| Knapp | Behåll ofta från Kapitel 3 och framåt |
| Buzzer | Behåll ofta från Kapitel 4 och framåt |
| OLED | Kan bli standarddisplay från Kapitel 8 och framåt |
| Servo | Kan återanvändas i Kapitel 10, 12 och 14 |

---

# Komponenter som bör vara tillfälliga

| Komponent | Kommentar |
|---|---|
| HC-SR04 | Tar plats och används i block |
| PIR | Används i larm/smarta projekt, men behöver inte sitta kvar |
| MicroSD | Bör kopplas separat i dataloggningsblock |
| RFID RC522 | SPI-koppling, bör få eget tydligt block |
| Motorer | Ska inte blandas in i tidigare kapitel |
| Stegmotor | Bonus och bör ligga separat |

---

# Rekommendation inför illustrationer

Varje kapitel bör ha:

1. en första "ren" breadboardbild,
2. en bild där ny komponent läggs till,
3. en bild där föregående koppling återanvänds,
4. en slutbild för kapitelprojektet.

Undvik att varje experiment får en helt ny layout om samma koppling kan utvecklas stegvis.
