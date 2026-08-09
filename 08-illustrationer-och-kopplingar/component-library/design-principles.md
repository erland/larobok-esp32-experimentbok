# Bildprinciper

## Grundstil

- Bakgrund: `#fffdf7`
- Pedagogisk blå kant: `#1f6688`
- Pilar och neutrala linjer: `#777`
- Neutral text: `#222`
- Sekundär text: `#444`
- Typsnitt: `Arial, Helvetica, sans-serif`
- Former ska vara tydliga, mjuka och barnvänliga.
- Undvik onödig text inne i bilder när markdown-texten redan förklarar bilden.

## Text i bilder

Använd text i bilden när texten hjälper direkt i ögonblicket:

- `PÅ`
- `AV`
- `LED 1`
- `LED 2`
- `GPIO 23`
- `GND`
- `börja om`
- tider som `500 ms`

Undvik:

- långa instruktioner,
- upprepning av bildtext,
- antal komponenter i Dagens delar-bilder,
- fraser som “Säg rytmen” när bilden redan visar rytmen.

## Dagens delar

- En komponentkategori visas med en enkel, tydlig komponentbild.
- Kategoritexten placeras under rutan, inte inne i rutan.
- Antal komponenter visas i materiallistan i markdown, inte i bilden.

## Kopplingsöversikter

Standardprincip:

```text
GPIO → LED-lampans långa ben → LED-lampans korta ben → motstånd → GND
```

För flera LED-lampor används parallella rader.

## Sekvensbilder

- Visa tillstånd över tid från vänster till höger.
- Använd en ruta per steg.
- Använd pilar mellan stegen.
- Loop-pilen ska börja på högersidan av sista rutan och gå in mot vänstersidan av första rutan.
- Visa hellre lampans tillstånd visuellt än med mycket text.

## Utforska-bilder

- Använd jämförelsepaneler när flera varianter jämförs.
- Håll etiketter korta och läsbara i PDF.
- Visa samma typ av sekvens i flera rader när poängen är att jämföra beteenden.

## Kopplingsöversikter efter E005-B v77

För LED-baserade kopplingsöversikter ska E003-B och E005-B v77 användas som visuell referens.

Standardkedjan ska synas i bilden:

`GPIO → LED-lampans långa ben → LED-lampans korta ben → motstånd → GND`

Praktiska bildregler:

- Rita helst en ren horisontell rad per ljusväg.
- Låt GPIO-tråden ansluta till LED-lampans långa ben, inte till LED-huvudet.
- Låt kort ben fortsätta till motståndet.
- Låt motståndet fortsätta till GND.
- Där det går ska vänster och höger ledare vid LED-lampan ligga i samma höjd.
- Etiketter för GPIO, GND, LED-ben och motstånd ska ha luft runt sig och inte kännas klippta.
- Om en bild blir rörig ska den förenklas innan PDF-preview skapas.
