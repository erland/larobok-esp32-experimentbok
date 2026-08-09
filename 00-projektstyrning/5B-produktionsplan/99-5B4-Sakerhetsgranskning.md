# 5B.4 – Säkerhetsgranskning

## Syfte

Säkerhetsgranskningen ska säkerställa att boken är trygg för barn och familjer.

## Bindande säkerhetsregler

- Ingen nätspänning.
- Inget krav på lödning i huvudspåret.
- Ingen litiumladdning.
- Motorer kopplas aldrig direkt till GPIO.
- Koppla ur USB vid större ombyggnad.
- Vattennära experiment kräver vuxenstöd.
- Makerlådan kräver tydligare vuxenmarkering.

## Säkerhetsmarkeringar

| Markering | Användning |
|---|---|
| Vuxenkoll | En vuxen bör kontrollera innan test |
| Strömkoll | Risk för för hög ström |
| Spänningskoll | Risk 5V/3,3V |
| Mekanikkoll | Servo/motor kan fastna |
| Nätverkskoll | WiFi kräver vuxenstöd |

## Experiment som alltid behöver vuxenruta

- HC-SR04 om Echo är 5V.
- Servo med mekanisk belastning.
- DC-motor och motordrivare.
- Robotik.
- MicroSD och WiFi.
- Vatten- eller jordfuktighetsprojekt.
