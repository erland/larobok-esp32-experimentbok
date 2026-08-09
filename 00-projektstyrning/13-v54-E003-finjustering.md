# v54 – E003 finjustering

## Syfte

Denna version finjusterar E003 efter granskning mot E001/E002, v52-bildprinciperna och 5B.6-designinriktningen.

## Genomförda ändringar

- E003 har fått en kortare **Innan du börjar**-påminnelse om den andra LED-lampans långa och korta ben.
- Formuleringen om att ESP32 styr "mer än en sak i taget" har ersatts med en mer exakt formulering: ESP32 håller ordning på två lampor i samma program.
- Mindre textputs har gjorts för att minska upprepning utan att ändra berättarrytm, struktur eller pedagogiskt djup.
- `E003-B-kopplingsoversikt.svg` har ritats om så att GPIO 23 och GPIO 22 går tydligare till respektive LED-lampas långa ben, i linje med v51/v52-principen.
- E003 är fortfarande markerat som manusutkast/pågår tills fysisk breadboardtest, teknisk granskning och PDF-layoutgranskning är gjorda.

## Kvarstående kontroller

- Fysisk testkoppling på breadboard.
- Teknisk granskning mot `E003-circuit.yaml` och Wokwi-diagram.
- Pedagogisk testläsning.
- PDF-preview för E001–E003 och visuell layoutkontroll.
