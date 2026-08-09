# Steg 4 – Experimentmatris

## Syfte

Experimentmatrisen är en kompakt vy över alla experiment. Den används för att kontrollera progression, komponentanvändning och beroenden innan kapitelstrukturen sätts.

| ID | Namn | Komponentnivå | Svårighetsgrad | Tema | Komponenter | Färdigheter | Bygger på |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E001 | Första blinket | Baslåda | Upptäckare | Lampor och ljus | E01, B01, B02, R01, L01 | EL01, EL02, EL03, EL04, PR01, PR02, PR03, PR04, MK01, MK02, MK03 | - |
| E002 | LED med egen rytm | Baslåda | Upptäckare | Lampor och ljus | E01, B01, B02, R01, L01 | EL03, EL04, PR04, PR05, MK08 | E001 |
| E003 | Två LED turas om | Baslåda | Upptäckare | Lampor och ljus | E01, B01, B02, R01, L01 | EL03, EL04, PR02, PR03, PR04, PR05, MK02, MK04 | E001 |
| E004 | Mini-trafikljus | Baslåda | Upptäckare | Lampor och ljus | E01, B01, B02, R01, L01 | EL03, EL04, PR03, PR04, PR05, MK02, MK04 | E003 |
| E005 | Polisljus | Baslåda | Upptäckare | Lampor och ljus | E01, B01, B02, R01, L01 | EL03, EL04, PR03, PR04, PR05, MK08 | E003 |
| E007 | LED-stafett | Baslåda | Uppfinnare | Lampor och ljus | E01, B01, B02, R01, L01 | EL03, EL04, PR05, PR11, PR12, MK05 | E004 |
| E008 | Rinnande ljus | Baslåda | Uppfinnare | Lampor och ljus | E01, B01, B02, R01, L01 | EL03, EL04, PR12, PR13, MK05, MK08 | E007 |
| E009 | Hemlig blinkkod | Baslåda | Uppfinnare | Lampor och ljus | E01, B01, B02, R01, L01 | EL03, EL04, PR05, PR11, PR13, MK10 | E008 | Bonusutkast |
| E010 | Morse med LED | Baslåda | Uppfinnare | Lampor och ljus | E01, B01, B02, R01, L01 | EL03, EL04, PR11, PR13, MK10, MK15 | E009 |
| E011 | RGB: tre färger i en LED | Baslåda | Upptäckare | Färger | E01, B01, B02, R01, L02 | EL03, EL04, PR03, PR05, MK03 | E001 |
| E012 | Färgblandaren | Baslåda | Uppfinnare | Färger | E01, B01, B02, R01, L02 | EL09, PR05, PR15, MK08 | E011 | Utkast |
| E013 | Regnbågslampan | Baslåda | Uppfinnare | Färger | E01, B01, B02, R01, L02 | EL09, PR12, PR15, MK08 | E012 |
| E014 | Humörlampan | Baslåda | Uppfinnare | Färger | E01, B01, B02, R01, L02 | EL09, PR05, PR11, PR15, MK12 | E012/E013 | Utkast |
| E015 | Dimbar LED | Baslåda | Uppfinnare | Lampor och ljus | E01, B01, B02, R01, L01 | EL09, PR15, MK08 | E012/E001 | Utkast |
| E016 | Andande ljus | Baslåda | Uppfinnare | Lampor och ljus | E01, B01, B02, R01, L01 | EL09, PR12, PR15, MK08 | E015 | Utkast |
| E017 | Nattlampa första versionen | Baslåda | Uppfinnare | Smarta ljus | E01, B01, B02, R01, L01, S01 | EL07, EL08, PR07, PR14, PR20, MK07, MK09 | E015 |
| E018 | Ljusmätaren i Seriell monitor | Baslåda | Uppfinnare | Mäta ljus | E01, B01, B02, R01, S01 | EL07, EL08, PR14, PR20, MK07, MK08 | E017 |
| E019 | Ljusstyrd dimmer | Baslåda | Ingenjör | Smarta ljus | E01, B01, B02, R01, L01, S01 | EL07, EL08, EL09, PR14, PR15, MK09 | E015, E018 |
| E020 | Soluppgångslampan | Baslåda | Ingenjör | Smarta ljus | E01, B01, B02, R01, L01 | EL09, PR12, PR15, PR16, MK08 | E016 |
| E021 | Blink utan delay | Baslåda | Ingenjör | Lampor och ljus | E01, B01, B02, R01, L01 | EL04, PR16, MK14 | E002 |
| E022 | Två saker samtidigt | Baslåda | Ingenjör | Lampor och ljus | E01, B01, B02, R01, L01 | EL04, PR16, PR17, MK14 | E021 |
| E023 | Mini-ljusshow | Baslåda | Ingenjör | Lampor och ljus | E01, B01, B02, R01, L01, L02 | EL04, EL09, PR11, PR12, PR13, PR15, MK11, MK12 | E008, E013 |
| E024 | Statuslampan | Baslåda | Ingenjör | Smarta ljus | E01, B01, B02, R01, L02 | EL09, PR07, PR11, PR17, MK12 | E014 |
| E025 | Designa din egen ljusuppfinning | Baslåda | Mästare | Eget projekt | E01, B01, B02, R01, L01, L02, S01 | EL03, EL04, EL07, EL09, PR11, PR12, PR14, PR15, PR16, MK11, MK12, MK15 | E001–E024 |
| E026 | Knappen tänder lampan | Baslåda | Upptäckare | Knappar | E01, B01, B02, R01, L01, K01 | EL05, EL06, PR06, PR07, MK02, MK05, MK06 | E001 |
| E027 | Omvänd knapp med INPUT_PULLUP | Baslåda | Upptäckare | Knappar | E01, B01, B02, R01, L01, K01 | EL05, EL06, PR06, PR07, MK06, MK14 | E026 |
| E028 | Tryckräknaren | Baslåda | Uppfinnare | Knappar | E01, B01, B02, K01 | EL05, PR06, PR07, PR09, PR20, MK07 | E027 |
| E029 | Lampan minns | Baslåda | Uppfinnare | Knappar | E01, B01, B02, R01, L01, K01 | EL05, PR06, PR07, PR08, PR17, MK05, MK14 | E027 |
| E030 | Tryck rätt färg | Baslåda | Uppfinnare | Knappar och färger | E01, B01, B02, R01, L02, K01 | EL05, EL09, PR06, PR07, PR10, PR15, MK08 | E014, E026 |
| E031 | Dubbelknappen | Baslåda | Uppfinnare | Knappar | E01, B01, B02, R01, L01, K01 | EL05, PR06, PR07, PR08, MK05 | E026 |
| E032 | Mini-kodlåset | Baslåda | Ingenjör | Knappar och spel | E01, B01, B02, R01, L01, L02, K01 | EL05, EL09, PR06, PR07, PR09, PR13, PR17, MK11, MK14 | E028, E031 |
| E033 | Passiv buzzer första tonen | Baslåda | Upptäckare | Ljud | E01, B01, B02, A01 | EL10, PR03, PR04, PR05, MK02, MK06 | E001 |
| E034 | Sirenen | Baslåda | Uppfinnare | Ljud | E01, B01, B02, A01, L01, R01 | EL10, PR05, PR12, MK08 | E033 |
| E035 | Morse med ljud | Baslåda | Uppfinnare | Ljud | E01, B01, B02, A01, K01 | EL10, EL05, PR06, PR11, PR13, MK10, MK15 | E010, E033 |
| E036 | Mini-pianot med knappar | Baslåda | Uppfinnare | Ljud och musik | E01, B01, B02, A01, K01 | EL05, EL10, PR06, PR07, PR13, MK05 | E031, E033 |
| E037 | Melodimaskinen | Baslåda | Uppfinnare | Ljud och musik | E01, B01, B02, A01 | EL10, PR12, PR13, PR11, MK10 | E033 |
| E038 | Knappstyrd jukebox | Baslåda | Ingenjör | Ljud och musik | E01, B01, B02, A01, K01, L02, R01 | EL05, EL10, EL09, PR06, PR07, PR11, PR13, PR17, MK11 | E029, E037 |
| E039 | Elektronisk tärning med LED | Baslåda | Uppfinnare | Spel | E01, B01, B02, R01, L01, K01 | EL05, EL04, PR06, PR07, PR10, PR13, MK08 | E028, E007 |
| E040 | Tärning i Seriell monitor | Baslåda | Upptäckare | Spel | E01, B01, B02, K01 | EL05, PR06, PR07, PR10, PR20, MK07 | E028 |
| E041 | Reaktionsspelet v1 | Baslåda | Ingenjör | Spel | E01, B01, B02, R01, L01, K01 | EL05, EL04, PR06, PR07, PR10, PR16, PR20, MK07, MK14 | E021, E028 |
| E042 | Reaktionsspelet med ljud | Baslåda | Ingenjör | Spel | E01, B01, B02, R01, L01, K01, A01 | EL05, EL04, EL10, PR06, PR07, PR10, PR16, PR17, MK11, MK14 | E041, E033 |
| E043 | Snabbast av två | Baslåda | Ingenjör | Spel | E01, B01, B02, R01, L01, K01, A01 | EL05, EL04, EL10, PR06, PR07, PR16, PR17, MK11, MK14 | E042 |
| E044 | Simon Says v1 | Baslåda | Ingenjör | Spel | E01, B01, B02, R01, L01, K01, A01 | EL05, EL04, EL10, PR06, PR07, PR10, PR13, PR17, MK11, MK14 | E036, E039 |
| E045 | Gissa ljusmönstret | Baslåda | Uppfinnare | Spel | E01, B01, B02, R01, L01, K01 | EL05, EL04, PR06, PR07, PR10, PR13, MK08, MK15 | E008, E039 |
| E046 | Nedräknaren | Baslåda | Uppfinnare | Tid och spel | E01, B01, B02, R01, L01, A01 | EL04, EL10, PR04, PR11, PR12, MK08 | E034 |
| E047 | Bomben tickar | Baslåda | Ingenjör | Tid och spel | E01, B01, B02, R01, L01, K01, A01 | EL05, EL04, EL10, PR06, PR07, PR16, PR17, MK14 | E021, E046 |
| E048 | Poänglampan | Baslåda | Uppfinnare | Spel | E01, B01, B02, R01, L01, K01 | EL05, EL04, PR06, PR07, PR09, PR12, MK08 | E028 |
| E049 | Spelkontroll för framtida projekt | Baslåda | Ingenjör | Knappar | E01, B01, B02, K01 | EL05, PR06, PR07, PR11, MK11, MK14 | E031 |
| E050 | Designa ditt eget knapp- och ljudspel | Baslåda | Mästare | Eget projekt | E01, B01, B02, R01, L01, L02, K01, A01 | EL05, EL10, EL09, PR06, PR07, PR10, PR11, PR13, PR17, MK11, MK12, MK15 | E026–E049 |
| E051 | Ljusdetektiven | Baslåda | Upptäckare | Mäta ljus | E01, B01, B02, R01, S01 | EL07, EL08, PR14, PR20, MK07, MK08 | E018 |
| E052 | Skuggjakten | Baslåda | Uppfinnare | Mäta ljus | E01, B01, B02, R01, L01, S01 | EL07, EL08, EL04, PR07, PR14, MK08, MK09 | E017, E051 |
| E053 | Ljusbarometern | Baslåda | Ingenjör | Mäta ljus | E01, B01, B02, R01, L01, S01 | EL07, EL08, EL04, PR12, PR14, PR20, MK07, MK09 | E051 |
| E054 | Avstånd i Seriell monitor | Baslåda | Upptäckare | Avstånd | E01, B01, B02, S02 | EL11, PR20, PR05, MK07, MK08 | E021 |
| E055 | Parkeringssensorn v1 | Baslåda | Uppfinnare | Avstånd | E01, B01, B02, R01, L01, A01, S02 | EL11, EL10, EL04, PR07, PR16, MK09, MK14 | E034, E054 |
| E056 | Avståndslampan | Baslåda | Uppfinnare | Avstånd | E01, B01, B02, R01, L02, S02 | EL11, EL09, PR07, PR15, MK09 | E024, E054 |
| E057 | Osynliga måttbandet | Baslåda | Ingenjör | Avstånd | E01, B01, B02, S02 | EL11, PR20, PR11, MK07, MK10 | E054 |
| E058 | Dörrvakten | Baslåda | Uppfinnare | Magnet och larm | E01, B01, B02, R01, L01, A01, S04 | EL12, EL04, EL10, PR06, PR07, MK06, MK09 | E035 |
| E059 | Hemlig skattlåda – sensorversion | Baslåda | Ingenjör | Magnet och larm | E01, B01, B02, R01, L02, A01, S04 | EL12, EL09, EL10, PR06, PR07, PR17, MK11, MK14 | E032, E058 |
| E060 | Skaklarmet | Baslåda | Uppfinnare | Lutning och rörelse | E01, B01, B02, R01, L01, A01, S03 | EL13, EL10, EL04, PR06, PR07, PR16, MK06, MK09 | E047 |
| E061 | Lutningsspelet | Baslåda | Ingenjör | Lutning och spel | E01, B01, B02, R01, L01, S03 | EL13, EL04, PR06, PR07, PR09, PR17, MK08, MK11 | E060 |
| E062 | Temperatur i rummet | Pluslåda | Upptäckare | Temperatur | E01, B01, B02, S05 | EL15, PR19, PR20, MK07, MK08 | E051 |
| E063 | Väderstation första versionen | Pluslåda | Uppfinnare | Temperatur | E01, B01, B02, S05, D01 | EL14, EL15, PR19, PR21, MK07, MK10 | E062 |
| E064 | Varmt eller kallt? | Pluslåda | Uppfinnare | Temperatur | E01, B01, B02, R01, L02, S05 | EL15, EL09, PR07, PR15, PR19, MK09 | E024, E062 |
| E065 | Temperaturjämförelsen | Pluslåda | Ingenjör | Temperatur | E01, B01, B02, S05, S06 | EL15, PR19, PR20, MK07, MK10 | E062 |
| E066 | Vattentemperatur-testet | Pluslåda | Ingenjör | Temperatur | E01, B01, B02, R01, S06 | EL15, PR19, PR20, MK07, MK10 | E065 |
| E067 | Rörelsevakten | Pluslåda | Uppfinnare | Rörelsesensor | E01, B01, B02, R01, L01, A01, S07 | EL16, EL04, EL10, PR06, PR07, PR16, MK06, MK09 | E058 |
| E068 | Spökhuset | Pluslåda | Ingenjör | Rörelsesensor | E01, B01, B02, R01, L02, A01, S07 | EL16, EL09, EL10, PR07, PR17, PR16, MK11, MK12 | E067, E034 |
| E069 | Smart blomkruka v1 | Pluslåda | Uppfinnare | Jordfukt | E01, B01, B02, R01, L01, S08 | EL07, EL08, PR14, PR07, MK09, MK10 | E051 |
| E070 | Växtvakten med statusfärg | Pluslåda | Ingenjör | Jordfukt | E01, B01, B02, R01, L02, S08 | EL07, EL08, EL09, PR14, PR15, PR07, MK09, MK12 | E069, E024 |
| E071 | Ljudnivå i Seriell monitor | Pluslåda | Upptäckare | Ljudsensor | E01, B01, B02, S09 | EL07, PR14, PR20, MK07, MK08 | E051 |
| E072 | Klappströmbrytaren | Pluslåda | Ingenjör | Ljudsensor | E01, B01, B02, R01, L01, S09 | EL07, EL04, PR14, PR07, PR17, MK09, MK14 | E029, E071 |
| E073 | Ljusorgel första versionen | Pluslåda | Ingenjör | Ljudsensor | E01, B01, B02, R01, L01, L02, S09 | EL07, EL09, PR14, PR15, PR12, MK08, MK09 | E071, E023 |
| E074 | Sensorlaboratoriet | Pluslåda | Mästare | Mätning | E01, B01, B02, R01, L01, L02, S01, S02, S05 | EL07, EL08, EL11, EL15, PR14, PR19, PR20, MK07, MK10, MK14 | E051–E073 |
| E075 | Designa ett eget sensorlarm | Pluslåda | Mästare | Eget projekt | E01, B01, B02, R01, L01, L02, A01, S01, S02, S03, S04, S07 | EL05, EL07, EL11, EL12, EL13, EL16, PR07, PR16, PR17, MK11, MK12, MK15 | E051–E074 |
| E076 | OLED säger hej | Baslåda | Upptäckare | Display | E01, B01, B02, D01 | EL14, PR19, PR21, MK02, MK06 | E001 |
| E077 | OLED visar mätvärden | Baslåda | Uppfinnare | Display | E01, B01, B02, D01, S01 | EL14, EL07, PR14, PR19, PR21, MK07 | E051, E076 |
| E078 | OLED-menyn | Baslåda | Ingenjör | Display | E01, B01, B02, D01, K01 | EL14, EL05, PR06, PR07, PR17, PR21, MK11, MK14 | E029, E076 |
| E079 | Mini-instrumentpanelen | Pluslåda | Ingenjör | Display och mätning | E01, B01, B02, D01, S01, S05, S02 | EL14, EL07, EL11, EL15, PR14, PR19, PR21, MK10, MK14 | E063, E077 |
| E080 | OLED-reaktionsspelet | Baslåda | Ingenjör | Display och spel | E01, B01, B02, D01, K01, R01, L01 | EL14, EL05, EL04, PR06, PR10, PR16, PR19, PR21, MK11 | E041, E076 |
| E081 | Pixel-smileyn | Pluslåda | Upptäckare | LED-matris | E01, B01, B02, D02 | EL19, PR19, PR22, MK02, MK06 | E076 |
| E082 | Matris-animationen | Pluslåda | Uppfinnare | LED-matris | E01, B01, B02, D02 | EL19, PR12, PR13, PR19, PR22, MK08 | E081 |
| E083 | Mini-Snake-idé | Pluslåda | Ingenjör | LED-matris och spel | E01, B01, B02, D02, K01 | EL19, EL05, PR06, PR13, PR17, PR22, MK11, MK14 | E049, E082 |
| E084 | NeoPixel första regnbågen | Pluslåda | Upptäckare | NeoPixel | E01, B01, B02, L03 | EL18, PR19, PR12, MK02, MK06 | E013 |
| E085 | NeoPixel-timer | Pluslåda | Uppfinnare | NeoPixel | E01, B01, B02, L03, K01 | EL18, EL05, PR06, PR12, PR16, PR17, MK08, MK14 | E047, E084 |
| E086 | Reaktionsring | Pluslåda | Ingenjör | NeoPixel och spel | E01, B01, B02, L03, K01, A01 | EL18, EL05, EL10, PR06, PR10, PR16, PR17, PR19, MK11 | E041, E084 |
| E087 | Servo första rörelsen | Pluslåda | Upptäckare | Servo | E01, B01, B02, M01 | EL20, PR19, PR05, MK02, MK06 | E015 |
| E088 | Vredstyrd servo | Pluslåda | Uppfinnare | Servo | E01, B01, B02, K02, M01 | EL07, EL20, PR14, PR19, MK08 | E087 |
| E089 | Avståndsstyrd visare | Pluslåda | Ingenjör | Servo och sensor | E01, B01, B02, S02, M01 | EL11, EL20, PR11, PR14, PR19, MK09, MK14 | E056, E087 |
| E090 | Skattkistan öppnas | Pluslåda | Ingenjör | Servo och uppdrag | E01, B01, B02, K01, M01, L02, A01 | EL05, EL20, EL09, EL10, PR06, PR07, PR17, PR19, MK11, MK12 | E032, E087 |
| E091 | Temperaturvisaren | Pluslåda | Ingenjör | Servo och mätning | E01, B01, B02, S05, M01 | EL15, EL20, PR19, PR11, MK09 | E063, E087 |
| E092 | Automatisk dörrvakt | Pluslåda | Ingenjör | Smart uppfinning | E01, B01, B02, S07, M01, L02 | EL16, EL20, EL09, PR06, PR07, PR17, PR19, MK11, MK14 | E067, E087 |
| E093 | Smart nattlampa deluxe | Pluslåda | Ingenjör | Smart uppfinning | E01, B01, B02, R01, S01, L03, D01 | EL07, EL14, EL18, PR14, PR16, PR19, PR21, MK09, MK12 | E017, E076, E084 |
| E094 | Växtvakt med display | Pluslåda | Ingenjör | Smart uppfinning | E01, B01, B02, S08, D01, L02 | EL07, EL14, EL09, PR14, PR19, PR21, MK09, MK10 | E070, E076 |
| E095 | Rumsklimatets humör | Pluslåda | Ingenjör | Smart uppfinning | E01, B01, B02, S05, D01, L03 | EL15, EL14, EL18, PR19, PR21, PR17, MK10, MK12 | E063, E084 |
| E096 | Interaktiv larmcentral | Pluslåda | Mästare | Smart uppfinning | E01, B01, B02, S04, S07, D01, L02, A01 | EL12, EL16, EL14, EL09, EL10, PR06, PR07, PR17, PR18, PR19, MK11, MK14 | E058, E067, E078 |
| E097 | Mini-kontrollpanel | Pluslåda | Mästare | Smart uppfinning | E01, B01, B02, K01, K02, D01, L02 | EL05, EL07, EL14, EL09, PR06, PR14, PR17, PR19, PR21, MK11, MK12 | E078, E088 |
| E098 | Touch-pianot | Pluslåda | Ingenjör | Touch och ljud | E01, B01, B02, K03, A01, L03 | EL17, EL10, EL18, PR19, PR13, PR17, MK08, MK11 | E036, E084 |
| E099 | Touch-kodlåset | Pluslåda | Mästare | Touch och uppdrag | E01, B01, B02, K03, M01, L02, A01 | EL17, EL20, EL09, EL10, PR13, PR17, PR18, PR19, MK11, MK14 | E032, E090, E098 |
| E100 | Designa en smart uppfinning | Pluslåda | Mästare | Eget projekt | E01, B01, B02, D01, L02, L03, M01, S01, S02, S05, S07, S08, A01, K01, K02 | EL07, EL11, EL14, EL15, EL16, EL18, EL20, PR11, PR14, PR16, PR17, PR19, PR21, MK11, MK12, MK15 | E076–E099 |
| E101 | DC-motor första snurret | Makerlåda | Upptäckare | Motorer | E01, B01, B02, M03, M04 | EL21, PR03, PR05, MK06, MK13 | E087 |
| E102 | Motor åt båda hållen | Makerlåda | Uppfinnare | Motorer | E01, B01, B02, M03, M04, K01 | EL21, EL05, PR06, PR07, MK13, MK14 | E101 |
| E103 | Fartkontroll med PWM | Makerlåda | Ingenjör | Motorer | E01, B01, B02, M03, M04, K02 | EL21, EL07, EL09, PR14, PR15, MK08, MK13 | E101, E088 |
| E104 | Mini-fläkten | Makerlåda | Uppfinnare | Motorer och uppfinning | E01, B01, B02, M03, M04, S05 | EL21, EL15, PR07, PR19, MK11, MK13 | E062, E101 |
| E105 | Robotbas första versionen | Makerlåda | Ingenjör | Robotik | E01, B01, B02, M03, M04 | EL21, PR11, PR17, MK13, MK14 | E102 |
| E106 | Robot som undviker hinder | Makerlåda | Mästare | Robotik | E01, B01, B02, S02, M03, M04 | EL11, EL21, PR07, PR11, PR17, PR18, MK11, MK13, MK14 | E055, E105 |
| E107 | Stegmotor första stegen | Makerlåda | Uppfinnare | Stegmotor | E01, B01, B02, M02 | EL22, PR12, PR19, MK06, MK13 | E087 |
| E108 | Mini-karusellen | Makerlåda | Ingenjör | Stegmotor | E01, B01, B02, M02, K01, L02 | EL22, EL05, EL09, PR06, PR12, PR17, PR19, MK11, MK12 | E107 |
| E109 | RFID första läsningen | Makerlåda | Upptäckare | RFID | E01, B01, B02, C01 | EL23, PR19, PR20, MK07, MK10 | E076 |
| E110 | RFID-passersystem | Makerlåda | Ingenjör | RFID | E01, B01, B02, C01, L02, A01 | EL23, EL09, EL10, PR07, PR13, PR17, PR19, MK11, MK14 | E032, E109 |
| E111 | RFID-skattkista | Makerlåda | Mästare | RFID och servo | E01, B01, B02, C01, M01, L02, A01 | EL23, EL20, EL09, EL10, PR13, PR17, PR18, PR19, MK11, MK12, MK14 | E090, E110 |
| E112 | IR-fjärrens hemliga koder | Makerlåda | Upptäckare | IR | E01, B01, B02, C02 | EL24, PR19, PR20, MK07, MK10 | E028 |
| E113 | Fjärrstyrd lampa | Makerlåda | Uppfinnare | IR | E01, B01, B02, C02, R01, L02 | EL24, EL09, PR07, PR13, PR17, PR19, MK11 | E024, E112 |
| E114 | Fjärrstyrd servo | Makerlåda | Ingenjör | IR och servo | E01, B01, B02, C02, M01 | EL24, EL20, PR07, PR13, PR17, PR19, MK11, MK14 | E087, E112 |
| E115 | Klockan vaknar | Makerlåda | Uppfinnare | Tid | E01, B01, B02, D03, D01 | EL14, EL25, PR19, PR21, MK06, MK10 | E076 |
| E116 | Tidsstyrd påminnare | Makerlåda | Ingenjör | Tid och smart pryl | E01, B01, B02, D03, D01, L02, A01 | EL25, EL14, EL09, EL10, PR07, PR17, PR19, PR21, MK11, MK12 | E115 |
| E117 | SD-kort första loggen | Makerlåda | Ingenjör | Dataloggning | E01, B01, B02, D04, S05 | EL15, EL26, PR19, PR23, MK10, MK14 | E062 |
| E118 | Min väderloggare | Makerlåda | Mästare | Dataloggning | E01, B01, B02, D04, D03, S05, D01 | EL15, EL25, EL26, EL14, PR19, PR21, PR23, MK10, MK12, MK14 | E115, E117 |
| E119 | Första WiFi-sidan | Makerlåda | Ingenjör | WiFi och IoT | E01, B01, B02, R01, L01 | EL04, PR24, PR25, MK14 | E021 |
| E120 | Familjens smarta uppfinning | Makerlåda | Mästare | Eget Makerprojekt | E01, B01, B02, D01, L02, L03, M01, M03, M04, S01, S02, S05, S07, S08, C01, C02 | EL11, EL14, EL15, EL16, EL18, EL20, EL21, EL23, EL24, PR17, PR18, PR19, PR24, PR25, PR26, MK11, MK12, MK13, MK14, MK15 | E001–E119 |
