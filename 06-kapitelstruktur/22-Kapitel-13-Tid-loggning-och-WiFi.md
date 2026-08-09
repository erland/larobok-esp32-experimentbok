# Kapitel 13 – Tid, loggning och WiFi

## Pedagogisk roll

Kapitel 13 gör projekten mer självständiga och uppkopplade. Barnet lär sig att en apparat kan veta vad klockan är, spara data och visa information via nätverk.

Det här är ett mer avancerat kapitel och bör skrivas med extra tydliga steg. Det ska inte kännas som en kurs i nätverk eller filsystem, utan som praktiska uppfinningar: klocka, påminnare, väderloggare och enkel webbkontroll.

## Förkunskaper

Barnet bör kunna:

- använda bibliotek,
- läsa och visa sensorvärden,
- använda OLED,
- förstå statuslägen,
- följa längre kod,
- felsöka steg för steg.

## Huvudexperiment

| Ordning | ID | Namn | Roll i kapitlet |
|---:|---|---|---|
| 1 | E115 | Klockan vaknar | Introducerar RTC |
| 2 | E116 | Tidsstyrd påminnare | Tid används för beslut |
| 3 | E117 | SD-kort första loggen | Introducerar datalogging |
| 4 | E118 | Min väderloggare | RTC + sensor + SD + OLED |
| 5 | E119 | Första WiFi-sidan | Introducerar WiFi/webbserver |

## Rekommenderad klassning

| ID | Klassning | Motivering |
|---|---|---|
| E115 | Huvudspår | Grund för tid |
| E116 | Huvudspår | Tid blir användbar |
| E117 | Huvudspår/bonus | Viktig men tekniskt känslig |
| E118 | Kapitelprojekt | Stor men tydlig syntes |
| E119 | Huvudspår eller bonus | Mycket viktig ESP32-funktion men kan kräva nätverksstöd |

## Breadboard-progression

1. Koppla RTC + OLED.
2. Lägg till RGB/buzzer för påminnare.
3. Koppla SD-kortmodul separat.
4. Kombinera RTC, sensor, SD och OLED i väderloggare.
5. Koppla bort SD vid WiFi-introduktion för att minska komplexitet.

WiFi-delen bör helst kunna köras i enklaste möjliga form, gärna med tydliga alternativ för hemnätverk eller access point-läge i senare revision.

## Kodprogression

| Moment | Kodidé |
|---|---|
| E115 | läsa tid från RTC |
| E116 | jämföra aktuell tid med mål |
| E117 | öppna fil och skriva rad |
| E118 | tidstämplad sensorlogg |
| E119 | enkel webbserver och HTML-text |

## Komponentprogression

Introduceras:

- D03 DS3231 RTC
- D04 MicroSD-modul
- ESP32 WiFi

Återanvänds:

- D01 OLED
- S05 DHT22
- L02 RGB-LED
- A01 buzzer

## Illustrationer som behövs

| Figur | Typ | Beskrivning |
|---|---|---|
| 13-1 | Modulbild | DS3231 RTC |
| 13-2 | Breadboard | RTC + OLED |
| 13-3 | Skärm | klocka på OLED |
| 13-4 | Flöde | tid → påminnelse |
| 13-5 | Modulbild | MicroSD-modul |
| 13-6 | Dataexempel | CSV-logg med tid och temperatur |
| 13-7 | Systembild | väderloggare |
| 13-8 | Nätverksbild | ESP32 som enkel webbsida |
| 13-9 | Webbsida | LED-status/styrning i webbläsare |

## Vanliga fallgropar

- RTC-batteri saknas eller är slut.
- MicroSD-modulen är inte 3,3V-kompatibel.
- SD-kortet är fel formaterat.
- WiFi-uppgifter skrivs fel.
- Hemnätverk kan blockera eller krångla.
- Webbserverkod blir snabbt lång och abstrakt.

## Pedagogisk rytm

Kapitlet bör inte pressa in för mycket teori. Varje avancerad komponent ska kopplas till en begriplig nytta:

- klocka,
- påminnare,
- loggbok,
- väderstation,
- webbsida.

## Kapitelprojekt

**Min väderloggare**

Barnet bygger en liten apparat som mäter temperatur/fukt, visar senaste värde och sparar mätningar med tid.

WiFi-projektet kan vara ett efterföljande bonus- eller avslutningsexperiment beroende på bokens längd.

## Produktionschecklista

- [ ] Markera kapitlet som avancerat.
- [ ] Lägg in vuxenstöd för SD/WiFi.
- [ ] Ha alternativa vägar om WiFi krånglar.
- [ ] Visa loggfil visuellt.
- [ ] Håll HTML mycket enkel.
- [ ] Undvik molntjänster i huvudspåret.
