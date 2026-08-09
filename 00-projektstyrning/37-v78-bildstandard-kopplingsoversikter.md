# v78 – Bildstandard för kopplingsöversikter inför E006 och framåt

Syftet med denna version är att låsa den bildstandard som fungerade bäst efter arbetet med E003 och E005-B v77.

## Huvudregel

Kopplingsöversikter ska i första hand följa den visuella standard som fungerade bäst i E003 och E005-B v77:

- använd rena horisontella kopplingsrader,
- visa signaltråden från GPIO fram till LED-lampans långa ben,
- visa LED-lampans korta ben vidare till motstånd,
- visa motståndet vidare till GND,
- låt kopplingstrådar ansluta visuellt till LED-benen, inte till LED-huvudet,
- där det går ska vänster och höger ledare ligga i samma horisontella linje,
- undvik korsande eller onödigt böjda ledare,
- undvik att GPIO-, GND- eller komponentetiketter hamnar för nära ledare så att bilden känns trång.

## Visuell referens

När en ny kopplingsbild skapas ska följande bilder användas som praktisk referens:

1. `E003-B-kopplingsoversikt.svg`
2. `E005-B-kopplingsoversikt.svg` från v77 eller senare

E003 används som ursprunglig standard för två LED-lampor. E005-B v77 används som referens för en renare två-raderslayout med tydligt linjerade ledare.

## När bilden ska justeras

En kopplingsbild bör justeras innan PDF-preview om den:

- visar trådar som går till LED-huvudet i stället för benen,
- har trådar som slutar nära men inte tydligt på LED-benet,
- har signaltråd och motståndsledare i olika höjd utan pedagogisk anledning,
- gör GND-vägen svår att följa,
- har etiketter som ser klippta, trånga eller felplacerade ut,
- skiljer sig visuellt från tidigare fungerande kopplingsbilder utan tydlig anledning.

## Rekommenderad kontrollfråga före PDF

Innan PDF byggs bör följande fråga besvaras:

> Kan ett barn följa vägen med fingret från GPIO till långt ben, från kort ben till motstånd och från motstånd till GND utan att behöva gissa?

Om svaret är nej ska bilden förenklas eller justeras.
