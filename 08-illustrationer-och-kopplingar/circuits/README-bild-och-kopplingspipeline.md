# 08 – Bild- och kopplingspipeline för E001–E002

## Syfte

Detta dokument etablerar en praktisk pipeline för att skapa tekniskt korrekta bilder till E001 och E002.

Målet är att kunna skapa en nästan färdig PDF-preview där text, kod, tabeller och bilder samverkar, utan att kopplingsbilderna bygger på fria AI-genererade gissningar.

## Grundprincip

> AI får gärna hjälpa till med stil, rytm och dekorativa bilder, men AI ska inte vara sanningskällan för tekniska kopplingar.

Sanningskällan ska vara:

1. strukturerad kopplingsspecifikation,
2. Wokwi-diagram eller motsvarande validerbar diagramkälla,
3. fysisk breadboardtest,
4. först därefter slutlig illustration.

---

# Ny mappstruktur

```text
08-illustrationer-och-kopplingar/
  circuits/
    E001-circuit.yaml
    E002-circuit.yaml
  wokwi/
    E001-diagram.json
    E002-diagram.json
  prompts/
    E001-image-prompts.md
    E002-image-prompts.md
  generated/
    E001/
      E001-C-connection-map.svg
    E002/
      E002-C-rhythm-timeline.svg
  briefs/
    E001-bildpipeline-brief.md
    E002-bildpipeline-brief.md
```

---

# Bildtyper

| Bildtyp | Sanningskälla | Rekommenderad metod |
|---|---|---|
| Breadboardkoppling | `circuit.yaml` + Wokwi JSON | Wokwi/Fritzing/egen SVG |
| Kopplingsschema | `circuit.yaml` | KiCad/Circuitikz/egen SVG |
| Rytm/tidslinje | kodens `delay()`-värden | egen SVG |
| Felsökningsbild | kopplingsspec + manuella markeringar | egen SVG eller annoterad teknisk bild |
| Dagens delar | komponentlista | AI/illustratör/komponentbibliotek |
| Wow/dekorativ bild | manus | AI/illustratör |

---

# Arbetsflöde

## Steg 1 – Strukturera kopplingen

Varje experiment får en `*-circuit.yaml`.

Den beskriver:

- komponenter,
- pinval,
- kopplingsväg,
- säkerhetsnoter,
- vad som ska verifieras fysiskt.

## Steg 2 – Skapa Wokwi-diagram

Varje experiment får en `*-diagram.json`.

Den är inte slutlig layout, men ger en validerbar och reproducerbar teknisk bildkälla.

## Steg 3 – Skapa bokbilder

Från strukturerad källa tas bokbilder fram:

- breadboardbild,
- kopplingsöversikt,
- zoom-bilder,
- felsökningsbilder.

## Steg 4 – Skapa promptar för icke-tekniska bilder

Prompter används för:

- dagens delar,
- wow-bilder,
- stämningsbilder,
- ikoner,
- kapitelkänsla.

Prompter används inte som sanningskälla för kopplingar.

## Steg 5 – Verifiera

Innan bild används i slutlig PDF:

- jämför bild mot `circuit.yaml`,
- jämför bild mot Wokwi-diagram,
- gör fysisk breadboardtest,
- kontrollera att bildtext och manus säger samma sak.

---

# Status v48

Bildpipeline är etablerad för E001–E002.

Kvarstår:

- rendera faktiska breadboardbilder från Wokwi/Fritzing eller egen komponent-SVG,
- göra fysisk test,
- skapa komplett bok-PDF med faktiska bilder,
- ersätta tekniska platshållare i PDF-preview.
