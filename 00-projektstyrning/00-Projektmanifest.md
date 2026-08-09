# Projektmanifest – ESP32 Experimentbok

## Vision
Skapa den mest pedagogiska svenskspråkiga experimentboken för barn (7–12 år) och deras föräldrar, byggd kring ESP32, breadboard och billiga standardkomponenter.

## Projektmål
- 120 planerade experiment med tydlig progression.
- Återanvänd samma komponenter och kopplingar så långt som möjligt.
- Experimenten ska vara roliga, säkra och ge tidiga framgångar.
- Bas-, Plus- och Makerlådor ska hålla inköpskostnaden låg.

## Målgrupp
- Barn 7–12 år.
- Barn 7–9 år arbetar tillsammans med vuxen.
- Barn 10–12 år kan genomföra många experiment mer självständigt.

## Pedagogiska principer
1. Ett nytt huvudkoncept per experiment.
2. Learning by doing.
3. Bygg vidare på tidigare kopplingar.
4. Regelbundna 'wow'-projekt.
5. Felsökning är en naturlig del av lärandet.
6. Säkerhet prioriteras alltid.

## Teknisk plattform
- ESP32 DevKit som standard.
- Arduino IDE.
- Breadboard utan lödning.
- Billiga standardmoduler.
- USB-ström som normalfall.

## Projektstruktur
- 00-projektstyrning – styrande dokument.
- 01–03 – komponenter, färdigheter och progression.
- 04 – experimentbank.
- 05 – analyser.
- 06–08 – kapitel, illustrationer och bokproduktion.

## Produktionsflöde
Planering → Experimentbank → Analys → Kapitel → Experiment → Illustrationer → Revision → EPUB/PDF.

## Kvalitetskrav
Varje experiment ska på sikt innehålla:
- syfte
- lärandemål
- komponentlista
- kopplingsschema
- kod
- förklaring
- felsökning
- utmaning
- bonusidé
- uppskattad byggtid
- säkerhetsnotering vid behov

## Viktiga beslut
- Plattform: ESP32.
- 120 experiment planeras.
- Tre komponentnivåer: Bas, Plus och Maker.
- Återanvändning prioriteras framför unika komponenter.
- Huvudmål: lust att fortsätta experimentera.

## Projektstatus
Genomfört:
- Steg 0–4.5.
Nästa steg:
- Steg 5 – Kapitelstruktur.


## Produktionsdesignstatus

- 5A.1 Kapiteldesign: klar första komplett version för 14 kapitel.
- Nästa steg: 5A.2 Breadboard-progression.


## v25.1 – Fördjupade styrdokument

Kapitelöversikten och kapiteldesignprinciperna har fördjupats och är nu styrande för kommande produktion. Kvarvarande 5A.1-korrigering är att fördjupa Kapitel 1–4.


## v25.2 – Kapitel 1–2 fördjupade

Kapitel 1 och 2 har reviderats och fördjupats. De beskriver nu tydligt första framgången, LED/PWM/RGB-progressionen, kapitelprojekt och produktionskrav.


## v25.3 – 5A.1 konsoliderad

Kapitel 3 och 4 har fördjupats och samtliga kapiteldesignfiler har nu tillräckligt jämn struktur för att gå vidare till 5A.3 – Komponentlivscykel.


## 5A.3 – Komponentlivscykel

Komponenternas livscykel har analyserats. Baslådan är fortsatt huvudspår, Pluslådan ger starkt mervärde och Makerlådan bör behandlas som frivillig fördjupning.


## 5A.4 – Illustrationsplan

Bokens illustrationsbehov har planerats med bildtyper, kapitelvis bildlista, komponentbildlista, prioriterad illustrationskö och standardiserade breadboardbilder.


## 5A.5 – Kodprogression

Bokens programmeringsprogression har planerats med kodnivå per kapitel, bibliotek, kodstil, mallar och kodkonceptmatris.


## 5A.6 – Pedagogisk rytm

Bokens tempo, variation, wow-faktor, byggtid och teori/praktik-balans har analyserats. 5A-produktionsdesignen är därmed komplett på första nivå.


## 5B.1 – Produktionsmatris uppgraderad

