# v97 – E013 Regnbågslampan

Denna version skapar första fullständiga utkastet till E013.

## Skapade filer

- `07-experimentutkast/kapitel-02/E013-Regnbagslampan.md`
- `08-illustrationer-och-kopplingar/generated/E013/E013-A-dagens-delar.svg`
- `08-illustrationer-och-kopplingar/generated/E013/E013-B-kopplingsoversikt.svg`
- `08-illustrationer-och-kopplingar/generated/E013/E013-C-regnbagssekvens.svg`
- `08-illustrationer-och-kopplingar/generated/E013/E013-D-sma-steg-ger-mjuk-farg.svg`
- `08-illustrationer-och-kopplingar/circuits/E013-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E013-diagram.json`
- `08-illustrationer-och-kopplingar/briefs/E013-bildpipeline-brief.md`
- `08-illustrationer-och-kopplingar/prompts/E013-image-prompts.md`

PNG-renderingar finns för E013-bilderna.

## Progressionsbedömning enligt v83

E013 bedöms fungera som eget huvudexperiment.

Det återanvänder E011/E012-kopplingen men tillför en ny huvudidé:

- längre färgsekvens,
- många små RGB-steg,
- mjukare färgövergångar,
- upplevelsen av en levande regnbågslampa.

Det är därför ett tydligt nytt upplevelse- och kodsteg.

## Tekniskt observandum

Manuset använder samma `setColor()`/`analogWrite()`-modell som E012.

Det tekniska beslutet om `analogWrite()` kontra ESP32:s LEDC/PWM-API kvarstår därför även för E013 och bör granskas samlat för hela RGB-spåret.

## Kvar att göra

- Fysisk breadboardtest.
- Kompilera/verifiera koden i vald ESP32-miljö.
- Teknisk granskning av `analogWrite()`-valet.
- Pedagogisk granskning.
- PDF-layoutgranskning.
