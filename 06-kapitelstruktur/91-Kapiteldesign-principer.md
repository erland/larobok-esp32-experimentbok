# 91 – Kapiteldesignprinciper

## Syfte

Detta dokument beskriver hur varje kapitel i boken ska designas, skrivas och kvalitetssäkras. Det är ett styrdokument för kommande produktion och ska användas tillsammans med kapitelöversikten och de enskilda kapiteldesignfilerna.

---

# 1. Kapitel som pedagogisk enhet

Ett kapitel ska inte bara vara en grupp experiment. Det ska vara en liten resa med början, mitt och avslut.

Varje kapitel ska därför ha:

1. ett tydligt tema,
2. en ny central idé,
3. återanvändning av tidigare kunskap,
4. flera små experiment,
5. ett större kapitelprojekt,
6. en sammanfattning som förbereder nästa kapitel.

---

# 2. Standardstruktur för ett kapitel

Varje kapitel bör i produktionsfasen följa denna struktur:

## 2.1 Kapitelöppning

Innehåller:

- kort berättande inledning,
- vad barnet kommer att bygga,
- vilka komponenter som behövs,
- ungefärlig svårighetsnivå,
- vad kapitlet bygger vidare på.

## 2.2 Förkunskaper

Kort lista över vad barnet redan bör ha gjort.

## 2.3 Experimentserie

6–9 huvudexperiment.

Varje experiment ska:

- introducera en tydlig idé,
- ge synligt/hörbart resultat,
- återanvända tidigare kopplingar där möjligt,
- vara kort nog att slutföra i en sittning.

## 2.4 Bonusruta

0–2 bonusprojekt som inte krävs för fortsatt progression.

## 2.5 Kapitelprojekt

Ett större projekt som kombinerar kapitlets kunskap.

## 2.6 Sammanfattning

Barnvänlig reflektion:

- Vad kan du nu?
- Vad var svårt?
- Vad kan du bygga vidare på?

---

# 3. Regler för experimentordning

Experimenten i ett kapitel ska sorteras efter:

1. enklaste fungerande koppling,
2. första synliga resultat,
3. en ny komponent,
4. en ny kodidé,
5. kombination av tidigare idéer,
6. kapitelprojekt.

Undvik att börja ett kapitel med både ny komponent och ny komplex kod.

---

# 4. En ny huvudidé i taget

Ett experiment får gärna repetera många tidigare saker, men bör bara introducera en ny huvudidé.

Exempel på ny huvudidé:

- första LED,
- första knapp,
- första analog sensor,
- första OLED,
- första servo,
- första WiFi-webbsida.

Om ett experiment kräver både ny sensor, nytt bibliotek, ny display och ny kodstruktur bör det delas upp.

---

# 5. Breadboard-principer

## 5.1 Konsekvent layout

Rekommenderad layout:

| Zon | Innehåll |
|---|---|
| Vänster | input: knappar och sensorer |
| Mitten | ESP32 |
| Höger | output: LED, buzzer, display, servo |
| Överkant | ström |
| Nederkant | tillfälliga moduler |

## 5.2 Återanvänd output

När en ny sensor introduceras bör output ofta vara bekant.

Exempel:

```text
ny sensor + gammal RGB/buzzer-output
```

## 5.3 Återanvänd input

När en ny output introduceras bör input ofta vara bekant.

Exempel:

```text
gammal knapp + ny OLED/servo-output
```

---

# 6. Kodprogression

Kod ska växa långsamt.

## Tidiga kapitel

- mycket kort kod,
- `delay()` accepteras,
- få variabler,
- få funktioner.

## Mellankapitel

- funktioner,
- arrayer,
- `millis()`,
- bibliotek,
- enkla tillstånd.

## Sena kapitel

- flera moduler,
- längre program,
- tydligare uppdelning,
- projektstruktur,
- nätverk och loggning.

## Regel

Om koden blir lång ska den delas upp pedagogiskt, inte bara presenteras som en stor kodlista.

---

# 7. Teori och praktik

Praktik ska komma före teori.

Rekommenderat mönster:

1. Bygg något.
2. Testa.
3. Observera.
4. Fråga vad som händer.
5. Förklara kort.
6. Utmana barnet att ändra något.

Teori bör placeras i små faktarutor.

---

# 8. Wow-faktor

Varje kapitel ska ha minst ett experiment som känns särskilt roligt, överraskande eller användbart.

