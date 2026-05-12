# 7 SEO fouten die je maakt en hoe AI kan helpen

Na tientallen websites te hebben gemaakt voor ondernemers en een persoonlijk portfolio van meer dan 500 projecten te hebben opgebouwd (grootste deel persoonlijke projecten), zie ik dezelfde technische fouten opnieuw en opnieuw. Fouten die direct of indirect invloed hebben op je SEO-score.

In dit artikel ga ik de 7 fouten bespreken die ik bijna overal zie, plus de AI-fixes die je per fout kunt toepassen om het probleem sneller en efficiënter op te lossen.

Maar voordat we verder gaan: wie ben ik, en waarom zou je überhaupt naar een woord luisteren van wat ik te zeggen heb? Ik ben Loc, software-ontwikkelaar met meer dan 10 jaar ervaring. En bij die 10 jaar moet ik wel benadrukken dat ik het grootste deel van mijn carrière echt dagelijks achter de code heb gezeten.

Daarnaast heb ik zelf hele software-architecturen van begin tot eind gebouwd, een UX/UI-designopleiding gedaan, marketing-kennis opgedaan (150 miljoen impressies op social media), en werk ik samen met mijn broertje die SEO-professional is.

Genoeg over mij. Laten we de 7 SEO-fouten doornemen. Als concreet voorbeeld gebruik ik mijn recente werk voor een antiekwinkel genaamd Antiquewarehouse [link].

## 1. Geen HTTPS

Dit was voor mij een verrassing toen ik met mijn eigen B2B-softwarebedrijf begon: hoeveel websites nog op de onbeveiligde HTTP-technologie draaien. Voor degenen die niet weten wat het verschil is tussen HTTP en HTTPS, of überhaupt niet weten wat dat inhoudt:

Je hoeft niet te weten wat het precies doet, maar dat kleine verschil in de letter 's' betekent een hele hoop. Die 's' staat voor security, en als je die niet hebt, is je website onbeveiligd. Verder hoef je eigenlijk niks te weten.

Google zal je zwaar bestraffen als je website onbeveiligd is. En niet alleen dat. Mensen krijgen ook nog eens een waarschuwingsscherm te zien voor ze überhaupt iets van je site kunnen zien — een scherm dat hen waarschuwt dat de website onbeveiligd is en of ze 'm echt willen bezoeken. Je kunt je vast wel voorstellen dat dit je bezoekers gigantisch afschrikt en voorkomt dat ze überhaupt op je site komen.

Het is dus niet alleen Google die je straft voor een onbeveiligde HTTP-website. Je bezoekers vertrouwen je site vanaf het eerste contactmoment ook niet.

### 1.1 AI fix

Van alle punten in dit artikel heeft dit eigenlijk geen echte AI-fix. Het is namelijk een hele simpele fix: Let's Encrypt installeren via je hosting. Dit moet je wel om de zoveel tijd verlengen, maar afhankelijk van je webhost moet je dat zelf doen of gebeurt het automatisch.

Bij de antiekwinkel Antiquewarehouse stond 96% van de webpagina's op HTTP. Dat is rampzalig. Na de overstap van HTTP naar HTTPS zagen we vrijwel direct een influx aan bezoekers (en "vrijwel direct" in SEO-termen is ongeveer 2 weken).

## 2. Geen of generieke meta descriptions

Een beveiligde website is helaas slechts het topje van de ijsberg (alhoewel wel een essentieel topje, want als je nog op HTTP draait heeft de rest hieronder vrijwel geen impact). Naast die fundamentele HTTPS-beveiliging heb je goeie paginabeschrijvingen nodig.

Google moet namelijk weten waar je webpagina over gaat, om vervolgens een preview-tekst te kunnen weergeven in de zoekresultaten. Tenzij je nog nooit Google hebt gebruikt, heb je het waarschijnlijk al gezien: wanneer je iets opzoekt krijg je per resultaat de titel én een beschrijving te zien.

En daar hebben we het nu over: die beschrijving. De beschrijving van je webpagina kan Google op twee manieren bemachtigen. Of Google pakt zelf een willekeurig stuk tekst (kan je cookie-banner zijn, of een stuk navigatie), of jij geeft Google een speciale HTML-tag door genaamd `meta description` waar je precies aangeeft wat de paginabeschrijving is.

Nou... je kunt je voorstellen dat als Google een willekeurig stukje tekst pakt, er een probleem kan ontstaan als dat stukje toevallig uit je cookie-banner komt haha.

De beschrijving van je webpagina heeft dus directe invloed op je CTR (Click Through Rate). Voor de website Antiquewarehouse heb ik voor elke pagina een unieke meta description geschreven, waardoor de CTR steeg van 2% naar 4-5%.

