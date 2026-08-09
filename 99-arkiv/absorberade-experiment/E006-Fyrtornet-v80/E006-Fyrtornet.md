# E006 – Fyrtornet

## Uppdraget: ge lampan en plats i mörkret

Tänk dig att det är mörkt.

Långt borta syns ett ljus.

Inte hela tiden.

Det blinkar.

Sedan blir det mörkt igen.

Sedan kommer ljuset tillbaka.

Ett fyrtorn använder ljus för att visa att något finns där ute.

I det här experimentet ska din LED-lampa inte kännas snabb och stökig som i E005.

Den ska kännas lugn, tydlig och trygg.

Du använder samma enkla koppling som i E002, men du ger lampan en ny rytm.

Plötsligt känns den inte bara som en lampa längre.

Den känns som ett litet fyrtorn.

---

## Dagens uppfinning

Du ska bygga ett blinkmönster som liknar ett fyrtorn.

När du är klar ska lampan göra en enkel fyrsignal:

- ett långt blink,
- en kort mörk paus,
- ett kortare blink,
- och sedan en lång mörk paus innan allt börjar om.

Det viktiga är inte att det blir en exakt riktig fyr.

Det viktiga är att du märker att:

> samma LED kan få en helt ny känsla när du ändrar tiden.

---

## Du lär dig

När du gjort experimentet har du lärt dig att:

- återanvända LED-kopplingen från E001 och E002,
- skapa ett blinkmönster med både långa och korta delar,
- använda flera `delay()`-tider i samma sekvens,
- se att långa pauser gör signalen lugnare,
- läsa en `loop()` som berättar ett mönster steg för steg,
- skapa ett berättande ljus med bara en LED-lampa.

---

## Du behöver

![E006 - Dagens delar](../../08-illustrationer-och-kopplingar/generated/E006/E006-A-dagens-delar.svg)

_Dagens delar: samma delar som i E001 och E002 – ESP32, breadboard, LED-lampa, motstånd, kablar och USB._

| Del | Antal | Kommentar |
|---|---:|---|
| ESP32 DevKit | 1 | Samma som tidigare |
| Breadboard | 1 | Samma koppling kan återanvändas |
| LED-lampa | 1 | Gärna vit, gul eller blå – men vilken färg som helst fungerar |
| Motstånd 220–330 Ω | 1 | Skyddar LED-lampan |
| Kopplingskablar | 2–3 | Hane–hane |
| USB-kabel | 1 | För ström och uppladdning |

> **Vuxenkoll:** Kontrollera att LED-lampan fortfarande sitter i serie med ett motstånd. Om ni återanvänder kopplingen från E002 är det främst rytmen i koden som ändras.

---

## Innan du börjar

Om du har kvar kopplingen från E002 kan du använda den igen.

I det här experimentet använder vi:

- en LED-lampa på GPIO 23,
- ett motstånd mellan LED-lampans korta ben och GND.

Om du har flera färger kan du gärna välja en som känns som fyr-ljus för dig.

Vit eller gul känns ofta tydligt, men alla färger fungerar.

---

# Koppla så här

Börja med att titta på kopplingsvägen.

![E006 - Kopplingsöversikt](../../08-illustrationer-och-kopplingar/generated/E006/E006-B-kopplingsoversikt.svg)

_Förenklad kopplingsöversikt: GPIO 23 styr en LED-lampa. LED-lampans korta ben går via motstånd tillbaka till GND._

Det här är samma grundkoppling som i E001 och E002:

> GPIO 23 → LED-lampans långa ben → LED-lampans korta ben → motstånd → GND

Du behöver alltså inte bygga något större system den här gången.

Det nya sitter i rytmen.

---

## Steg 1 – Kontrollera LED-lampan

Sätt LED-lampan så att benen hamnar i olika rader på breadboarden.

- Långt ben går mot GPIO 23.
- Kort ben går mot motståndet.

---

## Steg 2 – Kontrollera vägen till GND

Följ vägen från LED-lampans korta ben till motståndet.

