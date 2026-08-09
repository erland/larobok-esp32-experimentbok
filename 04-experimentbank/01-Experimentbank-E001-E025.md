# Steg 3.1 – Experimentbank E001–E025
## Omfattning
Detta är första delen av experimentbanken och täcker grundläggande elektronik, LED, färg, PWM, ljusmätning och enkla ljusuppfinningar.
Experimenten är fortfarande kandidater. De kan senare flyttas, slås ihop, byta ordning eller tas bort efter komponentanalys och kapitelstruktur.
## Experiment
| ID | Namn | Tema | Komponentnivå | Svårighetsgrad | Komponenter | Elektronikfärdigheter | Programmeringsfärdigheter | Makerfärdigheter | Byggtid | Vuxenhjälp | Bygger på | Kort beskrivning | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E001 | Första blinket | Lampor och ljus | Baslåda | Upptäckare | E01, B01, B02, R01, L01 | EL01, EL02, EL03, EL04 | PR01, PR02, PR03, PR04 | MK01, MK02, MK03 | 10–15 min | Ja | - | Barnet får sin första LED att blinka. | Kandidat |
| E002 | LED med egen rytm | Lampor och ljus | Baslåda | Upptäckare | E01, B01, B02, R01, L01 | EL03, EL04 | PR04, PR05 | MK08 | 10–15 min | Ja | E001 | Ändra blinkhastighet, skapa olika rytmer och testa en fyrtornsvariant. | Kandidat |
| E003 | Två LED turas om | Lampor och ljus | Baslåda | Upptäckare | E01, B01, B02, R01, L01 | EL03, EL04 | PR02, PR03, PR04, PR05 | MK02, MK04 | 15–20 min | Ja | E001 | Två lampor blinkar växelvis som en enkel signal. | Kandidat |
| E004 | Mini-trafikljus | Lampor och ljus | Baslåda | Upptäckare | E01, B01, B02, R01, L01 | EL03, EL04 | PR03, PR04, PR05 | MK02, MK04 | 20–25 min | Ja | E003 | Bygg ett trafikljus med röd, gul och grön LED. | Kandidat |
| E005 | Polisljus | Lampor och ljus | Baslåda | Upptäckare | E01, B01, B02, R01, L01 | EL03, EL04 | PR03, PR04, PR05 | MK08 | 15–20 min | Ja | E003 | Skapa blinkande blå/röda ljus med snabba mönster. | Kandidat |
| E006 | Fyrtornet (infogad i E002) | Lampor och ljus | Baslåda | Upptäckare | E01, B01, B02, R01, L01 | EL03, EL04 | PR04, PR05 | MK08 | 15–20 min | Ja | E002 | Inte längre eget experiment; idén ingår i E002 som fyrtornsutmaning. | Infogad i E002 |
| E007 | LED-stafett | Lampor och ljus | Baslåda | Uppfinnare | E01, B01, B02, R01, L01 | EL03, EL04 | PR05, PR11, PR12 | MK05 | 20–30 min | Ja | E004 | Flera LED tänds i tur och ordning med en enkel funktion. | Kandidat |
| E008 | Rinnande ljus | Lampor och ljus | Baslåda | Uppfinnare | E01, B01, B02, R01, L01 | EL03, EL04 | PR12, PR13 | MK05, MK08 | 25–35 min | Ja | E007 | Fyra LED bildar ett rinnande ljus med array/lista och for-loop. | Kandidat |
| E009 | Hemlig blinkkod | Lampor och ljus | Baslåda | Uppfinnare | E01, B01, B02, R01, L01 | EL03, EL04 | PR05, PR11, PR13 | MK10 | 25–35 min | Ja | E008 | Parkerad bonusidé: enkel hemlig blinkkod, ej aktivt huvudsteg i Kapitel 2. | Parkerad | Kandidat |
| E010 | Morse med LED | Lampor och ljus | Baslåda | Uppfinnare | E01, B01, B02, R01, L01 | EL03, EL04 | PR11, PR13 | MK10, MK15 | 30–40 min | Ja | E009 | Parkerad idé: Morse med LED, ej aktivt huvudsteg i Kapitel 2. | Parkerad |
| E011 | RGB: tre färger i en LED | Färger | Baslåda | Upptäckare | E01, B01, B02, R01, L02 | EL03, EL04 | PR03, PR05 | MK03 | 20–25 min | Ja | E008 | Upptäck att en RGB-LED består av röd, grön och blå kanal i samma lampa. | Utkast |
| E012 | Färgblandaren | Färger | Baslåda | Uppfinnare | E01, B01, B02, R01, L02 | EL09 | PR05, PR15 | MK08 | 25–35 min | Ja | E011 | Blanda färger med RGB-LED genom 0–255-värden och PWM-ljusstyrka. | Utkast |
| E013 | Regnbågslampan | Färger | Baslåda | Uppfinnare | E01, B01, B02, R01, L02 | EL09 | PR12, PR15 | MK08 | 30–40 min | Ja | E012 | Låt RGB-LED växla mjukt mellan flera färger. | Kandidat |
| E014 | Humörlampan | Färger | Baslåda | Uppfinnare | E01, B01, B02, R01, L02 | EL09 | PR05, PR11, PR15 | MK12 | 25–35 min | Ja | E012/E013 | Skapa färger som betyder olika humör eller status med namngivna RGB-funktioner. | Utkast |
| E015 | Dimbar LED | Lampor och ljus | Baslåda | Uppfinnare | E01, B01, B02, R01, L01 | EL09 | PR15 | MK08 | 20–30 min | Ja | E012/E001 | Använd PWM/0–255-värden för att göra en vanlig LED svagare eller starkare. | Utkast |
| E016 | Andande ljus | Lampor och ljus | Baslåda | Uppfinnare | E01, B01, B02, R01, L01 | EL09 | PR12, PR15 | MK08 | 25–35 min | Ja | E015 | LED-ljuset tonar långsamt upp och ned med PWM-värden som räknas i en loop. | Utkast |
| E017 | Nattlampa första versionen | Smarta ljus | Baslåda | Uppfinnare | E01, B01, B02, R01, L01, S01 | EL07, EL08 | PR07, PR14, PR20 | MK07, MK09 | 30–40 min | Ja | E015 | Låt en LED tändas när det blir mörkt. | Kandidat |
| E018 | Ljusmätaren i Seriell monitor | Mäta ljus | Baslåda | Uppfinnare | E01, B01, B02, R01, S01 | EL07, EL08 | PR14, PR20 | MK07, MK08 | 20–30 min | Ja | E017 | Läs ljusvärden och se hur de ändras när handen skuggar sensorn. | Kandidat |
| E019 | Ljusstyrd dimmer | Smarta ljus | Baslåda | Ingenjör | E01, B01, B02, R01, L01, S01 | EL07, EL08, EL09 | PR14, PR15 | MK09 | 30–45 min | Ja | E015, E018 | Låt LED-ljusstyrkan följa hur ljust det är i rummet. | Kandidat |
| E020 | Soluppgångslampan | Smarta ljus | Baslåda | Ingenjör | E01, B01, B02, R01, L01 | EL09 | PR12, PR15, PR16 | MK08 | 35–45 min | Ja | E016 | Skapa en långsam ljusökning som liknar soluppgång. | Kandidat |
| E021 | Blink utan delay | Lampor och ljus | Baslåda | Ingenjör | E01, B01, B02, R01, L01 | EL04 | PR16 | MK14 | 30–40 min | Ja | E002 | Lär LED blinka medan programmet fortfarande kan göra annat. | Kandidat |
| E022 | Två saker samtidigt | Lampor och ljus | Baslåda | Ingenjör | E01, B01, B02, R01, L01 | EL04 | PR16, PR17 | MK14 | 35–45 min | Ja | E021 | Två LED blinkar i olika takt utan att stoppa varandra. | Kandidat |
| E023 | Mini-ljusshow | Lampor och ljus | Baslåda | Ingenjör | E01, B01, B02, R01, L01, L02 | EL04, EL09 | PR11, PR12, PR13, PR15 | MK11, MK12 | 40–50 min | Ja | E008, E013 | Kombinera flera blink- och färgmönster till en show. | Kandidat |
| E024 | Statuslampan | Smarta ljus | Baslåda | Ingenjör | E01, B01, B02, R01, L02 | EL09 | PR07, PR11, PR17 | MK12 | 30–40 min | Ja | E014 | En RGB-LED visar olika statuslägen: okej, varning, fel. | Kandidat |
| E025 | Designa din egen ljusuppfinning | Eget projekt | Baslåda | Mästare | E01, B01, B02, R01, L01, L02, S01 | EL03, EL04, EL07, EL09 | PR11, PR12, PR14, PR15, PR16 | MK11, MK12, MK15 | 45–60 min | Ja | E001–E024 | Barnet väljer själv en ljusuppfinning och förklarar hur den fungerar. | Kandidat |

## Kommentarer

Den här första gruppen är avsiktligt tung på LED och ljus eftersom den ska ge snabb återkoppling och många synliga resultat. Den introducerar successivt:

- digital output,
- blinkmönster,
- flera LED,
- RGB-LED,
- PWM,
- LDR,
- Seriell monitor,
- `millis()` utan blockering,
- enklare egen design.

## Preliminär bedömning

Alla 25 experiment kan genomföras med Baslådan.
