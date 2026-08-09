# Kapitel 4 – Ljud, spel och reaktion

## Pedagogisk roll

Kapitel 4 gör elektroniken lekfull. Nu kombineras knappar, LED och buzzer till musik, signaler och spel. Det är här många barn börjar känna att ESP32 inte bara är teknik utan en liten spel- och uppfinningsmaskin.

Kapitlet introducerar ljud, toner, slump, arrayer och enkla spelregler. Det ska ha hög energi och tydliga belöningar.

## Kapitelmål

Efter kapitlet ska barnet kunna:

- koppla en passiv buzzer,
- spela enkla toner,
- skapa ljudmönster,
- använda knappar i spel,
- använda slump,
- förstå enkla arrayer,
- bygga reaktionsspel eller Simon Says,
- kombinera ljus, ljud och knapptryck.

## Förkunskaper

Barnet bör kunna:

- koppla LED,
- koppla knapp,
- använda `if`,
- använda tillstånd,
- förstå enkla variabler,
- följa en sekvens i kod.

## Huvudexperiment

| Ordning | ID | Namn | Roll i kapitlet |
|---:|---|---|---|
| 1 | E033 | Passiv buzzer första tonen | Introducerar ljud |
| 2 | E034 | Sirenen | Toner i sekvens |
| 3 | E035 | Morse med ljud | Ljud som meddelande |
| 4 | E036 | Mini-pianot med knappar | Knappar styr toner |
| 5 | E037 | Melodimaskinen | Arrayer och melodier |
| 6 | E039 | Elektronisk tärning med LED | Slump och spel |
| 7 | E041 | Reaktionsspelet v1 | Timing och reaktion |
| 8 | E042 | Reaktionsspelet med ljud | Ljudfeedback |
| 9 | E044 | Simon Says v1 | Kapitelprojekt |

## Bonusprojekt

| ID | Klassning | Kommentar |
|---|---|---|
| E038 | Bonus | Jukebox passar som kreativ ljudlek |
| E040 | Bonus/reserv | Tärning i Seriell monitor är enklare variant |
| E043 | Bonus | Tvåspelarläge kan bli sidoutmaning |
| E045 | Bonus | Gissa ljusmönstret |
| E046 | Bonus | Nedräknare |
| E047 | Bonus | Bomben tickar, hög lekfaktor men större |
| E048 | Bonus | Poänglampan |
| E049 | Bonus | Spelkontroll för framtida projekt |
| E050 | Stor bonus | Eget knapp- och ljudspel |

## Rekommenderad ordning och motiv

Börja med ljud helt enkelt: en ton. Gå sedan till siren och mönster. Först därefter kopplas knappar in. Slump och spel kommer när både input och output känns bekanta.

Simon Says bör inte komma för tidigt, eftersom det kombinerar:

- flera inputs,
- ljud,
- ljus,
- arrayer,
- minne,
- spelstatus.

## Breadboard-progression

```text
knapp + LED från Kapitel 3
  ↓
lägg till buzzer
  ↓
buzzer ensam spelar ton
  ↓
buzzer + knapp
  ↓
buzzer + flera knappar
  ↓
LED + buzzer + slump
  ↓
reaktionsspel
  ↓
Simon Says
```

## Återanvändning

Knappkopplingen från Kapitel 3 bör sitta kvar. LED/RGB från Kapitel 2 bör återanvändas som status. Buzzern läggs till som ny output.

Detta ger ett tydligt mönster:

```text
input: knapp
output: ljus + ljud
logik: spelregel
```

## Kodprogression

| Experiment | Ny kodidé |
|---|---|
| E033 | spela ton |
| E034 | ändra ton i loop |
| E035 | kort/lång signal |
| E036 | knapp till ton |
| E037 | arrayer med toner och längder |
| E039 | slumpvärde |
| E041 | reaktionstid och `millis()` |
| E042 | spelstatus + ljudfeedback |
| E044 | växande sekvens och minne |

## Komponentprogression

Introduceras:

- A01 passiv buzzer

Återanvänds:

- K01 knapp
- L01 LED
- L02 RGB-LED
- tidigare tillståndslogik
- Seriell monitor som stöd

## Illustrationer som behövs

| Figur | Typ | Beskrivning |
|---|---|---|
| 4-1 | Breadboard | buzzer kopplad till ESP32 |
| 4-2 | Begreppsbild | ton = snabb vibration |
| 4-3 | Flöde | siren går upp och ned i ton |
| 4-4 | Breadboard | knapp + buzzer |
| 4-5 | Tabell | knapp → ton |
| 4-6 | Kodbild | array med toner |
| 4-7 | Flöde | reaktionsspel |
| 4-8 | Flöde | Simon Says-sekvens |
| 4-9 | Projektbild | färdigt Simon Says-spel |

## Vanliga fallgropar

| Problem | Möjlig orsak | Förebyggande |
|---|---|---|
| Buzzern låter inte | aktiv/passiv buzzer blandas ihop | ange passiv buzzer |
| Ljudet är svagt | fel pinne eller dålig kontakt | felsökningsruta |
| Toner låter fel | värden/frekvenser förväxlas | använd färdig ton-tabell |
| Reaktionsspelet startar direkt | slumpfördröjning saknas | visa tydligt spelsteg |
| Simon Says blir för svårt | för lång sekvens | börja med 2–3 steg |

## Teori som bör ingå

Faktarutor:

- Vad är en buzzer?
- Vad är en ton?
- Varför blir olika toner olika?
- Vad är slump i programmering?
- Hur kan ett spel ha regler?

Undvik avancerad ljudteori. Barnet behöver bara förstå att olika frekvenser ger olika toner.

## Barnets aktiva roll

Barnet ska få:

- välja egna ljud,
- hitta på larm,
- skapa en melodi,
- tävla i reaktionsspel,
- bygga ett eget spel,
- utmana en förälder.

## Vuxenroll

Den vuxne bör:

- kontrollera buzzer-typen,
- hjälpa till om ljudbibliotek/tonfunktioner krånglar,
- uppmuntra korta testcykler,
- hjälpa barnet att hålla spelreglerna enkla.

## Kapitelprojekt

**Simon Says v1**

Barnet bygger ett minnesspel där ljus och ljud visar en sekvens som barnet ska upprepa med knappar.

Om detta blir för stort kan **Reaktionsspelet med ljud** användas som huvudprojekt och Simon Says som bonus.

## Produktionschecklista

- [ ] Introducera buzzer med mycket enkel kod.
- [ ] Återanvänd knappkopplingen.
- [ ] Ge färdiga tonvärden.
- [ ] Varva ljudexperiment med spel.
- [ ] Håll Simon Says kort och barnvänligt.
- [ ] Markera större spel som bonus om kapitlet blir för långt.
