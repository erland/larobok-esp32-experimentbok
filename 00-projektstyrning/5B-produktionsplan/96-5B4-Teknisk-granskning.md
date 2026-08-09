# 5B.4 – Teknisk granskning

## Syfte

Teknisk granskning säkerställer att koppling, kod och komponentval är rimliga.

## Checklista

- [ ] Rätt komponenter används.
- [ ] GPIO-pinnar är lämpliga för ESP32.
- [ ] LED har motstånd där det behövs.
- [ ] GND är gemensam.
- [ ] 3,3V/5V-risker är markerade.
- [ ] Motorer drivs via motordrivare, inte GPIO.
- [ ] Servo har rimlig strömnotering.
- [ ] I²C/SPI-pinnar är konsekventa.
- [ ] Bibliotek är angivna där de behövs.
- [ ] Kod och koppling stämmer överens.

## Särskild kontroll

| Område | Kontroll |
|---|---|
| HC-SR04 | Echo-signal och ESP32-kompatibilitet |
| Servo | ström och mekanisk belastning |
| DC-motor | motordrivare och extern ström vid behov |
| MicroSD | 3,3V-kompatibilitet |
| WiFi | tydliga vuxensteg |
| Vatten/jordfukt | vuxenstöd och försiktighet |