Produktionsmatrisen är nu en masterlista för E001–E120 med kapitel, spår, kodnivå, wow-faktor, komponenter, beroenden och statusfält för text, kod, test, illustration och layout.


## 5B.2 – Experimentmall

Standardmall, skrivregler och checklistor för produktion av enskilda experiment har skapats.


## 5B.2.1 – Pedagogisk experimentcykel

Experimentmallen har kompletterats med Testa, Utforska, Experimentera, Utmaning och Jag undrar för att stärka barnets utforskande arbetssätt.


## 5B.3 – Produktionsordning

Skrivordning och produktionsblock har fastställts. Boken produceras i fyra block: grund, sensorer, smarta prylar och Maker/slutprojekt.


## 5B.4 – Kvalitetssäkring

Kvalitetssäkringsflöde, teknisk granskning, pedagogisk granskning, testplan och säkerhetsgranskning har skapats.


## 5B.5 – Produktionspipeline

Produktionspipelinen är fastställd. Projektet är redo att gå från planering till produktion av experiment.


## 6.1.1 – Kapitel 1 pilotrevision

E001 och E002 har fördjupats som guldstandard för experimentens ton, struktur, kod, felsökning och pedagogiska experimentcykel.


## 5B.6 Del A – Kreativ designbibel

Bokens berättarröst, läsupplevelse och emotionella progression har definierats. Detta ska styra revidering av E001–E002 och all fortsatt experimentproduktion.


## 5B.6 Del B – Wow, storytelling och visuellt berättande

Wow-kurva, storytelling-regler och visuellt berättande har definierats för att stärka bokens läsupplevelse och barnets motivation.


## 5B.6 Del D
Designbibeln är komplett och styr fortsatt experimentproduktion.


## 6.1.1 – E001 reviderad enligt 5B.6

E001 har skrivits om för att fungera som första guldstandard-kandidat enligt den kreativa designbibeln 5B.6.


## 6.1.1 – E001 granskad och finjusterad

E001 har granskats mot 5B.6.11 och finjusterats för byggtrygghet, breadboardtydlighet, första wow och övergång till E002.


## Stabilisering v45 – 5B.6 komplett

v45 reparerar versionsmissen där 5B.6 Del C saknades i v44. Del C har återinförts och fördjupats, Del D har stärkts och E001 från v44 behålls som guldstandard-kandidat.


## v46 – E001 teknisk och 5B.6-språklig finjustering

E001 har justerats efter stabiliserad 5B.6: GPIO 23 används, kopplingsvägen är konsekventgjord, språket är putsat enligt Del C och en separat illustrationsbrief har skapats.


## v47 – E002 reviderad enligt 5B.6

E002 har skrivits om enligt stabiliserad 5B.6 och E001/v46-nivån. Experimentet använder GPIO 23 och samma kopplingsväg som E001, med fokus på att samma hårdvara kan få nytt beteende genom ändrad kod.


## v48 – Bild- och kopplingspipeline E001–E002

Projektet har fått en strukturerad pipeline för tekniskt korrekta bilder. Kopplingsbilder ska baseras på `circuit.yaml`, Wokwi-diagram eller annan strukturerad källa, medan AI-prompter endast används för dekorativa eller icke-tekniskt styrande bilder.


## v49 – Första kompletta SVG-bildpaket E001–E002

Första kompletta SVG-bildpaketet för E001 och E002 har skapats. Bilderna är kontrollerbara tekniska/pedagogiska SVG-underlag och ska användas i nästa PDF-preview.


## v50 – Justerat SVG-bildpaket

Kopplingsöversikterna för E001/E002 har förenklats: ingen breadboard ritas, LED-lampans långa/korta ben visas och GPIO 23/GND kopplas till rätt ben/väg. Förvirrande bilder har arkiverats.


## v51 – Förenklad märkning i kopplingsöversikter

Kopplingsöversikterna för E001/E002 använder nu en renare märkning där endast 'Långt ben' och 'Kort ben' indikeras i själva bilden.


## v52 – PDF-generering och läsflöde stabiliserat

E001/E002 markdown har nu explicita SVG-bildreferenser och läsflödet har justerats genom att generella blockquote-insikter görs till `Insikt:` i stället för stora 'Tänk på'-rutor.
