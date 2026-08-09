# 90 – Kapitelöversikt och produktionsöversikt

## Syfte

Detta dokument är den samlade produktionsöversikten för bokens kapitelstruktur. Det ska användas innan enskilda experiment skrivs, så att varje kapitel får rätt pedagogisk roll, rätt komponentnivå och rätt plats i helheten.

Dokumentet ersätter den tidigare kortare översikten och ska ses som styrande för kommande steg i bokproduktionen.

---

# Bokens pedagogiska resa

Boken är tänkt som en resa i fyra stora rörelser.

## 1. Jag kan styra elektronik

Barnet lär sig att ESP32 kan få saker att hända:

- tända LED,
- blinka,
- skapa färg,
- reagera på knapp,
- spela ljud,
- göra enkla spel.

Detta motsvarar Kapitel 1–4.

## 2. Jag kan mäta världen

Barnet lär sig att ESP32 kan uppfatta omgivningen:

- ljus,
- avstånd,
- magnet,
- lutning,
- rörelse,
- temperatur,
- jordfuktighet,
- ljudnivå.

Detta motsvarar Kapitel 5–7.

## 3. Jag kan bygga riktiga prylar

Barnet kombinerar input, output, display och rörelse till användbara saker:

- OLED-gränssnitt,
- LED-matris,
- NeoPixel,
- servo,
- smarta lampor,
- larm,
- växtvakt,
- skattkista.

Detta motsvarar Kapitel 8–10.

## 4. Jag kan skapa egna makerprojekt

Barnet bygger mer avancerade eller öppna projekt:

- robotik,
- RFID,
- IR,
- tid,
- loggning,
- WiFi,
- eget slutprojekt.

Detta motsvarar Kapitel 11–14.

---

# Kapitelstruktur

| Kapitel | Titel | Primär komponentnivå | Pedagogisk huvudroll | Kapitelprojekt |
|---:|---|---|---|---|
| 1 | Kom igång | Baslåda | Första framgången | Blinkande namnskylt |
| 2 | LED och PWM | Baslåda | Ljus, färg och styrning | Trafikljus/stämningslampa |
| 3 | Knappar | Baslåda | Digital input och tillstånd | Kodlås |
| 4 | Ljud och spel | Baslåda | Interaktion, ljud och spelregler | Simon Says/reaktionsspel |
| 5 | Ljus och avstånd | Baslåda | Första mätinstrumenten | Parkeringshjälpen |
| 6 | Larm, rörelse och närvaro | Bas/Plus | Händelsesensorer | Spökhuset |
| 7 | Temperatur, miljö och mätningar | Pluslåda | Miljödata och kalibrering | Sensorlaboratoriet |
| 8 | OLED och användargränssnitt | Bas/Plus | Visa information | Mini-instrumentpanelen |
| 9 | NeoPixel och LED-matris | Pluslåda | Animation, spel och ljuseffekter | Reaktionsringen |
| 10 | Servo och smarta prylar | Pluslåda | Fysisk rörelse och smarta system | Interaktiv larmcentral |
| 11 | Motorer och robotik | Makerlåda | Motorstyrning och robotlogik | Hinderrobot |
| 12 | RFID, IR och identifiering | Makerlåda | Identifiering och fjärrstyrning | RFID-skattkistan |
| 13 | Tid, loggning och WiFi | Makerlåda | Självständiga och uppkopplade prylar | Väderloggare/webbstatus |
| 14 | Familjens Makerprojekt | Valfri | Eget skapande | Familjens smarta uppfinning |

---

# Kapitelberoenden

```text
Kapitel 1
  ↓
Kapitel 2
  ↓
Kapitel 3
  ↓
Kapitel 4
  ↓
Kapitel 5
  ↓
Kapitel 6
  ↓
Kapitel 7
  ↓
Kapitel 8
  ↓
Kapitel 9
  ↓
Kapitel 10
  ↓
Kapitel 11–13
  ↓
Kapitel 14
```

## Kritiska beroenden

| Senare kapitel | Kräver särskilt från tidigare |
|---|---|
| Kapitel 3 | LED och enkel output från Kapitel 1–2 |
| Kapitel 4 | knapphantering från Kapitel 3 |
| Kapitel 5 | Seriell monitor, LED/RGB/buzzer från Kapitel 1–4 |
| Kapitel 6 | larm-output från Kapitel 4–5 |
| Kapitel 7 | sensorvärden och trösklar från Kapitel 5 |
| Kapitel 8 | sensorvärden från Kapitel 5–7 |
| Kapitel 9 | `for`, arrayer och färg från Kapitel 2–4 |
| Kapitel 10 | sensorer, statusfärg och bibliotek från Kapitel 5–9 |
| Kapitel 11 | PWM, sensorer och säkerhet från tidigare kapitel |
| Kapitel 12 | statuslogik, servo och bibliotek |
| Kapitel 13 | OLED, sensorer och bibliotek |
| Kapitel 14 | hela bokens byggblock |

