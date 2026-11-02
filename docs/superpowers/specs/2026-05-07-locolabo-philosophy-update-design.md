# LocoLabo Philosophy Update: Design Spec

**Status:** Draft, awaiting user review
**Date:** 2026-05-07
**Owner:** Michael Borck
**Repo:** loco-labo (the umbrella site for the LocoLab research lab)

---

## 1. Context and goal

### Why this update

LocoLab now has six active projects (LocoLLM, LocoBench, LocoConvoy, LocoEnsayo, LocoAgente, LocoPuente) plus the LocoLabo umbrella. Two recent additions sharpened what the lab is *for*:

- **The MoE-on-a-budget work in LocoBench**: design spec, implementation plan, and 80% of the harness library shipped (commits `fd61834` and `ffaf26f` in `loco-bench`). Establishes "engineering before hardware" as a tangible LocoLab claim: 5 `llama.cpp` flags + system RAM let a $80 used GPU run a 30B-parameter MoE model at reading speed.
- **The conversational harness in LocoAgente**: design spec, full Phase 1 library shipped (27 commits, 63 passing tests, commits `45a8c52` through `38c1234` in `loco-agente`). Establishes "harness > model" as a LocoLab thesis backed by working code.

These additions name principles that were already implicit in the lab's other work (the Keep Asking research thread, LocoLLM's routing thesis, LocoConvoy's multi-GPU experiments) but never lifted to the umbrella level. The umbrella site (`loco-labo/`) needs to articulate the unifying philosophy and surface the artifacts behind it, so a new visitor can see what the lab takes a position on, not just what hardware it owns.

### What "done" looks like

The update is successful if a first-time reader who lands on `index.mdx` can:

1. Identify within 30 seconds that LocoLab takes a position about local AI, not just hosts it
2. Find the thesis in one click from the home page
3. Find the evidence behind the thesis in one more click (findings)
4. See their own audience persona mapped to the relevant principle(s)
5. Understand the bridge (LocoPuente) as the synthesis project that answers "ok but who uses this?"

A returning skeptic can:

6. Test the principles against artifacts: every claim in the thesis links to a status-marked entry in findings, with what would invalidate it
7. See progress over time: findings page entries move through the status ladder as runs complete and papers ship

### Non-goals

- Not a navigation restructure. New pages slot into the existing sidebar without reorganising menus.
- Not a rewrite of operational pages (`getting-started.md`, `machine-setup.md`, `ai-landscape.md`, `ollama-model-guide.md`, `local-llm-tools.md`, `nvidia-gpu-reference.md`, `learning-how-llms-work.md`, `economics-of-local-training.md`, `faq.md`).
- Not a rewrite of the biographical pages (`origin-story.md`, `meet-the-lab.md`, `meet-the-team.md`).
- Not new project landing pages: each project repo owns its own site (locobench.org, locoagente.org, etc.); the umbrella links to them.
- Not "five principles" branding *inside* individual project repos. Cross-references are bidirectional via links, not by injecting umbrella branding into project READMEs.

---

## 2. The five principles + the methodological frame

This is the load-bearing content. The thesis doc is structured around it. Each principle maps to a layer of the stack and to specific projects.

### Methodological frame (opening, not numbered)

The lab's epistemic stance, lifted from the existing `index.mdx` "Mapping the floor" card:

> *Most AI research documents the ceiling. We document the floor, what local small models can do on modest hardware, because most people live there and nobody is doing it honestly.*

This includes the corollary **confidence ≠ competence**: a confident-sounding model is not a correct model, and the lab's job is to make uncertainty legible. Honest baselines, surfaced uncertainty, willingness to publish negative results.

### The five principles

