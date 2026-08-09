# Kapitel 11 – Motorer och robotik

## Pedagogisk roll

Kapitel 11 introducerar bokens första riktiga motor- och robotikprojekt. Efter servo-kapitlet har barnet sett hur elektronik kan skapa rörelse, men DC-motorer och robotar kräver ett nytt tankesätt: motorer behöver mer ström, motordrivare och tydligare vuxenkontroll.

Målet är inte att bygga en perfekt robot, utan att barnet ska förstå grunderna i motorstyrning och hur sensorer kan styra rörelse.

## Förkunskaper

Barnet bör kunna:

- följa kopplingsscheman noggrant,
- använda `digitalWrite()`,
- använda PWM,
- använda potentiometer,
- förstå sensor → beslut → output,
- känna till att GPIO-pinnar inte får driva motorer direkt.

## Huvudexperiment

| Ordning | ID | Namn | Roll i kapitlet |
|---:|---|---|---|
| 1 | E101 | DC-motor första snurret | Introducerar DC-motor och motordrivare |
| 2 | E102 | Motor åt båda hållen | Riktning och knappstyrning |
| 3 | E103 | Fartkontroll med PWM | Hastighet med potentiometer |
| 4 | E104 | Mini-fläkten | Temperatur styr motor |
| 5 | E105 | Robotbas första versionen | Två motorer som plattform |
| 6 | E106 | Robot som undviker hinder | Kapitelprojekt med sensorstyrning |

## Bonusprojekt

| ID | Klassning | Kommentar |
|---|---|---|
| E107 | Bonus | Stegmotor introducerar exakt rörelse |
| E108 | Bonus | Mini-karusell ger kreativ mekanik |

## Breadboard-progression

1. Börja med ESP32 + motordrivare + en DC-motor.
2. Lägg till knapp för riktning.
3. Lägg till potentiometer för fart.
4. Lägg till temperatursensor för automatisering.
5. Gå från en motor till två motorer.
6. Lägg till HC-SR04 för hinderundvikning.

Motorprojekten bör ha tydliga pauser där vuxen kontrollerar kopplingen innan ström ansluts.

## Kodprogression

| Moment | Kodidé |
|---|---|
| E101 | motor av/på via motordrivare |
| E102 | riktning med två styrsignaler |
| E103 | PWM för hastighet |
| E104 | sensortröskel styr motor |
| E105 | två motorer som funktioner |
| E106 | enkel robotlogik: framåt, stoppa, sväng |

## Komponentprogression

Introduceras:

- M03 DC-motor
- M04 L9110S motordrivare
- M02 stegmotor + ULN2003 som bonus

Återanvänds:

- S02 HC-SR04
- S05 DHT22
- K01 knapp
- K02 potentiometer

## Illustrationer som behövs

| Figur | Typ | Beskrivning |
|---|---|---|
| 11-1 | Säkerhetsbild | varför motor inte kopplas direkt till ESP32 |
| 11-2 | Breadboard | ESP32 + L9110S + motor |
| 11-3 | Flöde | riktning: framåt/bakåt/stopp |
| 11-4 | Breadboard | potentiometer styr motorhastighet |
| 11-5 | Systembild | temperaturstyrd fläkt |
| 11-6 | Mekanikbild | robotbas med två motorer |
| 11-7 | Flöde | hinder upptäckt → sväng |
| 11-8 | Bonusbild | stegmotor + ULN2003 |

## Vanliga fallgropar

- Motor kopplas direkt till ESP32.
- Motordrivare matas fel.
- Gemensam jord saknas.
- Motor drar för mycket ström via USB.
- Robotens mekanik gör att motorerna fastnar.
- Barnet vill bygga en avancerad robot direkt.

## Säkerhetsnotering

Det här kapitlet ska ha tydligare vuxenmarkering än tidigare kapitel. Alla motorprojekt bör ha en ruta:

> En vuxen bör kontrollera kopplingen innan ström ansluts. Motorer får inte kopplas direkt till ESP32-pinnar.

## Kapitelprojekt

**Robot som undviker hinder**

Barnet bygger en enkel robot eller testplattform där avståndssensorn avgör om roboten ska fortsätta, stoppa eller svänga.

## Produktionschecklista

- [ ] Lägg in tydliga motorvarningar.
- [ ] Visa motordrivaren mycket pedagogiskt.
- [ ] Förklara gemensam jord.
- [ ] Håll mekaniken enkel.
- [ ] Markera stegmotor som bonus.
- [ ] Undvik att robotprojektet kräver perfekt chassi.
