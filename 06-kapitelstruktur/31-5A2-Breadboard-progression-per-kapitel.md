# 5A.2 – Breadboard-progression per kapitel

## Kapitel 1 – Kom igång

```text
ESP32 på breadboard
  ↓
LED + motstånd
  ↓
LED blinkar
  ↓
två LED
  ↓
tre LED / enkel signal
```

**Återanvändning:** LED-kopplingen ska bli bokens första standardkoppling.

**Viktig princip:** Första fungerande resultat ska komma snabbt.

---

## Kapitel 2 – LED, PWM och färg

```text
LED-standardkoppling
  ↓
flera LED
  ↓
RGB-LED
  ↓
PWM på LED
  ↓
PWM på RGB
  ↓
ljusshow
```

**Återanvändning:** behåll grundläggande LED och lägg till RGB utan att byta hela layouten.

**Risk:** för många LED kan göra breadboarden rörig; håll layouten konsekvent.

---

## Kapitel 3 – Knappar

```text
LED + motstånd
  ↓
lägg till knapp
  ↓
knapp styr LED
  ↓
knapp växlar tillstånd
  ↓
två knappar
  ↓
kodlås
```

**Återanvändning:** knappen bör bli en standardkomponent som återkommer i nästan alla senare kapitel.

**Layout:** knappar på vänster sida, LED/output på höger sida.

---

## Kapitel 4 – Ljud och spel

```text
knapp + LED
  ↓
lägg till buzzer
  ↓
knapp + buzzer
  ↓
LED + buzzer + spelstatus
  ↓
flera knappar
  ↓
reaktionsspel / Simon Says
```

**Återanvändning:** output-sidan blir LED + buzzer. Den används senare i larm, spel och smarta projekt.

---

## Kapitel 5 – Ljus och avstånd

```text
LED/RGB/buzzer-output
  ↓
lägg till LDR
  ↓
LDR styr LED
  ↓
LDR + LED-barometer
  ↓
byt sensor till HC-SR04
  ↓
HC-SR04 + buzzer
  ↓
HC-SR04 + RGB-status
```

**Återanvändning:** byt input, behåll output. Detta är ett viktigt pedagogiskt mönster.

---

## Kapitel 6 – Larm, rörelse och närvaro

```text
RGB + buzzer-output
  ↓
reedkontakt + magnet
  ↓
skattlåde-larm
  ↓
byt till tilt-sensor
  ↓
byt till PIR
  ↓
spökhusprojekt
```

**Återanvändning:** output-sidan ska vara nästan identisk genom kapitlet.

**Viktig poäng:** olika sensorer kan trigga samma larmreaktion.

---

## Kapitel 7 – Temperatur, miljö och levande mätningar

```text
sensor + Serial Monitor
  ↓
DHT22
  ↓
DHT22 + OLED
  ↓
DHT22 + RGB-status
  ↓
jordfuktighet + RGB
  ↓
mikrofon + LED/RGB
  ↓
sensorlaboratorium
```

**Återanvändning:** statusfärg och OLED bör återkomma som generella sätt att visa mätvärden.

---

## Kapitel 8 – OLED och användargränssnitt

```text
OLED ensam
  ↓
OLED + sensor
  ↓
OLED + knapp
  ↓
OLED + meny
  ↓
OLED + flera värden
  ↓
OLED + spelresultat
```

**Återanvändning:** OLED blir från och med nu standard för status och mätvärden.

---

## Kapitel 9 – NeoPixel och LED-matris

```text
LED-matris separat
  ↓
matris-symbol
  ↓
matris-animation
  ↓
NeoPixel separat
  ↓
NeoPixel-regnbåge
  ↓
NeoPixel + knapp
  ↓
reaktionsring
```

**Återanvändning:** gör LED-matris och NeoPixel som två separata block för att undvika för komplex koppling.

---

## Kapitel 10 – Servo och smarta prylar

```text
servo ensam
  ↓
servo + potentiometer
  ↓
servo + avståndssensor
  ↓
servo + kodlås
  ↓
servo + temperatur/PIR
  ↓
servo + OLED/RGB
  ↓
larmcentral
```

**Återanvändning:** servon blir en fysisk output, på samma sätt som RGB är visuell output.

---

## Kapitel 11 – Motorer och robotik

```text
motor + motordrivare
  ↓
motor + knapp
  ↓
motor + potentiometer/PWM
  ↓
motor + sensor
  ↓
två motorer
  ↓
robot + avståndssensor
```

**Återanvändning:** motorblocket bör ligga separat från övriga kapitel på grund av ström och säkerhet.

---

## Kapitel 12 – RFID, IR och identifiering

```text
RFID ensam
  ↓
RFID + RGB/buzzer
  ↓
RFID + servo
  ↓
IR ensam
  ↓
IR + RGB
  ↓
IR + servo
```

**Återanvändning:** RGB/buzzer/servo är samma outputs som tidigare, men triggas av nya typer av input.

---

## Kapitel 13 – Tid, loggning och WiFi

```text
RTC + OLED
  ↓
RTC + påminnare
  ↓
SD-kort separat
  ↓
sensor + SD-logg
  ↓
sensor + RTC + SD + OLED
  ↓
WiFi + LED/webbstatus
```

**Återanvändning:** OLED och DHT22 återkommer. SD och WiFi bör inte blandas för tidigt.

---

## Kapitel 14 – Familjens Makerprojekt

```text
välj input
  ↓
välj output
  ↓
bygg minsta version
  ↓
lägg till status
  ↓
lägg till display eller rörelse
  ↓
testa
  ↓
förbättra
```

**Återanvändning:** kapitlet ska ge mallar snarare än fasta kopplingar.
