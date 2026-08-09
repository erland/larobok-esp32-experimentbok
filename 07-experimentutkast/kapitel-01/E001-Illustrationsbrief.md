# E001 – Illustrationsbrief

## Syfte

Denna brief gör E001:s visuella berättande mer produktionsklart. Den ska användas när illustrationer, breadboardbilder eller layoutskisser tas fram.

E001 ska visuellt kännas tryggt, stegvis och tydligt. Barnet ska kunna jämföra sin egen koppling med bilden utan att behöva tolka för mycket text.

---

# Vald kopplingsväg

E001 använder följande konsekventa kopplingsväg:

> GPIO 23 → LED-lampans långa ben → LED-lampans korta ben → motstånd → GND

Denna ordning ska användas i text, bild och bildtext.

---

# Bildlista

| Bild-ID | Placering | Syfte | Måste visa |
|---|---|---|---|
| E001-A | Efter “Du behöver” | Visa dagens delar | ESP32 DevKit, breadboard, LED, 220–330 Ω motstånd, kopplingskablar, USB-kabel |
| E001-B | Efter “Innan du börjar” | Visa LED-riktning | långt ben, kort ben, gärna plus/minus eller signal/GND-markering |
| E001-C | Efter kopplingsstegen | Visa komplett koppling | GPIO 23 till LED:s långa ben, LED:s korta ben via motstånd till GND |
| E001-D | I felsökningsdelen | Visa vanliga ledtrådar | LED baklänges, LED-ben i samma rad, kabel till annan GPIO |
| E001-E | Vid “Nu händer det” | Visa resultatet | LED tänd/släckt, gärna två små rutor “på” och “av” |

---

# Bildstil

Illustrationerna ska vara:

- rena och luftiga,
- konsekventa i färger,
- tydligt numrerade,
- inte överlastade med text,
- anpassade för att kunna läsas av barn och vuxen tillsammans.

---

# Färgprinciper

Rekommenderade färger i illustrationerna:

| Funktion | Rekommenderad färg |
|---|---|
| Signal från GPIO 23 | gul eller orange |
| GND | svart eller blå |
| Ny del i aktuellt steg | markerad med ljus ram |
| Risk/vanlig ledtråd | mild varningsmarkering, inte aggressivt röd |

---

# Viktiga zoom-detaljer

## LED-riktning

Visa tydligt:

- långt ben,
- kort ben,
- platt sida om sådan syns,
- vilken sida som går mot GND.

## Breadboardrad

Visa att LED-benen inte ska sitta i samma rad.

## GPIO 23

Visa att märkningen på olika ESP32-kort kan se lite olika ut, men att läsaren ska följa pinnen som motsvarar GPIO 23.

---

# Bildtexter

Bildtexter ska vara aktiva och hjälpa barnet se vad som är viktigt.

Exempel:

> Följ signalen: GPIO 23 → LED → motstånd → GND.

> Här är ledtråden: om båda LED-benen sitter i samma rad går signalen inte genom lampan på rätt sätt.

---

# Status

Illustrationsbriefen är klar för produktionsplanering. Färdiga illustrationer återstår.
