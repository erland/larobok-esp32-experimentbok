# 5A.2 – Konsekvenser för illustrationer

## Syfte

Breadboard-progressionen påverkar hur illustrationer ska planeras. Om kopplingar återanvänds bör även bilderna visa förändring steg för steg, inte bara färdiga slutkopplingar.

---

# Bildtyper

| Bildtyp | När den används |
|---|---|
| Startbild | när ett nytt kopplingsblock introduceras |
| Lägg-till-bild | när en komponent adderas till befintlig koppling |
| Byt-sensor-bild | när output behålls men input ändras |
| Slutbild | kapitelprojektets fulla koppling |
| Säkerhetsbild | motorer, HC-SR04, SD, extern matning |
| Systembild | smarta projekt med flera delar |

---

# Rekommenderat bildmönster per kapitel

Varje kapitel bör ha:

1. en ren startkoppling,
2. 2–4 lägg-till-bilder,
3. en kapitelprojektbild,
4. en felsökningsbild eller säkerhetsbild vid behov.

---

# Färgkodning

Rekommenderad konsekvent kabelsymbolik:

| Färg | Betydelse |
|---|---|
| Röd | 3,3V eller positiv matning |
| Svart/blå | GND |
| Gul/orange | digital signal |
| Grön | analog signal |
| Lila | I²C/SPI/kommunikation |
| Grå | motor/extern styrning |

Detta bör senare formaliseras i illustrationsguiden.

---

# Viktig designregel

Om en illustration visar en koppling som bygger vidare på föregående experiment bör bilden tydligt markera:

- vad som är nytt,
- vad som sitter kvar,
- vad som tas bort,
- vad som flyttas.

Det gör boken mycket lättare att följa för barn och föräldrar.
