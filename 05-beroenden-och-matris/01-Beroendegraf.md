# Steg 4 – Beroendegraf

## Syfte

Detta är en textbaserad första beroendeöversikt. Den visar vilka experiment som uttryckligen bygger på tidigare experiment. Den kan senare göras om till en visuell graf.

## Beroendelista

| Experiment | Bygger på |
|---|---|
| E001 | - |
| E002 | E001 |
| E003 | E001 |
| E004 | E003 |
| E005 | E003 |
| E007 | E004 |
| E008 | E007 |
| E009 | E008 |
| E010 | E009 (parkerad) |
| E011 | E008 |
| E012 | E011 |
| E013 | E012 |
| E014 | E012/E013 |
| E015 | E012/E001 |
| E016 | E015 |
| E017 | E015 |
| E018 | E017 |
| E019 | E015, E018 |
| E020 | E016 |
| E021 | E002 |
| E022 | E021 |
| E023 | E008, E013 |
| E024 | E014 |
| E025 | E001–E024 |
| E026 | E001 |
| E027 | E026 |
| E028 | E027 |
| E029 | E027 |
| E030 | E014, E026 |
| E031 | E026 |
| E032 | E028, E031 |
| E033 | E001 |
| E034 | E033 |
| E035 | E010, E033 |
| E036 | E031, E033 |
| E037 | E033 |
| E038 | E029, E037 |
| E039 | E028, E007 |
| E040 | E028 |
| E041 | E021, E028 |
| E042 | E041, E033 |
| E043 | E042 |
| E044 | E036, E039 |
| E045 | E008, E039 |
| E046 | E034 |
| E047 | E021, E046 |
| E048 | E028 |
| E049 | E031 |
| E050 | E026–E049 |
| E051 | E018 |
| E052 | E017, E051 |
| E053 | E051 |
| E054 | E021 |
| E055 | E034, E054 |
| E056 | E024, E054 |
| E057 | E054 |
| E058 | E035 |
| E059 | E032, E058 |
| E060 | E047 |
| E061 | E060 |
| E062 | E051 |
| E063 | E062 |
| E064 | E024, E062 |
| E065 | E062 |
| E066 | E065 |
| E067 | E058 |
| E068 | E067, E034 |
| E069 | E051 |
| E070 | E069, E024 |
| E071 | E051 |
| E072 | E029, E071 |
| E073 | E071, E023 |
| E074 | E051–E073 |
| E075 | E051–E074 |
| E076 | E001 |
| E077 | E051, E076 |
| E078 | E029, E076 |
| E079 | E063, E077 |
| E080 | E041, E076 |
| E081 | E076 |
| E082 | E081 |
| E083 | E049, E082 |
| E084 | E013 |
| E085 | E047, E084 |
| E086 | E041, E084 |
| E087 | E015 |
| E088 | E087 |
| E089 | E056, E087 |
| E090 | E032, E087 |
| E091 | E063, E087 |
| E092 | E067, E087 |
| E093 | E017, E076, E084 |
| E094 | E070, E076 |
| E095 | E063, E084 |
| E096 | E058, E067, E078 |
| E097 | E078, E088 |
| E098 | E036, E084 |
| E099 | E032, E090, E098 |
| E100 | E076–E099 |
| E101 | E087 |
| E102 | E101 |
| E103 | E101, E088 |
| E104 | E062, E101 |
| E105 | E102 |
| E106 | E055, E105 |
| E107 | E087 |
| E108 | E107 |
| E109 | E076 |
| E110 | E032, E109 |
| E111 | E090, E110 |
| E112 | E028 |
| E113 | E024, E112 |
| E114 | E087, E112 |
| E115 | E076 |
| E116 | E115 |
| E117 | E062 |
| E118 | E115, E117 |
| E119 | E021 |
| E120 | E001–E119 |

## Grov progression

```text
E001–E025  Grundläggande LED, färg, PWM och ljus
    ↓
E026–E050  Knappar, ljud och spel
    ↓
E051–E075  Sensorer och mätning
    ↓
E076–E100  Displayer, servo och smarta uppfinningar
    ↓
E101–E120  Robotik, RFID, datalogging, WiFi och Maker
```

## Notering

Flera beroenden anges som intervall, exempelvis `E001–E024`. Dessa bör brytas ned mer exakt när experimenten väljs ut för slutlig bokstruktur.
