---
title: 7 SEO fouten die je maakt en hoe AI kan helpen
language: nl
status: published
date: 2026-05-13
url: https://blog.snelstack.com/7-seo-fouten-die-je-maakt-en-hoe-ai-kan-helpen/
---

# 7 SEO fouten die je maakt en hoe AI kan helpen

Na tientallen websites te hebben gemaakt voor ondernemers zie ik dezelfde technische fouten opnieuw en opnieuw. Fouten die direct of indirect invloed hebben op je SEO-score.

In dit artikel ga ik de 7 fouten bespreken die ik bijna overal zie, plus de AI-fixes die je per fout kunt toepassen om het probleem sneller en efficiënter op te lossen.

Maar voordat we verder gaan: wie ben ik, en waarom zou je überhaupt naar een woord luisteren van wat ik te zeggen heb? Ik ben Loc, software-ontwikkelaar met meer dan 10 jaar ervaring. Het grootste deel van mijn carrière heb ik echt dagelijks achter de code gezeten.

Daarnaast heb ik zelf hele software-architecturen van begin tot eind gebouwd, een UX/UI-designopleiding gedaan, marketing-kennis opgedaan (150 miljoen impressies op social media), en werk ik samen met mijn broertje die SEO-professional is.

Genoeg over mij. Laten we de 7 SEO-fouten doornemen. Als concreet voorbeeld gebruik ik mijn recente werk voor een antiekwinkel genaamd [Antiquewarehouse](https://blog.snelstack.com/hoe-een-antiekwinkel-30-meer-clicks-kreeg-in-3-weken/).

## 1. Geen HTTPS

Dit was voor mij een verrassing toen ik met mijn eigen B2B-softwarebedrijf begon: hoeveel websites nog op de onbeveiligde HTTP-technologie draaien. Voor degenen die niet weten wat het verschil is: je hoeft niet te weten wat het precies doet, maar dat kleine verschil in de letter 's' betekent een hele hoop. Die 's' staat voor security, en als je die niet hebt, is je website onbeveiligd.

Google zal je zwaar bestraffen als je website onbeveiligd is. En niet alleen dat. Mensen krijgen ook nog eens een waarschuwingsscherm te zien voor ze überhaupt iets van je site kunnen zien, een scherm dat hen waarschuwt dat de website onbeveiligd is en of ze 'm echt willen bezoeken. Je kunt je vast wel voorstellen dat dit je bezoekers gigantisch afschrikt.

Het is dus niet alleen Google die je straft. Je bezoekers vertrouwen je site vanaf het eerste contactmoment ook niet.

### 1.1 AI fix

Van alle punten in dit artikel heeft dit eigenlijk geen echte AI-fix. Het is namelijk een hele simpele fix: Let's Encrypt installeren via je hosting. Dit moet je wel om de zoveel tijd verlengen, maar afhankelijk van je webhost moet je dat zelf doen of gebeurt het automatisch.

Bij de antiekwinkel Antiquewarehouse stond 96% van de webpagina's op HTTP. Dat is rampzalig. Na de overstap van HTTP naar HTTPS zagen we vrijwel direct een stroom bezoekers (en "vrijwel direct" in SEO-termen is ongeveer 2 weken).

## 2. Geen of generieke meta descriptions

Een beveiligde website is helaas slechts het topje van de ijsberg (alhoewel wel een essentieel topje, want als je nog op HTTP draait heeft de rest hieronder vrijwel geen impact). Naast die fundamentele HTTPS-beveiliging heb je goede paginabeschrijvingen nodig.

Google moet namelijk weten waar je webpagina over gaat, om vervolgens een preview-tekst te kunnen weergeven in de zoekresultaten. Tenzij je nog nooit Google hebt gebruikt, heb je het waarschijnlijk al gezien: wanneer je iets opzoekt krijg je per resultaat de titel én een beschrijving te zien.

En daar hebben we het nu over: die beschrijving. De beschrijving van je webpagina kan Google op twee manieren bemachtigen. Of Google pakt zelf een willekeurig stuk tekst (kan je cookie-banner zijn, of een stuk navigatie), of jij geeft Google een speciale HTML-tag door genaamd `meta description` waar je precies aangeeft wat de paginabeschrijving is. Die tag staat in de code van je pagina, je bezoekers zien hem nooit. Maar in Google zoekresultaten wel.

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

Net als de meta description is JSON-LD iets wat volledig achter de schermen werkt. Je bezoekers zien het nooit. Het is puur voor Google, een stukje code dat Google vertelt wat er precies op je pagina staat.

Wat je wél moet weten: dankzij JSON-LD kan Google je pagina begrijpen op een dieper niveau. Neem een productpagina. Zonder JSON-LD ziet Google gewoon een hoop tekst. Met JSON-LD weet Google: dit is een product, het kost €149, het heeft 4,5 sterren, en er zijn nog 3 op voorraad. En dat verschil zie je terug in de zoekresultaten. Concurrenten met structured data krijgen die sterretjes, prijzen en voorraadindicaties zichtbaar in Google. Jij niet.

Er is nog een reden waarom dit tegenwoordig extra belangrijk is: AI-assistenten zoals ChatGPT en Google AI Overviews pikken ook structured data op. Hoe beter je data gestructureerd is, hoe groter de kans dat jouw website wordt opgepikt als antwoord op een vraag.

Yoast genereert wel automatisch wat basisschema's op de achtergrond, Organization en WebPage, maar voor Product schema (de dingen die er echt toe doen voor een webshop) heb je hun WooCommerce SEO addon nodig. Ook betaald, bovenop Yoast Premium. En aanpassen wat Yoast genereert? Beperkt tot vrijwel onmogelijk zonder te betalen. Mijn eigen plugin (Snel SEO) doet dit gratis out of the box, en je kunt het per pagina aanpassen.

Bij Antiquewarehouse was er nul structured data aanwezig. Ik heb Product schema toegevoegd aan alle 1.767 producten, plus Organization schema en Breadcrumb schema sitewide. Dat klinkt als veel werk, maar het was grotendeels geautomatiseerd.

### 3.1 AI fix

Dit is precies het soort werk waar AI goed in is. Je geeft AI de inhoud van je pagina en vraagt het om de juiste JSON-LD te genereren. Voor een productpagina vraag je een Product schema, voor je homepage een Organization schema, voor je navigatiestructuur een Breadcrumb schema. AI genereert dat in 30 seconden in het juiste formaat, dat je vervolgens direct in je `<head>` kunt plakken.

```
Dit is de inhoud van mijn productpagina:
[plak hier je paginatekst]

Genereer JSON-LD structured data voor dit product.
Gebruik het Product schema van schema.org.
Neem naam, beschrijving, prijs en beschikbaarheid op waar van toepassing.
Output alleen de JSON-LD code, geen uitleg.
```

## 4. Geen XML sitemap

Dit klinkt technisch, maar het is simpeler dan je denkt. Een XML sitemap is gewoon een bestand met een lijst van alle pagina's op je website, dat je aan Google geeft. Zonder die lijst moet Google je hele site zelf uitpluizen om te ontdekken wat er allemaal op staat. En dat doet Google niet altijd even grondig.

Het gevolg: pagina's die wat dieper in je website zitten, worden niet of laat geïndexeerd. Stel je hebt een webshop met 500 producten. Google vindt er 200 en indexeert die. De andere 300 bestaan voor Google simpelweg niet. Je verkoopt ze dus ook niet via organisch zoekverkeer.

Bij Antiquewarehouse ging dit nog een stap verder. De webshop heeft 1.767 producten in 6 talen, dat zijn bijna 10.000 productpagina's die geïndexeerd moeten worden. Zonder een goed geconfigureerde sitemap had Google daar nooit doorheen gekomen.

Maar er is een tweede probleem dat de meeste mensen over het hoofd zien: wat je in je sitemap stopt. Veel WordPress-websites genereren automatisch sitemaps met van alles erin, paginanummers zoals `/pagina/2`, tag-archieven, auteurspagina's, lege categoriepagina's. Dat is pure rommel. En als je Google een sitemap vol rommel geeft, verdunt dat de waarde van je echte pagina's.

Bij Antiquewarehouse stond de sitemap vol met dit soort onnodige URLs. Ik heb de sitemap opgeschoond en configureerbaar gemaakt per post type, zodat alleen de pagina's die er echt toe doen aan Google worden doorgegeven.

### 4.1 AI fix

WordPress genereert sitemaps automatisch via plugins zoals Yoast of mijn eigen Snel SEO. Maar de echte waarde van AI zit hier in de strategie: wat hoort er wel en niet in je sitemap? Gooi je sitemap-inhoud in AI en vraag het om te analyseren welke URL-types weg mogen. AI herkent direct de patronen die Google verzwakken en geeft je een concrete lijst van wat je kunt uitzetten.

## 5. Trage website

Snelheid is een directe rankingfactor voor Google. Hoe trager je website, hoe lager je rankt. Maar los van Google: geen enkele bezoeker wacht langer dan 2 seconden. Als je pagina er langer over doet, zijn ze weg. Naar een concurrent die wel snel laadt.

De drie boosdoeners die ik het vaakst zie:

**Te veel plugins.** Elke plugin laadt extra code op elke pagina. Veel van die code heeft je bezoeker helemaal niet nodig. Ik heb hier een apart artikel over geschreven: [3 redenen waarom WordPress plugins verleden tijd zijn](https://blog.snelstack.com/3-redenen-waarom-wordpress-plugins-verleden-tijd-zijn/).

**Ongeoptimaliseerde afbeeldingen.** Een foto van 4MB die je gewoon uploadt zonder te comprimeren is een van de makkelijkste manieren om je website te vertragen. Tools zoals TinyPNG of Squoosh comprimeren afbeeldingen 70-80% zonder zichtbaar kwaliteitsverlies.

**Render-blocking fonts en scripts.** Google Fonts die de pagina blokkeren terwijl ze laden. Dit zien developers zelf vaak niet omdat ze op een snelle verbinding werken en het verschil niet merken.

Bij Antiquewarehouse heb ik de hero-image voorzien van `preload`, `srcset` en `fetchpriority="high"`, en Google Fonts asynchroon geladen. Kleine ingrepen, merkbaar verschil in laadtijd.

**Bonus: mobiel.** Sinds 2019 indexeert Google mobile-first. Dat betekent dat Google jouw site beoordeelt op basis van hoe hij eruitziet op een telefoon, niet op desktop. De meeste moderne WordPress-themes zijn al mobielvriendelijk, dus dit is meestal geen groot probleem. Maar check het even op een echte telefoon, niet door je browservenster kleiner te maken.

### 5.1 AI fix

Google PageSpeed Insights geeft je een rapport met alles wat traag is op je website. Het probleem: dat rapport is technisch en voor de meeste mensen onleesbaar. Kopieer de output en gooi het in AI. Vraag het om in gewone taal uit te leggen wat de drie grootste problemen zijn en hoe je ze oplost. Je krijgt direct een actielijst.

AI kan ook je lijst met geïnstalleerde plugins scannen en aangeven welke vervangen kunnen worden door een paar regels code. Minder plugins, minder code, snellere website.

Voor mobiel: maak screenshots van je site op desktop en mobiel en laat AI ze vergelijken. AI pikt layout-problemen op die je zelf over het hoofd ziet en stelt concrete CSS-fixes voor.

## 6. Geen of verouderde blogcontent

70% van alle Google-zoekopdrachten zijn long-tail. Dat zijn de langere, specifiekere zoekopdrachten zoals "beste bureaustoel voor rugpijn thuiswerken" in plaats van "bureaustoel". Die long-tail zoekopdrachten vang je bijna alleen met blogcontent. Niet met je homepage, niet met je productpagina's.

Het probleem voor de meeste ondernemers: ze proberen te ranken op de korte, drukke zoekwoorden. "WordPress developer", "webdesign", "bureaustoel". Dat zijn woorden waar je als kleine speler keihard moet concurreren met grote websites die al jaren domeinautoriteit opgebouwd hebben. Je maakt geen kans.

Blogs lossen dat op. Met een goede blog beantwoord je specifieke vragen van je klanten, en Google stuurt mensen jouw kant op die precies die vraag stellen. Mensen die al halfweg in hun aankoopbeslissing zitten.

En dan is er nog een tweede probleem: een website zonder recente content wordt door Google als inactief beschouwd. Hoe langer je niks publiceert, hoe minder Google reden heeft om je site te blijven crawlen en hoog te blijven ranken.

Een belangrijke nuance hier: het gaat erom wat je AI geeft om mee te werken. Schrijf zelf de outline met jouw verhaal, jouw voorbeelden en jouw ervaringen. Als AI dat als input krijgt, vult het aan vanuit jouw fundament. Het resultaat klinkt als jou. Gooi je alleen een onderwerp in zonder input, dan krijg je generieke tekst die klinkt als elke andere blog op het internet.

### 6.1 AI fix

AI is het meest waardevol aan het begin van het schrijfproces, niet aan het einde. Gebruik het voor keyword-onderzoek vanuit het klantprobleem, niet vanuit jouw aanbod. Vraag AI: "Wat zoekt iemand op Google die dit probleem heeft?" in plaats van "Geef me zoekwoorden voor mijn dienst." Dat verschil bepaalt of je gevonden wordt.

Daarna kun je AI een outline laten maken op basis van jouw input. Jij bepaalt de richting, AI vult de structuur in. Dan schrijf jij de tekst. Dit is ook precies hoe Repurposa werkt: jij schrijft de ruwe outline, AI genereert de blog, en vanuit die ene blog maak je automatisch een maand aan social media posts. Lees hier hoe: [1 maand social media content in 15 minuten](https://blog.snelstack.com/1-maand-social-media-content-in-15-minuten/).

## 7. Schrijven in jouw jargon, niet wat klanten Googelen

Dit is de stilste killer van de zeven. Technische fouten zie je terug in rapporten en tools. Deze fout zie je nergens, tenzij je er actief naar zoekt.

Het probleem: ondernemers schrijven over hun producten en diensten in de taal die zij kennen. Vakjargon, branchetermen, interne benamingen. Maar klanten zoeken niet op jouw jargon. Ze zoeken op hun probleem.

Een paar voorbeelden. Een meubelmaker die "tropisch hardhout met tussenmaat lamellen" verkoopt, maar zijn klant zoekt op "buitentafel weerbestendig". Een ergonomisch meubelbedrijf dat "bureaustoel met lordosesteun" in de titel zet, terwijl de klant zoekt op "bureaustoel rugpijn". Google matcht op woorden, niet op de intentie achter je product. Als de woorden niet overeenkomen, word je niet gevonden.

Bij Antiquewarehouse speelde dit in het bijzonder bij meertaligheid. Producttitels werden eerst letterlijk vertaald, één op één vanuit het Nederlands naar vijf andere talen. Maar kopers in Duitsland zoeken anders dan kopers in Nederland. Ik heb de producttitels via GPT-4o-mini opnieuw laten genereren, marktgericht per taal. Niet vertalen, maar aanpassen aan wat mensen in dat land daadwerkelijk intypen. Lees hier hoe meertaligheid in WordPress werkt zonder 10.000 extra pagina's: [Multitalen in WordPress zonder 10.000 extra pagina's](https://blog.snelstack.com/multitalen-in-wordpress-zonder-10-000-extra-paginas/).

### 7.1 AI fix

Vraag AI: "Wat zoekt iemand op Google die dit product zou willen kopen? Geef me de zoekwoorden die ze gebruiken, niet het vakjargon dat een verkoper zou gebruiken." Dat geeft je direct een ander perspectief op je eigen producten.

Combineer dat met je Google Search Console data. Welke zoekwoorden brengen nu al verkeer? Bouw daarop verder, die woorden zijn bewijs dat mensen ernaar zoeken.

## Wat dit oplevert

Elke fout op zichzelf heeft beperkte impact. De combinatie maakt het verschil.

Bij Antiquewarehouse waren alle zeven fouten aanwezig. Na de technische schoonmaak — HTTPS, meta descriptions, structured data, sitemap, snelheid, en zoekwoordoptimalisatie — groeide het organisch verkeer met 30% in 3 weken. Geen advertentiebudget, geen betaalde links, alleen de fundering op orde. Lees de volledige case study hier: [Hoe een antiekwinkel 30% meer clicks kreeg in 3 weken](https://blog.snelstack.com/hoe-een-antiekwinkel-30-meer-clicks-kreeg-in-3-weken/).

Het is geen rocket science. Het is technische schoonmaak die de meeste websites al jaren nodig hebben maar nooit krijgen. AI maakt het verschil in snelheid: wat vroeger weken kostte aan handmatig werk, doe je nu in uren.

De basis, HTTPS, sitemap, structured data, doe je één keer goed en je hebt er jaren rendement van. Begin met de fout die jou het meest opvalt. Eén fix per week, en over twee maanden begrijpt Google je site beter dan die van de meeste concurrenten.
