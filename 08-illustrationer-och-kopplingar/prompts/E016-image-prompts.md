# E016 image prompts – Andande ljus

## Övergripande stil

Följ komponentbiblioteket och v78 LED-kopplingsstandard:

- ljus bakgrund,
- korta etiketter,
- tydlig LED-riktning,
- lugn rörelsekänsla,
- bilderna ska visa stegvis förändring och andning.

## E016-A – Dagens delar

Samma delar som E015: ESP32 DevKit, breadboard, en LED, ett motstånd, kopplingskablar och USB-kabel.

## E016-B – Kopplingsöversikt

Visa standardvägen:

GPIO 23 → LED långt ben → LED kort ben → motstånd → GND.

## E016-C – Andningssekvens

Visa ljuset som växer och minskar:

- av,
- svag,
- mellan,
- stark,
- svag,
- börja om.

Budskap: många små steg kan kännas som andning.

## E016-D – Loop upp och ned

Visa två loopidéer:

- värdet räknar upp: 0 → 5 → 10 → ... → 255,
- värdet räknar ned: 255 → 250 → 245 → ... → 0.

Budskap:

> Upp och ned tillsammans blir ett andande ljus.

# v104 – puts av andningsbilder

E016-C ska ha en lugn loop-pil som inte dominerar bildens ljusstyrkekort.

E016-D ska ge talraderna och kurvorna tydlig luft. Kortare talrader är bättre än för trång tekniktext.
