# Kapitel 7 – Temperatur, miljö och levande mätningar

## Pedagogisk roll

Kapitel 7 fördjupar mätspåret och kopplar elektroniken till vardag och natur: temperatur, luftfuktighet, jordfuktighet och ljudnivå. Kapitlet ska kännas som ett litet laboratorium där barnet undersöker hemmet, växter och ljudmiljöer.

Det är viktigt att kapitlet inte blir för passivt. Varje mätning bör följas av något som tolkar värdet eller gör något användbart med det.

## Förkunskaper

Barnet bör kunna:

- använda Seriell monitor,
- förstå sensorvärden,
- använda tröskelvärden,
- använda LED/RGB som status,
- följa kopplingar med moduler.

## Huvudexperiment

| Ordning | ID | Namn | Roll i kapitlet |
|---:|---|---|---|
| 1 | E062 | Temperatur i rummet | Introducerar DHT22 |
| 2 | E063 | Väderstation första versionen | Visar mätvärden på OLED |
| 3 | E064 | Varmt eller kallt? | Gör temperatur till statusfärg |
| 4 | E065 | Temperaturjämförelsen | Jämför två sensorer |
| 5 | E069 | Smart blomkruka v1 | Introducerar jordfuktighet |
| 6 | E070 | Växtvakten med statusfärg | Gör växtdata begriplig |
| 7 | E071 | Ljudnivå i Seriell monitor | Introducerar mikrofonmodul |
| 8 | E072 | Klappströmbrytaren | Gör ljud till styrning |
| 9 | E074 | Sensorlaboratoriet | Kapitelprojekt |

## Bonusprojekt

| ID | Klassning | Kommentar |
|---|---|---|
| E066 | Bonus | Vattentemperatur kräver extra vuxenkontroll |
| E073 | Bonus | Ljusorgel är rolig men kan passa bättre som sidoprojekt |
| E075 | Bonus/Kapitelutmaning | Eget sensorlarm passar som avslutande utmaning |

## Breadboard-progression

1. Starta med DHT22 som modul.
2. Lägg till OLED för att visa värden.
3. Lägg till RGB-LED som snabb status.
4. Byt eller komplettera med DS18B20.
5. Byt till jordfuktighetssensor men behåll RGB-statusmönster.
6. Byt till mikrofonmodul men behåll principen: mät → tolka → agera.
7. Kombinera flera sensorer i Sensorlaboratoriet.

## Kodprogression

| Moment | Kodidé |
|---|---|
| DHT22 | bibliotek och sensorobjekt |
| OLED-väderstation | textlayout på display |
| Temperaturstatus | gränsvärden |
| Jämförelse | två sensorer och skillnad |
| Jordfukt | kalibrering torr/våt |
| Mikrofon | analog ljudnivå |
| Klappströmbrytare | tröskel + tillstånd |
| Sensorlaboratorium | flera mätvärden i samma program |

## Komponentprogression

Introduceras:

- S05 DHT22
- S06 DS18B20
- S08 kapacitiv jordfuktighetssensor
- S09 mikrofonmodul

Återanvänds:

- D01 OLED
- L02 RGB-LED
- A01 buzzer
- S01/S02 som jämförelse från tidigare kapitel

## Illustrationer som behövs

| Figur | Typ | Beskrivning |
|---|---|---|
| 7-1 | Modulbild | DHT22 |
| 7-2 | Breadboard | DHT22 + ESP32 |
| 7-3 | Skärmbild | OLED med temperatur och fukt |
| 7-4 | Färgruta | Temperatur till blå/grön/röd |
| 7-5 | Modulbild | Jordfuktighetssensor |
| 7-6 | Kalibreringsbild | Torr jord / fuktig jord |
| 7-7 | Breadboard | Mikrofonmodul |
| 7-8 | Flöde | Klapp → växla ljus |
| 7-9 | Projektöversikt | Sensorlaboratoriet |

## Vanliga fallgropar

- DHT22 läses för ofta och ger konstiga resultat.
- Jordfuktighetssensorer kräver kalibrering.
- Mikrofonmoduler varierar mycket i känslighet.
- DS18B20 kräver rätt koppling/pullup.
- Barn kan tro att alla sensorer ger "sanningen"; förklara att mätningar är ungefärliga.

## Pedagogisk rytm

Kapitlet bör växla mellan:

- mäta,
- visa,
- tolka,
- agera,
- jämföra,
- förbättra.

Undvik flera experiment i rad där det enda resultatet är siffror i Seriell monitor.

## Kapitelprojekt

**Sensorlaboratoriet**

Barnet bygger en liten teststation som kan läsa flera typer av värden och visa dem på OLED eller med färgstatus.

Möjliga kombinationer:

- temperatur + ljus,
- jordfukt + temperatur,
- ljudnivå + ljusstatus,
- egen sensorval.

## Produktionschecklista

- [ ] Håll bibliotekshantering enkel.
- [ ] Förklara kalibrering med exempel från verkligheten.
- [ ] Använd statusfärger så ofta som möjligt.
- [ ] Låt barnet mäta olika rum, växter eller ljud.
- [ ] Lägg in tydliga vuxennoteringar för vatten/DS18B20.
- [ ] Avsluta med ett projekt som känns som ett riktigt laboratorium.
