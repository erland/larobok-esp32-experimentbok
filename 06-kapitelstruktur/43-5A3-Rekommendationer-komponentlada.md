# 5A.3 – Rekommendationer för komponentlådan

## Sammanfattning

Komponentlådan fungerar överlag väl, men livscykelanalysen pekar på några viktiga designbeslut.

---

# Baslådan

Baslådan är stark och bör vara huvudspåret i bokens första halva.

## Behåll som kärna

| ID | Komponent | Motivering |
|---|---|---|
| E01 | ESP32 DevKit | permanent bas |
| B01/B02/B03 | breadboard och kablage | permanent bas |
| R01 | motstånd | används genom hela boken |
| L01 | LED | första output och återkommande felsökning |
| L02 | RGB-LED | central statuskomponent |
| K01 | knapp | central input |
| A01 | buzzer | central feedback |
| S01 | LDR | billig och pedagogisk analog sensor |
| S02 | HC-SR04 | stark wow-faktor och många tillämpningar |
| D01 | OLED | gör projekt användbara och bör ligga i Bas/Plus beroende på budget |

## Möjlig justering

OLED är relativt avancerad men mycket värdefull. Den kan ligga kvar i Baslådan om boken vill kännas modern, men kan också markeras som “Bas+” om budgeten ska pressas.

---

# Pluslådan

Pluslådan ger tydligt mervärde.

## Starka Plus-komponenter

| ID | Komponent | Motivering |
|---|---|---|
| S05 | DHT22 | tydliga miljöprojekt |
| S07 | PIR | larm och smarta hem |
| L03 | NeoPixel-ring | hög wow-faktor |
| D02 | LED-matris | spel och animation |
| M01 | SG90 servo | mycket stark makerkomponent |
| K03 | TTP229 touch | rolig men bör vara bonus |

## Rekommendation

Pluslådan bör markeras som den nivå där projekten börjar kännas som “riktiga smarta prylar”.

---

# Makerlådan

Makerlådan bör vara frivillig fördjupning.

## Behåll men gör frivilligt

| ID | Komponent | Rekommendation |
|---|---|---|
| C01 | RFID | mycket rolig, men sen fördjupning |
| C02 | IR | bra vardagskoppling |
| D03 | RTC | användbar för datalogging |
| D04 | MicroSD | bra men tekniskt känslig |
| M03/M04 | DC-motor + drivare | robotik men kräver vuxenstöd |
| M02 | stegmotor | bör vara bonus, inte huvudspår |

---

# Riskkomponenter

Följande komponenter kräver extra tydliga säkerhets- eller felsökningsrutor:

| Komponent | Risk |
|---|---|
| HC-SR04 | Echo kan vara 5V på vissa moduler |
| Servo | kan dra mer ström än USB/ESP32 klarar |
| DC-motor | får inte drivas direkt från GPIO |
| MicroSD | modulkompatibilitet och filsystem |
| WiFi | nätverksstrul kan skapa frustration |
| DS18B20 i vatten | kräver vuxenkontroll vid vattennära experiment |

---

# Huvudspår kontra bonus

## Bör vara huvudspår

- LED
- RGB
- knapp
- buzzer
- LDR
- HC-SR04
- OLED
- DHT22
- PIR
- servo

## Kan vara bonus/fördjupning

- touchsensor
- LED-matris
- stegmotor
- RFID
- IR
- RTC
- MicroSD
- WiFi
- DC-motor/robotik

Det betyder inte att de ska tas bort, utan att boken bör kunna ge en bra resa även om familjen inte köper Makerlådan från början.

---

# Rekommendation inför nästa steg

I 5A.4 Illustrationsplan bör varje komponent få en standardiserad bildtyp:

- komponentfoto/ikon,
- breadboardintroduktion,
- vanlig felkoppling,
- typisk användning i projekt.

Detta är särskilt viktigt för komponenter som återkommer många gånger.
