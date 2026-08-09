# ESP32 Experimentbok – Standardiserad experimentlåda v3

## Syfte

Detta dokument definierar bokens standardlåda. Målet är att 50–100 experiment ska kunna byggas med en begränsad uppsättning billiga, lättillgängliga och breadboard-vänliga komponenter.

## Plattform

Boken baseras på **ESP32 DevKit** med Arduino IDE.

Motiv:

- Billig och lätt att få tag i.
- Inbyggt WiFi och Bluetooth.
- Många GPIO-pinnar.
- Flera analoga ingångar.
- Bra stöd i Arduino IDE.
- Mer framtidssäker än ESP8266/NodeMCU.

## Nivåer

| Nivå | Mål | Ungefärligt antal experiment |
|---|---|---:|
| Baslåda | Kom igång billigt | 35–40 |
| Pluslåda | Sensorer, rörelse och mer lek | 60–70 |
| Makerlåda | IoT, robotik och mer avancerade projekt | 80–100 |

## Designprinciper

- Återanvänd samma komponenter i många experiment.
- Introducera helst bara en ny komponent åt gången.
- Använd breadboard i huvudspåret.
- Undvik lödkrav i grundexperimenten.
- Undvik 230V, litiumladdning och andra riskmoment.
- Märk varje komponent med ett fast ID.
- Låt varje experiment hänvisa till komponent-ID istället för långa komponentnamn.
