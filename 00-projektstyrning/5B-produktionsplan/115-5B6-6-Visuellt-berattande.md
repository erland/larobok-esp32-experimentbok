# 5B.6.6 – Visuellt berättande

## Syfte

Detta dokument definierar hur bilder, diagram, breadboardillustrationer och visuella ledtrådar ska stödja läsupplevelsen.

I en barnbok om elektronik är bilder inte dekoration. Bilder är instruktioner, trygghet och berättelse.

---

# Visuella principer

## 0. Använd komponentbiblioteket där det är relevant

Nya illustrationer bör i normalfallet utgå från komponentbiblioteket i:

```text
08-illustrationer-och-kopplingar/component-library/
```

Syftet är att LED-lampor, motstånd, pilar, sekvenskort och kopplingsbilder får ett konsekvent formspråk.

Biblioteket är i nuläget ett manuellt designbibliotek, inte en automatisk generator. Det ska användas som ritunderlag och standard, särskilt för nya experiment från E005 och framåt.

## 1. Bild före lång förklaring

Om något är lättare att se än att läsa ska det visas.

Exempel:

- LED-polaritet,
- breadboardrader,
- knappens placering,
- RGB-LED-ben,
- servo-kabelfärger,
- sensor riktning,
- motor får inte kopplas direkt till GPIO.

## 2. Visa förändring

När en komponent läggs till ska bilden visa vad som är nytt.

Använd gärna bildtext:

> Nytt i det här experimentet: knappen.

## 3. Zooma där barn gör fel

Detaljbilder behövs särskilt för:

- LED åt rätt håll,
- knapp över mittspåret,
- GND,
- 3,3V,
- SDA/SCL,
- servo-kablar,
- motordrivare.

## 4. Visa förväntat resultat

En bild kan visa vad barnet ska se:

- blinkmönster,
- skärmtext,
- NeoPixel-färg,
- servo-vinkel,
- sensorläge.

---

# Bildtyper i en upplevelse

| Bildtyp | Funktion |
|---|---|
| Startbild | vad vi bygger idag |
| Komponentbild | vad delen är |
| Kopplingsbild | hur den kopplas |
| Zoom-bild | kritisk detalj |
| Resultatbild | vad som händer |
| Systembild | hur input blir output |
| Felsökningsbild | vad som kan vara fel |
| Projektbild | den färdiga uppfinningen |

---

# LEGO-principen

Kopplingsbilder ska efterlikna tydligheten i bygginstruktioner:

- ett steg i taget,
- ny del tydligt markerad,
- inga onödiga detaljer,
- konsekvent vinkel,
- konsekventa färger,
- samma layout återkommer.

---

# Text och bild ska samarbeta

Dåligt:

> Koppla LED enligt bilden.

Bättre:

> Sätt LED-lampans långa ben på raden som går till motståndet. Titta på bilden: det nya i det här steget är markerat.

---

# Visuellt berättande i E001

E001 bör helst ha:

1. Bild på ESP32 + breadboard + LED.
2. Bild på LED:s långa/korta ben.
3. Breadboardbild med motstånd och LED.
4. Zoom på GND och GPIO.
5. Liten resultatbild: LED blinkar.

Det gör att första experimentet känns tryggt.

---

# Visuellt berättande i kapitelprojekt

Kapitelprojekt bör ha:

- en inspirationsbild,
- systembild,
- stegvis kopplingsbild,
- färdig projektbild,
- felsökningsbild.

---

# Bildtexter

Bildtexter ska vara aktiva.

Bra:

> Här är det nya: knappen kopplar pinnen till GND när du trycker.

Mindre bra:

> Figur 3.2 Knappkoppling.

---

# Säkerhetsbilder

Säkerhetsbilder behövs när felet kan skada komponenten eller skapa stor frustration.

Alltid för:

- motor direkt till GPIO,
- fel spänning,
- servo-ström,
- HC-SR04 Echo,
- MicroSD-kompatibilitet,
- vattennära experiment.

---

# Beslut

När experiment produceras ska illustrationer planeras som en del av berättelsen, inte som något som läggs till i efterhand.

---

# Sekvensbilder och loopar

Sekvensbilder ska visa tillstånd över tid, inte bara vara dekorativa tidslinjer.

Bra sekvensbilder visar:

- vad som är på,
- vad som är av,
- i vilken ordning det händer,
- ungefär hur länge steget varar när tiden är viktig,
- hur sekvensen börjar om.

## Loopregel

I sekvensbilder ska loop-pilen börja vid högersidan av sista steget och gå tillbaka mot vänstersidan av första steget.

Det gör att barnet ser att `loop()` inte är ett avslut, utan en återgång.

## Text i sekvensbilder

Använd korta etiketter som:

- `PÅ`
- `AV`
- `LED 1`
- `LED 2`
- `börja om`
- `500 ms`

Undvik längre fraser som redan förklaras i markdown, till exempel:

- “Säg rytmen”
- längre instruktioner
- resonemang som hör hemma i brödtexten

Bilden ska visa det som är lättare att se än att läsa. Texten i experimentet ska bära förklaringen.

---

# Standard för enkel LED-koppling

När en enkel LED-koppling beskrivs ska standardprincipen vara:

```text
GPIO → LED-lampans långa ben → LED-lampans korta ben → motstånd → GND
```

Undvik formuleringar som kan tolkas som att LED-lampans korta ben ska direkt till GND utan motstånd.

Bra:

> LED-lampans korta ben går mot motståndet och vidare till GND.

Mindre bra:

> LED-lampans korta ben går till GND.

Den kortare formuleringen kan bara användas när bilden eller sammanhanget redan tydligt visar motståndet.
