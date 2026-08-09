# Komponentpass

Varje komponentpass kan senare byggas ut till ett eget uppslag i boken.

## E01 – ESP32 DevKit

| Fält | Innehåll |
|---|---|
| Nivå | Baslåda |
| Typ | Styrenhet |
| Rekommenderat antal | 2 |
| Nyttopoäng | ★★★★★ |
| Vad gör den? | Hjärnan i nästan alla experiment. Har WiFi, Bluetooth, många pinnar och programmeras via USB. |
| Används i | Alla experiment |
| Vanliga misstag | Fel USB-kabel, fel kort valt i Arduino IDE, 3,3V-logik förväxlas med 5V. |
| Visste du att...? | ESP32 används i många riktiga IoT-prylar. |

## B01 – Breadboard 830 punkter

| Fält | Innehåll |
|---|---|
| Nivå | Baslåda |
| Typ | Byggmiljö |
| Rekommenderat antal | 2 |
| Nyttopoäng | ★★★★★ |
| Vad gör den? | Kopplingsplattan där experimenten byggs utan lödning. |
| Används i | Alla breadboardexperiment |
| Vanliga misstag | Glapp i kontakterna, fel rad/kolumn, plus- och minusräls ihopblandade. |
| Visste du att...? | Breadboard gör att man kan bygga om samma krets många gånger. |

## B02 – Jumperkablar hane-hane

| Fält | Innehåll |
|---|---|
| Nivå | Baslåda |
| Typ | Kablage |
| Rekommenderat antal | 65 |
| Nyttopoäng | ★★★★★ |
| Vad gör den? | Kablar för kopplingar mellan ESP32, breadboard och komponenter. |
| Används i | Alla experiment |
| Vanliga misstag | För långa kablar ger rörig koppling, kablar sitter inte helt i. |
| Visste du att...? | Färgkodning gör felsökning mycket lättare. |

## B03 – Jumperkablar hane-hona

| Fält | Innehåll |
|---|---|
| Nivå | Baslåda |
| Typ | Kablage |
| Rekommenderat antal | 30 |
| Nyttopoäng | ★★★★☆ |
| Vad gör den? | Kablar för moduler och sensorer med färdiga stift. |
| Används i | Sensor- och displayexperiment |
| Vanliga misstag | Hane/hona blandas ihop, lösa kontakter. |
| Visste du att...? | Många moduler blir mycket enklare att koppla med dessa. |

## R01 – Motståndssats

| Fält | Innehåll |
|---|---|
| Nivå | Baslåda |
| Typ | Passiv komponent |
| Rekommenderat antal | 1 |
| Nyttopoäng | ★★★★★ |
| Vad gör den? | Skyddar lysdioder och används i enkla sensorkretsar. |
| Används i | LED, knappar, LDR, grundelektronik |
| Vanliga misstag | Fel motståndsvärde, LED utan motstånd. |
| Visste du att...? | Motstånd är elektronikens bromsar. |

## L01 – LED blandade färger

| Fält | Innehåll |
|---|---|
| Nivå | Baslåda |
| Typ | Ljus |
| Rekommenderat antal | 25 |
| Nyttopoäng | ★★★★★ |
| Vad gör den? | Små lysdioder för första experimenten, signaler och spel. |
| Används i | Blink, trafikljus, spel, indikatorer |
| Vanliga misstag | Fel polaritet, saknat motstånd. |
| Visste du att...? | En LED släpper bara igenom ström åt ett håll. |

## L02 – RGB-LED

| Fält | Innehåll |
|---|---|
| Nivå | Baslåda |
| Typ | Ljus |
| Rekommenderat antal | 5 |
| Nyttopoäng | ★★★★☆ |
| Vad gör den? | En lysdiod som kan blanda rött, grönt och blått. |
| Används i | Färgspel, statuslampor, humörlampa |
| Vanliga misstag | Gemensam anod/katod blandas ihop. |
| Visste du att...? | Skärmar bygger också färger med rött, grönt och blått. |

## K01 – Tryckknapp