Exempel på wow-projekt:

- reaktionsspel,
- parkeringssensor,
- spökhus,
- växtvakt,
- NeoPixel-ring,
- skattkista,
- robot,
- RFID-nyckel,
- webbstyrd lampa.

Wow-projekt bör placeras efter några förberedande experiment, inte först.

---

# 9. Vuxenstöd

Boken riktar sig till barn 7–12 år men yngre barn behöver vuxenstöd.

Vuxenmarkering ska användas vid:

- motorer,
- extern ström,
- MicroSD,
- WiFi,
- mekaniska byggen,
- risk för felkoppling,
- vattennära experiment,
- längre felsökning.

Vuxen ska hjälpa utan att ta över.

---

# 10. Säkerhet

Följande är bindande:

- ingen 230V,
- ingen litiumladdning,
- inget lödkrav i huvudspåret,
- motorer kopplas aldrig direkt till GPIO,
- LED ska normalt ha motstånd,
- ESP32 ska skyddas från 5V-signaler,
- koppla ur USB vid större ändringar.

---

# 11. Illustrationer i kapitel

Varje kapitel bör planera illustrationer i förväg.

Miniminivå:

- startkoppling,
- lägg-till-bild för ny komponent,
- kapitelprojektbild,
- felsöknings- eller säkerhetsbild vid behov.

Varje bild ska tydligt visa:

- vad som är nytt,
- vad som sitter kvar,
- vad som tas bort,
- vilken pinne som används,
- plus/minus/jord.

---

# 12. Felsökning

Felsökning ska normaliseras.

Varje kapitel bör ha återkommande felsökningsrutor med:

| Problem | Möjlig orsak | Testa detta |
|---|---|---|

Typiska kategorier:

- fel pinne,
- lös kabel,
- fel polaritet,
- fel bibliotek,
- fel I²C-adress,
- fel tröskelvärde,
- för lite ström.

---

# 13. Kapitelprojekt

Kapitelprojektet ska:

- kombinera flera experiment i kapitlet,
- kännas användbart eller lekfullt,
- inte introducera för mycket ny teknik,
- gärna ha ett tydligt uppdrag,
- kunna förenklas om barnet blir trött.

Exempel:

- Kapitel 4: reaktionsspel eller Simon Says,
- Kapitel 5: parkeringshjälp,
- Kapitel 6: spökhus,
- Kapitel 10: larmcentral,
- Kapitel 14: egen smart uppfinning.

---

# 14. Bonus och reserv

Bonusprojekt ska:

- vara roliga,
- vara frivilliga,
- inte krävas för fortsatt progression,
- gärna ha hög wow-faktor.

Reservprojekt kan användas som:

- webbmaterial,
- framtida upplaga,
- lärar-/föräldratips,
- extra utmaning.

---

# 15. Checklista för kapiteldesign

Innan ett kapitel går till skrivproduktion ska följande vara besvarat:

- [ ] Vad är kapitlets nya huvudidé?
- [ ] Vilka experiment är huvudspår?
- [ ] Vilka experiment är bonus?
- [ ] Vilket är kapitelprojektet?
- [ ] Vilka komponenter introduceras?
- [ ] Vilka komponenter återanvänds?
- [ ] Vilka kodidéer introduceras?
- [ ] Vilka illustrationer behövs?
- [ ] Vilka säkerhetsrutor behövs?
- [ ] Var finns kapitlets wow-ögonblick?
- [ ] Vilken koppling kan sitta kvar mellan experiment?
- [ ] Finns det för många mätövningar i rad?
- [ ] Finns det för mycket teori innan första byggmomentet?
- [ ] Kan yngre barn vara aktiva även om vuxen hjälper?

---

# 16. Kvalitetsnivå

Ett kapitel är tillräckligt moget för produktion när det går att skriva experimenten utan att behöva fatta stora struktur- eller ordningsbeslut.

Om en författare eller AI-assistent fortfarande behöver fråga:

- "Vilka experiment ska ingå?"
- "Vad ska kapitlet lära ut?"
- "Vad är kapitelprojektet?"
- "Vilka bilder behövs?"

är kapiteldesignen inte färdig.

---

# 17. Användning i framtida steg

Detta dokument ska användas i:

- 5A.3 Komponentlivscykel,
- 5A.4 Illustrationsplan,
- 5A.5 Kodprogression,
- 5B Produktionsmatris,
- faktisk skrivproduktion av experimenten.
