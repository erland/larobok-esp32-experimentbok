# E002 – Bildprompter

## Viktig princip

Dessa prompter får användas för dekorativa eller pedagogiska bilder, men **inte som sanningskälla för kopplingsbilden**.

Tekniska kopplingsbilder ska baseras på:

- `../circuits/E002-circuit.yaml`
- `../wokwi/E002-diagram.json`
- fysisk breadboardtest

---

# Stilprompt

Varm, tydlig svensk barnfaktabok för 7–12 år, ren vit bakgrund, mjuka färger, känsla av ljusrytm och upptäckt, inte för barnslig, inga felaktiga kopplingar, tekniskt respektfull.

---

# E002-A – Samma koppling, ny kod

Prompt:

> En pedagogisk barnboksillustration som visar idén “samma lampa, ny rytm”. En LED lyser i två små blink och en paus, visualiserat med diskreta ljusmarkeringar eller små tidsrutor. Tekniken ska kännas tydlig och varm, men kopplingsdetaljerna ska inte vara exakta.

Användning:

- Inledande idébild.
- Ska kompletteras av teknisk kopplingsbild från strukturerad källa.

---

# E002-C/E002-D – Rytmbilder

Rytmbilder bör inte AI-genereras. De ska skapas som enkla SVG-diagram från kodens `delay()`-värden.

Se:

- `../generated/E002/E002-C-rhythm-timeline.svg`

---

# Bilder som inte bör AI-genereras fritt

- E002-B kopplingskontroll
- E002-E felsökningsbild

Dessa ska baseras på strukturerad SVG/Wokwi/Fritzing eller manuell teknisk illustration.

# v81 – E002-E Fyrtornssekvens

E002-E ska inte AI-genereras fritt. Den ska skapas som enkel SVG från kodens `delay()`-värden.

Bildens syfte är att visa fyrtornsvarianten som tidigare låg i E006:

1. PÅ – 500 ms
2. AV – 250 ms
3. PÅ – 180 ms
4. AV – 1400 ms
5. börja om

Bilden ska vara kort, tydlig och följa samma sekvensstil som E002-C, E004-C och E005-C.