| Fält | Innehåll |
|---|---|
| Nivå | Baslåda |
| Typ | Inmatning |
| Rekommenderat antal | 10 |
| Nyttopoäng | ★★★★★ |
| Vad gör den? | Barnets enklaste sätt att styra programmet. |
| Används i | Spel, meny, kodlås, reaktionstest |
| Vanliga misstag | Knappen sitter fel över breadboard-mitten, pullup/pulldown saknas. |
| Visste du att...? | Knappar studsar elektriskt när man trycker på dem. |

## K02 – Potentiometer 10kΩ

| Fält | Innehåll |
|---|---|
| Nivå | Baslåda |
| Typ | Inmatning |
| Rekommenderat antal | 3 |
| Nyttopoäng | ★★★★★ |
| Vad gör den? | Ett vred som ger ett analogt värde. |
| Används i | Volym, ljusstyrka, spelkontroll, menyer |
| Vanliga misstag | Ytterben och mittenben blandas ihop. |
| Visste du att...? | En potentiometer är ett justerbart motstånd. |

## A01 – Passiv buzzer

| Fält | Innehåll |
|---|---|
| Nivå | Baslåda |
| Typ | Ljud |
| Rekommenderat antal | 2 |
| Nyttopoäng | ★★★★★ |
| Vad gör den? | Liten högtalarliknande komponent som kan spela toner. |
| Används i | Melodier, larm, spel, reaktionstest |
| Vanliga misstag | Aktiv och passiv buzzer blandas ihop. |
| Visste du att...? | Olika toner skapas genom att vibrera olika snabbt. |

## S01 – LDR fotomotstånd

| Fält | Innehåll |
|---|---|
| Nivå | Baslåda |
| Typ | Sensor |
| Rekommenderat antal | 5 |
| Nyttopoäng | ★★★★★ |
| Vad gör den? | Sensor vars motstånd ändras med ljus. |
| Används i | Nattlampa, ljusmätare, larm |
| Vanliga misstag | Spänningsdelare saknas, ljus från rummet stör. |
| Visste du att...? | Samma idé används i många ljusmätare. |

## S02 – HC-SR04 avståndssensor

| Fält | Innehåll |
|---|---|
| Nivå | Baslåda |
| Typ | Sensor |
| Rekommenderat antal | 2 |
| Nyttopoäng | ★★★★★ |
| Vad gör den? | Mäter avstånd med ultraljud. |
| Används i | Parkeringssensor, robotögon, avståndsmätare |
| Vanliga misstag | Echo-signalen kan behöva nivåanpassas till 3,3V. |
| Visste du att...? | Den skickar ljud som människor inte hör. |

## S03 – Tilt-sensor

| Fält | Innehåll |
|---|---|
| Nivå | Baslåda |
| Typ | Sensor |
| Rekommenderat antal | 2 |
| Nyttopoäng | ★★★☆☆ |
| Vad gör den? | Känner av lutning eller skakning. |
| Används i | Skaklarm, lutningsspel, rörelseindikator |
| Vanliga misstag | Ger ibland studsiga signaler. |
| Visste du att...? | En enkel mekanisk sensor kan ersätta mer avancerad elektronik. |

## S04 – Reedkontakt + magnet

| Fält | Innehåll |
|---|---|
| Nivå | Baslåda |
| Typ | Sensor |
| Rekommenderat antal | 2 |
| Nyttopoäng | ★★★★☆ |
| Vad gör den? | En brytare som påverkas av magnetfält. |
| Används i | Dörrlarm, skattkista, räknare |
| Vanliga misstag | Magneten hamnar för långt från kontakten. |
| Visste du att...? | Reedkontakter används ofta i dörr- och fönsterlarm. |

## D01 – OLED 0,96 tum I²C

| Fält | Innehåll |
|---|---|
| Nivå | Baslåda |
| Typ | Display |
| Rekommenderat antal | 1 |
| Nyttopoäng | ★★★★★ |
| Vad gör den? | Liten skärm för text, symboler och enkla spel. |
| Används i | Mätvärden, menyer, småspel, status |
| Vanliga misstag | Fel I²C-adress, SDA/SCL förväxlas. |
| Visste du att...? | OLED-pixlar lyser själva och behöver ingen bakbelysning. |

## S05 – DHT22 temperatur/fukt