Kontrollera sedan att motståndet går vidare till GND.

---

## Steg 3 – Kontrollera hela ljusvägen

Följ kopplingen med fingret:

- GPIO 23,
- långt ben,
- kort ben,
- motstånd,
- GND.

> **Mikrokoll:** Om E002 fungerade är kopplingen troligen redan rätt. Då är det nya här framför allt koden och rytmen.

---

# Koden

Skriv in eller ersätt koden med denna:

```cpp
const int ledPin = 23;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Första långa blinket
  digitalWrite(ledPin, HIGH);
  delay(500);

  // Kort mörk paus
  digitalWrite(ledPin, LOW);
  delay(250);

  // Andra kortare blinket
  digitalWrite(ledPin, HIGH);
  delay(180);

  // Lång mörk paus innan allt börjar om
  digitalWrite(ledPin, LOW);
  delay(1400);
}
```

## Stanna och gissa

Titta på koden innan du laddar upp den.

- Vilken del tror du lyser längst?
- Var finns den längsta pausen?
- Vilken del tror du gör att lampan känns som ett fyrtorn och inte som ett snabbt larm?

Ladda sedan upp koden till ESP32.

> **Vuxenkoll:** Om uppladdningen inte fungerar, börja med samma korttyp, port och USB-kabel som fungerade i E001–E005. Om inget blir varmt är det ofta säkert att felsöka lugnt i kod och portval först.

---

# Nu händer det

Titta på lampan.

Om allt är rätt ska rytmen kännas ungefär så här:

> långt blink ... kort blink ........ paus

![E006 - Fyrsekvens](../../08-illustrationer-och-kopplingar/generated/E006/E006-C-fyrsekvens.svg)

_Sekvensen i E006: långt blink, kort blink och sedan en lång mörk paus innan allt börjar om._

Nu känns lampan inte bara som en blinkande pryl.

Den börjar kännas som ett ljus som visar riktning eller plats.

Det viktiga steget är:

> pausen är en del av signalen.

---

## Stanna och se mörkret också

Försök att inte bara titta på när lampan lyser.

Titta också på när den är släckt.

Det är den långa mörka pausen som gör att signalen känns lugn och tydlig.

Utan den skulle ljuset mest kännas som ett vanligt blinkmönster.

---

# Vad händer egentligen?

Du såg att en enda LED-lampa kan få en egen personlighet.

Koden tänder lampan länge först.

Sedan blir det mörkt en kort stund.

Sedan kommer ett kortare blink.

Till sist blir det mörkt länge innan allt börjar om.

Det gör att ögat uppfattar mönstret som en liten signal i mörkret.

> Ett blinkmönster består både av ljus och av väntan.

I riktiga fyrar är rytmen viktig. Olika fyrar kan ha olika blinkmönster så att de går att känna igen.

Här gör du en enkel modell av samma idé.

---

# Testa

Ändra den långa mörka pausen från:

```cpp
delay(1400);
```

till:

```cpp
delay(2500);
```

Ladda upp igen.

Vad händer?

Nu känns signalen lugnare och mer utdragen.

Ändra sedan tillbaka till `1400` och prova att ändra det korta blinket från:

```cpp
delay(180);
```

till:

```cpp
delay(350);
```

Nu blir skillnaden mellan långt och kort blink mindre tydlig.

---

# Utforska

![E006 - Fyrvariationer](../../08-illustrationer-och-kopplingar/generated/E006/E006-D-fyrvariationer.svg)

_Samma LED kan kännas lugn, tydlig eller snabb beroende på hur blink och pauser kombineras._

Prova några olika tider.

| Ändring | Vad tror du händer? | Vad hände? |
|---|---|---|
| långt blink `300` ms |  |  |
| långt blink `700` ms |  |  |
| kort blink `120` ms |  |  |
| kort blink `300` ms |  |  |
| lång paus `900` ms |  |  |
| lång paus `2500` ms |  |  |

Titta inte bara på om lampan blinkar.

Titta på hur signalen känns:

- lugn,
- tydlig,
- snabb,
- avlägsen,
- nästan som en kod.

