# Kapitel 2 – LED, PWM och färg

## Pedagogisk roll

Kapitel 2 bygger vidare på barnets första framgångar med LED. Nu blir ljuset mer uttrycksfullt: flera LED, mjuka förändringar, RGB-färger och enklare ljusshower. Kapitlet introducerar PWM som ett praktiskt fenomen snarare än som teori.

Barnet ska uppleva att samma grundkrets kan bli mycket mer spännande med små kodändringar och en ny komponent.

## Kapitelmål

Efter kapitlet ska barnet kunna:

- koppla flera LED,
- förstå att PWM kan få en LED att se svagare/starkare ut,
- använda RGB-LED för färger,
- skapa enkla ljusmönster,
- förstå att färg kan användas som status,
- se skillnaden mellan digitalt på/av och gradvis styrning.

## Förkunskaper

Barnet bör ha gjort Kapitel 1 och kunna:

- koppla LED med motstånd,
- ladda upp kod,
- ändra `delay()`,
- känna igen `digitalWrite()`.

## Huvudexperiment

| Ordning | ID | Namn | Roll i kapitlet |
|---:|---|---|---|
| 1 | E007 | LED-stafett | Flera LED och första funktionstänk |
| 2 | E008 | Rinnande ljus | Loopar/arrayer som ljusmönster |
| 3 | E011 | RGB: tre färger i en LED | Introducerar RGB |
| 4 | E012 | Färgblandaren | Introducerar PWM på RGB |
| 5 | E013 | Regnbågslampan | Mjuka färgövergångar |
| 6 | E014 | Humörlampan | Färg som betydelse/status |
| 7 | E015 | Dimbar LED | Förtydligar PWM på en LED |
| 8 | E016 | Andande ljus | Kapitelprojekt/visuell effekt |

## Bonusprojekt

| ID | Klassning | Kommentar |
|---|---|---|
| E009 | Bonus | Hemlig blinkkod passar bra som frivillig utmaning |
| E010 | Bonus | Morse med LED kan bli historisk/fördjupande ruta |
| E017 | Flyttas/senare | Nattlampa hör pedagogiskt bättre till sensorkapitlet |
| E018 | Flyttas/senare | Ljusmätning hör till Kapitel 5 |

## Rekommenderad ordning och motiv

Det är bättre att introducera flera LED och mönster innan RGB, eftersom RGB annars kan kännas som tre LED på en gång. När barnet förstår flera LED blir RGB mer begripligt.

PWM bör först upplevas praktiskt:

> Ljuset blir svagare och starkare.

Först därefter kan boken förklara att ESP32 egentligen blinkar mycket snabbt.

## Breadboard-progression

```text
flera vanliga LED
  ↓
LED-stafett
  ↓
rinnande ljus
  ↓
byt/lägg till RGB-LED
  ↓
RGB grundfärger
  ↓
PWM/färgblandning
  ↓
regnbågslampa
  ↓
andande ljus/stämningslampa
```

## Återanvändning

De vanliga LED från Kapitel 1 bör återanvändas i början. RGB-LED introduceras först när flera LED redan känns bekanta.

Om möjligt bör breadboarden organiseras så att:

- vanliga LED sitter i en rad,
- RGB-LED får en separat tydlig plats,
- motstånd visas konsekvent.

## Kodprogression

| Experiment | Ny kodidé |
|---|---|
| E007 | enkel funktion eller upprepad kod för flera LED |
| E008 | `for`-loop eller array över pinnar |
| E011 | tre färgkanaler |
| E012 | PWM-värden |
| E013 | färgsekvens |
| E014 | färg betyder status/humör |
| E015 | dimning på en LED |
| E016 | långsam mjuk förändring |

## Komponentprogression

Introduceras:

- fler L01 LED
- L02 RGB-LED
- PWM som styrprincip

Återanvänds senare:

- RGB-LED blir standard för status i många projekt.
- PWM återkommer i motorer, servo-tänk och ljusstyrning.
- färgstatus återkommer i sensor-, larm- och smarta prylar.

## Illustrationer som behövs

| Figur | Typ | Beskrivning |
|---|---|---|
| 2-1 | Breadboard | flera LED i rad |
| 2-2 | Flöde | LED-stafett |
| 2-3 | Begreppsbild | RGB = röd + grön + blå |
| 2-4 | Breadboard | RGB-LED med tre motstånd |
| 2-5 | Begreppsbild | PWM som snabb blinkning |
| 2-6 | Färgkarta | enkla RGB-färger |
| 2-7 | Projektbild | humörlampa/stämningslampa |
| 2-8 | Effektbild | andande ljus |

## Vanliga fallgropar

| Problem | Möjlig orsak | Förebyggande |
|---|---|---|
| RGB visar fel färg | fel ben eller RGB-typ | visa tydlig pinout |
| LED tänds inte | saknat motstånd/fel polaritet | återanvänd kapitel 1-felsökning |
| PWM fungerar inte på vald pinne | fel pinne eller boardinställning | ange rekommenderade pinnar |
| Kod blir repetitiv | många LED styrs manuellt | introducera loopar försiktigt |
| Barnet blandar ihop färger | värdena för kanalerna är otydliga | använd färgkarta och små uppdrag |

## Teori som bör ingå

Faktarutor:

