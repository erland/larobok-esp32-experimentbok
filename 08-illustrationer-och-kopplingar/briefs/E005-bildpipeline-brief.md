# E005 bildpipeline-brief – Polisljus

## Status

Skapad i v71 som första E005-utkast.

## Teknisk sanningskälla

- `08-illustrationer-och-kopplingar/circuits/E005-circuit.yaml`
- `08-illustrationer-och-kopplingar/wokwi/E005-diagram.json`
- Manus: `07-experimentutkast/kapitel-01/E005-Polisljus.md`

## Bildprincip

Följ v68/v69-principen:

- använd komponentbibliotekets formspråk,
- kort text i bilder,
- sekvensbilder ska visa tillstånd över tid,
- loop-pil ska gå från högersidan av sista steget till vänstersidan av första steget,
- varje LED ska ha eget motstånd till GND.

## Bilder

| ID | Fil | Syfte | Status |
|---|---|---|---|
| E005-A | `generated/E005/E005-A-dagens-delar.svg` | Dagens delar | Utkast |
| E005-B | `generated/E005/E005-B-kopplingsoversikt.svg` | Förenklad kopplingsöversikt | v72-granskad: signaler går till långa LED-ben |
| E005-C | `generated/E005/E005-C-polisljussekvens.svg` | Sekvens för röd-röd/blå-blå | Utkast |
| E005-D | `generated/E005/E005-D-vanliga-ledtradar.svg` | Visuella ledtrådar, ej obligatorisk i manus | Utkast |

## Layoutgranskning som återstår

- Kontrollera att E005-C är läsbar i PDF.
- Kontrollera att E005-B är tydlig nog för faktisk koppling.
- Vid behov skapa en extra Utforska-bild för långsam/snabb signal.


## v73-notis

E005-B ritades om i v73 med renare, E003-liknande layout för att minska visuellt brus i kopplingsöversikten.


## v74-notis

E005-B justerades i v74 så att kopplingstrådarna från GPIO-pinnarna går ända fram till LED-lampornas långa ben, i linje med bildspråket i tidigare experiment.


## v75-notis

E005-B justerades i v75 så att GPIO-trådarna ansluter längst ned på LED-lampornas långa ben, inte högst upp. Det gör kopplingslogiken mer konsekvent med tidigare experiment.


## v76-notis

E005-B bildputsades i v76. GPIO-trådarna gjordes rakare och GND-etiketten på ESP32 flyttades för att minska trängsel mot den svarta GND-linjen.


## v77-notis

E005-B justerades i v77 så att GPIO-utgångarna flyttades ned i höjd med respektive motståndsledare. Vänster och höger ledare vid varje LED ligger nu i samma horisontella linje. GPIO-etiketterna breddades också något för att undvika textklippning.
