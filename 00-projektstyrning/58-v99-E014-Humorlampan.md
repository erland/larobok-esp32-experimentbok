# v99 – E014 Humörlampan

Denna version skapar första fullständiga utkastet till E014.

## Skapade filer

- `07-experimentutkast/kapitel-02/E014-Humorlampan.md`
- `08-illustrationer-och-kopplingar/generated/E014/E014-A-dagens-delar.svg`
- `08-illustrationer-och-kopplingar/generated/E014/E014-B-kopplingsoversikt.svg`
- `08-illustrationer-och-kopplingar/generated/E014/E014-C-humorsekvens.svg`
- `08-illustrationer-och-kopplingar/generated/E014/E014-D-farg-som-status.svg`
- `08-illustrationer-och-kopplingar/circuits/E014-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E014-diagram.json`
- `08-illustrationer-och-kopplingar/briefs/E014-bildpipeline-brief.md`
- `08-illustrationer-och-kopplingar/prompts/E014-image-prompts.md`

PNG-renderingar finns för E014-bilderna.

## Progressionsbedömning enligt v83

E014 bedöms fungera som eget huvudexperiment.

Det återanvänder RGB-LED-kopplingen och `setColor()`-modellen men tillför ett nytt användningssätt:

- färg som betydelse,
- färg som humör/status,
- namngivna funktioner som `glad()`, `lugn()` och `varning()`,
- brygga mot statuslampor, sensorer och smarta prylar.

Det är därför inte bara en ny färgsekvens utan ett nytt sätt att tänka om färg.

## Tekniskt observandum

Manuset använder samma `setColor()`/`analogWrite()`-modell som E012/E013.

Det tekniska beslutet om `analogWrite()` kontra ESP32:s LEDC/PWM-API kvarstår och bör granskas samlat för hela RGB-spåret.

## Kvar att göra

- Fysisk breadboardtest.
- Kompilera/verifiera koden i vald ESP32-miljö.
- Teknisk granskning av `analogWrite()`-valet.
- Pedagogisk granskning.
- PDF-layoutgranskning.