---

# Programmeringsprogression

| Kapitel | Nya eller fördjupade programmeringsidéer |
|---:|---|
| 1 | `setup()`, `loop()`, `pinMode()`, `digitalWrite()`, `delay()` |
| 2 | variabler, PWM, enkla funktioner |
| 3 | `digitalRead()`, `INPUT_PULLUP`, `if`, booleska lägen |
| 4 | slump, arrayer, enklare spelstatus, ljudsekvenser |
| 5 | `analogRead()`, tröskelvärden, sensorfunktioner |
| 6 | digitala sensorer, statuslägen, enkla larmtillstånd |
| 7 | bibliotek, kalibrering, flera sensorvärden |
| 8 | text, skärmlägen, enkel meny |
| 9 | pixel-arrayer, animationer, loopar över ljuspunkter |
| 10 | servo-bibliotek, mappning av sensorvärde till rörelse |
| 11 | motorfunktioner, PWM på motor, enkel robotlogik |
| 12 | ID-jämförelse, fjärrkommandon, `switch`/tabell |
| 13 | tid, filskrivning, enkel webbserver |
| 14 | projekttänkande, funktioner, stegvis förbättring |

---

# Komponentprogression

| Fas | Komponenter som introduceras |
|---|---|
| Start | ESP32, breadboard, LED, motstånd |
| Basinteraktion | RGB-LED, knapp, potentiometer, buzzer |
| Bas-sensorik | LDR, HC-SR04, reedkontakt, tilt |
| Plus-sensorik | DHT22, DS18B20, PIR, jordfuktighet, mikrofon |
| Visning | OLED, LED-matris, NeoPixel |
| Rörelse | servo |
| Maker | DC-motor, motordrivare, stegmotor, RFID, IR, RTC, MicroSD, WiFi |

---

# Tempo- och motivationsanalys

## Kapitel 1–2

Måste ge snabba vinster. Barnet ska se resultat efter några minuter.

Risk: för mycket teori om ström och motstånd.  
Motåtgärd: teori placeras i små faktarutor efter att LED lyser.

## Kapitel 3–4

Interaktionen gör projekten mer lekfulla.

Risk: kodlogik blir abstrakt.  
Motåtgärd: använd spel och uppdrag för att motivera `if`, slump och arrayer.

## Kapitel 5–7

Sensorer kan bli för mätorienterade.

Risk: flera experiment i rad visar bara siffror.  
Motåtgärd: varva alltid mätning med ett användbart projekt.

## Kapitel 8–10

Detta är bokens stora “det känns som riktiga prylar”-del.

Risk: för många bibliotek och moduler samtidigt.  
Motåtgärd: introducera en output i taget och återanvänd tidigare input.

## Kapitel 11–13

Makerdelen är tekniskt mer avancerad.

Risk: motorer, SD och WiFi kan frustrera.  
Motåtgärd: varje block börjar med ett minimalt test innan större projekt.

## Kapitel 14

Slutkapitlet ska ge självförtroende, inte ny komplexitet.

Risk: projektet blir för stort.  
Motåtgärd: börja med minsta fungerande version.

---

# Rekommenderad omfattning

| Typ | Rekommenderat antal |
|---|---:|
| Huvudexperiment | 75–90 |
| Bonusprojekt | 20–30 |
| Reserv/webbmaterial | 5–15 |

Boken bör inte nödvändigtvis trycka alla 120 experiment som huvudspår. Experimentbanken är medvetet större än den slutliga boken för att ge flexibilitet.

---

# Produktionsprioritering

## Första produktionsblock

Kapitel 1–4 bör produceras först eftersom de sätter stil, ton och kodnivå för hela boken.

## Andra produktionsblock

Kapitel 5–7 bör skrivas därefter och testas extra noga, eftersom sensorkapitlen avgör om barnet förstår input/output-mönstret.

## Tredje produktionsblock

Kapitel 8–10 kan sedan byggas som bokens mest engagerande “smarta prylar”-del.

## Fjärde produktionsblock

Kapitel 11–14 bör produceras sist och kan eventuellt delas i huvudbok + bonusmaterial.

---

# Kvalitetskontroll före skrivstart

Innan ett kapitel skrivs ska följande vara känt:

- vilka experiment som är huvudspår,
- vilka experiment som är bonus,
- vilken ny komponent kapitlet introducerar,
- vilken ny kodidé kapitlet introducerar,
- vilket kapitelprojekt som avslutar kapitlet,
- vilka breadboardbilder som behövs,
- vilka säkerhetsrutor som behövs,
- vilka experiment som kan återanvända samma koppling.

---

# Nästa steg

Efter v25.1 bör Kapitel 1–4 fördjupas till samma detaljnivå som Kapitel 5–14. Därefter är kapiteldesignen tillräckligt robust för 5A.3 – Komponentlivscykel.
