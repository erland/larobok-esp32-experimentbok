# 6.1.1 – v46 E001 teknisk och 5B.6-språklig finjustering

## Sammanfattning

E001 har finjusterats efter stabiliseringen av 5B.6 i v45.

Revisionen är medvetet begränsad. E001 skrivs inte om från grunden, eftersom den redan fungerar som guldstandard-kandidat. Syftet är i stället att göra den tekniskt tryggare och mer konsekvent med den fördjupade Del C.

---

# Genomförda ändringar

## 1. GPIO-byte

Standardpinnen har ändrats från GPIO 5 till GPIO 23.

Motiv:

- GPIO 5 kan vara olämplig som första standardpinne på vissa ESP32-kort eftersom den kan ha boot-/strapping-relaterade egenskaper.
- GPIO 23 är oftare ett tryggare val för ett första LED-experiment på vanliga ESP32 DevKit-kort.
- Första experimentet bör minimera onödiga tekniska specialfall.

## 2. Konsekvent kopplingsväg

Kopplingsvägen har förtydligats och standardiserats:

> GPIO 23 → LED-lampans långa ben → LED-lampans korta ben → motstånd → GND

Samma väg ska användas i text och illustrationer.

## 3. Språklig puts enligt 5B.6 Del C

Texten har justerats för att:

- minska onödiga förekomster av “bara”,
- undvika formuleringar som kan kännas som misslyckande,
- stärka felsökning som ledtrådar och mysterier,
- behålla varm ton utan att bli tramsig.

## 4. Tydligare huvudflöde

Faktarutan om GPIO har bytt rubrik till:

> Om du vill förstå mer: Vad är en GPIO?

Det gör att yngre läsare kan följa huvudspåret utan att känna att de måste förstå allt direkt.

## 5. Separat illustrationsbrief

En ny fil har lagts till:

- `E001-Illustrationsbrief.md`

Den gör bildbehoven mer produktionsklara.

---

# Status

E001 är fortfarande:

> Guldstandard-kandidat

Kvarstår innan färdigstatus:

- fysisk breadboardtest,
- kodkompilering i vald miljö,
- kontroll mot vald ESP32 DevKit-modell,
- färdiga illustrationer,
- pedagogisk testläsning.
