# v74 – E005-B anslutningar till LED-ben

I v73 ritades E005-B om för renare layout, men kopplingstrådarna från GPIO-pinnarna gick inte tydligt ända fram till LED-lampornas ben på samma sätt som i tidigare experiment.

## Åtgärd i v74

Bilden justerades så att:

- GPIO 23-tråden går fram till röda LED-lampans långa ben,
- GPIO 22-tråden går fram till blå LED-lampans långa ben,
- kort ben fortsätter vidare till respektive motstånd,
- motstånd går vidare till gemensam GND.

## Resultat

E005-B är nu mer konsekvent med E003/E004 samtidigt som den renare v73-layouten behålls.
