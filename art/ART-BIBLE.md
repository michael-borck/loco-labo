# LocoLabo art bible

Every LocoLabo site shares one look: 16-bit pixel art, a cozy night palette, and a place
for each project. Secondhand hardware, fossils, and "the floor" suit a retro game better
than a glossy render, and pixel art hides the small inconsistencies of generated images.

## The world

LocoLabo is a small valley at night. Each project is a place in it:

| Project | Place | Icon |
|---|---|---|
| LocoLabo | the valley overworld (hub map) | brass lantern |
| LocoLLM | a lone alchemist tower | llama in a wizard hat |
| LocoBanco | an inventor's test bench | brass medal |
| LocoFósil | a natural history museum of old GPUs | circuit-board fossil |
| LocoAgente | a robot workshop | robot head |
| LocoConvoy | trucks on a mountain road | cargo truck |
| LocoNotas | a library desk and field notebook | notebook |
| LocoPuente | a stone bridge into town | stone arch |
| LocoMusa | a hilltop observatory | lightbulb with a star |
| LocoEnsayo | a small theatre stage | theatre masks |

New projects get a new place before they get a new page.

## Recipe

- Tool: `limn` (SwarmUI provider), model `juggernautXL_v9`, LoRA `pixel-art-xl:1`.
- Scene prompt: `16-bit pixel art game scene, chunky pixels, limited color palette, crisp
  pixels, subtle dithering: {scene}, deep indigo night, warm amber lamplight, soft cyan
  screen glow, cozy, game art`
- Icon prompt: `16-bit pixel art game inventory icon, chunky pixels, limited color palette,
  bold dark outline: a single large {thing}, centered and filling most of the frame, plain
  flat dark indigo background, ...palette..., game sprite`
- Negative: photo, 3D render, bokeh, blur, smooth gradients, text, letters, numbers,
  watermark, logo, border, frame, UI elements, deformed.
- Sizes: scenes 1216x832, icons 1024x1024.
- Seeds are fixed per job (`BASE_SEED` + job index), so a rerun reproduces the same image.

## Lessons from the first batch

- Put the most important words in capitals when the model ignores them ("MOONLIT NIGHT").
- Abstract metaphors fail ("graphics cards embedded in rock like fossils"). Concrete,
  familiar scenes work ("a museum display case holding a graphics card mounted like a
  dinosaur skeleton").
- Icons come out small in the frame; the processor crops to the subject before
  downscaling, so favicons stay readable at 32px.

## Workflow

```bash
python3 scripts/loco_art.py generate --name musa-hero --candidates 3
python3 scripts/loco_art.py pick musa-hero 2
python3 scripts/loco_art.py process      # writes hero.webp, icon.png, favicon.png into each repo
```

Candidates, picks, and contact sheets stay in `art/` and are gitignored. Only processed
files ship: `src/assets/art/hero.webp`, `src/assets/art/icon.png`, and `public/favicon.png`
in each site, plus the map and marker icons in this repo.
