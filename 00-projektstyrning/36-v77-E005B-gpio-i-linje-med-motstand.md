# v77 – E005-B GPIO i linje med motstånd

I v76 var kopplingslogiken korrekt, men GPIO-utgångarna låg något högre än motståndsledarna. Det gjorde att signalvägen på vänster sida om LED-lamporna inte låg i samma linje som ledaren på högersidan.

## Åtgärd i v77

- GPIO 23 flyttades ned i höjd med övre motståndsledaren.
- GPIO 22 flyttades ned i höjd med nedre motståndsledaren.
- Signalledarna ritades horisontellt in till LED-lampornas långa ben.
- GPIO-etiketterna breddades något för att undvika klippt text.

## Resultat

Bilden får en rakare och lugnare kopplingsväg:
GPIO → långt ben → kort ben → motstånd → GND.
