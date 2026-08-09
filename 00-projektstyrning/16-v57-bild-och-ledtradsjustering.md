# v57 – Bild- och ledtrådsjustering

## Syfte

v57 gör två layout- och bildförbättringar efter granskning av PDF-preview för E001–E004.

## Genomfört

- Bilder i sektionen **Vanliga ledtrådar** har tagits bort ur manus för E002, E003 och E004.
- Ledtrådssektionerna finns kvar som text/tabeller, eftersom bilderna tog sidutrymme men inte tillförde tillräckligt mycket.
- `E003-B-kopplingsoversikt.svg` har ritats om som två separata horisontella kopplingsrader.
- `E004-B-kopplingsoversikt.svg` har ritats om som tre separata horisontella kopplingsrader.
- De nya kopplingsbilderna undviker korsande linjer och linjer som går ovanpå varandra.
- Bildprompter och bildbriefs för E003/E004 har uppdaterats med den nya principen.

## Ny bildprincip från v57

För kopplingsöversikter med flera LED används en **parallell radstruktur**:

- ESP32 till vänster.
- En rad per LED/färg.
- Signal går till LED-lampans långa ben.
- LED-lampans korta ben går vidare till motstånd.
- Motståndet går till gemensam GND-buss.
- Inga korsande linjer.

## Status

E003 och E004 är fortfarande markerade som utkast/pågår. PDF-layoutgranskning, teknisk granskning och fysisk test återstår.
