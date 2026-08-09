# Kapitel 10 – Servo och smarta prylar

## Pedagogisk roll

Kapitel 10 introducerar fysisk rörelse. Efter många kapitel med ljus, ljud, sensorer och skärmar får barnet nu se elektroniken flytta något i den verkliga världen. Detta är en stark motivationspunkt: en servo som öppnar en lucka eller pekar på ett värde känns som en riktig uppfinning.

Kapitlet fungerar också som en syntes av tidigare kunskap: sensorer, knappar, OLED, RGB, ljud och servo kombineras till smarta prylar.

## Förkunskaper

Barnet bör kunna:

- använda potentiometer,
- läsa sensorvärden,
- använda statusfärger,
- använda enklare bibliotek,
- förstå `if` och tillstånd,
- följa säkerhetsnoteringar.

## Huvudexperiment

| Ordning | ID | Namn | Roll i kapitlet |
|---:|---|---|---|
| 1 | E087 | Servo första rörelsen | Introducerar SG90 |
| 2 | E088 | Vredstyrd servo | Kopplar analog input till rörelse |
| 3 | E089 | Avståndsstyrd visare | Sensor styr fysisk visare |
| 4 | E090 | Skattkistan öppnas | Kodlås + servo + ljud/färg |
| 5 | E091 | Temperaturvisaren | Servo som analog mätare |
| 6 | E092 | Automatisk dörrvakt | PIR + servo |
| 7 | E093 | Smart nattlampa deluxe | Sensor + NeoPixel + OLED |
| 8 | E094 | Växtvakt med display | Praktisk smart pryl |
| 9 | E096 | Interaktiv larmcentral | Kapitelprojekt |

## Bonusprojekt

| ID | Klassning | Kommentar |
|---|---|---|
| E095 | Bonus | Bra men överlappar med E093/E094 |
| E097 | Bonus | Mini-kontrollpanel passar som friare projekt |
| E098 | Bonus | Touch-piano har hög wow-faktor men kräver K03 |
| E099 | Bonus/fördjupning | Touch-kodlås är stort och passar efter E090 |
| E100 | Stor utmaning | Sammanfattande egen uppfinning |

## Breadboard-progression

1. Servo ensam.
2. Lägg till potentiometer.
3. Byt input till avståndssensor.
4. Lägg till knappkod/status och gör skattkista.
5. Byt sensor till temperatur/PIR.
6. Lägg till OLED/NeoPixel i smarta prylar.
7. Kombinera flera sensorer och outputs i larmcentral.

Det är viktigt att output-delen byggs successivt så barnet inte möter en för stor koppling för tidigt.

## Kodprogression

| Moment | Kodidé |
|---|---|
| E087 | servo-bibliotek och vinklar |
| E088 | mappa analogt värde till vinkel |
| E089 | sensorvärde till servo-position |
| E090 | tillstånd: låst/öppet/fel kod |
| E091 | mätvärde till analog visning |
| E092 | PIR → rörelsebeslut |
| E093–E096 | kombinationslogik med flera outputs |

## Komponentprogression

Introduceras:

- M01 SG90 servo

Fördjupas:

- K02 potentiometer
- S02 HC-SR04
- S05 DHT22
- S07 PIR
- D01 OLED
- L03 NeoPixel
- L02 RGB-LED
- A01 buzzer

## Illustrationer som behövs

| Figur | Typ | Beskrivning |
|---|---|---|
| 10-1 | Modulbild | SG90 servo och kabelfärger |
| 10-2 | Breadboard | servo kopplad till ESP32 |
| 10-3 | Vinkelbild | 0°, 90°, 180° |
| 10-4 | Breadboard | potentiometer styr servo |
| 10-5 | Funktionsbild | sensorvärde till visare |
| 10-6 | Projektbild | skattkista med servo |
| 10-7 | Flöde | låst/öppet/fel kod |
| 10-8 | Projektbild | automatisk dörrvakt |
| 10-9 | Systembild | interaktiv larmcentral |

## Vanliga fallgropar

- Servo drar för mycket ström via ESP32-kortet.
- Servo rycker vid start.
- Fel kabelfärger antas utan kontroll.
- Servo monteras mekaniskt så den fastnar.
- För många moduler kopplas in samtidigt.
- Kod för smarta prylar blir för lång om den inte delas upp.

## Säkerhets- och vuxennotering

Servo är inte farlig i sig, men kan dra mer ström än väntat. Boken bör tydligt ange:

- använd liten SG90-servo,
- undvik belastning i första experimenten,
- koppla inte större motorer som servo,
- en vuxen kontrollerar strömförsörjning vid större projekt.

## Pedagogisk rytm

Kapitlet bör kännas som "nu bygger vi riktiga saker":

1. servo rör sig,
2. barnet styr den,
3. sensorer styr den,
4. den öppnar något,
5. den blir del av smarta prylar.

## Kapitelprojekt

**Interaktiv larmcentral**

Ett större projekt där sensorer och outputs samverkar:

- reedkontakt eller PIR triggar larm,
- OLED visar status,
- RGB/NeoPixel visar läge,
- buzzer varnar,
- servo kan fungera som lås eller indikator.

## Produktionschecklista

- [ ] Lägg in tydlig servokabelbild.
- [ ] Lägg in strömförsörjningsnotering.
- [ ] Håll första servoexperimentet mycket enkelt.
- [ ] Gör skattkistan till ett starkt narrativt projekt.
- [ ] Dela stora smarta projekt i tydliga steg.
- [ ] Markera touchprojekten som bonus.
- [ ] Avsluta med larmcentral eller egen smart pryl.
