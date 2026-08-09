# Steg 1 – Säkerhet och kompatibilitet

## Grundprincip

ESP32 DevKit använder normalt **3,3V-logik**. Det betyder att ingångar på ESP32 inte bör utsättas för 5V-signaler.

Detta påverkar valet av moduler och hur vissa komponenter kopplas.

---

# Viktiga regler

## 1. Motorer får inte drivas direkt från ESP32

Motorer, servon och reläer ska inte drivas direkt från GPIO-pinnar.

Använd:

- separat matning vid behov,
- motordrivare,
- gemensam jord,
- rimliga strömgränser.

## 2. LED ska ha motstånd

Vanliga lysdioder ska normalt kopplas med seriemotstånd.

Rekommenderade startvärden:

- 220Ω
- 330Ω
- 1kΩ

## 3. HC-SR04 kräver kontroll

Många HC-SR04-moduler drivs med 5V och kan ge 5V på Echo-pinnen.

För ESP32 bör boken antingen:

- använda en 3,3V-kompatibel avståndssensor,
- eller visa enkel nivådelning på Echo-signalen,
- eller tydligt ange att vuxen ska kontrollera kopplingen.

## 4. I²C-moduler bör kontrolleras

OLED, RTC och vissa sensorer använder I²C.

Kontrollera:

- SDA/SCL-pinnar,
- spänningsnivå,
- I²C-adress,
- att pullup-motstånd inte drar signalen till 5V.

## 5. MicroSD-moduler varierar

Alla MicroSD-moduler är inte lika bra för 3,3V-system. Makerlådan bör ange att modulen ska vara ESP32-kompatibel.

## 6. Reläer och nätspänning undviks

Boken ska inte innehålla experiment med 230V. Om relä används ska det endast styra lågspänningslaster i pedagogiskt syfte.

---

# Rekommenderad säkerhetsruta i boken

> Koppla ur USB-kabeln innan du ändrar kopplingen.  
> Kontrollera plus och minus innan du ansluter ström.  
> Motorer och starkare laster ska aldrig kopplas direkt till ESP32-pinnar.  
> En vuxen bör kontrollera kopplingen innan experimentet startas.

---

# Komponenter som bör få särskild varning

| ID | Komponent | Notering |
|---|---|---|
| S02 | HC-SR04 | Echo kan vara 5V på vissa moduler |
| M01 | SG90 servo | Kan dra mer ström än ESP32-kortets USB-matning klarar |
| M02 | Stegmotor + ULN2003 | Kräver separat motorström vid belastning |
| M03 | DC-motor | Får inte kopplas direkt till GPIO |
| M04 | L9110S motordrivare | Kontrollera motor- och logikmatning |
| D04 | MicroSD-modul | Välj ESP32-/3,3V-kompatibel modul |