| Fält | Innehåll |
|---|---|
| Nivå | Pluslåda |
| Typ | Sensor |
| Rekommenderat antal | 1 |
| Nyttopoäng | ★★★★☆ |
| Vad gör den? | Mäter temperatur och luftfuktighet. |
| Används i | Väderstation, rumsklimat, växthus |
| Vanliga misstag | Fel bibliotek, för täta mätningar. |
| Visste du att...? | Fuktighet påverkar hur varmt ett rum upplevs. |

## S06 – DS18B20 temperatursensor

| Fält | Innehåll |
|---|---|
| Nivå | Pluslåda |
| Typ | Sensor |
| Rekommenderat antal | 2 |
| Nyttopoäng | ★★★★☆ |
| Vad gör den? | Robust temperatursensor som även kan användas med vattentät kapsling. |
| Används i | Ute/innenmätning, vatten, jämförelser |
| Vanliga misstag | Pullup-motstånd saknas på datalinjen. |
| Visste du att...? | Flera DS18B20 kan sitta på samma dataledning. |

## S07 – PIR-rörelsesensor

| Fält | Innehåll |
|---|---|
| Nivå | Pluslåda |
| Typ | Sensor |
| Rekommenderat antal | 1 |
| Nyttopoäng | ★★★★☆ |
| Vad gör den? | Känner av rörelse från varma kroppar. |
| Används i | Rörelselarm, nattlampa, spökhus |
| Vanliga misstag | Behöver uppvärmningstid, känner inte stilla personer. |
| Visste du att...? | PIR-sensorer används ofta i automatiska lampor. |

## S08 – Kapacitiv jordfuktighetssensor

| Fält | Innehåll |
|---|---|
| Nivå | Pluslåda |
| Typ | Sensor |
| Rekommenderat antal | 1 |
| Nyttopoäng | ★★★★☆ |
| Vad gör den? | Mäter ungefär hur fuktig jorden är. |
| Används i | Smart blomkruka, bevattningslarm |
| Vanliga misstag | Billiga sensorer behöver kalibreras. |
| Visste du att...? | Kapacitiva sensorer rostar mindre än resistiva jordfuktighetssensorer. |

## S09 – Mikrofonmodul

| Fält | Innehåll |
|---|---|
| Nivå | Pluslåda |
| Typ | Sensor |
| Rekommenderat antal | 1 |
| Nyttopoäng | ★★★☆☆ |
| Vad gör den? | Känner av ljudnivå eller klapp. |
| Används i | Klappströmbrytare, ljudmätare, ljusorgel |
| Vanliga misstag | Tröskelvärden behöver justeras. |
| Visste du att...? | Ljud är vibrationer i luften. |

## L03 – NeoPixel-ring 16 LED

| Fält | Innehåll |
|---|---|
| Nivå | Pluslåda |
| Typ | Ljus |
| Rekommenderat antal | 1 |
| Nyttopoäng | ★★★★★ |
| Vad gör den? | Programmerbara RGB-lysdioder i ringform. |
| Används i | Animationer, spel, timer, status |
| Vanliga misstag | Behöver rätt bibliotek och stabil matning. |
| Visste du att...? | Varje LED har en liten styrkrets inbyggd. |

## D02 – MAX7219 LED-matris 8x8

| Fält | Innehåll |
|---|---|
| Nivå | Pluslåda |
| Typ | Display |
| Rekommenderat antal | 1 |
| Nyttopoäng | ★★★★☆ |
| Vad gör den? | Rutnät med 64 lysdioder för symboler och spel. |
| Används i | Animationer, smileys, Snake-liknande spel |
| Vanliga misstag | Orienteringen kan bli fel i koden. |
| Visste du att...? | En matris kan visa bilder genom att tända många punkter. |

## M01 – SG90 mikroservo

| Fält | Innehåll |
|---|---|
| Nivå | Pluslåda |
| Typ | Motor |
| Rekommenderat antal | 2 |
| Nyttopoäng | ★★★★★ |
| Vad gör den? | Motor som går till en viss vinkel. |
| Används i | Robotarm, visare, lås, skattkista |
| Vanliga misstag | Kan behöva separat ström vid belastning. |
| Visste du att...? | Servon används i radiostyrda modeller. |

## K03 – TTP229 touch-sensor

