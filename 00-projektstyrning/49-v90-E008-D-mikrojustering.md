# v90 – Mikrojustering av E008-D

Denna version gör en mycket liten konsekvensjustering i E008-D.

## Ändring

Kodraden i bilden ändrades från:

```cpp
ledPins[] = {23, 22, 21, 19};
```

till:

```cpp
int ledPins[] = {23, 22, 21, 19};
```

## Varför

Manuset använder raden med `int`, och bilden ska visa samma kodrad för att undvika onödig skillnad mellan bild och text.

## Berörda filer

- `08-illustrationer-och-kopplingar/generated/E008/E008-D-lista-och-loop.svg`
- `08-illustrationer-och-kopplingar/generated/E008/E008-D-lista-och-loop.png`

## Oförändrat

- Manus är oförändrat.
- Koppling och kod är oförändrade.
- Layoutidén från v89 är oförändrad.
