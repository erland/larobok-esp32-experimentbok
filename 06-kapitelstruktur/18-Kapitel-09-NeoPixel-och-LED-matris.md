# Kapitel 9 – NeoPixel och LED-matris

## Pedagogisk roll

Kapitel 9 handlar om att skapa mer uttrycksfulla ljusprojekt. Barnet har redan använt vanliga LED och RGB-LED, men nu introduceras programmerbara ljus där varje pixel kan styras separat. Det ger hög wow-faktor och öppnar för animationer, spel och visuella timers.

Kapitlet bör vara färgstarkt, lekfullt och visuellt belönande.

## Förkunskaper

Barnet bör ha mött:

- RGB-färger,
- `for`-loopar,
- arrayer,
- enklare bibliotek,
- knappar,
- timer-/reaktionsspel.

## Huvudexperiment

| Ordning | ID | Namn | Roll i kapitlet |
|---:|---|---|---|
| 1 | E081 | Pixel-smileyn | Introducerar LED-matris |
| 2 | E082 | Matris-animationen | Bildrutor och enkla animationer |
| 3 | E084 | NeoPixel första regnbågen | Introducerar NeoPixel |
| 4 | E085 | NeoPixel-timer | Gör ljusringen användbar |
| 5 | E086 | Reaktionsring | Spel med hög wow-faktor |
| 6 | E083 | Mini-Snake-idé | Bonus/fördjupning för spelintresserade |

## Rekommenderad klassning

| ID | Klassning | Motivering |
|---|---|---|
| E081 | Huvudspår | Första LED-matrisen |
| E082 | Huvudspår | Introducerar animation |
| E084 | Huvudspår | Första NeoPixel-projektet |
| E085 | Huvudspår | Praktisk tillämpning |
| E086 | Kapitelprojekt | Hög wow-faktor och spelkoppling |
| E083 | Bonus | Roligt men kan bli kodmässigt svårt |

## Breadboard-progression

1. Koppla LED-matris ensam.
2. Testa symbol och enkel animation.
3. Koppla NeoPixel-ring separat.
4. Återanvänd knapp från tidigare spel.
5. Kombinera knapp, buzzer och NeoPixel i reaktionsring.

Kapitlet bör inte kräva att LED-matris och NeoPixel sitter inkopplade samtidigt i huvudspåret, för att undvika för mycket kabeltrassel.

## Kodprogression

| Moment | Kodidé |
|---|---|
| E081 | styra en matris via bibliotek |
| E082 | arrayer av bildrutor |
| E084 | styra en lista av RGB-pixlar |
| E085 | loop som fyller/tömmer ring |
| E086 | spelstatus + NeoPixel-animation |
| E083 | enkel spelposition på rutnät |

## Komponentprogression

Introduceras:

- D02 MAX7219 LED-matris
- L03 NeoPixel-ring

Återanvänds:

- K01 knapp
- A01 buzzer
- färgbegrepp från RGB-LED
- `for`-loopar och arrayer

## Illustrationer som behövs

| Figur | Typ | Beskrivning |
|---|---|---|
| 9-1 | Modulbild | MAX7219 LED-matris |
| 9-2 | Breadboard | LED-matris till ESP32 |
| 9-3 | Pixelkarta | 8x8-koordinater |
| 9-4 | Bildruta | smiley som binärt/visuellt mönster |
| 9-5 | Modulbild | NeoPixel-ring |
| 9-6 | Breadboard | NeoPixel med ESP32 |
| 9-7 | Animation | regnbågsrörelse |
| 9-8 | Spelflöde | reaktionsring |

## Vanliga fallgropar

- LED-matrisen är roterad fel.
- NeoPixel kräver rätt datapin och bibliotek.
- Färger visas i annan ordning än väntat.
- För många pixlar med hög ljusstyrka kan dra mer ström.
- Barnet vill direkt bygga avancerade spel; håll första stegen små.

## Pedagogisk rytm

Kapitlet ska kännas som en belöning efter sensorkapitlen. Det bör ha:

- snabb visuell framgång,
- korta experiment,
- mycket testande,
- frivilligt svårare spelprojekt.

## Kapitelprojekt

**Reaktionsringen**

NeoPixel-ringen visar en ljussignal. Barnet ska trycka i rätt ögonblick. Projektet kombinerar:

- NeoPixel,
- knapp,
- slump/timing,
- ljudfeedback,
- enkel poäng eller resultat.

## Produktionschecklista

- [ ] Lägg in ström-/ljusstyrkevarning för NeoPixel.
- [ ] Visa pixelriktning tydligt.
- [ ] Håll matrisgrafik enkel.
- [ ] Markera Mini-Snake som bonus.
- [ ] Undvik att kräva både matris och NeoPixel samtidigt i huvudspåret.
- [ ] Avsluta med ett tydligt spelprojekt.
