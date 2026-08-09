# Kapitel 1 – Kom igång med ESP32

## Pedagogisk roll

Kapitel 1 är bokens viktigaste första möte. Det ska ge barnet och den vuxne en snabb känsla av att "det här fungerar" och "det här kan vi göra tillsammans". Kapitlet får därför inte bli en teoritung introduktion till elektronik. Teori ska komma efter första lyckade blinket, inte före.

Kapitlet ska etablera tre saker:

1. ESP32 är "hjärnan".
2. Breadboard är "byggplatsen".
3. Kod kan få något fysiskt att hända.

## Kapitelmål

Efter kapitlet ska barnet ha:

- sett en LED tändas och blinka,
- förstått att ESP32 styr pinnar,
- kopplat sin första enkla krets,
- laddat upp sitt första program,
- ändrat något i koden och sett effekt,
- börjat känna igen plus, minus, GND, LED och motstånd.

## Förkunskaper

Inga tekniska förkunskaper krävs.

Föräldern bör däremot kunna hjälpa med:

- Arduino IDE,
- välja rätt kort och port,
- kontrollera LED-polaritet,
- kontrollera att USB-kabeln är datakabel.

## Huvudexperiment

| Ordning | ID | Namn | Roll i kapitlet |
|---:|---|---|---|
| 1 | E001 | Första blinket | Första fungerande resultatet |
| 2 | E002 | LED med egen rytm | Barnet ändrar koden |
| 3 | E003 | Två LED turas om | Första flera outputs |
| 4 | E005 | Polisljus | Två LED med snabbare signalmönster |
| 5 | E004 | Mini-trafikljus | Första lilla systemet och kapitelavslutning |

## Rekommenderad klassning

| ID | Klassning | Motivering |
|---|---|---|
| E001 | Huvudspår | Absolut startpunkt |
| E002 | Huvudspår | Visar att kod kan ändras |
| E003 | Huvudspår | Bygger vidare utan stor omkoppling |
| E005 | Bonus/Huvudspår | Hög lekfaktor och repetition efter E003 |
| E004 | Kapitelprojekt | Ger tydlig systemavslutning med tre LED |

## Rekommenderad ordning och rytm

Kapitlet bör hålla högt tempo i början:

1. Koppla.
2. Ladda upp.
3. Se blink.
4. Ändra hastighet.
5. Lägg till en LED.
6. Bygg ett mönster.

Första experimentet bör vara mycket kort. Om barnet måste läsa flera sidor innan LED blinkar riskerar kapitlet att tappa energi.

## Breadboard-progression

```text
Tom breadboard
  ↓
ESP32 placerad
  ↓
en LED + motstånd
  ↓
samma LED blinkar
  ↓
lägg till andra LED
  ↓
lägg till tredje LED
  ↓
polisljus/trafikljus
```

## Återanvändning av koppling

LED-kopplingen från E001 bör ligga kvar genom hela kapitlet. E003–E005 ska helst bygga vidare utan onödig omkoppling.

Det är viktigt att inte byta pinne mellan varje experiment i onödan. En fast rekommenderad pinne för första LED bör användas genom hela kapitlet.

## Kodprogression

| Experiment | Ny kodidé |
|---|---|
| E001 | `setup()`, `loop()`, `pinMode()`, `digitalWrite()`, `delay()` |
| E002 | ändra värden i `delay()` |
| E003 | två pinnar och sekvens |
| E005 | snabbare mönster med två LED |
| E004 | flera steg i ordning med tre LED |

## Komponentprogression

Introduceras:

- E01 ESP32 DevKit
- B01 breadboard
- B02 jumperkablar
- R01 motstånd
- L01 LED

Återanvänds i senare kapitel:

- LED + motstånd blir bokens första standard-output.
- `digitalWrite()` återkommer i nästan alla kapitel.

## Illustrationer som behövs

| Figur | Typ | Beskrivning |
|---|---|---|
| 1-1 | Översikt | ESP32, breadboard, USB-kabel, LED och motstånd |
| 1-2 | Breadboard | Placera ESP32 på breadboard |
| 1-3 | Breadboard | Första LED med motstånd |
| 1-4 | Begreppsbild | LED har plus/minus |
| 1-5 | Kodbild | var `setup()` och `loop()` finns |
| 1-6 | Breadboard | två LED |
| 1-7 | Breadboard | tre LED som trafikljus |
| 1-8 | Projektbild | fyrtorn/polisljus som berättande ljus |

## Vanliga fallgropar

| Problem | Möjlig orsak | Förebyggande |
|---|---|---|
| LED lyser inte | LED sitter åt fel håll | visa tydlig plus/minus-bild |
| Kod laddas inte upp | fel port eller fel kort | vuxenruta med kontrollsteg |
| LED lyser svagt eller konstigt | fel motstånd/kontakt | felsökningsruta |
| Barnet ändrar för mycket i koden | för många fria ändringar | ge en ändring i taget |
| Breadboardrader missförstås | komponent sitter i fel rad | visa närbild på rader |

## Teori som bör ingå

Teori ska vara kort och kopplad till det barnet just sett.

Faktarutor:

- Vad är en LED?
- Varför behövs motstånd?
- Vad är en pinne?
- Vad betyder GND?
- Vad gör `delay()`?

Undvik längre teori om ström, Ohms lag och mikrocontrollers i detta kapitel.

## Barnets aktiva roll

Barnet ska få:

- välja LED-färg,
- ändra blinkhastighet,
- hitta på ett eget mönster,
- beskriva vad ljuset betyder,
- testa vad som händer om `delay()` blir kortare/längre.

## Vuxenroll

Den vuxne bör:

- kontrollera kopplingen före USB,
- hjälpa till med Arduino IDE,
- inte ta över experimenten,
- ställa frågor i stället för att ge alla svar.

Exempel:

> Vad tror du händer om vi ändrar 1000 till 200?

## Kapitelprojekt

**Mini-trafikljus**

Barnet bygger ett litet system med tre LED-lampor som följer en ordning. Projektet fungerar bra som kapitelavslut eftersom det:

- bygger vidare på tidigare LED-kopplingar,
- använder flera GPIO-pinnar,
- har en tydlig vardagsmodell,
- visar att flera enkla delar kan bli ett litet system.

**Fyrtornet** används inte längre som eget experiment. Idén är infogad i E002 som en utmaning med berättande blinkmönster.

## Produktionschecklista

- [ ] Första blinket ska komma mycket tidigt.
- [ ] Visa LED-polaritet tydligt.
- [ ] Håll kodexempel korta.
- [ ] Använd samma pinne konsekvent.
- [ ] Ge barnet små ändringsuppdrag.
- [ ] Lägg säkerhet och teori i korta rutor.
- [ ] Avsluta med ett mönster barnet själv kan designa.

# v83-notis – Lärdom för kommande kapitel

Kapitel 1 visar en viktig produktionsprincip:

- E006 Fyrtornet var en bra idé, men för lik E002 som eget experiment.
- Idén blev starkare när den flyttades in som utmaning i E002.
- E004 blev starkare som kapitelavslut eftersom det fungerar som syntes med tre LED och tydlig vardagsmodell.

Samma princip ska användas i kommande kapitel:

> Varianter stärker ofta ett befintligt experiment.  
> Synteser passar ofta som kapitelavslut.
