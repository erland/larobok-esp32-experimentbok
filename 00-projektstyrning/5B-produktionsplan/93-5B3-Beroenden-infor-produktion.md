# 5B.3 – Beroenden inför produktion

## Syfte

Detta dokument pekar ut beroenden som påverkar skrivordningen.

## Kritiska beroendekedjor

```text
LED → RGB → statusfärg → sensorstatus → smarta prylar
```

```text
Knapp → tillstånd → spel → kodlås → skattkista/RFID
```

```text
Seriell monitor → analogRead → tröskelvärden → kalibrering → miljöprojekt
```

```text
OLED första text → sensorvärde på OLED → instrumentpanel → väderloggare
```

```text
Servo första rörelse → servo styrs av sensor → skattkista → RFID-skattkista
```

```text
Motor första snurr → motordrivare → två motorer → hinderrobot
```

## Produktionsregel

Ett experiment får inte skrivas slutligt förrän dess centrala föregångare har minst status:

- Textutkast
- Kodutkast
- Preliminär breadboardbild
