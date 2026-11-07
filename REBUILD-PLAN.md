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

## Phase 2: shared theme package

- [ ] Create `@locolabo/theme`: design tokens, Starlight config factory, `<ProjectNav>`.
- [ ] Replace the ~50 lines of copied `custom.css` in each site with the shared package.
- [ ] Generate the Related sidebar from the manifest so it can never drift again.
- Acceptance: changing the accent colour or a project URL is a one-file change.

## Phase 3: consolidate content

- [ ] `loco-labo/nvidia-gpu-reference.md` becomes a short page linking to LocoFósil.
- [ ] `loco-labo/machine-setup.md` becomes a short page linking to LocoBase and Fósil Setup.
- [ ] Slim project READMEs to a 20-line pointer at the live site (keep install commands).
- Acceptance: no topic has two canonical explanations.

## Phase 4: tools and missing sources

- [ ] Move LocoBench Picker into LocoBanco as an Astro island fed by real result JSON.
- [ ] Bring LocoMusa and LocoEnsayo site sources into this workspace.
- [ ] Add a shared result schema (`gpu.results[benchmark_id]` with confidence).
- Acceptance: every public surface is versioned here and every benchmark result is
  traceable to a raw run.

## Deferred: single-site consolidation

Only if cross-domain SEO and unified search become the top priority. Cost is high and it
breaks existing URLs. The Phase 2 package gets most of the benefit without the move.
