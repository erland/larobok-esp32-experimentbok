# v101 – E015 Dimbar LED

Denna version skapar första fullständiga utkastet till E015.

## Skapade filer

- `07-experimentutkast/kapitel-02/E015-Dimbar-LED.md`
- `08-illustrationer-och-kopplingar/generated/E015/E015-A-dagens-delar.svg`
- `08-illustrationer-och-kopplingar/generated/E015/E015-B-kopplingsoversikt.svg`
- `08-illustrationer-och-kopplingar/generated/E015/E015-C-ljusstyrkenivaer.svg`
- `08-illustrationer-och-kopplingar/generated/E015/E015-D-pwm-pa-en-led.svg`
- `08-illustrationer-och-kopplingar/circuits/E015-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E015-diagram.json`
- `08-illustrationer-och-kopplingar/briefs/E015-bildpipeline-brief.md`
- `08-illustrationer-och-kopplingar/prompts/E015-image-prompts.md`

PNG-renderingar finns för E015-bilderna.

## Progressionsbedömning enligt v83

E015 bedöms fungera som eget huvudexperiment trots att kopplingen är enklare än E011–E014.

Det återvänder till en vanlig LED för att isolera PWM-idén:

- ett värde styr ljusstyrkan,
- ingen RGB-blandning stör observationen,
- barnet kan jämföra av/svag/mellan/stark,
- E016 Andande ljus får en tydlig förberedelse.

Det är därför ett förtydligande steg, inte en repetition av E001.

## Tekniskt observandum

Manuset använder samma `analogWrite()`-modell som E012–E014.

Det tekniska beslutet om `analogWrite()` kontra ESP32:s LEDC/PWM-API kvarstår och bör granskas samlat för hela Kapitel 2.

## Kvar att göra

- Fysisk breadboardtest.
- Kompilera/verifiera koden i vald ESP32-miljö.
- Teknisk granskning av `analogWrite()`-valet.
- Pedagogisk granskning.
- PDF-layoutgranskning.
