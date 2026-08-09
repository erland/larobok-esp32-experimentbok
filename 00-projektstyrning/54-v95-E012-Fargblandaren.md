# v95 – E012 Färgblandaren

Denna version skapar första fullständiga utkastet till E012.

## Skapade filer

- `07-experimentutkast/kapitel-02/E012-Fargblandaren.md`
- `08-illustrationer-och-kopplingar/generated/E012/E012-A-dagens-delar.svg`
- `08-illustrationer-och-kopplingar/generated/E012/E012-B-kopplingsoversikt.svg`
- `08-illustrationer-och-kopplingar/generated/E012/E012-C-fargrecept.svg`
- `08-illustrationer-och-kopplingar/generated/E012/E012-D-pwm-snabb-blinkning.svg`
- `08-illustrationer-och-kopplingar/circuits/E012-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E012-diagram.json`
- `08-illustrationer-och-kopplingar/briefs/E012-bildpipeline-brief.md`
- `08-illustrationer-och-kopplingar/prompts/E012-image-prompts.md`

PNG-renderingar finns för E012-bilderna.

## Progressionsbedömning enligt v83

E012 bedöms fungera som eget huvudexperiment.

Det återanvänder E011-kopplingen men tillför ett nytt huvudkoncept:

- PWM/0–255-ljusstyrka,
- färgrecept med tre RGB-värden,
- blandning av färgkanaler.

Det är därför ett tydligt nytt kod- och förståelsesteg.

## Tekniskt observandum

Manuset använder `analogWrite()` som barnvänlig ingång till PWM.

Detta behöver verifieras mot vald ESP32/Arduino-version i teknisk granskning. Om `analogWrite()` inte fungerar i den valda miljön behöver E012 bytas till ESP32:s LEDC/PWM-API, men den pedagogiska 0–255-modellen bör behållas.

## Kvar att göra

- Fysisk breadboardtest.
- Kompilera/verifiera koden i vald ESP32-miljö.
- Teknisk granskning av `analogWrite()`-valet.
- Pedagogisk granskning.
- PDF-layoutgranskning.
