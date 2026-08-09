# v62 – struktur och läsflöde

Denna version stabiliserar E001–E004 som mall för kommande experiment.

## Genomförda ändringar

1. **Du behöver**
   - Dagens delar-bilden ligger nu först.
   - Komponenttabellen med antal kommer efter bilden.
   - Fristående rubriken **Bild** är borttagen i denna sektion.

2. **Koppla så här**
   - Kopplingsöversikten ligger tidigt i sektionen.
   - Instruktionerna kommer efter att läsaren först sett helheten.
   - Fristående rubriken **Bild** är borttagen även här.

3. **Stanna och gissa**
   - Flyttad närmare kodmomentet där den gör mest nytta.
   - Gäller framför allt E003 och E004.

4. **Vad händer egentligen**
   - Synkad mot en mer observationsnära och konkret stil.
   - Förklaringen börjar i det barnet just såg och kopplar sedan tillbaka till kod/koppling.

5. **Insiktsrutor**
   - Ordet **Insikt:** är borttaget.
   - Rutan används fortfarande för att markera viktiga poänger.

## Tekniskt oförändrat

- E001/E002 använder GPIO 23.
- E003 använder GPIO 23 och GPIO 22.
- E004 använder GPIO 23, GPIO 22 och GPIO 21.
- Kopplingsprincipen är fortsatt: GPIO → långt ben → kort ben → motstånd → GND.
