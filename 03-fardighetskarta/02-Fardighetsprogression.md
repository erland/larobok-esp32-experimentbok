# Steg 2 – Färdighetsprogression

## Syfte

Detta dokument beskriver en möjlig ordning för hur färdigheter bör introduceras. Progressionen är inte en färdig kapitelstruktur, men den ger ett ramverk för att senare skapa experimentbanken och beroendegrafen.

---

# Progressionsnivåer

| Nivå | Arbetsnamn | Fokus |
|---|---|---|
| 1 | Tända och styra | LED, output, enkel kod |
| 2 | Reagera på världen | knappar, sensorer, input |
| 3 | Göra saker roliga | ljud, spel, slump och poäng |
| 4 | Mäta världen | analog input, avstånd, ljus, temperatur |
| 5 | Visa information | OLED, matris, text och grafik |
| 6 | Röra på saker | servo och motorer |
| 7 | Smarta uppfinningar | kombinera sensorer, beslut och output |
| 8 | Robotik och mekanik | motorstyrning, avstånd, rörelse |
| 9 | Internet och data | WiFi, webb, loggning |
| 10 | Egna projekt | kombinera och designa själv |

---

# Nivå 1 – Tända och styra

## Centrala färdigheter

| Typ | ID |
|---|---|
| Elektronik | EL01, EL02, EL03, EL04 |
| Programmering | PR01, PR02, PR03, PR04, PR05 |
| Maker | MK01, MK02, MK03, MK04 |

## Typiska experiment

- Blinkande LED
- Flera LED i rad
- Trafikljus
- Polisljus
- Fyrtorn
- Färgblandning med RGB-LED

---

# Nivå 2 – Reagera på världen

## Centrala färdigheter

| Typ | ID |
|---|---|
| Elektronik | EL05, EL06, EL07, EL08 |
| Programmering | PR06, PR07, PR08, PR14 |
| Maker | MK05, MK06, MK07, MK08 |

## Typiska experiment

- Knapp som tänder LED
- Ljus som växlar med knapp
- Nattlampa med LDR
- Hemligt dörrlarm med reedkontakt
- Skaklarm med tilt-sensor
- Ljusstyrka med potentiometer

---

# Nivå 3 – Göra saker roliga

## Centrala färdigheter

| Typ | ID |
|---|---|
| Elektronik | EL09, EL10 |
| Programmering | PR09, PR10, PR11, PR12 |
| Tillämpning | AP01, AP02, AP06 |

## Typiska experiment

- Elektronisk tärning
- Reaktionsspel
- Morsekod
- Litet piano
- Simon Says
- Gissa talet
- Poängräknare

---

# Nivå 4 – Mäta världen

## Centrala färdigheter

| Typ | ID |
|---|---|
| Elektronik | EL07, EL08, EL11, EL15, EL16 |
| Programmering | PR14, PR16, PR20 |
| Maker | MK07, MK08, MK09 |

## Typiska experiment

- Avståndsmätare
- Parkeringssensor
- Ljusmätare
- Temperaturmätare
- Rörelselarm
- Smart blomkruka
- Ljudnivåmätare

---

# Nivå 5 – Visa information

## Centrala färdigheter

| Typ | ID |
|---|---|
| Elektronik | EL14, EL18, EL19 |
| Programmering | PR13, PR19, PR21, PR22 |
| Tillämpning | AP05 |

## Typiska experiment

- Visa text på OLED
- Visa sensorvärden på OLED
- Mini-animation
- Enkel meny
- LED-matris-smiley
- Temperaturdisplay
- Timer med display

---

# Nivå 6 – Röra på saker

## Centrala färdigheter

| Typ | ID |
|---|---|
| Elektronik | EL20 |
| Programmering | PR15, PR16, PR17 |
| Tillämpning | AP07 |

## Typiska experiment

- Servo som pekare
- Mini-grind
- Skattkista som öppnas
- Robotarm med två servon
- Servo som reagerar på avstånd
- Servo som styrs av potentiometer

---

# Nivå 7 – Smarta uppfinningar

## Centrala färdigheter

| Typ | ID |
|---|---|
| Elektronik | flera tidigare |
| Programmering | PR17, PR18, PR19 |
| Maker | MK10, MK11, MK12 |
| Tillämpning | AP08, AP12 |

## Typiska experiment

- Smart nattlampa
- Växtvakt
- Hemlarm
- Interaktiv skattkista
- Automatisk dörrvakt
- Rumsklimatindikator
- Ljudstyrd lampa

---

# Nivå 8 – Robotik och mekanik

## Centrala färdigheter

| Typ | ID |
|---|---|
| Elektronik | EL21, EL22 |
| Programmering | PR16, PR17, PR18 |
| Maker | MK13, MK14 |
| Tillämpning | AP09 |

## Typiska experiment

- Motor som snurrar åt två håll
- Enkel robotbil
- Robot som undviker hinder
- Stegmotor-visare
- Mini-karusell
- Avståndsstyrd motor

---

# Nivå 9 – Internet och data

## Centrala färdigheter

| Typ | ID |
|---|---|
| Elektronik | EL23, EL24, EL25, EL26 |
| Programmering | PR23, PR24, PR25, PR26 |
| Tillämpning | AP10, AP11 |

## Typiska experiment

- Visa IP-adress
- Webbsida som tänder LED
- Mobilstyrd lampa
- Enkel väderstation
- Logga temperatur till SD-kort
- RFID-passersystem
- Internetstyrd statuslampa

---

# Nivå 10 – Egna projekt

## Centrala färdigheter

| Typ | ID |
|---|---|
| Maker | MK11, MK12, MK14, MK15 |
| Tillämpning | AP12 |

## Typiska experiment

- Designa ett eget spel
- Bygg ett eget larm
- Bygg en egen smart pryl
- Kombinera sensor, display och servo
- Skapa ett familjeprojekt
- Förklara och demonstrera din uppfinning

---

# Viktig designregel

Varje nytt experiment bör markeras med:

| Fält | Exempel |
|---|---|
| Ny huvudfärdighet | PR16 – `millis()` utan blockering |
| Repetition | LED, knapp, buzzer |
| Komponentnivå | Baslåda |
| Svårighetsgrad | Uppfinnare |
| Bygger på | Reaktionsspel, trafikljus |

Det gör att experimentbanken senare kan sorteras och balanseras.
