# v86 – E007 kopplingsbild: motståndsledare till LED-ben

Denna version gör en fokuserad bildkorrigering i E007-B.

## Problem

I PDF-previewen för Kapitel 2 såg det ut som att motståndens vänstra ledare inte gick ända fram till LED-lampornas korta ben.

## Ändring

I `E007-B-kopplingsoversikt.svg` har de tre vänstra motståndsledarna förlängts så att de visuellt möter LED-lampornas korta ben.

## Berörda filer

- `08-illustrationer-och-kopplingar/generated/E007/E007-B-kopplingsoversikt.svg`
- `08-illustrationer-och-kopplingar/generated/E007/E007-B-kopplingsoversikt.png`

## Oförändrat

- Manus är oförändrat.
- Kod är oförändrad.
- Kopplingsprincipen är oförändrad:
  `GPIO → LED långt ben → LED kort ben → motstånd → GND`.
