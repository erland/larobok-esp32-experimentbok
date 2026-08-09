# E014 image prompts – Humörlampan

## Övergripande stil

Följ komponentbiblioteket och E011–E013-bilderna:

- ljus bakgrund,
- korta etiketter,
- tydliga färgkort,
- barnnära status/humör-känsla,
- undvik långa förklaringar i bilder.

## E014-A – Dagens delar

Samma delar som RGB-experimenten: ESP32 DevKit, breadboard, RGB-LED, tre motstånd, kopplingskablar och USB.

## E014-B – Kopplingsöversikt

Samma koppling som E011–E013:

- GPIO 23 → motstånd → rött ben,
- GPIO 22 → motstånd → grönt ben,
- GPIO 21 → motstånd → blått ben,
- gemensamt ben → GND.

## E014-C – Humörsekvens

Visa fem färgkort:

- glad,
- lugn,
- fokus,
- varning,
- magi.

Korten ska kännas lekfulla men enkla.

## E014-D – Färg som status

Visa färg som meddelande/status:

- grön = allt okej,
- gul = vänta/titta hit,
- röd = varning/stanna,
- blå = lugn.

Lägg gärna till en påminnelse om att färger inte alltid betyder samma sak.

# v100 – puts av E014-bilder

E014-C ska använda "Favorit" i stället för "Magi" om bilden ska stödja status-/läge-tanken tydligare.

E014-D ska ha fyra lika stora statuskort om möjligt:

- grön / allt okej / fortsätt,
- gul / vänta / titta hit,
- röd / varning / stanna,
- blå / lugn / ta det lugnt.
