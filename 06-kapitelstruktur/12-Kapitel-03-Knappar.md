# Kapitel 3 – Knappar och styrning

## Pedagogisk roll

Kapitel 3 är första gången barnet går från att bara få ESP32 att göra saker till att själv kunna styra vad som händer. Knappar är därför ett stort pedagogiskt steg: barnet blir en del av systemet.

Kapitlet introducerar digital input, `INPUT_PULLUP`, tillstånd och enklare interaktion. Det ska kännas som början på spel, kodlås och styrpaneler.

## Kapitelmål

Efter kapitlet ska barnet kunna:

- koppla en knapp på breadboard,
- läsa en knapp med `digitalRead()`,
- förstå att en knapp kan vara `HIGH` eller `LOW`,
- använda `if` för att reagera på input,
- växla ett tillstånd, till exempel lampa på/av,
- använda två knappar eller flera knapptryck i en enkel logik,
- bygga ett första kodlås.

## Förkunskaper

Barnet bör kunna:

- koppla LED med motstånd,
- förstå digital output,
- ändra enkla kodvärden,
- känna igen `setup()` och `loop()`,
- följa breadboardrader.

## Huvudexperiment

| Ordning | ID | Namn | Roll i kapitlet |
|---:|---|---|---|
| 1 | E026 | Knappen tänder lampan | Första digitala input |
| 2 | E027 | Omvänd knapp med INPUT_PULLUP | Introducerar intern pullup |
| 3 | E028 | Tryckräknaren | Räknare och Seriell monitor |
| 4 | E029 | Lampan minns | Första tillståndet |
| 5 | E030 | Tryck rätt färg | Knapp + RGB + enkel spelidé |
| 6 | E031 | Dubbelknappen | Två inputs |
| 7 | E032 | Mini-kodlåset | Kapitelprojekt |

## Rekommenderad klassning

| ID | Klassning | Motivering |
|---|---|---|
| E026 | Huvudspår | Grund för all input |
| E027 | Huvudspår | Nödvändig för robust knappkoppling |
| E028 | Huvudspår | Gör input synlig och mätbar |
| E029 | Huvudspår | Introducerar tillstånd |
| E030 | Bonus/Huvudspår | Lekfull färginteraktion |
| E031 | Huvudspår | Förbereder spelkontroller |
| E032 | Kapitelprojekt | Samlar knappsekvens, status och logik |

## Rekommenderad ordning och motiv

Kapitlet bör börja med en mycket konkret koppling:

> Tryck → lampan lyser.

Först efter detta introduceras `INPUT_PULLUP`, eftersom omvänd logik kan kännas förvirrande om barnet inte redan sett vad knappen gör.

Tillstånd kommer efter tryckräknaren, eftersom barnet då redan förstår att programmet kan minnas något.

## Breadboard-progression

```text
LED-standardkoppling
  ↓
lägg till knapp
  ↓
knapp styr LED
  ↓
knapp med INPUT_PULLUP
  ↓
knapp + räknare
  ↓
knapp växlar läge
  ↓
två knappar
  ↓
kodlås
```

## Återanvändning

LED- och RGB-kopplingar från Kapitel 1–2 ska återanvändas. Knappen placeras konsekvent på vänster sida av breadboarden. Output hålls på höger sida.

Knappkopplingen blir en standardkoppling som senare används i:

- ljudspel,
- reaktionsspel,
- OLED-menyer,
- servo-kontroll,
- Makerprojekt.

## Kodprogression

| Experiment | Ny kodidé |
|---|---|
| E026 | `digitalRead()` och `if` |
| E027 | `INPUT_PULLUP` och inverterad logik |
| E028 | räknarvariabel |
| E029 | booleskt tillstånd |
| E030 | input + slump/färg |
| E031 | flera inputs |
| E032 | sekvens och enkel tillståndslogik |

## Komponentprogression

Introduceras:

- K01 tryckknapp

Återanvänds:

- L01 LED
- L02 RGB-LED
- R01 motstånd
- Seriell monitor
- tidigare LED-statusmönster

## Illustrationer som behövs

| Figur | Typ | Beskrivning |
|---|---|---|
| 3-1 | Breadboard | knapp + LED |
| 3-2 | Begreppsbild | knapp öppen/stängd |
| 3-3 | Kodbild | `digitalRead()` och `if` |
| 3-4 | Begreppsbild | `INPUT_PULLUP` betyder tryckt = LOW |
| 3-5 | Seriell monitor | tryckräknaren |
| 3-6 | Flöde | lampan minns på/av |
| 3-7 | Breadboard | två knappar |
| 3-8 | Projektbild | mini-kodlås med statusfärg |

## Vanliga fallgropar

| Problem | Möjlig orsak | Förebyggande |
|---|---|---|
| Knappen gör inget | knappen sitter fel över breadboardmitt | visa närbild |
| Logiken känns bakvänd | `INPUT_PULLUP` ger LOW vid tryck | förklara med tydlig ruta |
| Flera tryck räknas som många | knappstuds | nämn enkel fördröjning/debounce |
| Lampan minns inte | tillståndsvariabel återställs fel | visa variabel utanför loop |
| Kodlåset blir för svårt | för lång sekvens | börja med 2–3 steg |

## Teori som bör ingå

Faktarutor:

- Vad är input?
- Varför behöver en knapp en tydlig signal?
- Vad betyder `INPUT_PULLUP`?
- Vad är ett tillstånd?
- Varför kan en knapp "studsa"?

Studs bör förklaras mycket enkelt och inte bli ett avancerat elektronikavsnitt.

## Barnets aktiva roll

Barnet ska få:

- trycka och observera,
- bestämma vad knappen ska göra,
- skapa en egen hemlig kod,
- testa att trycka snabbt/långsamt,
- utmana någon annan att gissa koden.

## Vuxenroll

Den vuxne bör:

- kontrollera knappens placering över breadboardens mittspår,
- hjälpa till med `INPUT_PULLUP`-förvirring,
- uppmuntra barnet att felsöka med Seriell monitor,
- inte ge färdig kod till kodlåset för snabbt.

## Kapitelprojekt

**Mini-kodlåset**

Barnet bygger ett enkelt lås där en viss knappsekvens ger grön signal medan fel sekvens ger röd signal eller ljud.

Projektet förbereder senare:

- skattkistan,
- RFID-passersystem,
- touch-kodlås,
- Makerprojekt.

## Produktionschecklista

- [ ] Visa knappens breadboardplacering mycket tydligt.
- [ ] Förklara `INPUT_PULLUP` med bild.
- [ ] Använd samma knappkoppling i flera experiment.
- [ ] Låt barnet skapa egen kodsekvens.
- [ ] Undvik avancerad debounce i huvudspåret.
- [ ] Avsluta med kodlås som tydligt kapitelprojekt.
