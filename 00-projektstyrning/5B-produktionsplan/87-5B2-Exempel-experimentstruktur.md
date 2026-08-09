# 5B.2 – Exempel på experimentstruktur

Detta är inte ett färdigt experiment, utan en kort strukturmodell.

# E001 – Första blinket

## Kort idé

Vi ska få en liten LED att blinka med hjälp av ESP32.

## Du lär dig

Efter experimentet kan du:

- koppla en LED med motstånd,
- ladda upp kod till ESP32,
- ändra blinkhastighet.

## Du behöver

| Komponent | Antal |
|---|---:|
| ESP32 | 1 |
| Breadboard | 1 |
| LED | 1 |
| Motstånd | 1 |
| Jumperkablar | 2 |

## Koppla så här

1. Sätt LED på breadboarden.
2. Koppla motståndet i serie.
3. Koppla signalpinnen till LED.
4. Koppla andra sidan till GND.

## Koden

Kort kodexempel enligt kodstilen.

## Testa

LED ska blinka.

## Ändra och prova

Ändra tiden i `delay()`.

## Vanliga fel

| Problem | Möjlig orsak |
|---|---|
| LED lyser inte | LED sitter åt fel håll |
| Koden laddas inte | fel port vald |
