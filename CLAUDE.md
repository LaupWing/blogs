# Blogs — Claude Instructions

## Workflow

Blogs move through three stages:

```
/drafts      ← raw writing from Loc
/ai          ← Claude has reviewed and improved it (Loc checks here)
/published   ← approved and live on WordPress
```

**Draft → AI:**
Read the draft fully, improve grammar and flow, then save one `.md` file to `/ai/`. Keep the original in `/drafts/` untouched — it's the archive. Add the CLAUDE REVIEW block at the top of the `/ai/` file so Loc can review.

**AI → Published (only when Loc approves):**
1. Copy the `.md` from `/ai/` to `/published/` — keep the `/ai/` version intact as archive
2. Strip the CLAUDE REVIEW comment block from the `/published/` file
3. Update the frontmatter: add `status: published` and `date: <today>`
4. Run `python3 scripts/clipboard.py "/published/<filename>.md"` — this converts markdown to HTML on-the-fly and copies it to clipboard
5. Remind Loc: **"Klaar — ga naar WordPress en plak (Cmd+V) in de visual editor."**
6. After Loc confirms it's live, ask: **"Wat is de live URL? Dan voeg ik hem toe aan de frontmatter."** Then add `url: <url>` to the frontmatter of the `/published/` file.

All three folders are kept as archive: `/drafts/` = raw original, `/ai/` = Claude improved, `/published/` = final clean version.

## How to approach a draft

1. **Read the draft as-is.** Understand what it's saying and what tone it has.
2. **Improve grammar and flow** — fix errors, tighten sentences, improve readability. Do not change the voice.
3. **Always add a CLAUDE REVIEW block** at the top of the improved file (as an HTML comment). Include: what works, what doesn't, and concrete recommendations. Be direct, not diplomatic.
4. **Never overhaul a draft** — if the structure or hook is already working, say so. Only flag things that are genuinely weak.

## References

- `STRUCTURE.md` — general blog structure (intro, body, takeaway). Use as a lens, not a template.
- `HOOK.md` — what makes a strong hook and title. Offer alternatives only if the current hook is weak.

## Blog Brands

This repo contains two distinct brands. Keep them completely separate in tone, audience, and purpose.

### Tech/WordPress (Snelstack)
- **Audience:** small business owners who need a website, OR developers who want to validate Loc's expertise
- **Goal:** generate leads for €2.500–3.500 WordPress projects
- **Content mix:**
  - *Laag 1 — ondernemer-gericht:* business results, herkenbare problemen ("waarom jouw site klanten kost"), case studies (Antiquewarehouse)
  - *Laag 2 — technisch:* AI workflows, Lighthouse scores, plugins, custom themes — builds credibility
- **Language:** Dutch (primary), English possible

### Fitness (personal brand)
- **Audience:** fitness enthusiasts, people wanting discipline and results
- **Goal:** maintain existing 45K following
- **Tone:** personal, direct, no coaching-speak
- **Language:** Dutch or English

When a draft comes in, check the filename or topic to determine which brand it belongs to and apply the right lens.

## Language

Write in the same language as the draft. If the draft is in Dutch, improve in Dutch. If it's in English, improve in English. Do not switch or mix languages.

## Tone

Loc writes conversational, direct, no fluff. Preserve that. Do not make it sound formal or corporate.

## AI Filters

Strip out words and phrases that sound AI-generated or fake. These kill authenticity.

**Banned words/phrases:**
- Delve, dive into, explore
- Unlock, unleash, leverage
- Game-changer, groundbreaking, revolutionary
- Seamlessly, effortlessly
- It's worth noting, it's important to note
- In today's world, in today's fast-paced world
- At the end of the day
- Empower, foster, facilitate
- Robust, comprehensive, cutting-edge
- Navigate (used metaphorically)
- Tailored, curated
- Fluff (and fluffy)
- Overmatig gebruik van — (em dash) — AI misbruikt dit constant. Gebruik het hooguit 1x per tekst, alleen als het echt de beste optie is.
- In conclusion, to summarize (as openers to a closing paragraph)

**What to do instead:**
- Use the word the human would actually say
- If a sentence needs a filler word to work, rewrite the sentence
- Short and direct beats smooth and fluffy every time
