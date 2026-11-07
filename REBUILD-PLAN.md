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

## Phase 4: tools and shared results (in progress)

- [x] Shared result contract: `loco-banco/src/data/results.schema.json`.
- [x] Dependency-free validator: `loco-banco/scripts/validate-results.mjs` (`npm run validate:results`).
- [x] GPU Picker moved into LocoBanco at `/picker/`, served under locobanco.org and fed at
      build time from `loco-banco/src/data/picker-data.json`. Placeholder values relabelled
      `estimated` so no unmeasured number is presented as measured.
- [x] Public [result contract page](https://locobanco.org/result-contract/) documents the shape.
- [x] LocoEnsayo migrated to the shared theme (nested repo `loco-ensayo/loco-ensayo`).
- [x] LocoMusa migrated from the static `docs/index.html` to an Astro Starlight site on the
      shared theme, with the methodology, human-judging, and authoring docs as pages.
- [ ] Switch the LocoMusa GitHub Pages source to GitHub Actions; until then `docs/` keeps serving.
- [ ] Convert `/picker/` from a standalone Astro route to a hydrated island. The current
      route keeps the instrument UI intact and is the safer base.
- Acceptance: every public surface is versioned here and every result traces to a raw run.
  The contract enforces the second half; real runs still have to replace the estimates.

## Deferred: single-site consolidation

Only if cross-domain SEO and unified search become the top priority. Cost is high and it
breaks existing URLs. The Phase 2 package gets most of the benefit without the move.
