# Kapitel 5 – Ljus, avstånd och de första mätinstrumenten

## Pedagogisk roll

Kapitel 5 markerar övergången från att styra saker till att **mäta världen**. Barnet har redan använt LED, knappar, ljud, slump och enklare programlogik. Nu får ESP32 "sinnen" genom att läsa sensorvärden och reagera på dem.

Det viktiga är att barnet inte bara ser siffror, utan förstår att mätvärden kan användas för att skapa beteenden: larm, nattlampor, avståndsvarningar och enkla instrument.

## Förkunskaper

Barnet bör ha mött:

- LED och motstånd
- digital output
- knapp som input
- `if`
- variabler
- Seriell monitor
- enklare spel eller reaktionslogik

## Huvudexperiment

| Ordning | ID | Namn | Roll i kapitlet |
|---:|---|---|---|
| 1 | E051 | Ljusdetektiven | Introducerar analog mätning med LDR |
| 2 | E052 | Skuggjakten | Gör ljusmätningen direkt användbar |
| 3 | E053 | Ljusbarometern | Bygger ett visuellt mätinstrument |
| 4 | E054 | Avstånd i Seriell monitor | Introducerar HC-SR04 |
| 5 | E055 | Parkeringssensorn v1 | Gör avstånd till ett användbart varningssystem |
| 6 | E056 | Avståndslampan | Använder färg som status |
| 7 | E057 | Osynliga måttbandet | Bonus/fördjupning: jämföra mätning med verkligheten |

## Rekommenderad klassning

| ID | Klassning | Motivering |
|---|---|---|
| E051 | Huvudspår | Grundläggande analog sensorförståelse |
| E052 | Huvudspår | Visar sensor → beslut → output |
| E053 | Huvudspår | Första enkla mätinstrumentet |
| E054 | Huvudspår | Introducerar avståndssensor |
| E055 | Huvudspår | Hög igenkänning och tydlig wow-faktor |
| E056 | Huvudspår | Kombinerar sensor och RGB-status |
| E057 | Bonus | Bra för förståelse, men inte nödvändig för progression |

## Breadboard-progression

1. Starta med LDR + motstånd som spänningsdelare.
2. Behåll LED från tidigare kapitel.
3. Lägg till fler LED för ljusbarometern.
4. Byt till HC-SR04 när avståndsblocket börjar.
5. Lägg till buzzer för parkeringssensorn.
6. Byt enkel LED mot RGB-LED för statusfärg.

Målet är att barnet först lär sig att **läsa värden**, och sedan att **använda värden**.

## Kodprogression

| Moment | Kodidé |
|---|---|
| E051 | `analogRead()` och Seriell monitor |
| E052 | `if` med tröskelvärde |
| E053 | flera tröskelvärden |
| E054 | funktion för avståndsmätning |
| E055 | avstånd styr ljudintervall |
| E056 | avstånd styr färg |
| E057 | mäta, jämföra och dokumentera |

## Komponentprogression

Introduceras i kapitlet:

- S01 LDR
- S02 HC-SR04

Återanvänds:

- LED
- RGB-LED
- buzzer
- motstånd
- Seriell monitor
- `if` och variabler

## Illustrationer som behövs

| Figur | Typ | Beskrivning |
|---|---|---|
| 5-1 | Breadboard | LDR som spänningsdelare |
| 5-2 | Begreppsbild | Ljusvärde: mörkt/ljust |
| 5-3 | Breadboard | LED-barometer |
| 5-4 | Breadboard | HC-SR04 kopplad till ESP32 |
| 5-5 | Säkerhetsruta | Echo-signal och 3,3V-kompatibilitet |
| 5-6 | Funktionsbild | Parkeringssensor: närmare = snabbare pip |
| 5-7 | Färgruta | Avstånd till grön/gul/röd status |

## Vanliga fallgropar

- LDR kopplas utan motstånd och ger därför konstiga värden.
- Tröskelvärden fungerar i ett rum men inte i ett annat.
- HC-SR04-moduler kan ge 5V Echo-signal.
- Barnet tolkar sensorvärden som "exakta" i stället för ungefärliga.
- För många mätvärden i rad kan kännas tråkigt.

## Förebyggande pedagogik

Efter varje rent mätande experiment ska nästa experiment göra något synligt eller hörbart med mätningen. Kapitlet ska inte fastna i "skriv ut värde"-logik.

## Kapitelprojekt

**Parkeringshjälpen**

Barnet bygger ett system som varnar med ljud och färg när något kommer närmare. Projektet kombinerar:

- HC-SR04
- buzzer
- RGB-LED
- tröskelvärden
- enkel statuslogik

## Produktionschecklista

- [ ] Kontrollera att LDR-koppling visas tydligt.
- [ ] Lägg in säkerhetsnotering för HC-SR04 och ESP32.
- [ ] Ge exempel på hur man kalibrerar tröskelvärden i olika rum.
- [ ] Håll kodexempel korta.
- [ ] Lägg in frågor som "vad händer om du skuggar sensorn?"
- [ ] Avsluta med ett projekt som känns praktiskt och användbart.
