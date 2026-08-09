# 5A.5 – Kodprogression per kapitel

| Kapitel | Kodnivå | Nya kodidéer | Viktiga återkomster |
|---:|---|---|---|
| 1 | Nybörjare | `setup()`, `loop()`, `pinMode()`, `digitalWrite()`, `delay()` | pin-namn, små ändringar |
| 2 | Nybörjare+ | variabler, PWM, enkel `for` | LED-sekvenser, färgvärden |
| 3 | Grund | `digitalRead()`, `INPUT_PULLUP`, `if`, booleska lägen | LED/RGB-status |
| 4 | Grund+ | toner, slump, arrayer, spelstatus | knapp, LED, buzzer |
| 5 | Mellan | `analogRead()`, tröskelvärden, sensorfunktioner | Seriell monitor, statusfärg |
| 6 | Mellan | digitala sensorer, larmstatus, enkel filtrering | buzzer/RGB som larm |
| 7 | Mellan+ | bibliotek, kalibrering, flera mätvärden | OLED/statusfärg |
| 8 | Mellan+ | OLED-text, skärmlägen, enkel meny | sensorvärden |
| 9 | Mellan+ | pixel-arrayer, animation, loop över pixlar | färg och spel |
| 10 | Avancerad | servo-bibliotek, `map()`, kombinationslogik | sensorer, status, tillstånd |
| 11 | Avancerad | motorfunktioner, PWM för motor, robotbeslut | HC-SR04, säkerhet |
| 12 | Avancerad | ID-jämförelse, fjärrkommandon, `switch` | servo/RGB/buzzer |
| 13 | Avancerad+ | tid, filskrivning, WiFi, webbserver | OLED, sensorvärden |
| 14 | Projekt | funktioner, stegvis projektkod | alla tidigare mönster |

## Viktiga kapitelövergångar

### Kapitel 1 till 2

Barnet går från enkel digital output till fler LED och PWM. Kod ska fortfarande vara kort och direkt.

### Kapitel 2 till 3

Barnet går från output till input. `digitalRead()` och `if` blir centrala.

### Kapitel 3 till 4

Input används i spel. Koden börjar hantera regler, slump och sekvenser.

### Kapitel 4 till 5

Barnet går från knappvärden till sensorvärden. Seriell monitor blir viktigt verktyg.

### Kapitel 7 till 8

Bibliotek och OLED gör koden längre. Därför ska första OLED-exemplet vara extremt litet.

### Kapitel 10 till 11

Motorer introduceras. Kod och säkerhet måste hänga ihop: motordrivare, funktioner och tydliga stopp-lägen.

### Kapitel 13 till 14

Inga nya kodkrav ska införas. Fokus är att kombinera tidigare kodmönster.
