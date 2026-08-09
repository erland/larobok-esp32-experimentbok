# 6.1.1 – Granskning och finjustering av E001

## Syfte

Detta dokument beskriver granskningen och finjusteringen av `E001-Forsta-blinket.md` efter den stora 5B.6-revisionen.

Målet var inte att skriva om experimentet igen från grunden, utan att säkerställa att det fungerar som första guldstandard-kandidat.

---

# Granskningsresultat

## Styrkor

E001 uppfyller nu de viktigaste principerna i 5B.6:

- tydlig berättande öppning,
- starkt första uppdrag,
- tidig wow-effekt,
- varm felsökning,
- aktiv experimentcykel,
- tydlig vuxenroll,
- planerade illustrationer,
- emotionell progression från nyfikenhet till egen kontroll.

Experimentet känns nu mer som början på en upptäckarbok än som en vanlig teknisk instruktion.

---

# Finjusteringar som genomförts

## 1. Tydligare byggtrygghet

En byggrekommendation har lagts till:

> Koppla helst med USB-kabeln urdragen.

Detta stärker säkerhet och trygghet utan att göra texten tung.

## 2. Tydligare breadboardkontroll

En mikrokoll har lagts till om att LED-benen inte ska sitta i samma rad.

Det minskar risken för ett vanligt nybörjarfel.

## 3. Mer robust GPIO-text

Texten för GPIO 5 har kompletterats med att olika ESP32-kort kan märka pinnen på olika sätt.

## 4. Bättre vuxenstöd vid uppladdningsproblem

Vuxenkollen efter koden nämner nu port, kortinställning och USB-kabel.

Detta gör att vuxenstödet täcker ett vanligt praktiskt problem.

## 5. Starkare första seger

Efter första blinket har en liten seger-markering lagts till.

Det gör att första wow blir tydligare som emotionell milstolpe.

## 6. Mer aktiv Testa-sektion

Barnet uppmanas att gissa innan `delay()` ändras.

Det gör läsningen mer aktiv och mer experimentell.

## 7. Starkare övergång till E002

Avslutningen har gjorts något mer lockande genom att antyda att lampan snart kan “prata med blinkningar”.

---

# Kontroll mot 5B.6.11

| Kontrollpunkt | Bedömning |
|---|---|
| Inledningen väcker nyfikenhet | Uppfyllt |
| Experimentet har tydligt uppdrag | Uppfyllt |
| Barnet får ett tidigt wow | Uppfyllt |
| Avslutningen pekar mot nästa upptäckt | Uppfyllt |
| En ny huvudidé | Uppfyllt |
| Testa/Utforska/Experimentera/Utmaning finns | Uppfyllt |
| Felsökning är uppmuntrande | Uppfyllt |
| Barnet får göra egna val | Uppfyllt |
| Språket känns varmt | Uppfyllt |
| Bilder är planerade där de behövs | Uppfyllt |
| Vuxenrutor används sparsamt | Uppfyllt |
| Kod testad | Kvarstår |
| Koppling verifierad på fysisk breadboard | Kvarstår |
| Säkerhetskontroll | Delvis uppfyllt, fysisk test kvarstår |

---

# Rekommendation

E001 kan nu användas som **första guldstandard-kandidat** för tonen och strukturen i kapitel 1.

Innan E001 markeras som färdigt bör följande göras:

1. fysisk breadboardtest med minst en vanlig ESP32 DevKit,
2. test av uppladdning i vald kodmiljö,
3. snabb läsning med målgruppen eller vuxen testläsare,
4. kontroll att framtida illustrationer matchar bildplanen.

---

# Status

E001 är finjusterad enligt 5B.6 och redo att fungera som referens inför revision av E002.