| # | Principle | Layer | Primary projects | Claim |
|---|---|---|---|---|
| **1** | **Engineer before hardware** | Substrate | LocoBench, LocoConvoy | Five flags + system RAM beat buying a bigger GPU. Multi-GPU on consumer PCIe beats waiting for a workstation card. The constraint is engineering effort, not silicon. |
| **2** | **Specialize and harness** | Intelligence | LocoLLM, LocoAgente | A routed swarm of task-specific small models with a good harness around them outcompetes one undifferentiated bigger model on focused work. The engineering around the model matters more than the model. |
| **3** | **Vary, don't average** | Output | LocoAgente, LocoLLM | Frontier models converge to a safe centre; that's why 50 of them write the same boy-and-dragon story. Local small models, properly harnessed, compete on creative tasks because their imprecision *becomes variance*, and variance is what creativity needs. |
| **4** | **Conversation, not delegation** | Interaction | LocoAgente, Keep Asking research, LocoEnsayo | Cognitive offloading is fine: *with* a verification loop. The harness's job is to make the loop cheap: surface uncertainty, expose tool outputs, maintain conversation state. The model handles the mechanical; the human keeps the judgment. |
| **5** | **Bridge experience, locally** | Synthesis | LocoPuente | Frontier *capability* and frontier *experience* are separable. You can give people the tools they get from frontier services (NotebookLM-style document chat, Claude-style assistance) on local infrastructure they own. LocoPuente is the bridge that proves it. |

### Why this set, not another set

- **Five principles, parallel structure**: each is a different layer of the stack (substrate → intelligence → output → interaction → synthesis). Easy to remember, each earns its place.
- **Each backed by built artifacts**: at least one specced/built/measured project per principle. Findings page can point to evidence.
- **Each has an invalidation condition**: if MoE+RAM run shows <10 tok/s, principle 1 weakens. If blind-test readers can't distinguish variants, principle 3 weakens. The principles are testable, not just slogans.
- **No "Built to teach" or "Local and private"**: those are *why* this lab exists (constraints / motivation), not principles about *how local AI works*. They live in `why-local-ai.md` and `audience.md`, not in the thesis doc.
- **No "AI-last" as its own numbered principle**: it shows up as principle 1 and is the meta-frame for the whole thesis. Mentioned by name in the opening, not numbered.
- **Methodological frame stays as the opening, not numbered as a sixth principle**: it's a stance, not a claim about how local AI works.

---

## 3. The two new documents

### the-loco-thesis.md: the manifesto

Approximate length: 700-900 words. Reading time: 4-5 minutes. Tone: punchy, opinionated, matches the existing "deliberate / secondhand / serious" voice. Sits alongside `why-local-ai.md` and `origin-story.md`.

**Outline:**

1. **Opening (~150 words)**: the methodological frame. *"Most AI research documents the ceiling. We document the floor."* Plus the lab's epistemic commitment (confidence ≠ competence; honest baselines; surfaced uncertainty; willingness to publish negative results).

2. **The five principles, one section each (~100-150 words each)**:
   - Each section: claim, why it matters, which projects enact it, one or two concrete examples
   - Linked terms: principle 1 references the MoE+RAM finding; principle 2 references LocoLLM router + LocoAgente harness; principle 3 references variance-engineering FrameStrategy; principle 4 references Keep Asking; principle 5 references LocoPuente PoC

3. **Closing (~100 words)**: what this means for who shows up:
   - Cross-link to `audience.md` (the six personas)
   - Cross-link to `findings.md` (evidence)
   - One-line tagline that distils the whole thesis: *"Local AI as a different bet, not a smaller one."*

**Voice check:** the existing site uses second person sparingly and avoids hype. The thesis can be confident but not preachy. No buzzwords ("game-changing", "revolutionary"). Each principle should be defensible against a hostile reviewer.

### findings.md: the living research notebook

Approximate length: 400-600 words at launch (grows over time). Reading time: 3 minutes initially. Tone: descriptive, almost lab-notebook-like. Sits next to `research.md` (papers) and complements it (artifacts).

