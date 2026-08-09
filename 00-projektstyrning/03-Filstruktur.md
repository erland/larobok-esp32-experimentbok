# Filstruktur

## Syfte

Filstrukturen är organiserad för att det ska vara lätt att se var i processen projektet befinner sig och var nytt material ska placeras.

---

# Struktur

```text
ESP32_Experimentbok_Projekt/
├── README.md
├── 00-projektstyrning/
│   ├── 01-Projektplan.md
│   ├── 02-Status-och-beslutslogg.md
│   └── 03-Filstruktur.md
├── 01-designprinciper/
│   └── 00-Bokens-designprinciper.md
├── 02-komponentlada/
│   ├── 01-Standardiserad-experimentlada.md
│   ├── 02-Komponent-ID-och-nyttopoang.md
│   ├── 03-Inkopslista-per-niva.md
│   ├── 04-Komponentpass.md
│   ├── 05-Mall-komponentruta-for-experiment.md
│   ├── 06-Steg-1-slutstatus.md
│   ├── 07-Kostnadsoversikt-v1.md
│   ├── 08-Sakerhet-och-kompatibilitet.md
│   └── 09-Inkopschecklista.md
├── 03-fardighetskarta/
├── 04-experimentbank/
├── 05-beroenden-och-matris/
├── 06-kapitelstruktur/
├── 07-experimentutkast/
├── 08-illustrationer-och-kopplingar/
├── 09-bokproduktion/
└── 99-arkiv/
```

---

# Regler för fortsatt arbete

## 1. Projektstyrning

Plan, status, beslut och arbetsordning läggs i:

- `00-projektstyrning/`

## 2. Designprinciper

Övergripande principer som ska styra hela boken läggs i:

- `01-designprinciper/`

## 3. Komponentlådan

Allt om komponenter, inköp, kostnader, komponentpass och säkerhetsnoteringar läggs i:

- `02-komponentlada/`

## 4. Kommande planeringssteg

Färdighetskarta, experimentbank, beroenden och kapitelstruktur har egna mappar även innan de är fyllda.

## 5. Experimentproduktion

Färdiga eller halvfärdiga experiment läggs i:

- `07-experimentutkast/`

När kapitelstrukturen är klar kan undermappar skapas, exempelvis:

- `07-experimentutkast/kapitel-01-ljus-och-lampor/`
- `07-experimentutkast/kapitel-02-knappar-och-spel/`

## 6. Arkiv

Äldre versioner, bortvalda listor eller material som inte längre gäller kan flyttas till:

- `99-arkiv/`
