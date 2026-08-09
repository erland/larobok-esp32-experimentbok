# Steg 0 – Bokens designprinciper

## Syfte

Detta dokument beskriver de grundprinciper som ska styra arbetet med boken. Det ska fungera som projektets gemensamma referens när vi senare skapar färdighetskarta, experimentbank, kapitelstruktur och färdiga experiment.

Målet är att boken ska bli mer än en samling fristående elektronikprojekt. Den ska kännas som en sammanhängande upptäcktsresa där barn och vuxen bygger, testar, felsöker, funderar och gradvis lär sig mer.

---

# 1. Målgrupp

Boken riktar sig till barn i åldern **7–12 år**.

## 7–9 år

För barn i den yngre delen av målgruppen utgår boken från att en vuxen hjälper till aktivt.

Den vuxne ansvarar särskilt för:

- att kopplingar görs säkert,
- att komponenter sätts rätt,
- att USB, batterier och strömförsörjning hanteras korrekt,
- att barnet får stöd vid felsökning,
- att programmeringen förklaras stegvis.

Barnet ska ändå kunna vara aktivt i varje experiment genom att:

- välja färger,
- trycka på knappar,
- ändra värden,
- testa hypoteser,
- observera vad som händer,
- föreslå förbättringar.

## 10–12 år

För äldre barn ska många experiment kunna genomföras mer självständigt, men fortfarande med vuxen närvarande vid nya kopplingar, motorer, strömförsörjning eller mer avancerade moment.

---

# 2. Pedagogisk grundidé

Varje experiment ska kännas som ett litet uppdrag, mysterium eller bygge.

Boken ska inte bara säga:

> Koppla så här och ladda upp koden.

Den ska istället hjälpa barnet att tänka:

> Vad tror du händer?  
> Hur kan vi testa det?  
> Vad ändras om vi gör så här?  
> Hur kan vi förbättra uppfinningen?

Målet är att utveckla nyfikenhet, tekniskt självförtroende och problemlösningsförmåga.

---

# 3. Experimentens grundstruktur

Alla experiment bör följa samma återkommande mall.

## Rekommenderad mall

1. **Uppdraget**  
   En kort berättelse eller konkret utmaning.

2. **Vad ska vi upptäcka?**  
   Det centrala fenomenet, komponenten eller programmeringsidén.

3. **Det här behöver du**  
   Komponent-ID och nivå: Baslåda, Pluslåda eller Makerlåda.

4. **Bygg kretsen**  
   Tydliga steg och gärna breadboardbild.

5. **Programmera**  
   Kort och tydligt kodexempel.

6. **Testa**  
   Vad barnet ska göra när allt är inkopplat.

7. **Vad händer?**  
   Observationer och enkel förklaring.

8. **Felsökning**  
   Vanliga fel och hur man hittar dem.

9. **Utmaningar**  
   Små vidareutmaningar i stigande svårighetsgrad.

10. **Visste du att...?**  
    Koppling till teknik i vardagen.

---

# 4. Progression

Experimenten ska vara ordnade så att de gradvis bygger vidare på varandra.

## Principer

- Introducera helst bara **en ny komponent** åt gången.
- Introducera helst bara **en ny programmeringsidé** åt gången.
- Återanvänd tidigare komponenter ofta.
- Låt barnet känna igen kopplingar och kodmönster.
- Gå från synliga, direkta effekter till mer abstrakta koncept.

## Exempel på progression

1. Tända en LED.
2. Blinka en LED.
3. Styra LED med knapp.
4. Göra ett trafikljus.
5. Lägga till ljud.
6. Göra ett reaktionsspel.
7. Visa poäng på skärm.
8. Bygga ett större spel.
9. Lägga till sensor.
10. Göra en smart uppfinning.

---

# 5. Komponentprinciper

Boken ska utgå från en standardiserad experimentlåda.

## Principer

- Billiga och lättillgängliga komponenter prioriteras.
- Breadboard-vänliga moduler prioriteras.
- Komponenter ska återanvändas i många experiment.
- Varje komponent ska ha ett fast ID.
- Varje ny komponent bör helst kunna användas i minst 5–10 experiment.
- Specialkomponenter som bara används i 1–2 experiment bör undvikas eller placeras i Makerlådan.

## Komponentnivåer

| Nivå | Syfte |
|---|---|
| Baslåda | Räcker till många enkla och roliga experiment |
| Pluslåda | Lägger till sensorer, rörelse, ljus och mer interaktion |
| Makerlåda | Lägger till mer avancerade IoT-, robot- och dataprojekt |

---

# 6. Säkerhetsprinciper

Säkerhet ska gå före allt annat.

## Boken ska undvika

- 230V/nätspänning,
- litiumbatteriladdning,
- starka motorer,
- hög värme,
- vassa verktyg som krav,
- lödning som krav i huvudspåret,
- kopplingar där ESP32-pinnar riskerar att belastas direkt av motorer eller hög ström.

## Boken ska betona

