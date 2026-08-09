# 5B.6.7 – Humor, språk och uppmuntran

## Syfte

Detta dokument fördjupar hur boken ska använda humor, språk och uppmuntran. Målet är att skapa en varm och trygg läsupplevelse där barnet vågar testa, vågar göra fel och vågar tänka själv.

Humor i den här boken ska inte vara ett separat lager ovanpå tekniken. Den ska hjälpa barnet att känna:

> Det här är roligt, jag vågar prova, och det gör inget om det inte fungerar direkt.

---

# Grundprincip

Bokens humor ska vara:

- lågmäld,
- konkret,
- kopplad till situationen,
- aldrig på barnets bekostnad,
- aldrig så skojig att instruktionen blir otydlig,
- aldrig beroende av att barnet kan vuxenreferenser.

Humor ska fungera som en liten hand på axeln, inte som en clownnäsa på elektroniken.

---

# Vad humor får göra

Humor får:

- minska stress,
- normalisera felsökning,
- göra komponenter mer begripliga,
- skapa en liten känsla av personlighet,
- ge barnet mod att testa igen.

Exempel:

> Om lampan inte blinkar kanske den bara är blyg. Eller så sitter den baklänges.

> ESP32 gör exakt vad koden säger. Även när koden råkar säga något konstigt.

> Ett fel är inte ett stopp. Det är en skylt som pekar mot nästa sak att undersöka.

---

# Vad humor inte får göra

Humor får inte:

- förlöjliga barnet,
- göra instruktionen vag,
- ersätta teknisk förklaring,
- göra boken för barnslig för 10–12-åringar,
- skapa intrycket att komponenter är magiska på riktigt.

Undvik:

> Oj, nu gjorde du tokfel!

> Den busiga lampan vägrar lyda!

> Hoppsan, datorn blev arg!

Bättre:

> Något i kopplingen säger inte samma sak som koden. Då letar vi efter ledtråden.

---

# Uppmuntrande språk

## Bra uppmuntran

Bra uppmuntran är specifik.

Exempel:

> Du ändrade bara en siffra, men beteendet ändrades i verkligheten.

> Nu har du hittat en ledtråd: lampan lyser hela tiden.

> Du felsöker som en uppfinnare.

## Svag uppmuntran

Undvik alltför generiska fraser:

> Bra jobbat!

> Duktigt!

De kan användas ibland, men bör inte bära texten.

Bättre är att beskriva **vad barnet faktiskt gjorde**.

---

# Felsökningston

Felsökning ska alltid beskrivas som undersökning, inte misslyckande.

Använd hellre:

- ledtråd,
- mysterium,
- testa en sak i taget,
- vad säger kopplingen?,
- vad säger koden?,
- börja där det senast fungerade.

Undvik:

- fel,
- misslyckades,
- gjorde fel,
- borde fungera,
- bara kontrollera.

Exempel:

> Om LED-lampan inte blinkar har du inte förstört experimentet. Du har hittat ett mysterium.

---

# Språk för olika åldrar

Boken riktar sig till 7–12 år. Det betyder att texten måste fungera på två nivåer.

## För yngre barn

- korta meningar,
- tydliga bilder,
- mycket konkret handling,
- vuxen kan läsa högt.

## För äldre barn

- undvik bebisspråk,
- ge möjlighet till egna varianter,
- använd riktiga tekniska ord efter upplevelsen,
- visa respekt för att barnet kan tänka själv.

Bra balans:

> Pinnen är på. Det tekniska ordet är `HIGH`.

Det gör att yngre barn kan förstå och äldre barn får rätt begrepp.

---

# Ordval

## Ord som stärker bokens känsla

- uppdrag,
- upptäck,
- ledtråd,
- signal,
- bygg vidare,
- testa,
- gissa,
- undersök,
- ändra,
- skapa,
- egen version.

## Ord som ska användas varsamt

- enkelt,
- bara,
- självklart,
- uppenbart,
- misslyckande,
- fel,
- korrekt/inkorrekt.

Orden "enkelt" och "bara" kan göra att barnet känner sig dumt om det inte fungerar.

Skriv inte:

> Koppla bara LED-lampan till GPIO 5.

Skriv hellre:

> Koppla LED-lampan till GPIO 5. Ta ett steg i taget.

---

# Kodkommentarer

Kodkommentarer ska vara korta och hjälpsamma.

Bra:

```cpp
// Tänd lampan
digitalWrite(ledPin, HIGH);
```

Mindre bra:

```cpp
// Nu säger vi åt vår lilla superglada blinkkompis att lysa jättemycket!
digitalWrite(ledPin, HIGH);
```

Koden ska vara lugn. Berättarrösten hör hemma i brödtexten.

---

# Vuxenrutor

Vuxenrutor ska ha en annan ton än barntexten:

- tydligare,
- mer teknisk,
- praktiskt stödjande,
- aldrig stressande.

Bra:

> Kontrollera att LED-lampan har ett seriemotstånd och att vald GPIO passar ert ESP32-kort.

Mindre bra:

> Se till att barnet inte gör fel.

Vuxenrollen är mentor, inte kontrollant.

---

# Uppmuntran efter svårighet

När ett experiment innehåller ett svårt moment ska texten erkänna det.

Exempel:

> Den här kopplingen har fler kablar än tidigare. Det är helt normalt att behöva titta på bilden flera gånger.

Detta gör att barnet inte tolkar långsamhet som misslyckande.

---

# Kontrollfrågor för språk och uppmuntran

Innan ett experiment godkänns:

- Finns minst en varm, situationsbunden uppmuntran?
- Är felsökning beskriven som ledtrådar?
- Har vi undvikit "bara", "enkelt" och "självklart" där de kan såra?
- Är humorn kopplad till experimentet?
- Känns texten respektfull även för ett äldre barn?
- Är tekniska ord introducerade efter upplevelsen när det är möjligt?

---

# Beslut

Humor, språk och uppmuntran ska granskas som en egen kvalitetsdimension. Ett experiment kan vara tekniskt korrekt men ändå behöva revideras om tonen gör barnet passivt, stressat eller mindre nyfiket.
