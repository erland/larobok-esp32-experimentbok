# E015 bildpipeline-brief – Dimbar LED

## Status

Skapad i v101 som första fullständiga E015-utkast.

## Teknisk sanningskälla

- `08-illustrationer-och-kopplingar/circuits/E015-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E015-diagram.json`
- Manus: `07-experimentutkast/kapitel-02/E015-Dimbar-LED.md`

## Progressionskontroll enligt v83

E015 bedöms fungera som eget huvudexperiment trots att kopplingen är enkel.

Det återvänder från RGB till en vanlig LED, men tillför ett pedagogiskt viktigt syfte:

- isolera PWM-idén,
- visa ljusstyrka utan färgblandning,
- förbereda E016 Andande ljus,
- göra 0–255-modellen tydligare.

Det är alltså ett förtydligande experiment, inte bara en repetition av E001.

## Bildprincip

- E015-A visar komponentkategorier, inte antal i bild.
- E015-B följer v78 LED-standard: GPIO → långt ben → kort ben → motstånd → GND.
- E015-C visar av/svag/mellan/stark som fyra tydliga nivåer.
- E015-D visar PWM på en LED med "lite på", "mer på", "mest på".

## Bilder

| ID | Fil | Syfte | Status |
|---|---|---|---|
| E015-A | `generated/E015/E015-A-dagens-delar.svg` | Dagens delar | Utkast |
| E015-B | `generated/E015/E015-B-kopplingsoversikt.svg` | Enkel LED-koppling | Utkast |
| E015-C | `generated/E015/E015-C-ljusstyrkenivaer.svg` | Ljusstyrkenivåer | Utkast |
| E015-D | `generated/E015/E015-D-pwm-pa-en-led.svg` | PWM på enkel LED | Utkast |

## Layoutgranskning som återstår

- Kontrollera att E015-C blir tydlig i PDF.
- Kontrollera att E015-D inte upprepar E012-D för mycket utan känns som en enkel LED-version.
- Kontrollera övergången E015 → E016.

## v102-notis – lätt puts

E015 putsades lätt efter analys:

- Texten förtydligar att E015 är en förenkling av E012: färgerna tas bort så att bara ljusstyrkan blir kvar.
- `Vad händer egentligen?` fick en tydligare brygga från E012 till enkel LED.
- E015-D fick mer barnnära rubrik: `Snabba blink kan bli olika starkt ljus`.
- E015-D betonar ögats upplevelse av snabba blinkningar, inte PWM-termen i sig.
