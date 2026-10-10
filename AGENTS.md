# Maintaining this guide

- Keep product facts tied to current official Kimi Code documentation and a verification date.
- Label scenario routing as this guide's recommendation; do not invent benchmark results.
- Attribute vendor-reported figures (speed, quota cost, capability claims) to Kimi's official documentation.
- Keep Kimi Code managed service, API access and third-party tool configuration distinct.
- Kimi agent files configure tools and prompts, not models. Model routing belongs in `/model`, `/secondary-model` and the `[secondary_model]` pool documentation — do not add per-agent model fields.
- Run the repository validator after changing links, agent templates or counted artifacts.
- Preserve accurate provenance: this guide ships Mermaid diagrams only; do not add generated images without truthful generation records.