Deze kleine stukjes tekst moet je vaak zelf invullen, meestal met behulp van een SEO-tool. Yoast SEO is een bekende voor WordPress. Zelf gebruik ik mijn eigen plugin, lees hier waarom: [Yoast SEO is overrated. Ik bouwde iets beters](https://blog.snelstack.com/yoast-seo-is-overrated-ik-bouwde-iets-beters/).

### 2.1 AI fix

De AI-fix hier is om je hele webpagina door AI te laten lezen en er een unieke meta description uit te laten genereren. Je laat AI een aantrekkelijke beschrijving maken die ervoor zorgt dat bezoekers ook echt doorklikken naar je site. Dit gaat er natuurlijk vanuit dat je wel redelijke content op je pagina hebt staan.

De meeste SEO-plugins hebben deze AI-functionaliteit inmiddels ingebouwd, dus je hoeft niet per se zelf een prompt te bouwen. Yoast SEO heeft bijvoorbeeld een "AI generate meta description"-feature, maar die zit achter een betaalmuur van €99 per jaar per website. Mijn eigen plugin (Snel SEO) doet precies hetzelfde, alleen dan gratis.

Als je het toch handmatig wilt doen, hier is een prompt die je kunt gebruiken:

```
[Plak hier de inhoud van je pagina]

Maak een meta description van bovenstaande tekst.
Mijn doelgroep is: [vul in].

Regels:
- Maximaal 150 tekens (belangrijk)
- Filter AI-onzin eruit (em-dashes, woorden als "ontdek", "leverage", "naadloos")
- Zet er een reden in om door te klikken
```

Met de juiste prompt produceer je zo 50 unieke descriptions in een uur.

## 3. Geen JSON-LD / structured data

- Wat is het: stukje code dat Google vertelt wat er op je pagina staat (product, prijs, voorraad)
- Pijn: geen rich results in Google (geen sterren, prijzen, voorraad)
- Pijn: concurrenten met schema springen eruit, jij niet
- AI-fix: AI leest pagina en genereert Product/Organization/Breadcrumb schema in 30 seconden
- Antiquewarehouse: Product schema op alle 1.767 producten + Organization + Breadcrumb sitewide

## 4. Geen XML sitemap

- Wat is het: bestand met lijst van alle pagina's voor Google
- Pijn: zonder sitemap moet Google je site zelf uitpluizen → diepere pagina's niet geïndexeerd
- Voorbeeld: 500 producten verkopen, Google heeft er 200 → 300 bestaan niet
- AI-fix: WordPress kan sitemap zelf, AI helpt beslissen WAT erin moet (welke categorieën, tags, archieven)
- AI-fix: te veel rommel in sitemap maakt 'm zwakker
- Antiquewarehouse: gecontroleerde sitemap, configureerbaar per post type

## 5. Trage website

- Pijn: rankingfactor + bezoekers haken af na 2 sec
- Boosdoeners: te veel plugins, ongeoptimaliseerde images, render-blocking fonts
- AI-fix: AI vertaalt PageSpeed-output naar normale taal
- AI-fix: image-compressie via TinyPNG/Squoosh → 70-80% kleiner zonder zichtbaar verlies
- AI-fix: AI scant plugin-lijst en stelt voor welke je kunt vervangen door simpele code
- Link naar [3 redenen waarom WordPress plugins verleden tijd zijn](https://blog.snelstack.com/3-redenen-waarom-wordpress-plugins-verleden-tijd-zijn/)
- Antiquewarehouse: hero-image preload + srcset + fetchpriority="high", Google Fonts async
- Bonus: mobiel-vriendelijkheid. Google indexeert sinds 2019 mobile-first → trage of rommelige mobiele site is extra dodelijk
- Nuance: meeste moderne WordPress-themes zijn al mobielvriendelijk by default, dus dit is meestal geen probleem. Wel even checken op een echte telefoon (geen desktop-resize) of het er goed uitziet
- AI-fix mobile: vraag AI om je mobile vs desktop screenshots te vergelijken — vindt layout-issues + stelt CSS-fixes voor

## 6. Geen of verouderde blogcontent

- 70% van Google-zoekopdrachten = long-tail
- Long-tail vang je alleen met content (blogs, gidsen, antwoorden op echte vragen)
- Korte transactionele zoekwoorden = keihard concurreren met grote spelers
- Pijn: site zonder blogs in 2 jaar = "verouderd" voor Google
- AI-fix: keyword-onderzoek vanuit klantprobleem, niet vanuit aanbod
- AI-fix: outlines + eerste drafts (jij geeft 'm de stem)
- AI-fix: 1 blog → 10 social posts via Repurposa
- Belangrijke nuance: laat AI niet alles schrijven, anders klinkt het AI

## 7. Schrijven in jouw jargon, niet wat klanten Googelen

- "Stilste killer" — meeste ondernemers zien dit niet
- Voorbeeld: "ergonomische bureaustoel met lordosesteun" vs "rugpijn bureaustoel"
- Voorbeeld: meubelmaker "tropisch hardhout met tussenmaat lamellen" vs "buitentafel weerbestendig"
- Google matcht op woorden, niet op product
- AI-fix: vraag AI "wat zoekt iemand op Google die dit zou willen kopen, niet in vakjargon?"
- AI-fix: combineer met Google Search Console-data (welke woorden brengen al verkeer)
- Antiquewarehouse: producttitels via GPT-4o-mini in 5 talen vertaald, marktgericht (niet 1-op-1)
- Link naar [Multitalen in WordPress zonder 10.000 extra pagina's](https://blog.snelstack.com/multitalen-in-wordpress-zonder-10-000-extra-paginas/)

## Wat dit oplevert (afsluiter)

- Losse fout = beperkte impact, combinatie wel
- Antiquewarehouse: 886 → +30% clicks in 3 weken, geen ads, geen budget
- Link naar [Hoe een antiekwinkel 30% meer clicks kreeg in 3 weken](https://blog.snelstack.com/hoe-een-antiekwinkel-30-meer-clicks-kreeg-in-3-weken/)
- Het is geen rocket science, alleen technische schoonmaak
- AI maakt quick wins kwestie van uren i.p.v. weken
- Basis (HTTPS, sitemap, schema-fundering) blijft handwerk maar één keer goed = jaren rendement
- Closer: begin met de fout die jou het meest opvalt. 1 fix per week → 2 maanden later begrijpt Google je site
