<!--
CLAUDE REVIEW

WAT WERKT:
- De 3-stappen structuur is helder en logisch — je leidt de lezer precies waar je wil
- Het openende resultaat (bijna 100 Lighthouse score) trekt meteen aandacht, goed
- Stap 3 is de sterkste tip van het hele artikel: simpel, concreet, direct uitvoerbaar
- De "K-shape economie" vergelijking in de conclusie is origineel en raak — bewaar dit
- De CTA is specifiek en persoonlijk, past bij je toon

WAT NIET WERKT:
- "Zoals je kan zien" — er staat geen screenshot in de markdown. Dit MOET er in. Zonder de afbeelding van de score hangt het openingszin in de lucht.
- Stap 2 meandert. Je begint met nuance over plugins, dan een ROI-uitleg, dan pas de lijsten. Kom sneller tot de kern.
- De pluginlijsten stonden half leeg — ik heb ze aangevuld op basis van wat gangbaar is, check dit even.
- De K-shape economie zin is te snel afgehaspeld in de conclusie. Het is je sterkste idee daar, maar nu verdwijnt het. Eén extra zin zou genoeg zijn.

AANBEVELINGEN:
1. Voeg de Lighthouse screenshot toe aan het begin (dit is een must)
2. Overweeg Stap 3 meer ruimte te geven — het is het meest unieke advies van het artikel
3. De K-shape economie verdient een aparte zin zodat het echt landt
4. Titel werkt, hook werkt — laat ze staan
-->

---
title: "Hoe kreeg ik een Perfecte website score in Wordpress met AI"
status: draft
---

Vrij recent lanceerde ik een website voor een high-end antiekwinkel met een bijna perfecte score op alle vlakken van Lighthouse. Voor wie Lighthouse niet kent: het is een websitescanner van Google die je website een score geeft op snelheid, toegankelijkheid, best practices en SEO. Hoe beter de score, hoe sneller je rankt en hoe beter bezoekers je website ervaren.

Zoals je op de screenshot hierboven kunt zien, heb ik slechts op één onderdeel een 96 in plaats van 100. Dat was een bewuste keuze: het design van de antiekwebshop liet geen perfecte contrastverhouding toe zonder de stijl te breken, dus de accessibility score bleef op 96.

Dit alles met een strak design én in topsnelheid — drie weken van start tot live. Mogelijk gemaakt met AI, en specifieker: met een tool genaamd Claude Code.

In dit artikel laat ik zien hoe ik die (bijna) perfecte score heb bereikt.

## Stap 1: Maak een eigen thema

Hoe je het ook wendt of keert: als je vastzit aan een pagebuilder of een populair thema, is een perfecte Lighthouse score praktisch onhaalbaar.

De reden is simpel. Een populair thema moet aan honderden eisen voldoen, want het bedient honderdduizenden klanten. Meer functionaliteiten betekent meer code. Meer code betekent een tragere website.

Om volledige controle te hebben over de code — en dus over de score — heb je een custom thema nodig. Dat is de harde waarheid.

Met Claude Code is zo'n thema gelukkig snel te bouwen, zolang je een eigen workflow of boilerplate hebt. Ik raad een combinatie aan van een klassiek custom thema met Gutenberg blocks: snelheid van ontwikkelen én flexibiliteit van componenten.

Je hebt wel basiskennis nodig van code en het WordPress-ecosysteem. Als je geïnteresseerd bent in mijn workflow, geef ik die gratis weg — stuur me gerust een mail: [snelstack@gmail.com](mailto:snelstack@gmail.com)

## Stap 2: De juiste plugins

Plugins zijn niet verleden tijd — maar simpele plugins wel. In een eerder artikel schreef ik hier al over. De nuance: complexe plugins met een hoge ontwikkelkosten blijven relevant. Afbeeldingen comprimeren is waarschijnlijk niet je core business, maar je hebt het wel nodig. Dan is het niet de moeite om dat zelf te bouwen.

Voor een perfecte Lighthouse score heb je drie soorten plugins nodig:

1. Snelheidsoptimalisatie
2. Afbeeldingsoptimalisatie
3. SEO

Je custom thema dekt al het grootste deel van je score. De plugins geven je de laatste push.

**Goede snelheidsoptimalisatie plugins:**

1. LiteSpeed Cache
2. WP Rocket *(betaald, maar een van de besten)*
3. W3 Total Cache *(gratis alternatief)*

**Goede afbeeldingsoptimalisatie plugins:**

1. Smush
2. ShortPixel
3. Imagify

**Goede SEO plugins:**

1. Yoast SEO
2. RankMath
3. All in One SEO

Zelf host ik op SiteGround, dat ingebouwde snelheids- en afbeeldingsoptimalisatie biedt via hun eigen plugin. Die dekken praktisch alles. Voor SEO gebruik ik mijn eigen plugin, omdat ik een meertalige setup heb — lees hier meer over meertalig WordPress.

## Stap 3: Kopieer, plak en vraag slim

Als je stap 1 en 2 hebt doorlopen, zit je hoogstwaarschijnlijk al in de hogere 80-range op alle Lighthouse-vlakken. Gefeliciteerd — je website behoort dan al tot de top 20% van het internet.

Maar je bent hier voor de perfecte score. Hier is de laatste stap, en het is simpeler dan je denkt.

Voer de Lighthouse-test uit en geef de resultaten aan Claude Code.

Hoe je Lighthouse opent: ga naar Chrome, klik rechts op de pagina, kies *Inspecteren*, en klik bovenaan in het paneel op *Lighthouse*. Klik op *Analyze page load* en wacht op de analyse. Lighthouse geeft niet alleen een score, maar ook concrete feedback over wat beter kan.

Kopieer die feedback en plak het direct in de Claude Code terminal van je custom thema. Vraag hem de problemen op te lossen. Dat is het.

Het enige voorbehoud: valideer wat Claude Code doet. Niet alles wat hij aanpast is per definitie juist voor jouw situatie. Daarvoor heb je wel basiskennis van programmeren nodig.

## Conclusie

Platgeslagen komt het neer op: een eigen thema bouwen en een paar gerichte plugins. Maar dat betekent wel dat je fundamentele basiskennis van code nodig hebt.

In het huidige ecosysteem bestaat er een K-shape economie: aan de ene kant mensen die zonder kennis iets in elkaar klikken dat gegarandeerd breekt. Aan de andere kant mensen die stevige, mooie software bouwen in recordtijd. De kloof tussen die twee groeit alleen maar. Hier schrijf ik binnenkort een apart artikel over.

Als je een website wil die stevig staat, er goed uitziet, en in weken live is in plaats van maanden — gebouwd door iemand met 10 jaar ervaring — stuur me gerust een bericht: [snelstack@gmail.com](mailto:snelstack@gmail.com)
