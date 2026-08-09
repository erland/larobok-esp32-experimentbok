# v56 – E004 finjustering

## Syfte

Finjustera E004 – Mini-trafikljus mot E001/E002-standard efter granskning, utan att ändra experimentets huvudidé eller tekniska koppling.

## Genomförda ändringar

- Manus har putsats varsamt för bättre tempo och mindre upprepning.
- Trafikljuset beskrivs tydligare som en förenklad modell där bara en färg lyser i taget.
- Gult betyder nu konsekvent **vänta**.
- Formuleringar som **gör dig redo** och **snart stopp** har tagits bort från E004-manus, kodkommentarer, bildprompt och sekvensbild.
- E004-C-trafikljussekvens.svg har uppdaterats så båda gula faserna märks med **vänta**.
- Bildbrief och bildprompter har synkats med den uppdaterade betydelsen för gult.

## Ej ändrat

- Kopplingsprincipen är oförändrad: varje LED har egen GPIO och eget motstånd till GND.
- GPIO-val är oförändrade: röd GPIO 23, gul GPIO 22, grön GPIO 21.
- Kodens förenklade sekvens är oförändrad: rött → gult → grönt → gult → omstart.
- E004 är fortsatt markerad som utkast/pågår.

## Kvar att göra

- Fysisk breadboardtest.
- Teknisk granskning mot circuit.yaml och Wokwi.
- Pedagogisk granskning mot 5B.6.
- PDF-layoutgranskning, särskilt E004-B och E004-D i faktisk tryckstorlek.
