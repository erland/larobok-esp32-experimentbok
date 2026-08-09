# 6.1.1 – Revision av E002 enligt 5B.6

## Sammanfattning

E002 har skrivits om enligt stabiliserad 5B.6 och anpassats till E001:s v46-nivå.

E002 fungerar nu som andra guldstandard-kandidat i kapitel 1, men fysisk testning och extern/pedagogisk granskning kvarstår.

---

# Viktiga ändringar

## 1. Starkare berättande öppning

Experimentet börjar nu med övergången från E001:

> från vanligt blink till egen rytm.

## 2. Samma tekniska grund som E001

E002 använder samma kopplingsväg och samma GPIO-val:

> GPIO 23 → LED-lampans långa ben → LED-lampans korta ben → motstånd → GND

## 3. Nytt huvudbudskap

E002 betonar att samma hårdvara kan få nytt beteende genom ändrad kod.

## 4. Tydligare första wow

Första wow är formulerat som:

> Samma lampa. Samma koppling. Nytt beteende.

## 5. Förbättrad felsökning

Felsökningen har skrivits som “Vanliga ledtrådar” snarare än fel.

## 6. Separat illustrationsbrief

En ny fil har lagts till:

- `E002-Illustrationsbrief.md`

## 7. Starkare bro till E003

Avslutningen pekar mot flera LED-lampor och ljus som får riktning.

---

# Status

E002 är nu:

> Guldstandard-kandidat

Kvarstår innan färdigstatus:

- fysisk breadboardtest,
- kodkompilering i vald miljö,
- kontroll mot vald ESP32 DevKit-modell,
- färdiga illustrationer,
- pedagogisk testläsning.
