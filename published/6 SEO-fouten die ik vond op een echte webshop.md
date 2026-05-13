---
status: published
date: 2026-05-13
url: https://blog.snelstack.com/6-seo-fouten-die-ik-vond-op-een-echte-webshop/
---

# 6 SEO-fouten die ik vond op een echte webshop

SEO blijft belangrijk. In 2026, in 2027, daarna ook nog. Zolang mensen dingen opzoeken op Google, wil je gevonden worden.

Maar wat ik keer op keer zie: de meeste bedrijven doen het fout. Niet omdat ze het niet willen, maar omdat ze het simpelweg niet weten.

Ik bouw WordPress-websites voor bedrijven. Meer dan 10 jaar. Elke keer als ik een bestaande website analyseer, kom ik dezelfde fouten tegen. In dit artikel laat ik je de 6 meest voorkomende zien, aan de hand van een echte klant: Antiquewarehouse.

---

## Fout 1: Geen HTTPS

Dit is het laagste hangende fruit en toch gaat het nog steeds fout.

Als je website geen HTTPS heeft, krijgen bezoekers een beveiligingswaarschuwing te zien voordat ze op je website komen. De meeste mensen klikken direct weg. Google ook — want een onbeveiligde website rankt lager.

Bij Antiquewarehouse was dit het geval. De oude website draaide nog op HTTP. Dat betekent: elke bezoeker die op een Google-resultaat klikte, kreeg eerst een rode waarschuwingspagina te zien.

Fix: HTTPS instellen via je hosting. Duurt 10 minuten.

---

## Fout 2: Generieke meta descriptions op elke pagina

De meta description is de tekst die je onder een link ziet in Google. Die bepaalt voor een groot deel of iemand klikt of niet.

Bij Antiquewarehouse stond op elke pagina exact dezelfde meta description. Homepagina, categoriepagina's, productpagina's — allemaal hetzelfde. Google koos dan zelf maar een stuk tekst van de pagina, en dat is zelden iets dat mensen overtuigt om te klikken.

Je wilt voor elke pagina een unieke meta description die aansluit bij wat iemand zoekt. Een bezoeker die zoekt op "antieke Franse tafel" wil een meta description zien over antieke Franse tafels, niet een generieke zin over je webshop.

Dit kun je instellen via Yoast SEO of via mijn eigen Snel SEO plugin. Snel SEO kan de meta description ook automatisch genereren op basis van de content van je pagina, zodat je dit niet handmatig hoeft te doen voor honderden producten.

---

## Fout 3: ID-gebaseerde URLs

De oude website van Antiquewarehouse had URLs als `/producten/show/2443`. Dat ID is intern handig, maar voor Google zegt het niets. En voor hackers zegt het wél iets.

Als je URL een product-ID bevat, kunnen kwaadwillenden dat ID gebruiken om je database te benaderen. Ze weten de structuur, ze weten het ID — dat is een aanvalsvector die je niet wil.

Betere URL: `/antieke-franse-tafel`. Google weet direct waar de pagina over gaat. Hackers hebben geen ID. En je klanten kunnen de URL gewoon lezen.

---

## Fout 4: Geen redirects bij de migratie

Dit is de fout die de meeste geld kost en de minste aandacht krijgt.

Stel: je laat een nieuwe website bouwen. De URL-structuur verandert. Je oude URL `/producten/show/2443` wordt `/antieke-franse-tafel`. Wat denk je dat er gebeurt met alle Google-rankings die je voor die oude URL had opgebouwd?

Die verdwijnen. Tenzij je een redirect instelt.

Een redirect stuurt Google én bezoekers automatisch door van de oude URL naar de nieuwe. Zonder redirect bouw je je rankings opnieuw op vanaf nul.

Voor Antiquewarehouse heb ik 2.026 redirects ingesteld — programmatisch, omdat je dat niet handmatig doet voor 2.000 producten. Meeste SEO-plugins rekenen hier extra voor. Ik doe het standaard.

---

## Fout 5: Geen structured data (JSON-LD)

Structured data is informatie die je aan Google geeft over wat er op je pagina staat. Niet in tekst, maar in een gestructureerd formaat dat Google direct kan lezen.

Zonder structured data ziet Google: een pagina met tekst.
Met structured data ziet Google: dit is een product, het kost €149, het is op voorraad, het merk is X.

Dat levert rich snippets op in de zoekresultaten — zoekresultaten met prijs en beschikbaarheid direct zichtbaar. Die trekken meer clicks zonder dat je hoger hoeft te ranken.

En het wordt steeds belangrijker. AI-platformen gebruiken structured data om relevante websites aan te bevelen. Als jouw website geen JSON-LD heeft, mis je die traffic.

---

## Fout 6: Duplicate content over pagina's

Elke pagina op je website moet unieke content hebben. Dat klinkt logisch, maar in de praktijk zie ik het regelmatig fout gaan: dezelfde introductietekst op de homepagina staat ook op categoriepagina's, of productomschrijvingen worden gekopieerd.

Google straft duplicate content met lagere rankings. Hij weet niet welke pagina hij moet tonen, dus toont hij ze allebei minder. Je verliest rankings op pagina's die je juist wilt laten scoren.

Bij Antiquewarehouse was dit gelukkig niet het geval. Elke categoriepagina had een eigen beschrijving. Maar ik vermeld het hier omdat ik het bij andere websites wél tegenkom, en het een makkelijke fout is om te maken als je snel content toevoegt.

---

## Hoe je dit zelf checkt

Je hoeft geen developer te zijn om dit te controleren:

- **HTTPS:** Kijk of je URL begint met `https://`. Begint het met `http://`? Dan is er een probleem.
- **Meta descriptions:** Zoek op Google naar je bedrijfsnaam. Wat staat er onder je link? Is het uniek per pagina?
- **URL structuur:** Staan er cijfers of IDs in je URLs? Dan is het tijd voor een schonere structuur.
- **Structured data:** Gebruik Google's Rich Results Test om te zien of je website structured data heeft.

---

Heb je een WordPress-website en weet je niet zeker of dit goed staat? [Neem contact op](mailto:snelstack@gmail.com) — ik kijk het gratis door.
