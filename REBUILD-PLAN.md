# Ecosystem rebuild plan

Status of the LocoLabo cross-project audit and rebuild. The goal is discoverability and a
single source of truth without merging the independent project repos.

## Principles

1. One manifest drives navigation, the hub index, and cross-links.
2. Every project keeps its own repo and domain. No big-bang merge.
3. Canonical content lives in one place; other pages link to it instead of duplicating.
4. Starlight stays for docs. Custom Astro pages handle the hub, landing, and tools.

## Phase 1: shared manifest and hub (done)

- [x] `src/data/projects.json` is the single source of truth for project metadata.
- [x] `/projects/` index page generated from the manifest, grouped by category.
- [x] Hub sidebar links the index and every project, including LocoBase and LocoNotas.
- [ ] Normalise each project site's Related sidebar to the same set (minus self).
- [ ] Add `public/CNAME` to sites that rely only on repo settings.
- [ ] Add cross-links from duplicated reference pages to their canonical source.

## Phase 2: shared theme package (done)

- [x] `loco-theme` repo: `@locolabo/theme`, shipped as a git dependency (`#v0.1.1`).
- [x] `loco()` builds social links, accent tokens, shared CSS, and the generated Related group.
- [x] `src/projects.json` moved to `loco-theme`; the hub imports it directly.
- [x] All eight sites migrated off copied `custom.css` and bespoke Related blocks.
- [x] `ignore-scripts=true` is set globally, so build cleanup lives in the `build` script.
- Acceptance met: accent colour or project URL is a one-file change plus a version tag.

## Phase 3: consolidate content (done)

- [x] `loco-labo/nvidia-gpu-reference.md` keeps the modern consumer reference but its
      outdated Kepler claim now defers to LocoFósil, which is canonical for the relic shelf.
- [x] `loco-labo/machine-setup.md` already defers to LocoBase for provisioning and to
      LocoFósil Setup for second-life cards; no duplication left.
- [x] Slimmed the four READMEs that mirrored their sites (labo, banco, llm, puente) to
      a pointer plus quick-start commands. Short READMEs left as-is; all gain a live-site link.
- Acceptance met: each topic has one canonical explanation, and GitHub READMEs point at it.

## Phase 4: tools and shared results (done)

- [x] Shared result contract: `loco-banco/src/data/results.schema.json`.
- [x] Dependency-free validator: `loco-banco/scripts/validate-results.mjs` (`npm run validate:results`).
      A `measured` result without a `source_run_id` is now an error, not a warning.
- [x] GPU Picker moved into LocoBanco at `/picker/`, served under locobanco.org and fed at
      build time from `loco-banco/src/data/picker-data.json`.
- [x] Picker shipped as a page-scoped bundled client module (D3 from npm, no CDN).
- [x] Placeholder values relabelled `estimated` so no unmeasured number is presented as measured.
- [x] Public [result contract page](https://locobanco.org/result-contract/) documents the shape.
- [x] LocoEnsayo migrated to the shared theme (nested repo `loco-ensayo/loco-ensayo`).
- [x] LocoMusa migrated from the static `docs/index.html` to an Astro Starlight site on the
      shared theme, with the methodology, human-judging, and authoring docs as pages.
- [x] LocoMusa GitHub Pages source switched to GitHub Actions and redeployed.
- Acceptance: every public surface is versioned here, and every `measured` result must trace
  to a raw run. The contract enforces the second half; real runs still replace the estimates.

## Phase 5: single hardware registry (done)

- [x] Canonical `gpus.json` lives in `@locolabo/theme` (v0.2.0).
- [x] Hub `/gpu-registry/` renders it with reconciled totals.
- [x] LocoBanco GPU Inventory is generated from it (fleet view by machine).
- [x] LocoFósil hardware inventory is generated from it (relic-shelf view with CUDA/driver).
- [x] The GTX 960 is recorded once and flagged for physical confirmation.
- Acceptance: a card change is one edit to `loco-theme/src/gpus.json` plus a version tag;
  the hub, Banco, and Fósil tables all follow. No table is hand-maintained in three places.

## Phases 6-10: make it fun to explore

Direction: self-funded and independent, so optimise for curiosity and contribution, not
sponsors. Personality lives on the hub and landing pages; the docs stay clean and plain.
Art style is 16-bit pixel art (fits secondhand hardware and "the floor"), generated with
`limn` + `juggernautXL_v9` + the `pixel-art-xl` LoRA, as in assume-breach and Lorekeeper.

### Phase 6: cleanup

- [ ] Hub homepage links the project map; counts come from the manifest; CTA explores projects.
- [ ] Hub gets its own tagline (LocoLLM keeps "Frontier AI on a budget").
- [ ] Naming: LocoBanco (not LocoBench), LocoLabo (not LocoLab), LocoFósil (with accent).
- [ ] Musa gets a favicon, logo and 404; Ensayo gets a 404.
- [ ] Puente footer links the hub; Puente's second splash stops looping to `/`.
- [ ] Hub sidebar loses duplicate entries; orphan pages are linked (labo, llm).
- [ ] Shared theme footer links every page on every site back to the hub.

### Phase 7: art bible and assets

- [ ] Art bible: prompt prefix, palette, negative prompt, seeds, sizes, per-site location.
- [ ] Test batch: hub map, LocoFósil dig, LocoBanco bench. Judge before scaling up.
- [ ] One 1216x832 location hero and one pixel favicon per project.

### Phase 8: identity rollout

- [ ] Every landing page leads with its location art, a one-line what/why, and a start path.
- [ ] Emoji favicons replaced by pixel sprites.

### Phase 9: hub as hub-and-spoke

- [ ] Homepage is a clickable pixel overworld of the projects, with a stats strip.
- [ ] Wayfinder: a few questions suggest a starting trail.
- [ ] A plain path ("just the docs") sits next to the playful one.

### Phase 10: quests

- [ ] Quest trails defined as data, progress and badges stored on the hub (spokes are on
      other domains, so progress cannot be shared across them).
- [ ] First quests: run a local model, wake a fossil GPU, benchmark your card, submit a result.

## Deferred: single-site consolidation

Only if cross-domain SEO and unified search become the top priority. Cost is high and it
breaks existing URLs. The Phase 2 package gets most of the benefit without the move.
