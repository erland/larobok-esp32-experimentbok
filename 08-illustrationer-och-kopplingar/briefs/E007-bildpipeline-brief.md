# E007 bildpipeline-brief – LED-stafett

## Status

Skapad i v84 som första fullständiga E007-utkast.

## Teknisk sanningskälla

- `08-illustrationer-och-kopplingar/circuits/E007-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E007-diagram.json`
- Manus: `07-experimentutkast/kapitel-02/E007-LED-stafett.md`

## Progressionskontroll enligt v83

E007 är motiverat som eget huvudexperiment trots att kopplingen liknar E004.

Skälet är att den nya huvudidén är **funktioner**:

- `lightOne(int pin)` introduceras som ett enkelt kodrecept,
- samma funktion används för flera LED,
- barnet kan ändra stafettens hastighet på ett ställe,
- E008 kan sedan bygga vidare med loop/array.

E007 är alltså inte bara en ny rytmvariant av E004, utan ett nytt kodsteg.

## Bildprincip

Följ komponentbiblioteket från v68/v69 och v78-standarden för kopplingsöversikter:

- kort text i bilder,
- tydliga LED-tillstånd,
- varje LED ska ha eget motstånd,
- signaltrådar ska visuellt gå till LED-benen,
- sekvensbilder ska visa tillstånd över tid,
- loop-pil ska gå från högersidan av sista steget till vänstersidan av första steget.

## Bilder

| ID | Fil | Syfte | Status |
|---|---|---|---|
| E007-A | `generated/E007/E007-A-dagens-delar.svg` | Dagens delar | Utkast |
| E007-B | `generated/E007/E007-B-kopplingsoversikt.svg` | Förenklad kopplingsöversikt | Utkast, återanvänder E004-standard |
| E007-C | `generated/E007/E007-C-stafettsekvens.svg` | Sekvens röd → gul → grön → gul | Utkast |
| E007-D | `generated/E007/E007-D-kodrecept.svg` | Förklarar funktionen som kodrecept | Utkast |

## Layoutgranskning som återstår

- Kontrollera att E007-D inte blir för tät i PDF.
- Kontrollera att E007-B känns konsekvent med E004 och v78-standarden.
- Kontrollera att kodexemplet inte blir för långt på en sida.

## v85-notis – pedagogisk puts

I v85 mjukades E007 upp pedagogiskt:

- barntexten förtydligar att `void lightOne(int pin)` inte behöver förstås fullt ut direkt,
- `lightOne()` förklaras tydligare som ett kodrecept,
- parentesen beskrivs som sättet att tala om vilken LED receptet ska använda,
- E007-D förenklades så bilden inte visar `digitalWrite(pin, HIGH);` utan visar den barnnära idén: släck alla, tänd vald, vänta.
