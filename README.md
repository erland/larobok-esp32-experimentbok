# ESP32 Experimentbok – Projektpaket

Detta projektpaket innehåller planeringsmaterial för en experimentbok med ESP32, breadboard och billiga standardkomponenter för barn 7–12 år tillsammans med vuxen.

## Aktuell status

| Område | Status |
|---|---|
| Steg 0 – Bokens designprinciper | Klart |
| Steg 1 – Standardiserad experimentlåda | Klart |
| Steg 2 – Färdighetskarta | Klart |
| Steg 3 – Experimentbank | Klart som bruttolista: E001–E120 |
| Steg 4 – Beroendegraf och experimentmatris | Klart |
| Steg 5 – Kapitelstruktur | Nästa steg |
| Steg 6 – Komponentoptimering | Ej påbörjat |
| Steg 7 – Experimentmall och pedagogik | Delvis påbörjat |
| Steg 8 – Produktion av experiment | Ej påbörjat |
| Steg 9 – Illustrationer och kopplingar | Ej påbörjat |
| Steg 10 – Bokproduktion | Ej påbörjat |

## Rekommenderad nästa åtgärd

Fortsätt med:

> **Steg 3 – Experimentbanken**

Där definieras vilka elektronik-, programmerings- och problemlösningsfärdigheter boken ska bygga upp.


Senaste genomförda steg: **4.5 Kvalitetsoptimering**.


Nya styrdokument:
- 00-Projektmanifest.md
- 01-AI-Development-Guide.md

Steg 5.1 genomfört: övergripande bokstruktur framtagen.

Steg 5.2 genomfört: kapitelindelning fastställd.

Kapiteldesign Omgång 2 genomförd: Kapitel 5–7 tillagda.

Kapiteldesign Omgång 3 genomförd: Kapitel 8–10 tillagda.

Kapiteldesign Omgång 4 genomförd: Kapitel 11–14 tillagda. 5A.1 är komplett.

5A.2 genomfört: breadboard-progression, återanvändningsmatris och illustrationskonsekvenser tillagda.

v25.1 genomfört: `90-Kapiteloversikt.md` och `91-Kapiteldesign-principer.md` har fördjupats som produktionsstyrdokument.

v25.2 genomfört: Kapitel 1–2 har fördjupats till samma kapiteldesignnivå som senare kapitel.

v25.3 genomfört: Kapitel 3–4 har fördjupats och 5A.1 har fått slutlig konsistenskontroll.

5A.3 genomfört: komponentlivscykel, komponentintroduktion per kapitel och rekommendationer för komponentlådan tillagda.

5A.4 genomfört: illustrationsplan, bildkö, komponentbildlista och standard-breadboardbilder tillagda.

5A.5 genomfört: kodprogression, bibliotek, kodstil och kodkonceptmatris tillagda.

5A.6 genomfört: pedagogisk rytm, wow-faktor, motivationskurva, tempo och teori/praktik-balans tillagda.

5B.1 uppgraderad: produktionsmatrisen är nu ifylld med experimentdata, kapitel, spår, kodnivå, wow-faktor, komponenter och produktionsstatusfält.

5B.2 genomfört: experimentmall, skrivregler, checklista och exempelstruktur tillagda.

5B.2.1 genomfört: experimentmallen har uppdaterats med pedagogisk experimentcykel.

5B.3 genomfört: produktionsordning, produktionsblock, produktionskö och beroenden inför produktion tillagda.

5B.4 genomfört: kvalitetssäkring, teknisk/pedagogisk granskning, testplan och säkerhetsgranskning tillagda.

5B.5 genomfört: produktionspipeline, arbetsflöde, filstruktur, roller och produktionsstart-checklista tillagda.

6.1.1 pilotrevision genomförd: E001–E002 har fördjupats som guldstandard för experimentproduktion.

5B.6 Del A genomfört: berättarröst, läsupplevelse och emotionell progression tillagda.

5B.6 Del B genomfört: wow-kurva, storytelling-regler och visuellt berättande tillagda.

5B.6 Del D genomfört: kontrollista och slutstatus tillagda.

6.1.1 uppdaterad: E001 har reviderats enligt hela 5B.6 och markerats som guldstandard-kandidat.

6.1.1 uppdaterad: E001 har granskats och finjusterats enligt 5B.6.

Stabilisering v45 genomförd: 5B.6 Del C har återinförts och fördjupats, Del D har stärkts och v44:s reviderade E001 har behållits.

v46: E001 har fått teknisk och 5B.6-språklig finjustering. GPIO är ändrad till 23, kopplingsvägen är förtydligad och illustrationsbrief har skapats.

v47: E002 har reviderats enligt stabiliserad 5B.6 och anpassats till E001/v46-nivån. E001 och E002 är nu guldstandard-kandidater.

v48: Bild- och kopplingspipeline för E001–E002 har etablerats med circuit.yaml, Wokwi-diagram, bildprompter, briefs och första SVG-bilder.

v49: Första kompletta SVG-bildpaket för E001–E002 har skapats.

v50: SVG-bildpaketet har justerats efter granskning. Kopplingsöversikterna är förenklade utan breadboard och förvirrande bilder har arkiverats.

v51: Kopplingsöversikterna har förenklats ytterligare. Stora textrutor är borttagna och endast 'Långt ben'/'Kort ben' markeras.

v52: E001/E002 har explicita bildreferenser i markdown och 'Tänk på'-rutorna har ersatts av diskretare Insikt-rader i huvudflödet.


v53 genomfört: E003 – Två LED turas om har skapats som 5B.6-anpassat manusutkast med kod, kopplingsspecifikation, Wokwi-diagram, bildbrief och genererade SVG-bilder.

v54 genomfört: E003 har finjusterats mot E001/E002-standard. Kopplingsöversikten har ritats om så GPIO 23/GPIO 22 tydligt går till respektive LED-lampas långa ben, och manus har fått mindre språkputs samt en kort LED-polaritetspåminnelse.


v55 genomfört: E004 – Mini-trafikljus har skapats som 5B.6-anpassat manusutkast med kod, kopplingsspecifikation, Wokwi-diagram, bildbrief, bildprompter och genererade SVG-bilder. E004 är markerad som utkast/pågår; fysisk test, teknisk granskning, pedagogisk granskning och PDF-layoutgranskning återstår.


v56 genomfört: E004 – Mini-trafikljus har finjusterats. Gult betyder nu konsekvent 'vänta', trafikljusmodellen förklaras tydligare som en förenklad modell, manus har fått lätt textputs och E004-C/bildprompter har uppdaterats.

v57 genomfört: Ledtrådsbilderna har tagits bort ur manus för E002–E004 och kopplingsöversikterna för E003/E004 har ritats om med parallell radstruktur utan korsande linjer.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.


Senaste uppdatering: v104 – E016 har fått lätt pedagogisk och bildmässig puts: mildrat andas-språk, lugnare loop-pil och mer luft i E016-D.