| Fält | Innehåll |
|---|---|
| Nivå | Pluslåda |
| Typ | Inmatning |
| Rekommenderat antal | 1 |
| Nyttopoäng | ★★★★☆ |
| Vad gör den? | Flera touchknappar på en modul. |
| Används i | Piano, kodlås, memoryspel |
| Vanliga misstag | Känslighet kan påverkas av kablar och montering. |
| Visste du att...? | Kapacitiv touch känner av kroppen som en liten elektrisk förändring. |

## C01 – RFID RC522

| Fält | Innehåll |
|---|---|
| Nivå | Makerlåda |
| Typ | Kommunikation |
| Rekommenderat antal | 1 |
| Nyttopoäng | ★★★☆☆ |
| Vad gör den? | Läser RFID-kort och taggar. |
| Används i | Passersystem, skattkista, uppdragsspel |
| Vanliga misstag | 3,3V-koppling viktig, kortet måste vara nära läsaren. |
| Visste du att...? | Liknande teknik används i passerkort och bibliotek. |

## C02 – IR-mottagare + fjärrkontroll

| Fält | Innehåll |
|---|---|
| Nivå | Makerlåda |
| Typ | Kommunikation |
| Rekommenderat antal | 1 |
| Nyttopoäng | ★★★☆☆ |
| Vad gör den? | Tar emot signaler från fjärrkontroll. |
| Används i | Fjärrstyrning, spelkontroll, meny |
| Vanliga misstag | Olika fjärrkontroller skickar olika koder. |
| Visste du att...? | IR-fjärrar skickar ljus som ögat inte ser. |

## D03 – DS3231 RTC

| Fält | Innehåll |
|---|---|
| Nivå | Makerlåda |
| Typ | Tid |
| Rekommenderat antal | 1 |
| Nyttopoäng | ★★☆☆☆ |
| Vad gör den? | Håller reda på tid även när ESP32 startas om. |
| Används i | Klocka, timer, datalogger |
| Vanliga misstag | Knappcellsbatteri kan saknas eller vara slut. |
| Visste du att...? | RTC är en liten klocka som går vidare när datorn sover. |

## D04 – MicroSD-modul

| Fält | Innehåll |
|---|---|
| Nivå | Makerlåda |
| Typ | Lagring |
| Rekommenderat antal | 1 |
| Nyttopoäng | ★★☆☆☆ |
| Vad gör den? | Sparar mätdata på minneskort. |
| Används i | Datalogger, väderstation, experimentlogg |
| Vanliga misstag | 3,3V-kompatibilitet, filsystem och kortformat kan krångla. |
| Visste du att...? | Minneskort använder flashminne, ungefär som USB-minnen. |

## M02 – 28BYJ-48 stegmotor + ULN2003

| Fält | Innehåll |
|---|---|
| Nivå | Makerlåda |
| Typ | Motor |
| Rekommenderat antal | 1 |
| Nyttopoäng | ★★★☆☆ |
| Vad gör den? | Motor som kan röra sig i små steg. |
| Används i | Vridbord, mätare, mekaniska figurer |
| Vanliga misstag | Kräver många signaler och extern ström. |
| Visste du att...? | Stegmotorer används där position är viktig. |

## M03 – DC-motor

| Fält | Innehåll |
|---|---|
| Nivå | Makerlåda |
| Typ | Motor |
| Rekommenderat antal | 2 |
| Nyttopoäng | ★★★☆☆ |
| Vad gör den? | Enkel motor som snurrar när den får ström. |
| Används i | Fläkt, bil, snurrande projekt |
| Vanliga misstag | Får inte kopplas direkt till ESP32-pin. |
| Visste du att...? | DC-motorer finns i leksaker, fläktar och små pumpar. |

## M04 – L9110S motordrivare

| Fält | Innehåll |
|---|---|
| Nivå | Makerlåda |
| Typ | Motorstyrning |
| Rekommenderat antal | 1 |
| Nyttopoäng | ★★★☆☆ |
| Vad gör den? | Låter ESP32 styra DC-motorer åt båda håll. |
| Används i | Robotbil, fläktstyrning, motorlek |
| Vanliga misstag | Motor och logikmatning blandas ihop. |
| Visste du att...? | Motordrivare är som en förstärkare mellan dator och motor. |

