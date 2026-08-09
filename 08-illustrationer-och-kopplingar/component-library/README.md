# Komponentbibliotek för illustrationer

Detta är ett lättviktigt komponentbibliotek för ESP32 Experimentbok.

Biblioteket är i v68 ett **manuellt designbibliotek**, inte en automatisk genereringsmotor. Syftet är att ge ett gemensamt bildspråk när nya illustrationer skapas, särskilt från E005 och framåt.

## Mappstruktur

```text
component-library/
  README.md
  design-principles.md
  components/
  patterns/
  examples/
```

## Tanken

- `components/` innehåller återanvändbara grundkomponenter, till exempel LED, motstånd och pilar.
- `patterns/` innehåller återanvändbara layoutmönster, till exempel sekvenssteg och komponentkort.
- `examples/` visar hur komponenter och patterns kan användas i bilder som liknar bokens faktiska illustrationer.

## Arbetsprincip

När en ny illustration ska skapas:

1. välj relevant pattern,
2. kopiera in eller utgå från rätt komponenter,
3. placera och skala komponenterna,
4. använd samma färger, linjetjocklekar och textprinciper,
5. spara den färdiga bilden i `generated/E00X/`.

## Viktig avgränsning i v68

v68 uppdaterar inte automatiskt befintliga bilder i E001–E004. Den skapar ett underlag för konsekventare framtida illustrationer.

## Tillägg efter v68

- `components/led-on-blue.svg` lades till i samband med E005.
