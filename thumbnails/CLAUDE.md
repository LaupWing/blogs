# PanelForge — Thumbnail Prompt Generator

## Workflow

When opened, do the following steps:

1. **Ask which article** — list all `.md` files from `../published/` and ask the user to pick one by number
2. **Read the article** — extract the title (# heading) and key points (## headings)
3. **Ask which style** — list all `.md` files from `./styles/` and ask the user to pick one
4. **Read the style template** — open the chosen style file
5. **Fill in {{CONTEXT}}** — replace with: article title + numbered list of key points (written as visual scene descriptions, not just headings)
6. **Copy to clipboard** — run `pbcopy` with the completed prompt
7. **Generate alt text** — output a ready-to-use alt text in this format: `"Cyberpunk comic strip illustrating [topic]: [brief scene description]"`
8. **Generate filename** — output the filename in kebab-case matching the post slug, e.g. `hoe-99-procent-claude-code-verkeerd-gebruikt.png`
9. **Confirm** — tell the user the prompt is copied and ready to paste into Gemini, Midjourney, or DALL-E

## Context format

When filling in {{CONTEXT}}, translate the headings into visual scene descriptions. Example:
- Heading "Ze redirecten nooit" → "A developer blindly accepting wrong AI output while the system corrupts behind them"
- Heading "Bugs" → "A system crashing under the weight of too many plugins, error screens everywhere"

Keep it punchy — one sentence per panel.
