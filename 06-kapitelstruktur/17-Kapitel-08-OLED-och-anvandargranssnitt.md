# Kapitel 8 – OLED och användargränssnitt

## Pedagogisk roll

Kapitel 8 gör att projekten börjar kännas som riktiga apparater. Hittills har information främst visats med LED, RGB-färger, ljud och Seriell monitor. Nu får barnet en liten skärm som kan visa text, värden, menyer och resultat.

Kapitlet ska introducera OLED som ett användargränssnitt, inte bara som en ny komponent. Målet är att barnet förstår att skärmen gör projekt lättare att använda för andra människor.

## Förkunskaper

Barnet bör kunna:

- koppla moduler på breadboard,
- använda Seriell monitor,
- läsa sensorvärden,
- använda knappar,
- förstå enkla tillstånd,
- använda enklare bibliotek från tidigare kapitel.

## Huvudexperiment

| Ordning | ID | Namn | Roll i kapitlet |
|---:|---|---|---|
| 1 | E076 | OLED säger hej | Introducerar OLED och I²C |
| 2 | E077 | OLED visar mätvärden | Ersätter Seriell monitor med skärm |
| 3 | E078 | OLED-menyn | Introducerar enkel meny och skärmlägen |
| 4 | E079 | Mini-instrumentpanelen | Kombinerar flera sensorer på skärm |
| 5 | E080 | OLED-reaktionsspelet | Gör ett tidigare spel mer användarvänligt |

## Rekommenderad klassning

| ID | Klassning | Motivering |
|---|---|---|
| E076 | Huvudspår | Första OLED-experimentet |
| E077 | Huvudspår | Visar direkt nytta med skärm |
| E078 | Huvudspår | Viktigt för senare smarta prylar |
| E079 | Huvudspår | Bra kapitelprojekt/mini-dashboard |
| E080 | Bonus eller huvudspår | Stark återkoppling till tidigare spel |

## Breadboard-progression

1. Koppla OLED ensam för att minska felsökning.
2. Behåll OLED och lägg till LDR eller annan enkel sensor.
3. Lägg till knapp för att byta skärmläge.
4. Lägg till fler sensorer stegvis.
5. Återanvänd reaktionsspelets knapp och LED, men flytta resultatvisningen till OLED.

## Kodprogression

| Moment | Kodidé |
|---|---|
| E076 | bibliotek, initiering och första text |
| E077 | skriva sensorvärde på skärmen |
| E078 | enkel meny med knapptryck |
| E079 | layout: rubriker, rader och flera värden |
| E080 | visa speltillstånd och resultat |

## Komponentprogression

Introduceras/fördjupas:

- D01 OLED
- I²C som praktiskt begrepp
- skärmlayout
- text och statusinformation

Återanvänds:

- K01 knapp
- S01 LDR
- S02 HC-SR04
- S05 DHT22
- tidigare reaktionsspel

## Illustrationer som behövs

| Figur | Typ | Beskrivning |
|---|---|---|
| 8-1 | Breadboard | OLED kopplad till ESP32 |
| 8-2 | Begreppsbild | SDA/SCL och I²C på enkel nivå |
| 8-3 | Skärmexempel | "Hej!" på OLED |
| 8-4 | Skärmexempel | sensorvärde på en rad |
| 8-5 | Flöde | knapp byter skärmläge |
| 8-6 | Skärmexempel | mini-instrumentpanel |
| 8-7 | Skärmexempel | reaktionsspel med start/resultat |

## Vanliga fallgropar

- Fel I²C-adress.
- SDA/SCL förväxlas.
- Bibliotek saknas i Arduino IDE.
- Skärmen är svart men koden kör.
- För mycket text skrivs på för liten skärm.
- Barnet fokuserar mer på layout än funktion.

## Pedagogisk rytm

Kapitlet ska gå från:

1. skärmen fungerar,
2. skärmen visar något användbart,
3. skärmen låter användaren välja,
4. skärmen blir en del av ett riktigt projekt.

Det bör inte bli ett långt "displaykapitel" med enbart textvisning. Varje experiment ska koppla skärmen till något barnet redan byggt.

## Kapitelprojekt

**Mini-instrumentpanelen**

Barnet bygger en liten panel som visar flera värden eller lägen på OLED. Den kan till exempel visa:

- ljusnivå,
- temperatur,
- avstånd,
- valt läge,
- enkel varning.

## Produktionschecklista

- [ ] Beskriv installation av OLED-bibliotek enkelt.
- [ ] Ha felsökningsruta för I²C-adress.
- [ ] Visa tydliga exempel på kort text.
- [ ] Undvik för avancerad grafik.
- [ ] Återanvänd tidigare sensorprojekt.
- [ ] Låt kapitlet avslutas med en användbar instrumentpanel.
