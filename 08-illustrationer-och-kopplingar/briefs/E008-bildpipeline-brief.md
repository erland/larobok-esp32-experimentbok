# E008 bildpipeline-brief – Rinnande ljus

## Status

Skapad i v87 som första fullständiga E008-utkast.

## Teknisk sanningskälla

- `08-illustrationer-och-kopplingar/circuits/E008-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E008-diagram.json`
- Manus: `07-experimentutkast/kapitel-02/E008-Rinnande-ljus.md`

## Progressionskontroll enligt v83

E008 är motiverat som eget huvudexperiment.

Det bygger vidare från E007, men tillför två tydliga nya kodidéer:

- array/lista över LED-pinnar,
- `for`-loop som går igenom listan.

Dessutom lägger E008 till en fjärde LED för att ljusormen ska kännas tydligare än E007-stafetten.

E008 ska därför inte behandlas som en enkel rytmvariant av E007.

## Bildprincip

Följ komponentbiblioteket från v68/v69 och v78-standarden för kopplingsöversikter:

- kort text i bilder,
- tydliga LED-tillstånd,
- varje LED ska ha eget motstånd,
- signaltrådar ska visuellt gå till LED-benen,
- motståndsledare ska visuellt nå LED-lampans korta ben,
- sekvensbilder ska visa rörelse över tid,
- loop-/returpilar ska inte kollidera med kort eller text.

## Bilder

| ID | Fil | Syfte | Status |
|---|---|---|---|
| E008-A | `generated/E008/E008-A-dagens-delar.svg` | Dagens delar med fyra LED | Utkast |
| E008-B | `generated/E008/E008-B-kopplingsoversikt.svg` | Förenklad kopplingsöversikt för fyra LED | Utkast |
| E008-C | `generated/E008/E008-C-rinnande-sekvens.svg` | Sekvens LED1 → LED2 → LED3 → LED4 → LED3 → LED2 | Utkast |
| E008-D | `generated/E008/E008-D-lista-och-loop.svg` | Begreppsbild för array/lista och loop | Utkast |

## Layoutgranskning som återstår

- Kontrollera att E008-B inte blir för hög/tät i PDF.
- Kontrollera att E008-D är begriplig utan programmeringsteori.
- Kontrollera att kodexemplet inte blir för stort för en sida.

## v88-notis – pedagogisk puts

I v88 mjukades E008 upp pedagogiskt:

- barntexten förklarar att `for` och `ledPins[i]` inte behöver förstås fullt ut direkt,
- listan beskrivs tydligare som rutor i rad,
- `ledPins[i]` förklaras som "pinnen i den ruta loopen pekar på just nu",
- den andra baklänges-loopen fick en trygghetsförklaring,
- E008-D förenklades så den visar en lugnare rad med pinnar och en tydligare pekare.

## v89-notis – riktad bildputs av E008-D

E008-D förenklades ytterligare efter visuell granskning.

Ändringen följer v88-rekommendationen:

- den stora böjda pilen togs bort,
- markeringen flyttades till en enkel pekare ovanför den aktiva rutan,
- huvudtexten delades upp så LED-raden blir lugnare,
- bilden ska nu kännas mer som en barnnära begreppsbild än ett programmeringsdiagram.

## v90-notis – kodrad konsekvent med manus

E008-D uppdaterades så att kodraden i bilden matchar manuset:

```cpp
int ledPins[] = {23, 22, 21, 19};
```

Layouten från v89 är oförändrad.

## v94-notis – övergång till E011

E008:s avslutande `Nästa experiment`-sektion har uppdaterats så den leder vidare till E011/RGB i stället för blinkkod.

Detta följer v92-beslutet att aktiv huvudprogression i Kapitel 2 går:

E007 → E008 → E011 → E012
