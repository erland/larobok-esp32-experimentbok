# Kapitel 12 – RFID, IR och identifiering

## Pedagogisk roll

Kapitel 12 handlar om att elektroniken börjar känna igen saker och kommandon. RFID ger känslan av nyckelkort och hemliga passersystem. IR-fjärrkontroll ger barnet ett vardagligt exempel på trådlös styrning.

Kapitlet passar bra efter robotik eftersom det är tekniskt avancerat men inte mekaniskt lika tungt.

## Förkunskaper

Barnet bör kunna:

- installera och använda bibliotek,
- läsa värden i Seriell monitor,
- använda `if`,
- använda arrayer eller listor,
- förstå statuslägen,
- kombinera flera outputs.

## Huvudexperiment

| Ordning | ID | Namn | Roll i kapitlet |
|---:|---|---|---|
| 1 | E109 | RFID första läsningen | Läsa RFID-ID |
| 2 | E110 | RFID-passersystem | Godkänd/nekad identitet |
| 3 | E111 | RFID-skattkista | RFID + servo + narrativt projekt |
| 4 | E112 | IR-fjärrens hemliga koder | Läsa IR-koder |
| 5 | E113 | Fjärrstyrd lampa | IR styr RGB-läge |
| 6 | E114 | Fjärrstyrd servo | IR styr fysisk rörelse |

## Rekommenderad klassning

| ID | Klassning | Motivering |
|---|---|---|
| E109 | Huvudspår | Grund för RFID |
| E110 | Huvudspår | Tydlig vardagskoppling |
| E111 | Kapitelprojekt eller bonus | Väldigt roligt men ganska stort |
| E112 | Huvudspår | Grund för IR |
| E113 | Huvudspår | Enkel och tydlig styrning |
| E114 | Bonus/Huvudspår | Bra kombination med servo |

## Breadboard-progression

1. RFID-läsare ensam med Seriell monitor.
2. Lägg till RGB-LED och buzzer för passersystem.
3. Lägg till servo för skattkistan.
4. Byt till IR-mottagare.
5. Återanvänd RGB-LED som styrt objekt.
6. Återanvänd servo som fjärrstyrt objekt.

Kapitlet bör delas i två tydliga block: RFID först, IR sedan.

## Kodprogression

| Moment | Kodidé |
|---|---|
| E109 | läsa UID från RFID |
| E110 | jämföra UID med tillåten lista |
| E111 | status: låst/upplåst/fel kort |
| E112 | läsa IR-kod |
| E113 | switch/if för fjärrkommandon |
| E114 | fjärrkommando till servo-position |

## Komponentprogression

Introduceras:

- C01 RFID RC522
- C02 IR-mottagare + fjärrkontroll

Återanvänds:

- M01 servo
- L02 RGB-LED
- A01 buzzer
- D01 OLED som möjlig bonusvisning

## Illustrationer som behövs

| Figur | Typ | Beskrivning |
|---|---|---|
| 12-1 | Modulbild | RC522 och RFID-tagg |
| 12-2 | Breadboard | RC522 till ESP32 |
| 12-3 | Flöde | kort läses → godkänd/nekad |
| 12-4 | Projektbild | RFID-skattkista |
| 12-5 | Modulbild | IR-mottagare och fjärr |
| 12-6 | Breadboard | IR-mottagare till ESP32 |
| 12-7 | Kodtabell | fjärrknapp → kod → funktion |
| 12-8 | Projektbild | fjärrstyrd lampa/servo |

## Vanliga fallgropar

- RFID-läsaren kopplas till fel SPI-pinnar.
- RFID kräver 3,3V.
- Kortet hålls för långt från läsaren.
- Olika IR-fjärrar ger olika koder.
- Barnet tror att IR fungerar genom väggar.
- Biblioteksexempel kan vara för avancerade om de inte förenklas.

## Pedagogisk rytm

Kapitlet bör kännas som "hemliga nycklar och fjärrkontroller". Det är bra att använda berättelser:

- agentkort,
- skattkista,
- hemligt passersystem,
- fjärrstyrd uppfinning.

## Kapitelprojekt

**RFID-skattkistan**

En RFID-tagg fungerar som nyckel. Rätt tagg öppnar med servo och visar grön signal. Fel tagg ger röd signal och ljud.

## Produktionschecklista

- [ ] Visa RC522-koppling mycket tydligt.
- [ ] Ha felsökningsruta för SPI och 3,3V.
- [ ] Gör IR-kodtabell lätt att fylla i.
- [ ] Använd narrativ uppdragsstil.
- [ ] Markera RFID-skattkistan som större projekt.
