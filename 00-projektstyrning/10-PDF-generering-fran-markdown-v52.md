# PDF-generering från markdown – E001/E002

## Syfte

Detta dokument beskriver hur E001 och E002 nu är förberedda för mer robust PDF-generering i en ny chat eller annan pipeline.

Från v52 innehåller manusfilerna explicita bildreferenser till SVG-filerna i projektet. Det betyder att en PDF-generator inte längre behöver gissa vilken bild som ska placeras vid vilken illustrationsplatshållare.

## Berörda manusfiler

- `07-experimentutkast/kapitel-01/E001-Forsta-blinket.md`
- `07-experimentutkast/kapitel-01/E002-LED-med-egen-rytm.md`

## Bildreferenser

Bilderna refereras relativt från manusfilerna, exempel:

```markdown
![E001 - Kopplingsöversikt](../../08-illustrationer-och-kopplingar/generated/E001/E001-C-kopplingsoversikt.svg)
```

Det gör att generatorn kan läsa markdown och följa bilden direkt.

## Viktig layoutprincip från v52

Tidigare rendering använde lila rutor med rubriken “Tänk på” för vanliga citat och viktiga insikter. Det avbröt läsflödet.

Från v52 gäller följande princip:

- vanliga viktiga insikter skrivs som **Insikt:** i huvudflödet
- stora färgade rutor används främst för:
  - Vuxenkoll
  - Byggtips
  - Mikrokoll
  - säkerhet
  - tydliga sidospår

## Rekommenderad PDF-pipeline

1. Läs manusfilerna.
2. Rendera markdownens explicita SVG-bilder.
3. Hantera `**Insikt:**` som diskret markerad rad eller vanlig fet inledning.
4. Hantera `> **Vuxenkoll:**` och liknande som callout-rutor.
5. Rendera PDF.
6. Rendera PDF till PNG och kontrollera visuellt.

## Kvarstående begränsning

PDF:en är fortfarande en layout-preview. Innan slutproduktion bör följande göras:

- fysisk breadboardtest av E001/E002,
- teknisk bildgranskning mot `circuit.yaml`,
- kontroll av Wokwi-diagram,
- pedagogisk testläsning.
