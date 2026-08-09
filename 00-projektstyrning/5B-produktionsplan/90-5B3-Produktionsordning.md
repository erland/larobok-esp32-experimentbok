# 5B.3 – Produktionsordning

## Syfte

Detta steg beskriver i vilken ordning experiment, kapitel, kod, illustrationer och tester bör produceras.

Målet är att minska omarbete. De första kapitlen sätter stil, nivå, kodmall och illustrationsstil för resten av boken.

---

# Rekommenderad produktionsstrategi

Boken bör inte produceras strikt E001–E120 utan i fyra produktionsblock.

| Block | Kapitel | Fokus | Varför |
|---|---|---|---|
| Block 1 | Kapitel 1–4 | Grund, LED, knappar, ljud och spel | Sätter ton, mallar och kodstil |
| Block 2 | Kapitel 5–7 | Sensorer och mätning | Testar input/output-mönstret |
| Block 3 | Kapitel 8–10 | OLED, NeoPixel, servo och smarta prylar | Hög wow-faktor och många illustrationer |
| Block 4 | Kapitel 11–14 | Maker, RFID, WiFi och slutprojekt | Mest avancerat, bör bygga på etablerad stil |

---

# Huvudregel

Skriv först huvudspårsexperimenten i ett kapitel. Bonusprojekt skrivs först när huvudspåret fungerar.

```text
Kapitelintroduktion
  ↓
Huvudexperiment
  ↓
Kapitelprojekt
  ↓
Bonusprojekt
  ↓
Kapitelrevision
```

---

# Varför Kapitel 1–4 ska produceras först

Kapitel 1–4 etablerar:

- språk,
- kodstil,
- experimentmall,
- illustrationernas visuella nivå,
- felsökningsrutor,
- vuxenrutor,
- hur Testa/Utforska/Experimentera/Utmaning/Jag undrar används.

När dessa kapitel sitter rätt kan resten av boken följa samma form.

---

# Varför bonusprojekt väntar

Bonusprojekt ska inte styra huvudprogressionen. Om huvudspåret senare blir för långt kan bonusprojekt flyttas till webbmaterial utan att bokens kärna skadas.