---

# Experimentera

Nu får du göra din egen fyrsignal.

Du kan ändra:

- hur långt första blinket är,
- hur långt andra blinket är,
- hur lång den korta pausen är,
- hur lång den mörka havspausen är.

Börja med en enkel idé:

> långt blink ... långt mörker

eller:

> kort blink, kort blink ........ paus

eller:

> långt blink, kort blink ........ paus

Ändra bara en sak i taget.

Då blir det lättare att förstå vad som gav den nya känslan.

---

# Utmaning

Välj en nivå.

## Nivå 1 – Lugn fyr

Gör signalen ännu lugnare så att pausen känns tydlig och stor.

---

## Nivå 2 – Egen fyrsignatur

Hitta på ett mönster som du tycker känns som just din fyr.

Kan någon annan känna igen den om du visar den flera gånger?

---

## Nivå 3 – Ljuskod

Bestäm att olika fyrmönster betyder olika saker.

Exempel:

| Signal | Betydelse |
|---|---|
| långt blink | här är jag |
| långt-kort | kom hit |
| kort-kort | klart |

Visa signalen för någon annan. Kan de lista ut vilken som är vilken?

---

# Vanliga ledtrådar

Börja med samma saker som i E002: koppling, uppladdning och rytm.

| Det du ser | Möjlig ledtråd | Testa |
|---|---|---|
| Lampan blinkar som i E001 eller E002 | Den gamla koden kan fortfarande ligga kvar | Ladda upp E006-koden igen |
| Lampan lyser inte alls | Kopplingen kan ha ändrats | Kontrollera GPIO 23, LED-riktning och GND |
| Lampan lyser nästan hela tiden | Pauserna kan vara för korta eller uppladdningen kan ha misslyckats | Läs `delay()`-raderna och ladda upp igen |
| Mönstret känns inte som du tänkte | Ett av tiderna är för långt eller för kort | Testa en siffra i taget |
| Det går inte att ladda upp | USB-kabel, port eller korttyp kan vara fel | Testa samma inställningar som fungerade tidigare |

> **Vuxenkoll:** Om E002 fungerade men E006 känns fel är kopplingen ofta rätt. Börja då med att läsa tiderna i koden rad för rad och jämföra med det barnet faktiskt ser.

---

# För den vuxne

E006 fungerar som kapitelprojekt i slutet av Kapitel 1.

Tekniskt är det fortfarande en mycket enkel LED-koppling, men pedagogiskt gör experimentet något viktigt:

Barnet får uppleva att en enda lampa kan få en berättelse och en identitet.

Det här är ett bra tillfälle att prata om att teknik inte bara handlar om att något fungerar, utan också om **hur det beter sig**.

Barnet får dessutom träna på att observera rytm och jämföra känslor i olika sekvenser.

Frågor som hjälper:

- Vilken rad tänder lampan länge?
- Vilken rad tänder lampan kort?
- Var finns den längsta mörka pausen?
- Vad händer om båda blinkningarna blir lika långa?
- Vad händer om pausen nästan försvinner?
- När känns lampan mest som ett fyrtorn?

Det är också ett bra brobygge till senare experiment där blinkmönster blir mer som kod eller meddelanden.

---

# Jag undrar...

Fundera på de här frågorna:

- Hur kan en lampa kännas lugn?
- Varför behövs mörkret mellan blinkningarna?
- Kan två olika fyrar kännas olika fast de använder samma sorts lampa?
- Hur skulle du göra ett ljus som känns långt borta?
- Kan blinkmönster bli ett språk?

Du behöver inte svara på allt nu.

Några av idéerna kommer tillbaka senare när du bygger fler signaler.

---

# Nästa experiment

Nu har du byggt ett berättande ljus med bara en enda LED-lampa.

I kommande experiment ska flera lampor få samarbeta ännu mer.

Då kan ljuset börja röra sig, skicka tydligare signaler och till slut bli nästan som en liten kod.

> En enkel blinkning kan vara början på ett helt språk.
