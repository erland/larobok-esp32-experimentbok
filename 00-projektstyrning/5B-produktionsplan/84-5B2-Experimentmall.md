# 5B.2 – Experimentmall

## Syfte

Denna mall ska användas som standard för alla experiment i boken. Målet är att varje experiment ska kännas igen, vara lätt att följa och hjälpa barnet att utveckla ett experimenterande arbetssätt.

Varje experiment ska vara en liten berättelse:

```text
Vad ska vi bygga?
  ↓
Vad behöver vi?
  ↓
Hur kopplar vi?
  ↓
Vilken kod behövs?
  ↓
Fungerar det?
  ↓
Vad kan vi ändra?
  ↓
Vad tror vi händer?
  ↓
Vad kan vi bygga vidare?
```

---

# Standardmall för experiment

```markdown
# E0XX – Experimentnamn

## Kort idé

En kort, barnvänlig beskrivning av vad experimentet gör.

## Du lär dig

Efter experimentet kan du:

- ...
- ...
- ...

## Du behöver

| Komponent | Antal | Kommentar |
|---|---:|---|
| ESP32 | 1 | |
| Breadboard | 1 | |
| ... | ... | ... |

## Innan du börjar

Kort lista över vad som bör vara klart från tidigare experiment.

## Koppla så här

1. ...
2. ...
3. ...

**Bild:** `fig-xx-exxx-breadboard-kortnamn`

## Koden

```cpp
// Experiment E0XX – Namn
// Kort beskrivning.

void setup() {
}

void loop() {
}
```

## Testa

Här verifierar barnet att experimentet fungerar.

Exempel:

1. Ladda upp koden.
2. Titta på LED/skärm/ljud/sensor.
3. Kontrollera att resultatet stämmer.

## Vad händer?

Förklara med barnvänligt språk vad kopplingen och koden gör.

## Utforska

Små, trygga ändringar som barnet kan göra direkt.

Exempel:

- Ändra blinkhastigheten.
- Byt LED-färg.
- Ändra ett gränsvärde.
- Testa en annan ton.

## Experimentera

Barnet gissar först, testar sedan och jämför.

Exempel:

> Vad tror du händer om värdet ändras från 500 till 50?

Skriv gärna som:

1. Gissa.
2. Testa.
3. Vad hände?
4. Varför tror du att det blev så?

## Utmaning

En lite större frivillig uppgift.

Exempel:

- Kan du lägga till en LED?
- Kan du göra ett eget mönster?
- Kan du få larmet att låta annorlunda?
- Kan du göra en egen regel?

## Vanliga fel

| Problem | Möjlig orsak | Testa detta |
|---|---|---|
| ... | ... | ... |

## För den vuxne

Teknisk eller säkerhetsrelaterad kommentar vid behov.

## Bonus

Frivillig fördjupning som kan hoppas över.

## Jag undrar...

Öppna frågor som väcker nyfikenhet och pekar framåt.

Exempel:

- Vad skulle hända om vi lade till en knapp?
- Kan samma idé användas med en sensor?
- Hur skulle apparaten veta om det är mörkt?
- Kan vi visa resultatet på en liten skärm?

Ge inte alltid svaret här. Syftet är att skapa nyfikenhet inför senare experiment.

## Nästa experiment

Kort övergång till nästa experiment.
```

---

# Obligatoriska delar

Alla huvudexperiment ska innehålla:

- Kort idé
- Du lär dig
- Du behöver
- Koppla så här
- Koden
- Testa
- Vad händer?
- Utforska
- Experimentera
- Utmaning
- Vanliga fel
- Jag undrar...
- Nästa experiment

Bonusprojekt kan vara kortare men ska fortfarande innehålla komponentlista, koppling, kod och test.

---

# Pedagogisk experimentcykel

Experimenten ska inte bara visa instruktioner. De ska träna barnet i att tänka som en uppfinnare.

```text
Observera
  ↓
Gissa
  ↓
Testa
  ↓
Jämför
  ↓
Förbättra
```

Det är därför mallen skiljer på:

| Sektion | Syfte |
|---|---|
| Testa | Kontrollera att grundexperimentet fungerar |
| Utforska | Göra små ändringar |
| Experimentera | Gissa först och testa sedan |
| Utmaning | Skapa något nytt |
| Jag undrar... | Väcka nyfikenhet inför framtida experiment |

---

# Längd

| Experimenttyp | Rekommenderad längd |
|---|---:|
| Tidigt huvudexperiment | 1–3 sidor |
| Normalt huvudexperiment | 3–5 sidor |
| Kapitelprojekt | 5–8 sidor |
| Bonusprojekt | 1–4 sidor |
| Makerprojekt | 5–10 sidor |

---

# Regler

1. Introducera högst en ny huvudidé per experiment.
2. Koppla ny teknik till synligt resultat.
3. Ha alltid felsökningshjälp.
4. Ha alltid minst en Utforska-uppgift.
5. Ha ofta en Experimentera-uppgift med gissa → testa → jämför.
6. Ha en Utmaning i huvudexperiment.
7. Använd "Jag undrar..." för att bygga nyfikenhet.
8. Skriv kod som passar bokens kodstil.
9. Referera till illustrationsplanen.
10. Markera vuxenstöd tydligt.