**Status-marker ladder** (five rungs, borrowed from `research.md`'s paper-status pattern):

- `claim`: position taken, not yet built
- `architecture`: designed and specced, implementation pending
- `built`: implementation shipped, not yet measured at scale
- `measured`: empirical results, not yet published
- `published`: paper or report public

**Outline:**

```markdown
# What we've discovered

LocoLab claims five principles (see [The Loco Thesis](the-loco-thesis)).
Below are the artifacts — built, measured, or in progress — that those
claims rest on. Each entry has a status marker borrowed from research.md:

- claim — position taken, not yet built
- architecture — designed and specced, implementation pending
- built — implementation shipped, not yet measured at scale
- measured — empirical results, not yet published
- published — paper or report public

This page evolves. Items move down the status ladder as work matures.
```

Then five sections (one per principle). Each section may have multiple entries over time. Per-entry structure:

```markdown
## Engineer before hardware

### Qwen3-30B-A3B at reading speed on a GTX 1060 6GB
- **Status:** architecture (spec written, harness 80% built, hardware-dependent runs pending)
- **Claim:** five llama.cpp flags + system RAM allow a $80 used GPU to run a 30B-parameter MoE model at ~17 tok/s
- **Artifacts:** [LocoBench MoE-on-a-budget spec](https://locobench.org/...), implementation plan, 33 passing harness tests
- **What would invalidate:** if measured tok/s < 10 on the 1060 with the optimised preset
```

**Sections at launch:**

| Principle | First entry | Status at launch |
|---|---|---|
| Engineer before hardware | MoE+RAM trick | architecture |
| Specialize and harness | Conversational harness (LocoAgente Phase 1) | built |
| Specialize and harness | LocoLLM routing thesis | architecture |
| Vary, don't average | FrameStrategy variance engineering | built |
| Conversation, not delegation | Keep Asking Study 1 | architecture |
| Conversation, not delegation | Variant + Uncertainty contract | built |
| Bridge experience, locally | LocoPuente PoC on Ryzen + RTX 3090 | running (= measured) |

**Future additions:** as moe-budget runs complete, the MoE+RAM entry moves from `architecture` to `measured`. Numbers get filled in. As Keep Asking Study 1 runs, that entry moves to `measured`. The page tracks lab progress over time and enacts the methodology by showing work in flight, not just finished claims.

### Cross-references between the two docs

- Thesis links to findings ("see what we've built backing each principle")
- Findings links back to thesis ("see why this principle matters")
- Both link to relevant project repos (locobench.org, locoagente.org, etc.)
- Both link to `research.md` for the formal paper output thread

---

## 4. Targeted edits to existing files

### index.mdx: splash page

**Current state:** 4 cards (six projects / mapping the floor / local and private / built to teach), tagline *"The work is deliberate. The hardware is secondhand. The questions are serious."*

**Changes:**

1. **Replace Card 4 ("Built to teach")** with a new "Five principles" card pointing to the thesis:

```mdx
<Card title="Five principles, one bridge" icon="random">
  Engineer before hardware. Specialize and harness. Vary, don't average. Conversation, not delegation. And LocoPuente — the bridge that brings frontier-equivalent tools onto local infrastructure.
  [Read the thesis →](the-loco-thesis)
</Card>
```

2. **Edit Card 3 ("Local and private by design")**: drop "student privacy", broaden the framing:

```mdx
<Card title="Local and private by design" icon="approve-check">
  Data sovereignty, individual privacy, institutional governance. Local inference is not a workaround for policy constraints — it is the only fully compliant path for many organisations, and the only honest answer for anyone who doesn't want their data on someone else's machine.
</Card>
```

3. **Add a tagline subhead** to the hero block:

```yaml
hero:
  tagline: |
    The work is deliberate. The hardware is secondhand. The questions are serious.

    Local AI as a different bet, not a smaller one.
```

4. **Add a third hero action button** ("What we've found") alongside the existing "Meet the Lab" and "The Projects":

```yaml
    - text: What we've found
      link: /docs/findings/
      icon: external
      variant: minimal
```

That's it for `index.mdx`: no rewrite, just four small edits that surface the new docs and sharpen the positioning. Cards 1 ("Six active projects") and 2 ("Mapping the floor") stay exactly as they are.

### why-local-ai.md: add an offensive section

**Current state:** defensive case for local AI. Cloud-vs-local mental model, market shift, where local excels (boring use cases) vs struggles, then a closing.

**Change:** insert a new section between "Where Local AI Excels (and Where It Does Not)" and the existing closing. Title: **"Where local AI *wins* (not just where it doesn't lose)"**.

~250 words. Three sub-points, each one paragraph:

- **Creative work, because variance > precision.** Frontier models converge to a safe centre; harnessed local models compete *because* they don't. Links to thesis principle 3.
- **Verified offloading, where conversation beats delegation.** Local AI plus a good harness gives the human a verification loop frontier APIs don't bother surfacing. Links to thesis principle 4.
- **Frontier-equivalent UX, on hardware you own.** LocoPuente exists to prove that the *experience* of frontier tools (NotebookLM, Claude.ai, etc.) is separable from their cost and data exposure. Links to thesis principle 5.

### research.md: cross-links + Principles column

**Current state:** lists papers (Active / Planned / Published) with status.

**Changes:**

1. **Add an opening framing line** under the existing intro:

> *Each paper enacts one or more of the lab's [five principles](the-loco-thesis). The artifacts behind these papers, built but not yet published, live in [findings](findings).*

2. **Add a "Principles" column** to each table (Active, Planned, Published). Each paper is tagged with the short principle name(s) it enacts:

| Paper | Description | Status | Principles |
|-------|-------------|--------|------------|
| Cognitive Strategy Transfer | ... | In progress | conversation; vary |
| Keep Asking: Study 1 | ... | In progress | conversation |
| Keep Asking: Study 2 | ... | Planned | conversation |
| PCIe Multi-GPU Inference Scaling | ... | Planned | engineer |
| Context Length Effects on SLMs | ... | Planned | specialize |
| Perceived Intelligence vs Token Rate | ... | Planned | confidence (methodological) |

Principle short names: `engineer`, `specialize`, `vary`, `conversation`, `bridge`, plus methodological tag for papers that are about epistemic stance rather than technical claims.

### audience.md: light touch (one sentence per persona)

**Current state:** six personas (Budget Rebel, Tinkerer, Researcher, plus three not-yet-read), each with their own entry points.

**Change:** for each persona, add one sentence pointing to the relevant principle or to the bridge. No restructure, just connective tissue. Example shape:

- **Budget Rebel:** add "...and the [bridge](the-loco-thesis#bridge-experience-locally) is built for you specifically, the user who wants frontier tools without frontier costs."
- **Tinkerer:** add "...the harness is the part you'll most enjoy taking apart; see [principle 2: specialize and harness](the-loco-thesis#specialize-and-harness)."
- **Researcher:** add "...our methodology is laid out in [the thesis](the-loco-thesis), with honest baselines, surfaced uncertainty, status markers on every claim."

The implementation phase will read the three remaining personas in the existing file and add analogous one-sentence connective tissue for each.

---

## 5. Scope summary

| File | Change | Net new content |
|---|---|---|
| `src/content/docs/the-loco-thesis.md` | New | ~700-900 words |
| `src/content/docs/findings.md` | New | ~400-600 words at launch |
| `src/content/docs/index.mdx` | Replace Card 4, edit Card 3 (drop "student privacy"), add subhead, add hero action | ~30 lines |
| `src/content/docs/why-local-ai.md` | Insert "Where local AI wins" section | ~250 words |
| `src/content/docs/research.md` | Add framing line + Principles column on tables | ~10 lines |
| `src/content/docs/audience.md` | One sentence per persona (6 personas) | ~6 sentences |

**Total:** 6 files touched, 2 new + 4 edited. ~1500 words of new content, ~300 lines of net change.

---

## 6. Out of scope (parking lot)

Captured for visibility but **not in this update:**

- **Visual diagram of the four-axis stack**: could supplement the current 3-pillar image. Useful but additive; defer until empirical results from MoE+RAM and harness work mature.
- **Per-principle deep-dive pages**: if `the-loco-thesis.md` grows over time, individual principles might warrant their own pages. Wait until evidence accumulates before splitting.
- **Translation to Spanish**: LocoLab's Spanish naming hints at this but it's a separate project, not philosophy work.
- **Update the index.mdx hero image (`lab.svg`)** to reflect the bridge framing visually: design work, separate from this content update.
- **External-facing pitch deck or one-pager**: a "what is LocoLab?" PDF for grant applications, talks, etc. Different artifact, separate concern.
- **Footer / about-this-site updates**: if the philosophy lands well, the footer / about pages could echo the tagline. Defer to see whether thesis lands first.

---

## 7. Risks and mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Thesis doc reads as preachy or over-confident | Medium | Voice check against `why-local-ai.md` and `origin-story.md`; have the implementer flag any line that wouldn't pass a hostile reviewer; revise toward defensible claims with linked artifacts. |
| Findings page launches looking thin | Medium | The status-marker ladder is the answer: readers see "architecture" or "built" entries and understand work is in flight, not absent. The page is a living artifact, not a launch document. |
| Principle naming clashes with how individual project repos describe themselves | Low | Cross-references are link-based, not name-injection-based. Project repos retain their own framing; the umbrella adds the principle layer on top. |
| MoE+RAM run shows <10 tok/s, weakening principle 1 | Low-medium | Honest reporting matches the methodology. The findings page entry would update from "architecture (claim: 17 tok/s)" to "measured (X tok/s, claim partially refuted)". The principle stands or falls on evidence. |
| Reviewers (academic or external) find the principles set too business-flavoured | Low | The principles are derived from technical work in the lab, not borrowed from industry framing. The "Conversation, not delegation" principle in particular ties directly to the Cognitive Strategy Transfer + Keep Asking research thread, which is academically grounded. |

---

## 8. Cross-project impact

This update changes loco-labo only. It does **not** touch:

- Individual project repos (locobench.org, locoagente.org, locollm.org, etc.): they keep their own framing
- Project READMEs: the umbrella links to them but doesn't ask them to change

When a project ships a new finding worth surfacing on `findings.md`, the umbrella site's findings page is the place to add an entry, not the project's own README. Bidirectional link maintenance is a small ongoing cost; the alternative (each project replicates the principles) is worse.

---

## 9. References

- Existing index page: `loco-labo/src/content/docs/index.mdx`
- Existing why-local-ai: `loco-labo/src/content/docs/why-local-ai.md`
- Existing research: `loco-labo/src/content/docs/research.md`
- Existing audience: `loco-labo/src/content/docs/audience.md`
- LocoBench MoE-on-a-budget spec: `loco-bench/docs/superpowers/specs/2026-05-06-locobench-moe-budget-design.md`
- LocoBench MoE-on-a-budget plan: `loco-bench/docs/superpowers/plans/2026-05-06-locobench-moe-budget.md`
- LocoAgente conversational harness spec: `loco-agente/docs/superpowers/specs/2026-05-07-conversational-harness-design.md`
- LocoAgente Phase 1 plan: `loco-agente/docs/superpowers/plans/2026-05-07-conversational-harness-phase1.md` and `-part2.md`
- LocoAgente Phase 1 implementation commits: `0394a39..38c1234` in `loco-agente`

---

## Appendix A: Glossary

- **The five principles**: the lab's articulated positions: engineer before hardware, specialize and harness, vary don't average, conversation not delegation, bridge experience locally.
- **The methodological frame**: the lab's epistemic stance: map the floor honestly, confidence ≠ competence, status markers on every claim.
- **Status-marker ladder**: five rungs (claim / architecture / built / measured / published) borrowed from `research.md` paper-status pattern, used to indicate maturity of each finding.
- **The bridge**: LocoPuente's framing as the synthesis project that delivers frontier-equivalent UX on local infrastructure.
- **The thesis**: `the-loco-thesis.md`, the new manifesto page articulating the five principles.
- **Findings**: `findings.md`, the new living research notebook listing artifacts behind each principle with status markers.
