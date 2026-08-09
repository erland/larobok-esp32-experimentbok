# 5B.5 – Filstruktur för produktion

## Rekommenderad struktur

```text
07-experimentutkast/
  kapitel-01/
    E001-forsta-blinket.md
    E002-led-med-egen-rytm.md
  kapitel-02/
    ...
08-illustrationer-och-kopplingar/
  komponenter/
  breadboard/
  systembilder/
  projektbilder/
09-bokproduktion/
  manus/
  layout/
  epub/
  pdf/
```

## Namngivning

Experimentfiler:

```text
E0XX-kortnamn.md
```

Illustrationer:

```text
fig-kapitel-experiment-typ-kortnamn.svg
```

Kodfiler vid behov:

```text
E0XX-kortnamn.ino
```

## Regel

Markdownfilen är huvudkällan. Kod och bilder är stödartefakter som refereras från markdown.
