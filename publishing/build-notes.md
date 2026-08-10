# Build notes

GitHub Actions-konceptet infördes i v105 med samma övergripande upplägg som referenskitet:

- snabb validering vid PR/push till `main`,
- manuell Build Preview,
- preview bygger både EPUB och PDF,
- preview publicerar ett gemensamt artifact: `esp32-experimentbok-preview`,
- release på `v*`-taggar publicerar EPUB och PDF som separata release assets,
- Pandoc är låst till 3.1.11.1,
- validerings- och bygglogik ligger i `scripts/`.

## Projektspecifik anpassning

Det här ESP32-projektet är inte ett romanprojekt. Därför är byggscriptet anpassat till projektets faktiska kapitelstruktur:

- Kapitel 1: E001, E002, E003, E005, E004
- Kapitel 2: E007, E008, E011, E012, E013, E014, E015, E016

PDF byggs via Pandoc HTML + WeasyPrint eftersom boken innehåller många SVG-bilder, tabeller, kodblock och instruktionslayout. EPUB byggs via Pandoc EPUB3.

E009 och E010 är parkerade och ingår inte i aktiv bokexport.
