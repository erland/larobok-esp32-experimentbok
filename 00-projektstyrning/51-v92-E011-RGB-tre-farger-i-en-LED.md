# v92 – E011 RGB: tre färger i en LED

Denna version skapar första fullständiga utkastet till E011.

## Strategiskt beslut från v91 till v92

Efter granskning beslutades att:

- E009 inte ska drivas vidare som aktivt experiment i huvudflödet,
- E010 inte ska produceras i aktiv Kapitel 2-produktion just nu,
- huvudspåret i Kapitel 2 går vidare direkt till E011.

E009 kan ligga kvar som arkiverat bonusutkast, men är inte nästa produktionssteg.

## Skapade filer

- `07-experimentutkast/kapitel-02/E011-RGB-tre-farger-i-en-LED.md`
- `08-illustrationer-och-kopplingar/generated/E011/E011-A-dagens-delar.svg`
- `08-illustrationer-och-kopplingar/generated/E011/E011-B-kopplingsoversikt.svg`
- `08-illustrationer-och-kopplingar/generated/E011/E011-C-tre-farger-sekvens.svg`
- `08-illustrationer-och-kopplingar/generated/E011/E011-D-rgb-i-en-kapsel.svg`
- `08-illustrationer-och-kopplingar/circuits/E011-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E011-diagram.json`
- `08-illustrationer-och-kopplingar/briefs/E011-bildpipeline-brief.md`
- `08-illustrationer-och-kopplingar/prompts/E011-image-prompts.md`

PNG-renderingar skapades för E011-bilderna.

## Pedagogisk roll

E011 introducerar en tydligt ny komponent och ett nytt begrepp:

- en LED kan innehålla flera färgkanaler,
- tre GPIO-pinnar kan styra samma kapsel,
- färgblandning förbereds men förklaras fullt ut först i E012.

## Kvar att göra

- fysisk breadboardtest,
- kompilering/verifiering i vald ESP32-miljö,
- teknisk granskning,
- pedagogisk granskning,
- PDF-layoutgranskning.
