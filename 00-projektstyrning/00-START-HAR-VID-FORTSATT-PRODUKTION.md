# START HÄR vid fortsatt produktion

Den här filen ska läsas först när projektet öppnas i en ny chat eller när produktionen fortsätter efter ett uppehåll.

Syftet är att göra det tydligt vilka dokument som är styrande och i vilken ordning de bör användas.

---

# Snabbstart

När du ska fortsätta arbetet med boken:

1. Läs denna fil.
2. Läs senaste status och beslut i:

   ```text
   00-projektstyrning/02-Status-och-beslutslogg.md
   ```

3. Läs senaste styrnotiserna från de senaste versionerna, särskilt:

   ```text
   00-projektstyrning/38-v79-E006-Fyrtornet.md
   00-projektstyrning/37-v78-bildstandard-kopplingsoversikter.md
   00-projektstyrning/28-v69-5B6-uppdatering-efter-E001-E004.md
   00-projektstyrning/27-v68-komponentbibliotek.md
   ```

4. Använd E001–E004 som praktiska referensexperiment:

   ```text
   07-experimentutkast/kapitel-01/
   ```

5. Använd 5B6-reglerna som skriv- och kvalitetsstandard:

   ```text
   00-projektstyrning/5B-produktionsplan/
   ```

6. Använd komponentbiblioteket som bildstandard för nya illustrationer:

   ```text
   08-illustrationer-och-kopplingar/component-library/
   ```

---

# Vad är normerande?

Om olika filer verkar säga olika saker gäller denna ordning:

1. Senaste uttryckliga versionsbeslut i `02-Status-och-beslutslogg.md`.
2. Senaste versionsnotis i `00-projektstyrning/`, till exempel v68 eller v69.
3. 5B6-regler och kontrollistor.
4. Praktisk standard i E001–E004.
5. Äldre planerings- och utkastdokument.

Äldre dokument kan vara användbara som historik, men de ska inte väga tyngre än nyare beslut.

---

# Praktisk mall för nya experiment

När ett nytt experiment skapas, använd E001–E004 som referens och följ denna struktur om inget annat beslutats:

1. Titel
2. Uppdrag / berättande öppning
3. Dagens uppfinning
4. Du lär dig
5. Du behöver
6. Innan du börjar, om det behövs
7. Koppla så här
8. Koden
9. Stanna och gissa, placerad enligt principen nedan
10. Ladda upp koden
11. Nu händer det
12. Vad händer egentligen?
13. Testa
14. Utforska
15. Experimentera
16. Utmaning
17. Vanliga ledtrådar / felsökning
18. För den vuxne
19. Jag undrar...
20. Nästa experiment

Strukturen får anpassas, men avvikelser ska vara medvetna.

---

# Stanna och gissa

Placera **Stanna och gissa** så här:

- Före kodblocket när barnet ännu inte har sett ett relevant kodmönster och gissningen främst skapar nyfikenhet.
- Efter kodblocket men före uppladdning när barnet kan titta på koden och göra en enkel förutsägelse.

Gissningen ska alltid koppla direkt till något barnet snart kan observera.

---

# Bildprinciper

Nya bilder ska i normalfallet utgå från komponentbiblioteket:

```text
08-illustrationer-och-kopplingar/component-library/
```

Särskilt viktigt:

- återanvänd formspråk för LED-lampor, motstånd, pilar och sekvenskort,
- håll text i bilder kort,
- låt markdown-texten bära förklaringen,
- visa tillstånd över tid i sekvensbilder,
- låt loop-pilar gå från höger sida av sista steget till vänster sida av första steget.

---

# LED-standard

Standardformulering för enkel LED-koppling:

```text
GPIO → LED-lampans långa ben → LED-lampans korta ben → motstånd → GND
```

Undvik formuleringar som kan tolkas som att LED-lampans korta ben ska direkt till GND utan motstånd.

---

# När en ny version skapas

Vid varje ny version bör följande uppdateras:

1. Berörda manus- eller projektfiler.
2. `00-projektstyrning/02-Status-och-beslutslogg.md`.
3. En ny kort versionsnotis om ändringen är principiell.
4. README om projektets senaste status ändras.
5. Ny zip-fil med versionsnummer.
6. PDF-preview endast om manus, layout eller bilder som ingår i PDF-previewn ändras.

---

# Viktig avgränsning

Gissa inte fritt när projektet fortsätter.

Börja med styrdokumenten, använd E001–E004 som praktiska mallar och säg till om något är oklart eller om styrdokumenten verkar motsäga varandra.

## Bildstandard att kontrollera före nya LED-experiment

Vid nya LED-experiment, särskilt E006 och framåt, ska kopplingsöversikten kontrolleras mot den standard som fastställdes i v78:

- E003-B används som grundreferens.
- E005-B från v77 eller senare används som referens för ren två-raderslayout.
- GPIO-tråden ska visuellt ansluta till LED-lampans långa ben.
- Kort ben ska visuellt fortsätta till motstånd.
- Motstånd ska visuellt fortsätta till GND.
- Vänster och höger ledare vid LED-lampan bör ligga i samma höjd när layouten tillåter det.
- Om bilden avviker från detta ska den justeras innan PDF-preview byggs.

## Aktiv kapitelordning efter v81

Kapitel 1 ska efter v81 behandlas i denna ordning:

1. E001 – Första blinket
2. E002 – LED med egen rytm, inklusive fyrtornsutmaning
3. E003 – Två LED turas om
4. E005 – Polisljus
5. E004 – Mini-trafikljus

E006 Fyrtornet är inte längre ett aktivt separat experiment. Materialet är arkiverat och idén är infogad i E002.

## Progressionskontroll före nya experiment

Från och med v83 ska nya experiment kontrolleras mot principen:

> Ett huvudexperiment ska helst kännas som ett nytt steg. En variant ska helst kännas som en utmaning.

Läs därför även:

```text
00-projektstyrning/42-v83-principer-for-experimentprogression.md
```

innan nästa experiment produceras.


## Senaste producerade experiment i Kapitel 2

- E011 – RGB: tre färger i en LED
- E012 – Färgblandaren
- E013 – Regnbågslampan

Efter v104 är det aktiva huvudflödet i Kapitel 2 producerat och lätt putsat som utkast. Nästa rimliga steg är samlad pedagogisk granskning och PDF-layoutgranskning.


## Senaste versionsnotis

- `00-projektstyrning/57-v98-E013-latt-puts.md`


## Senaste producerade experiment i Kapitel 2

- E014 – Humörlampan

Senaste versionsnotis:

- `00-projektstyrning/58-v99-E014-Humorlampan.md`


## Senaste versionsnotis

- `00-projektstyrning/59-v100-E014-latt-puts.md`


## Senaste producerade experiment i Kapitel 2

- E015 – Dimbar LED

Senaste versionsnotis:

- `00-projektstyrning/60-v101-E015-Dimbar-LED.md`


## Senaste versionsnotis

- `00-projektstyrning/61-v102-E015-latt-puts.md`


## Senaste producerade experiment i Kapitel 2

- E016 – Andande ljus

Senaste versionsnotis:

- `00-projektstyrning/62-v103-E016-Andande-ljus.md`


## Senaste versionsnotis

- `00-projektstyrning/63-v104-E016-latt-puts.md`


## Senaste versionsnotis

- `00-projektstyrning/64-v105-github-actions-publicering.md`


## Senaste versionsnotis

- `00-projektstyrning/65-v106-github-actions-weasyprint-fix.md`


## Senaste versionsnotis

- `00-projektstyrning/66-v107-github-actions-pydyf-fix.md`
