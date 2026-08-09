# Kapitel 6 – Larm, rörelse och närvaro

## Pedagogisk roll

Kapitel 6 bygger vidare på sensorförståelsen från Kapitel 5, men flyttar fokus från mätvärden till **händelser**: dörren öppnas, lådan skakas, någon rör sig i rummet. Det här kapitlet passar särskilt bra för barn eftersom experimenten kan byggas in i lekfulla scenarier: skattlådor, spökhus, dörrlarm och hemliga vakter.

## Förkunskaper

Barnet bör kunna:

- läsa digital input,
- använda `if`,
- använda LED/buzzer som reaktion,
- förstå att sensorer kan ge HIGH/LOW eller analogt värde,
- felsöka lösa kablar och polaritet.

## Huvudexperiment

| Ordning | ID | Namn | Roll i kapitlet |
|---:|---|---|---|
| 1 | E058 | Dörrvakten | Introducerar reedkontakt och magnet |
| 2 | E059 | Hemlig skattlåda – sensorversion | Kombinerar statusfärg och ljud |
| 3 | E060 | Skaklarmet | Introducerar tilt-sensor |
| 4 | E061 | Lutningsspelet | Gör lutning till interaktion |
| 5 | E067 | Rörelsevakten | Introducerar PIR |
| 6 | E068 | Spökhuset | Kapitelprojekt med rörelse, ljus och ljud |

## Bonus/reserv från experimentbanken

| ID | Klassning | Kommentar |
|---|---|---|
| E062–E066 | Flyttas till Kapitel 7 | Temperatur/miljö passar bättre där |
| E058 | Huvudspår | Väldigt begriplig sensoridé |
| E059 | Huvudspår | Hög barnmotivation |
| E060 | Huvudspår | Enkel men rolig |
| E061 | Bonus/Huvudspår beroende på utrymme | Kan bli spelinslag |
| E067 | Huvudspår | Viktigt inför smarta hem och larm |
| E068 | Kapitelprojekt | Tydlig wow-faktor |

## Breadboard-progression

1. Återanvänd LED + buzzer från tidigare kapitel.
2. Lägg till reedkontakt.
3. Bygg statuslogik med RGB-LED.
4. Byt sensor till tilt-sensor utan att ändra output-delen.
5. Lägg till PIR-modul.
6. Kombinera PIR, RGB och buzzer i spökhuset.

Detta kapitel bör vara ett bra exempel på komponentåteranvändning: samma output-krets kan användas för flera olika sensorer.

## Kodprogression

| Moment | Kodidé |
|---|---|
| Dörrvakt | digital sensor som brytare |
| Skattlåda | statusläge: stängd/öppen/larm |
| Skaklarm | studsiga signaler och enkel filtrering |
| Lutningsspel | input blir spelkontroll |
| Rörelsevakt | sensor med uppvärmningstid |
| Spökhus | tillståndsmaskin light |

## Komponentprogression

Introduceras:

- S04 reedkontakt + magnet
- S03 tilt-sensor
- S07 PIR-rörelsesensor

Återanvänds:

- L01 LED
- L02 RGB-LED
- A01 buzzer
- K01 knapp som återställning/avstängning

## Illustrationer som behövs

| Figur | Typ | Beskrivning |
|---|---|---|
| 6-1 | Foto/ikon | Reedkontakt och magnet |
| 6-2 | Breadboard | Dörrlarm med reedkontakt |
| 6-3 | Scenario | Skattlåda stängd/öppen |
| 6-4 | Breadboard | Tilt-sensor som larm |
| 6-5 | Förklaring | HIGH/LOW från digital sensor |
| 6-6 | Breadboard | PIR kopplad till ESP32 |
| 6-7 | Projektbild | Spökhus med ljus och ljud |

## Vanliga fallgropar

- Reedkontakt och magnet sitter för långt från varandra.
- Tilt-sensorn ger flera snabba signaler.
- PIR-sensorn behöver starttid innan den fungerar stabilt.
- Barn kan tro att PIR "ser" som en kamera; förklara att den känner värme/rörelse.
- Larm blir irriterande om det piper hela tiden; ge avstängningsknapp eller tidsgräns.

## Pedagogisk rytm

Kapitlet bör vara lekfullt. Det ska inte kännas som "sensor nummer två, sensor nummer tre", utan som en serie uppdrag:

1. Vakta en dörr.
2. Skydda en skatt.
3. Upptäck skakning.
4. Lura ett spöke.
5. Bygg ett spökhus.

## Kapitelprojekt

**Spökhuset**

En PIR-sensor upptäcker rörelse. När någon går förbi händer flera saker:

- RGB-LED ändrar färg,
- buzzer spelar ett kort ljud,
- eventuellt visas status på OLED i senare variant,
- systemet återgår efter en stund.

## Produktionschecklista

- [ ] Markera vilka sensorpinnar som ger digital signal.
- [ ] Förklara skillnaden mellan brytare, tilt och PIR.
- [ ] Undvik för mycket teori om PIR.
- [ ] Lägg in barnvänliga scenarier.
- [ ] Ha tydliga felsökningsrutor.
- [ ] Avsluta med ett kapitelprojekt med hög wow-faktor.
