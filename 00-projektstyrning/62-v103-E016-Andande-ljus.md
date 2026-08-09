# v103 – E016 Andande ljus

Denna version skapar första fullständiga utkastet till E016.

## Skapade filer

- `07-experimentutkast/kapitel-02/E016-Andande-ljus.md`
- `08-illustrationer-och-kopplingar/generated/E016/E016-A-dagens-delar.svg`
- `08-illustrationer-och-kopplingar/generated/E016/E016-B-kopplingsoversikt.svg`
- `08-illustrationer-och-kopplingar/generated/E016/E016-C-andningssekvens.svg`
- `08-illustrationer-och-kopplingar/generated/E016/E016-D-loop-upp-och-ned.svg`
- `08-illustrationer-och-kopplingar/circuits/E016-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E016-diagram.json`
- `08-illustrationer-och-kopplingar/briefs/E016-bildpipeline-brief.md`
- `08-illustrationer-och-kopplingar/prompts/E016-image-prompts.md`

PNG-renderingar finns för E016-bilderna.

## Progressionsbedömning enligt v83

E016 bedöms fungera som eget huvudexperiment och som kapitelavslutande effekt.

Det återanvänder E015-kopplingen men tillför ett nytt huvudkoncept:

- PWM-värdet räknas upp och ned,
- `for`-loop används som långsam förändring,
- ljuset blir en mjukare visuell effekt,
- Kapitel 2 sammanfattas med ett konkret andande ljus.

## Tekniskt observandum

Manuset använder samma `analogWrite()`-modell som E015.

Det tekniska beslutet om `analogWrite()` kontra ESP32:s LEDC/PWM-API kvarstår och bör granskas samlat för hela Kapitel 2.

## Kvar att göra

- Fysisk breadboardtest.
- Kompilera/verifiera koden i vald ESP32-miljö.
- Teknisk granskning av `analogWrite()`-valet.
- Pedagogisk granskning.
- PDF-layoutgranskning.
