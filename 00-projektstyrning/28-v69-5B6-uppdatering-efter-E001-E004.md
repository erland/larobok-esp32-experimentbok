# v69 – 5B6-uppdatering efter E001–E004

Denna version fångar upp lärdomarna från arbetet med E001–E004 och gör dem till styrregler för fortsatt produktion.

## Syfte

E001–E004 har stabiliserat flera praktiska principer som bör gälla för E005 och framåt:

- hur **Stanna och gissa** ska placeras,
- hur **Nu händer det**, **Testa** och **Utforska** bör särskiljas,
- hur sekvensbilder och loop-pilar bör utformas,
- hur komponentbiblioteket från v68 ska användas,
- hur LED-kopplingar ska beskrivas utan att skapa teknisk tvetydighet,
- hur wow-känslan kan bevaras utan att samma fras återkommer i varje experiment.

## Uppdaterade filer

- `113-5B6-4-Wowkurva-och-motivation.md`
- `115-5B6-6-Visuellt-berattande.md`
- `118-5B6-8-Tempo-och-variation.md`
- `120-5B6-10-Guldstandard-experiment.md`
- `122-5B6-11-Kontrollista-berattarupplevelse.md`

## Viktiga beslut

### Stanna och gissa

- Före kod när barnet ännu inte kan läsa relevant kodmönster.
- Efter kod men före uppladdning när barnet kan förutsäga utifrån kod.

### Sekvensbilder

- Visa tillstånd över tid.
- Loop-pil ska gå från högersidan av sista rutan till vänstersidan av första rutan.
- Undvik onödig text inne i bilden.

### Komponentbibliotek

Nya illustrationer bör i normalfallet utgå från:

```text
08-illustrationer-och-kopplingar/component-library/
```

### LED-kopplingar

Standardprincip:

```text
GPIO → LED-lampans långa ben → LED-lampans korta ben → motstånd → GND
```

## Avgränsning

v69 ändrar inte manus eller bilder i E001–E004. Det är en regel- och styrdokumentsuppdatering.
