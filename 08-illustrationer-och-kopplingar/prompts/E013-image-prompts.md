# E013 image prompts – Regnbågslampan

## Övergripande stil

Följ komponentbiblioteket och E011/E012-bilderna:

- ljus bakgrund,
- korta etiketter,
- tydliga färgkort,
- enkel, barnvänlig begreppsbild,
- lugn PDF-läsbar layout.

## E013-A – Dagens delar

Samma delar som E011/E012: ESP32 DevKit, breadboard, RGB-LED, tre motstånd, kopplingskablar och USB.

## E013-B – Kopplingsöversikt

Samma koppling som E011/E012:

- GPIO 23 → motstånd → rött ben,
- GPIO 22 → motstånd → grönt ben,
- GPIO 21 → motstånd → blått ben,
- gemensamt ben → GND.

## E013-C – Regnbågssekvens

Visa en tydlig färd genom flera färger, till exempel:

- röd,
- orange,
- gul,
- grön,
- turkos,
- blå,
- lila.

Använd pilar mellan stegen och en loop-pil tillbaka till början.

## E013-D – Små steg ger mjuk färg

Visa 3–4 färgsteg där ett RGB-värde ändras lite i taget, till exempel:

- 255, 0, 0
- 255, 80, 0
- 255, 180, 0
- 255, 255, 0

Budskapet ska vara:

> Små ändringar i RGB-talen gör att färgen förändras steg för steg.

# v98 – puts av regnbågsbilder

E013-C ska ha en lugn loop-pil som inte dominerar färgkorten.

E013-D ska använda kort förklarande text. Prioritera formuleringen:

> färgen flyttar sig steg för steg

framför längre tekniska eller abstrakta meningar.
