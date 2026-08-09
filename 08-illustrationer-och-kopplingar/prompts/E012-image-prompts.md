# E012 image prompts – Färgblandaren

## Övergripande stil

Följ komponentbiblioteket och E011-bilderna:

- ljus bakgrund,
- korta etiketter,
- tydliga färgkort,
- RGB-värden ska visas som enkla recept,
- PWM ska visas som upplevelse, inte teknisk teori.

## E012-A – Dagens delar

Samma delar som E011: ESP32 DevKit, breadboard, RGB-LED, motstånd, kopplingskablar och USB.

## E012-B – Kopplingsöversikt

Samma koppling som E011:

- GPIO 23 → motstånd → rött ben,
- GPIO 22 → motstånd → grönt ben,
- GPIO 21 → motstånd → blått ben,
- gemensamt ben → GND.

## E012-C – Färgrecept

Visa färgkort för exempel:

- Röd: 255, 0, 0
- Grön: 0, 255, 0
- Blå: 0, 0, 255
- Gulaktig: 255, 160, 0
- Lila: 180, 0, 255
- Vitaktig: 180, 180, 180

## E012-D – PWM som snabb blinkning

Visa tre nivåer:

- lågt värde: kort på-stund och svagt ljus,
- mellanvärde: längre på-stund och mellanstarkt ljus,
- högt värde: lång på-stund och starkt ljus.

Använd formuleringen: "Högre tal gör färgen starkare."

# v96 – putsad PWM-begreppsbild

E012-D ska hellre säga:

- lite på,
- mer på,
- mest på,

än mer tekniska uttryck som "på-stund".

Huvudbudskapet ska vara:

> Högre tal gör ljuset starkare.