- Vad betyder RGB?
- Hur kan en LED dimmas?
- Vad är PWM, förklarat med snabb blinkning?
- Varför betyder färger olika saker i teknik?

Undvik fördjupning i frekvens, duty cycle och elektronikdetaljer. Det räcker att barnet förstår principen.

## Barnets aktiva roll

Barnet ska få:

- välja färgkombinationer,
- hitta på egen ljusshow,
- bestämma vad olika färger betyder,
- ändra hastighet och ljusstyrka,
- skapa ett "humör" med ljus.

## Vuxenroll

Den vuxne bör hjälpa med:

- RGB-LEDens ben,
- motstånd på varje kanal,
- felsökning av fel färg,
- att hålla kopplingen överskådlig.

## Kapitelprojekt

**Stämningslampan**

Barnet bygger en lampa med flera lägen:

- lugn färg,
- varningsfärg,
- festläge,
- andande ljus,
- eget favoritläge.

Projektet kan göras helt med Baslådan och blir en stark motivation för senare smarta lampor och statusindikatorer.

## Produktionschecklista

- [ ] Introducera RGB först efter flera vanliga LED.
- [ ] Visa pinout mycket tydligt.
- [ ] Förklara PWM med upplevelse före teori.
- [ ] Använd färger som berättande/status.
- [ ] Flytta LDR-experiment till sensorkapitel.
- [ ] Avsluta med ett projekt barnet kan anpassa själv.

# v84-notis – E007 producerad

E007 LED-stafett är första aktiva experimentet i Kapitel 2.

Progressionsroll:

- återanvänder tre LED från E004,
- introducerar `lightOne(int pin)` som första enkla funktion,
- förbereder E008 där ljusmönster kan göras mer automatiskt med loop/array.

E007 ska därför ses som ett kodprogressionssteg, inte som en ny kopplingsvariant.

# v87-notis – E008 producerad

E008 Rinnande ljus är nu första utkast efter E007.

Progressionsroll:

- bygger vidare på E007:s `lightOne()`-idé,
- lägger till en fjärde LED,
- introducerar `ledPins[]` som lista över pinnar,
- introducerar `for`-loop som går igenom listan,
- förbereder senare mönster, färgsekvenser och PWM-styrning.

E008 ska därför ses som ett kodprogressionssteg med lista/loop, inte som en enkel ny ljusrytm.

# v91-notis – E009 producerad som bonus

E009 Hemlig blinkkod är producerad som bonusprojekt.

Progressionsroll:

- återanvänder enkel LED-koppling,
- förstärker funktionsidén från E007,
- använder kort/lång/pause som betydelsebärande signaler,
- förbereder E010 Morse med LED,
- men är inte nödvändig för huvudprogressionen mot RGB/PWM.

E009 ska därför ligga kvar i bonusdelen av Kapitel 2.

# v92-notis – aktiv progression vidare till E011

Efter v91-granskning bedöms:

- E009 vara för nära tidigare blink-/rytmmaterial för att bära ett eget aktivt steg,
- E010 vara ett sidospår som inte tillför tillräckligt till huvudflödet just nu,
- E011 vara rätt nästa steg i Kapitel 2.

Aktivt huvudflöde i Kapitel 2 går därför vidare:

E007 → E008 → E011 → E012

# v94-notis – E008 övergång korrigerad

E008:s avslut har justerats så textflödet nu leder vidare till E011 och RGB-spåret.

Det aktiva huvudflödet i Kapitel 2 är fortsatt:

E007 → E008 → E011 → E012

# v95-notis – E012 producerad

E012 Färgblandaren är producerad som första utkast.

Progressionsroll:

- återanvänder E011:s RGB-LED-koppling,
- introducerar PWM som upplevd ljusstyrka,
- använder RGB-värden 0–255 som färgrecept,
- förbereder E013 där färger kan ändras mjukt över tid.

Aktivt huvudflöde är fortsatt:

E007 → E008 → E011 → E012 → E013

# v99-notis – E014 producerad

E014 Humörlampan är producerad som första utkast.

Progressionsroll:

- återanvänder RGB-LED och `setColor()` från E012/E013,
- introducerar färg som humör/status,
- använder namngivna funktioner för att koppla kod till betydelse,
- förbereder senare statuslampor, sensorer och smarta prylar.

Aktivt huvudflöde är fortsatt:

E007 → E008 → E011 → E012 → E013 → E014 → E015 → E016

# v101-notis – E015 producerad

E015 Dimbar LED är producerad som första utkast.

Progressionsroll:

- återgår till en enkel LED,
- isolerar PWM/0–255-ljusstyrka,
- gör skillnaden mellan av, svag, mellan och stark tydlig,
- förbereder E016 Andande ljus.

Aktivt huvudflöde är fortsatt:

E007 → E008 → E011 → E012 → E013 → E014 → E015 → E016

# v103-notis – E016 producerad

E016 Andande ljus är producerad som första utkast.

Progressionsroll:

- återanvänder E015:s enkla LED-koppling,
- använder PWM-värden som räknas upp och ned,
- gör en visuell effekt som sammanfattar ljusstyrka och stegvis förändring,
- fungerar som kapitelavslutning för Kapitel 2.

Aktivt huvudflöde i Kapitel 2 är nu producerat som utkast:

E007 → E008 → E011 → E012 → E013 → E014 → E015 → E016
