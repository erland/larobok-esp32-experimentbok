# v68 – lättviktigt komponentbibliotek

Denna version skapar ett första komponentbibliotek för illustrationerna i ESP32 Experimentbok.

## Syfte

Syftet är att göra framtida bilder mer konsekventa utan att införa ett tungt tekniskt system.

Biblioteket är i v68:

- manuellt,
- SVG-baserat,
- lätt att läsa,
- lätt att kopiera från,
- möjligt att automatisera senare om behov uppstår.

## Ny mapp

```text
08-illustrationer-och-kopplingar/component-library/
```

## Ingår

- `README.md`
- `design-principles.md`
- `components/`
- `patterns/`
- `examples/`

## Komponenter

Första uppsättningen komponenter:

- LED, tänd röd/gul/grön
- LED, släckt
- motstånd
- pil
- loop-pil
- kopplingskabel
- ESP32 DevKit
- breadboard

## Patterns

Första uppsättningen patterns:

- komponentkort
- sekvenssteg
- sekvensrad
- jämförelsepanel
- kopplingsrad

## Exempel

Exempelbilder visar hur biblioteket kan användas för sekvenser som liknar:

- E002: blink-blink-paus
- E003: två LED-lampor turas om
- E004: trafikljussekvens

## Viktig avgränsning

v68 ändrar inte befintliga bilder i manus. Den skapar ett designunderlag för E005 och framåt.

## Rekommenderad användning framåt

När E005 skapas bör nya bilder byggas med komponentbiblioteket som utgångspunkt. Om det fungerar bra kan vi senare backporta bildsystemet till E001–E004.
