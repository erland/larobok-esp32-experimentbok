# 5A.4 – Illustrationsplan

## Syfte

Detta dokument beskriver hur illustrationer, breadboardbilder, komponentbilder, systembilder och kodförklarande figurer ska planeras för boken.

Målet är att illustrationerna ska göra boken lättare att följa, särskilt för barn 7–12 år och vuxna som bygger tillsammans med dem.

Illustrationsplanen bygger på:

- 5A.1 Kapiteldesign
- 5A.2 Breadboard-progression
- 5A.3 Komponentlivscykel

---

# Grundprinciper

## 1. Bilder ska minska felsökning

Varje bild ska hjälpa läsaren att undvika vanliga fel:

- fel pinne,
- fel polaritet,
- fel breadboardrad,
- fel komponentriktning,
- saknad jord,
- fel modulspänning.

## 2. Bilder ska visa progression

Boken ska inte bara visa färdiga kopplingar. Den ska visa hur kopplingen växer.

Exempel:

```text
LED
  ↓
LED + knapp
  ↓
LED + knapp + buzzer
  ↓
LED + knapp + buzzer + OLED
```

## 3. Bilder ska markera vad som är nytt

När en komponent läggs till ska bilden tydligt visa:

- vad som redan fanns,
- vad som är nytt,
- vad som tas bort,
- vad som flyttas.

## 4. Bilder ska vara konsekventa

Samma komponent ska alltid ritas på samma sätt. Samma färger ska betyda samma sak genom hela boken.

## 5. Illustrationer ska stödja både barn och vuxen

Barnet ska kunna förstå vad som händer. Den vuxne ska kunna kontrollera kopplingen.

---

# Bildtyper

| Bildtyp | Syfte |
|---|---|
| Komponentbild | Visa hur komponenten ser ut och vad den gör |
| Breadboardbild | Visa exakt koppling |
| Lägg-till-bild | Visa vad som ändras från föregående experiment |
| Systembild | Visa sensor → ESP32 → output |
| Flödesschema | Visa logik, spel eller tillstånd |
| Kodförklaringsbild | Visa hur koddelar hänger ihop |
| Säkerhetsbild | Visa risker eller viktiga kontroller |
| Projektbild | Visa det färdiga kapitelprojektet |
| Felsökningsbild | Visa vanliga fel och kontroller |

---

# Rekommenderad miniminivå per experiment

Varje huvudexperiment bör ha minst:

1. komponentruta,
2. breadboardbild eller lägg-till-bild,
3. förväntat resultat.

Varje kapitelprojekt bör ha:

1. systembild,
2. full breadboardbild,
3. projektbild,
4. felsökningsbild.

---

# Färgstandard

| Färg | Betydelse |
|---|---|
| Röd | 3,3V eller positiv matning |
| Svart/blå | GND |
| Gul/orange | digital signal |
| Grön | analog signal |
| Lila | I²C/SPI/kommunikation |
| Grå | motor/extern styrning |
| Turkos | valfri/sekundär signal |
| Rosa | ny komponent i aktuell bild |

Färgerna är rekommendationer. Om verktyget inte stöder exakt färg bör samma princip ändå följas.

---

# Namngivningsstandard

Illustrationer bör namnges så här:

```text
fig-kapitel-experiment-typ-kortnamn
```

Exempel:

```text
fig-03-e026-breadboard-knapp-led
fig-05-e055-system-parkeringssensor
fig-10-e090-projekt-skattkista
```

## Filformat

| Användning | Rekommenderat format |
|---|---|
| Redigerbar originalbild | SVG eller Fritzing-projekt |
| Tryck/PDF | SVG eller PNG hög upplösning |
| Webb | SVG/PNG |
| Snabb skiss | PNG |
| Schematisk logik | Mermaid eller SVG |

---

# Produktionsprincip

Illustrationer ska produceras efter att experimenttexten är tillräckligt stabil, men planeras innan texten skrivs. Detta dokument är därför en kölista och kravspecifikation, inte färdiga bilder.
