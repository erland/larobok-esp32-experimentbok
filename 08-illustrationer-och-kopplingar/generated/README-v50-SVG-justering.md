# v50 – Justering av SVG-bildpaket efter layoutgranskning

## Sammanfattning

v50 justerar SVG-bildpaketet efter granskning av PDF-previewen.

## Ändringar

### E001 – Kopplingsöversikt

- Breadboarden har tagits bort ur kopplingsöversikten.
- Bilden visar nu elektrisk kopplingsväg, inte fysisk breadboardplacering.
- LED-lampans långa och korta ben visas tydligare.
- Kopplingen från GPIO 23 går nu till LED-lampans långa ben, inte till LED-huvudet.
- GND-vägen går tillbaka till GND på ESP32.

### E001 – Vanliga ledtrådar

- `E001-D-vanliga-ledtradar.svg` har flyttats till `archive-v49`.
- Bilden bedömdes tillföra mer förvirring än nytta i nuvarande form.

### E002 – Samma koppling, ny kod

- `E002-A-samma-koppling-ny-kod.svg` har flyttats till `archive-v49`.
- Bilden bedömdes inte tillföra tillräcklig tydlighet.

### E002 – Snabb kopplingskontroll

- Har ersatts med samma typ av förenklad kopplingsöversikt som E001.
- Bilden visar nu tydligt att kretsen går tillbaka till GND på ESP32.

## Beslut

Kopplingsöversikter ska inte försöka rita breadboard om vi inte har en mer exakt breadboardgenerator. För E001/E002 används därför en förenklad, kontrollerbar elektrisk kopplingsöversikt.

## Nästa steg

Rendera ny PDF-preview där borttagna/flyttade bilder inte längre placeras in och där E001/E002 använder samma kopplingsöversikt.
