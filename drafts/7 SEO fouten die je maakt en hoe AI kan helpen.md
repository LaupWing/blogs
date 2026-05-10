# 7 SEO fouten die je maakt en hoe AI kan helpen

## Intro
- Veel ondernemerssites laten 30-50% verkeer liggen door dezelfde paar fouten
- 7 fouten die ik bijna overal zie + AI-fix per fout
- Voorbeelden: mijn werk voor Antiquewarehouse (1.767 producten, echte data)
- Geen theorie, geen marketing-praatjes

## 1. Geen HTTPS
- Pijn: "Niet veilig"-waarschuwing in Chrome → bezoekers haken direct af
- Pijn: rankingfactor sinds 2014 → lagere positie
- AI-fix: Let's Encrypt installeer je via hosting (gratis), AI scant daarna op mixed content errors
- Antiquewarehouse: oude site stond voor 96% op HTTP, eerste ding dat we fixten

## 2. Geen of generieke meta descriptions
- Pijn: Google pakt zelf willekeurig stuk tekst (cookie-banner, navigatie...)
- Pijn: CTR blijft op 2% hangen i.p.v. 4-5%
- Veel sites: overal hetzelfde of niks
- AI-fix: ChatGPT/Claude leest pagina, schrijft conversion-gerichte description
- AI-fix: 50 unieke descriptions in een uur met juiste prompt
- Antiquewarehouse: 0 vóór migratie, nu custom per pagina via Snel SEO

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