- ESP32 använder 3,3V-logik.
- Motorer ska inte drivas direkt från GPIO-pinnar.
- LED ska normalt ha seriemotstånd.
- Felkoppling är normalt och en del av lärandet.
- Koppla ur USB innan större ändringar i kopplingen.
- En vuxen bör kontrollera kopplingar innan ström ansluts.

---

# 7. Programmeringsprinciper

Koden ska vara enkel, tydlig och gradvis växande.

## Kodstil

- Använd Arduino IDE som huvudspår.
- Håll programmen korta i början.
- Kommentera för att förklara idéer, inte varje rad.
- Återanvänd namn och kodmönster.
- Introducera bibliotek först när de behövs.
- Undvik onödigt avancerade abstraktioner tidigt.

## Progression i kod

Boken bör gradvis introducera:

- `setup()` och `loop()`,
- digital output,
- digital input,
- variabler,
- `if`,
- `for`,
- funktioner,
- analog input,
- PWM,
- `millis()`,
- arrayer,
- slump,
- bibliotek,
- tillståndsmaskiner,
- WiFi och enkel webbkommunikation.

---

# 8. Felsökning som lärande

Felsökning ska inte ses som ett misslyckande. Det ska vara en återkommande del av boken.

Varje experiment bör innehålla en liten felsökningsruta.

## Exempel

| Problem | Möjlig orsak |
|---|---|
| LED lyser inte | Den sitter åt fel håll eller saknar kontakt |
| Inget laddas upp | Fel kort eller fel port i Arduino IDE |
| Sensorn ger konstiga värden | Fel pinne, lös kabel eller fel spänning |
| Motorn rycker bara | För lite ström eller fel motordrivare |
| Skärmen är svart | Fel I²C-adress eller fel SDA/SCL |

---

# 9. Ton och berättarstil

Boken ska vara varm, uppmuntrande och nyfiken.

Den ska tala till barnet och den vuxne tillsammans.

## Stil

- Hellre “prova” än “gör exakt”.
- Hellre “vad tror du händer?” än “det rätta svaret är”.
- Hellre “uppdrag” än “övning”.
- Hellre konkreta vardagsexempel än lång teori.
- Förklaringar ska vara korta men inte förenklade på ett sätt som blir fel.

---

# 10. Visuell princip

Boken bör vara tydlig och visuell.

## Rekommendationer

- Varje experiment bör ha en enkel komponentruta.
- Breadboardkopplingar bör visas med tydliga bilder.
- Kodblock ska vara läsbara och inte för långa.
- Felsökningsrutor ska återkomma konsekvent.
- Symboler kan användas för nivå, tid, vuxenhjälp och riskmoment.

## Exempel på symboler

| Symbol | Betydelse |
|---|---|
| 🟢 | Baslåda |
| 🟡 | Pluslåda |
| 🔵 | Makerlåda |
| 👨‍👧 | Vuxen bör hjälpa |
| ⚠️ | Var extra försiktig |
| 🧪 | Testa och utforska |
| ⭐ | Utmaning |

---

# 11. Experimentens svårighetsgrad

Svårighetsgrad bör inte bara handla om komponentnivå. Ett experiment kan använda Baslådan men ändå vara programmeringsmässigt svårare.

## Rekommenderad modell

| Nivå | Beskrivning |
|---|---|
| Upptäckare | Koppla, testa och se direkt resultat |
| Uppfinnare | Ändra värden och bygg vidare |
| Ingenjör | Kombinera flera komponenter och idéer |
| Mästare | Designa egen variant eller större lösning |

---

# 12. Bokens kvalitetskriterier

Ett experiment bör bara tas med om det uppfyller flera av följande kriterier:

- Det är roligt eller överraskande för barn.
- Det ger synligt eller hörbart resultat.
- Det lär ut en tydlig komponent eller färdighet.
- Det återanvänder tidigare kunskap.
- Det går att bygga på breadboard.
- Det går att felsöka på ett begripligt sätt.
- Det kan byggas ut med minst en utmaning.
- Det har koppling till teknik i vardagen.

---

# 13. Beslut som gäller tills vidare

Dessa beslut gäller för kommande planeringssteg:

| Område | Beslut |
|---|---|
| Plattform | ESP32 DevKit |
| Programmering | Arduino IDE |
| Koppling | Breadboard |
| Målgrupp | 7–12 år |
| Vuxenstöd | Förväntas för 7–9 år |
| Grundstruktur | Baslåda, Pluslåda, Makerlåda |
| Komponentreferenser | Fasta komponent-ID |
| Säkerhet | Ingen nätspänning, ingen litiumladdning, inget lödkrav i huvudspår |
| Format | Markdown som primärt arbetsformat |

---

# 14. Nästa steg

Nästa planeringssteg är att skapa en **färdighetskarta**.

Den ska visa vilka elektronik-, programmerings- och problemlösningsfärdigheter boken ska bygga upp, och i vilken ungefärlig ordning de bör introduceras.
