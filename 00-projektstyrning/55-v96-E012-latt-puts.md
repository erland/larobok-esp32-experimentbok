# v96 – Lätt pedagogisk och bildmässig puts av E012

Denna version behåller E012:s grundidé, koppling och kodstruktur, men putsar språk och bilder.

## Textändringar i E012

- `0` beskrivs nu som `inget ljus` i stället för `nästan inget ljus`.
- `setColor()` introduceras tidigare som färgrecept.
- `analogWrite()` beskrivs som något som används inuti färgreceptet.
- Vuxenrutorna förtydligar att projektet behöver ett tekniskt beslut om faktisk ESP32-PWM-implementation innan slutversion.
- Den pedagogiska 0–255-modellen behålls som mål.

## Bildändringar

- E012-D har fått mer barnnära språk:
  - `lite på`
  - `mer på`
  - `mest på`
- E012-D:s slutsats ändrades till:
  > Högre tal gör ljuset starkare.
- E011-A och E012-A fick en mikroputs så RGB-LED-etiketten får lite mer luft.

## Oförändrat

- E012:s koppling är oförändrad.
- E012:s pedagogiska huvudidé är oförändrad.
- E012 använder fortsatt `setColor(red, green, blue)` och 0–255-värden.
