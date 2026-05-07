# LocoLabo Philosophy Update Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add two new pages (`the-loco-thesis.md`, `findings.md`) and surgically update four existing pages (`index.mdx`, `why-local-ai.md`, `research.md`, `audience.md`) so that LocoLabo articulates the five-principle philosophy and surfaces the artifacts behind it.

**Architecture:** Pure docs work in an Astro/Starlight site at `/Users/michael/Projects/loco-lab/loco-labo`. Each task creates or edits one markdown file, builds the site to verify Astro accepts the change, and commits. No code; no tests; the build is the test.

**Tech Stack:** Astro + Starlight (Markdown/MDX content). Build via `npm run build`. Local dev via `npm run dev`.

**Spec reference:** `docs/superpowers/specs/2026-05-07-locolabo-philosophy-update-design.md` (commit `ae57a90`).

---

## File structure

### New files

| Path | Responsibility |
|---|---|
| `src/content/docs/the-loco-thesis.md` | Manifesto: methodological frame + five principles + closing |
| `src/content/docs/findings.md` | Living research notebook: artifacts behind each principle, with status markers |

### Modified files

| Path | Change |
|---|---|
| `src/content/docs/index.mdx` | Replace Card 4 ("Built to teach") with "Five principles" card; edit Card 3 to drop "student privacy"; add tagline subhead; add a third hero action button |
| `src/content/docs/why-local-ai.md` | Insert new "Where local AI *wins*" section between the existing "Where Local AI Excels" section and the closing |
| `src/content/docs/research.md` | Add framing line + "Principles" column on the Active and Planned tables |
| `src/content/docs/audience.md` | Add one connective-tissue sentence per persona (six personas total) |

### Files NOT touched

`origin-story.md`, `getting-started.md`, `machine-setup.md`, `ai-landscape.md`, `meet-the-lab.md`, `meet-the-team.md`, `ollama-model-guide.md`, `local-llm-tools.md`, `nvidia-gpu-reference.md`, `learning-how-llms-work.md`, `economics-of-local-training.md`, `faq.md`. Per spec §1 non-goals.

---

## Phase 0: Pre-flight check

### Task 0: Verify the site builds clean before any changes

**Files:** none modified — runtime check only.

- [ ] **Step 1: Verify dependencies are installed**

```bash
cd /Users/michael/Projects/loco-lab/loco-labo
ls node_modules/@astrojs 2>/dev/null | head -3
```

Expected: directory listing showing Astro packages installed. If empty or missing, run `npm install` first.

- [ ] **Step 2: Build the site to establish the green baseline**

```bash
npm run build 2>&1 | tail -20
```

Expected: build succeeds (`X pages built in Yms`). No errors, no warnings about broken links. If the build fails on existing content, stop and surface to the user — fixing pre-existing breakage is out of scope for this plan.

- [ ] **Step 3: Confirm git working tree is clean**

```bash
git status --short
```

Expected: empty output (no uncommitted changes). If anything is dirty, commit or stash before proceeding.

No commit for this task — it's a baseline verification.

---

## Phase 1: New files

### Task 1: Write `the-loco-thesis.md`

**Files:**
- Create: `src/content/docs/the-loco-thesis.md`

- [ ] **Step 1: Write the file with this exact content**

Write to `src/content/docs/the-loco-thesis.md`:

````markdown
---
title: "The Loco Thesis"
description: The five principles LocoLab takes positions on, and the methodological frame that anchors them.
---

> *Most AI research documents the ceiling. We document the floor — what local small models can actually do on modest hardware — because most people live there and nobody is doing it honestly.*

That stance is the lab's epistemic commitment. It governs everything below. It also has a corollary worth naming explicitly: **confidence is not competence.** A confident-sounding model is not a correct model. Our job is to make uncertainty legible — through honest baselines, surfaced failure modes, status markers on every claim, and a willingness to publish negative results. We don't trust round numbers and we don't trust hype, including our own.

Below are the five positions LocoLab takes — claims about how local AI works, each backed by built artifacts (see [findings](findings)) and each with an explicit invalidation condition. They are in stack order: substrate, intelligence, output, interaction, synthesis.

---

## Map the floor honestly

We commit to three things across every project:

- **Honest baselines.** Numbers are measured on the actual hardware they claim to characterise, not extrapolated. Negative results are reported as data.
- **Surfaced uncertainty.** Every claim carries an invalidation condition. Every output that goes through the harness carries verification hooks.
- **Status markers.** Findings are tagged `claim` / `architecture` / `built` / `measured` / `published`. Nothing is promoted up the ladder without evidence.

The five principles below all rest on this. They are testable, not aspirational.

---

## Engineer before hardware

The cheapest performance is the performance you didn't need to hire. Five `llama.cpp` flags + system RAM let an eight-year-old GTX 1060 run a 30-billion-parameter Mixture-of-Experts model at reading speed. Multi-GPU on consumer PCIe x16 lets a 64GB VRAM aggregate cost less than one workstation card. The constraint, in 2026, is engineering effort, not silicon.

This principle is enacted by **[LocoBench](https://locobench.org)** (the MoE-on-a-budget work measures what flags + RAM unlock per VRAM tier) and **[LocoConvoy](https://lococonvoy.org)** (multi-GPU experiments on full-bandwidth PCIe, on an open frame for rapid card swaps).

*What would invalidate this claim:* if engineering tricks plateau early — if no flag combination on the GTX 1060 reaches reading speed — the principle weakens. The MoE+RAM run is the empirical test in flight.

---

## Specialize and harness

A routed swarm of task-specific small models, with a good harness around them, outcompetes one undifferentiated bigger model on focused work. The engineering around the model matters more than the model. Frontier providers know this — their systems are mostly harness — but they don't share the harness, only the model. We build both.

This principle is enacted by **[LocoLLM](https://locollm.org)** (adapter training, routing, specialist selection) and **[LocoAgente](https://locoagente.org)** (the conversational harness library shipped in Phase 1: 27 commits, 63 passing tests, four orchestration patterns, three Context profile bundles). Both treat the model as one component in a larger structure.

*What would invalidate this claim:* if a single Qwen3-4B with no routing matches a routed swarm of specialist 4B adapters on a focused benchmark suite, the principle weakens. The LocoLLM eval pipeline is where this gets tested.

---

## Vary, don't average

Frontier models converge to a safe centre. That's why if you ask 50 of them to write a story about a boy and a dragon, you get 50 stories with the same shape. They erode variance — and variance is what creativity needs.

Local small models, properly harnessed, compete on creative tasks for the inverted reason. Their imprecision *becomes variance*, and the harness's job is to channel that variance deliberately rather than fight it. This is what LocoAgente's `FrameStrategy` does: identity frames, discipline frames, constraint inversions — N variants engineered to differ, not N samples hoping to differ.

*What would invalidate this claim:* if a blind-test reader cannot reliably distinguish the variants from a single small-model run with framed prompts, the principle weakens. The Perspective Debate demo is the empirical test.

---

## Conversation, not delegation

Cognitive offloading is not surrender. It's amplification — *with* a verification loop. When you buy items at a shop, you delegate the addition to the till. When the total seems wrong, you ask to check the prices. That's the right cognitive shape: delegate the mechanical, keep the judgment, make the verification loop cheap.

The harness's job is to make that loop cheap: surface uncertainty, expose tool outputs, maintain conversation state so the human can push back without re-explaining. The model handles the mechanical; the human keeps the smell-test.

This principle is enacted by **[LocoAgente](https://locoagente.org)** (the `Variant` + `Uncertainty` contract bakes verification hooks into every output) and the **Keep Asking** research thread (Study 1: does the conversational nudge shift students from passive delegation to active conversation? Study 2: does conversation compensate for model quality?).

*What would invalidate this claim:* if the Keep Asking nudge studies show no effect on outcomes, or if the harness's verification hooks don't reduce hallucination harm, the principle weakens.

---

## Bridge experience, locally

Frontier *capability* and frontier *experience* are separable. Users don't want raw capability — they want the tools their friends have on the cloud (NotebookLM-style document chat, Claude-style coding assistance, voice and image generation, research workflows) running on infrastructure they own.

**[LocoPuente](https://locopuente.org)** is the bridge: a full local AI service stack that delivers frontier-equivalent UX without frontier costs or frontier data exposure. The bridge is the synthesis project. Without it, the rest of the stack is plumbing without a faucet. With it, the rest of the stack adds up to something a non-researcher actually wants.

*What would invalidate this claim:* if users with full LocoPuente access still prefer the cloud equivalent for non-privacy-sensitive use, the bridge isn't bridging. User feedback on the running PoC is the empirical test.

---

## What this means for who shows up here

Each [audience persona](audience) maps to one or more principles most directly:

- The **Budget Rebel** lives at the bridge. Frontier tools, locally, with no per-token bill.
- The **Tinkerer** lives at *specialize and harness*. The most rewarding part of the stack to take apart.
- The **Researcher** lives at the methodological frame and at every principle's invalidation condition.
- The **Educator** lives at *conversation, not delegation* — the pedagogical heart of the lab.
- The **Vault** lives at the bridge — capability and privacy in one stack you own.
- The **Scrapper** lives at *engineer before hardware*. Five flags beat a bigger card.

See [findings](findings) for the artifacts each principle rests on.

**Local AI as a different bet, not a smaller one.**
````

- [ ] **Step 2: Verify the site still builds**

```bash
npm run build 2>&1 | tail -10
```

Expected: build succeeds; the new page is included in the output (`X pages built` should be one higher than the Phase 0 baseline).

- [ ] **Step 3: Spot-check the rendered page**

```bash
ls dist/the-loco-thesis 2>/dev/null
```

Expected: `index.html` exists in that directory. (Starlight emits one HTML file per slug.) If `dist/` doesn't exist after build, check `npm run build` output for errors.

- [ ] **Step 4: Commit**

```bash
git add src/content/docs/the-loco-thesis.md
git commit -m "Add the-loco-thesis: five principles + methodological frame"
```

---

### Task 2: Write `findings.md`

**Files:**
- Create: `src/content/docs/findings.md`

- [ ] **Step 1: Write the file with this exact content**

Write to `src/content/docs/findings.md`:

````markdown
---
title: "What We've Discovered"
description: The artifacts behind each principle, with status markers — a living research notebook that evolves as work matures.
---

LocoLab claims [five principles](the-loco-thesis). Below are the artifacts — built, measured, or in progress — that those claims rest on. Each entry has a status marker borrowed from [research](research) (where papers carry similar markers):

- `claim` — position taken, not yet built
- `architecture` — designed and specced, implementation pending
- `built` — implementation shipped, not yet measured at scale
- `measured` — empirical results, not yet published
- `published` — paper or report public

This page evolves. Items move down the status ladder as work matures. Failed claims stay on the page with their evidence — that's the point.

---

## Engineer before hardware

### Qwen3-30B-A3B at reading speed on a GTX 1060 6GB

- **Status:** `architecture`
- **Claim:** five `llama.cpp` flags (`--n-cpu-moe`, `--no-mmap`, `--mlock`, `--cache-type-k q4_0`, `--cache-type-v q3_0`) plus 24-64GB of system RAM let a $80 used GTX 1060 run Qwen3-30B-A3B at ~17 tokens/sec
- **Artifacts:** [LocoBench MoE-on-a-budget design spec](https://locobench.org); implementation plan; Python harness library (33+ passing tests covering config loading, server boot, llama-bench wrapper, hardware fingerprinting); 17 cell configs across 4 VRAM tiers ready to run
- **What would invalidate:** if measured `tg128` < 10 tok/s on the 1060 with the optimised preset, or if the article's claim doesn't replicate

---

## Specialize and harness

### LocoAgente conversational harness — Phase 1

- **Status:** `built`
- **Claim:** a routed harness around small models (four-subsystem architecture: Orchestration / Context / Tools / Inference) makes a Qwen3-4B genuinely useful as a thinking partner for tasks where frontier models converge to the average
- **Artifacts:** [LocoAgente design spec](https://locoagente.org); Phase 1 library (27 commits, 63 tests at 98% coverage on `harness.core`); E primitive `generate_variants` enforcing `n >= 2`; four orchestration patterns (`SinglePass`, `DebatePattern`, `SynthesisPattern`, `IterativeRefinement`); three Context profile bundles (business, academic, writing)
- **What would invalidate:** if a blind-test reader cannot reliably distinguish the three frames in a Perspective Debate output (frame collapse on small models)

### LocoLLM routing thesis

- **Status:** `architecture`
- **Claim:** a routed swarm of task-specific Qwen3-4B adapters outperforms a single undifferentiated Qwen3-4B on focused tasks (math, code, summarisation, etc.)
- **Artifacts:** [LocoLLM repository](https://locollm.org); QLoRA training pipeline; routing layer; partial benchmark suite
- **What would invalidate:** if the router's task-classification accuracy drops below the gain from specialisation, the system is net-negative versus the unrouted baseline

---

## Vary, don't average

### `FrameStrategy` deliberate variance engineering

- **Status:** `built`
- **Claim:** N variants engineered to differ (identity frames, discipline frames, constraint inversions) produce more useful divergent output than N samples hoping to differ
- **Artifacts:** four `FrameStrategy` implementations in `harness/frames.py` (`IdentityFrames`, `DisciplineFrames`, `TemperatureLadder`, `ConstraintInversion`); test suite verifying each strategy produces structurally distinct prompts; documented variance-collapse warning on `TemperatureLadder` for narrow temperature spreads
- **What would invalidate:** if the four strategies all collapse to the same output distribution on small models — i.e., engineered framing doesn't actually channel variance through the model — the principle is just an aesthetic claim

---

## Conversation, not delegation

### `Variant` + `Uncertainty` verification contract

- **Status:** `built`
- **Claim:** every harness output carries a rationale and surfaced uncertainty (load-bearing `flags` + `verification_hooks`; auxiliary `confidence`); singular outputs are forbidden at the primitive level; the human's verification loop is cheap because the harness does the prep work
- **Artifacts:** `Variant` and `Uncertainty` dataclasses in `harness/core.py`; XML tag parser enforcing required `<text>` and `<rationale>`; `CalibrationLog` recording user picks/rejects/edits as JSONL for downstream analysis
- **What would invalidate:** if users routinely ignore the `verification_hooks` field — i.e., the harness produces hooks but they're not the right hooks — the principle is performative not functional

### Keep Asking — Study 1: Does the Nudge Work?

- **Status:** `architecture`
- **Claim:** a conversational nudge shifts students from passive delegation to active conversation and improves task outcomes (using frontier models, to isolate the nudge effect from model quality)
- **Artifacts:** research design under active development; see [research](research) for the full thread (Cognitive Strategy Transfer, DSR AI Education Simulation, Keep Asking Studies 1 and 2)
- **What would invalidate:** if nudged students don't differ from un-nudged controls on either conversation patterns or outcomes

---

## Bridge experience, locally

### LocoPuente PoC

- **Status:** `running` (= `measured` in operational terms)
- **Claim:** a single mid-range machine (Ryzen 5 2600 + RTX 3090 24GB) running an integrated stack (primary LLM, cited search, image generation, voice, research tooling) delivers frontier-equivalent UX for everyday user tasks at zero cloud cost
- **Artifacts:** [LocoPuente service](https://locopuente.org) running on the Puente machine; browser-accessible LAN deployment; usable today by lab members and visitors
- **What would invalidate:** if users with full LocoPuente access still prefer the cloud equivalent for non-privacy-sensitive work, the bridge isn't bridging
````

- [ ] **Step 2: Verify the site still builds**

```bash
npm run build 2>&1 | tail -10
```

Expected: build succeeds; new page included.

- [ ] **Step 3: Verify cross-links resolve**

The findings page links to `the-loco-thesis` and `research`. Both should exist after Task 1 + the existing `research.md`. Spot-check by viewing the built HTML or by running `npm run dev` and clicking through.

- [ ] **Step 4: Commit**

```bash
git add src/content/docs/findings.md
git commit -m "Add findings: living research notebook with status-marked artifacts per principle"
```

---

## Phase 2: Edited files

### Task 3: Edit `index.mdx` — replace Card 4, edit Card 3, add subhead, add hero action

**Files:**
- Modify: `src/content/docs/index.mdx`

The current file (per spec §4) has 4 cards: Six active projects / Mapping the floor / Local and private by design / Built to teach. We replace Card 4, edit Card 3, add a tagline subhead, and add a third hero action button.

- [ ] **Step 1: Read the current file to confirm structure**

```bash
cat src/content/docs/index.mdx
```

Expected: shows the existing 4 cards in a `<CardGrid stagger>` block plus the hero frontmatter with `actions` listing two buttons ("Meet the Lab" and "The Projects").

- [ ] **Step 2: Edit the hero tagline to add the subhead**

In `src/content/docs/index.mdx`, find this line in the frontmatter:

```yaml
  tagline: The work is deliberate. The hardware is secondhand. The questions are serious.
```

Replace with:

```yaml
  tagline: |
    The work is deliberate. The hardware is secondhand. The questions are serious.

    Local AI as a different bet, not a smaller one.
```

(YAML pipe `|` preserves newlines; the blank line in the tagline becomes a paragraph break in Starlight's hero rendering.)

- [ ] **Step 3: Add a third hero action button**

In `src/content/docs/index.mdx`, find the existing `actions:` block in the frontmatter:

```yaml
  actions:
    - text: Meet the Lab
      link: /docs/meet-the-lab/
      icon: right-arrow
      variant: primary
    - text: The Projects
      link: /docs/research/
      icon: external
      variant: secondary
```

Add a third entry at the end of the list:

```yaml
    - text: What we've found
      link: /docs/findings/
      icon: external
      variant: minimal
```

Final `actions:` block has three entries.

- [ ] **Step 4: Edit Card 3 to drop "student privacy" and broaden**

Find the existing Card 3:

```mdx
  <Card title="Local and private by design" icon="approve-check">
    Data sovereignty, student privacy, institutional governance. Local inference is not a workaround for policy constraints — it is the only fully compliant path for many organisations.
  </Card>
```

Replace with:

```mdx
  <Card title="Local and private by design" icon="approve-check">
    Data sovereignty, individual privacy, institutional governance. Local inference is not a workaround for policy constraints — it is the only fully compliant path for many organisations, and the only honest answer for anyone who doesn't want their data on someone else's machine.
  </Card>
```

- [ ] **Step 5: Replace Card 4 ("Built to teach") with the principles card**

Find the existing Card 4:

```mdx
  <Card title="Built to teach" icon="open-book">
    Students learn by building. Adapter training, evaluation pipelines, routing systems, deployment stacks — real engineering on real problems, not toy projects.
  </Card>
```

Replace with:

```mdx
  <Card title="Five principles, one bridge" icon="random">
    Engineer before hardware. Specialize and harness. Vary, don't average. Conversation, not delegation. And LocoPuente — the bridge that brings frontier-equivalent tools onto local infrastructure.
    [Read the thesis →](the-loco-thesis)
  </Card>
```

- [ ] **Step 6: Verify the site builds**

```bash
npm run build 2>&1 | tail -10
```

Expected: build succeeds. Cards 1 and 2 unchanged; Cards 3 and 4 have new copy; tagline has subhead; hero has third action button.

- [ ] **Step 7: Spot-check that no "student" reference remains in the cards**

```bash
grep -i 'student' src/content/docs/index.mdx
```

Expected: no output. (The two original references — "student privacy" in Card 3 and "Students learn by building" in Card 4 — are gone.)

- [ ] **Step 8: Commit**

```bash
git add src/content/docs/index.mdx
git commit -m "index: surface five principles + findings; broaden privacy framing"
```

---

### Task 4: Edit `why-local-ai.md` — insert the offensive section

**Files:**
- Modify: `src/content/docs/why-local-ai.md`

Per spec §4: insert a new section between the existing "Where Local AI Excels (and Where It Does Not)" section and the existing closing.

- [ ] **Step 1: Locate the existing "Where Local AI Excels" section's end**

```bash
grep -n '^---' src/content/docs/why-local-ai.md
```

Expected: this returns line numbers of horizontal rule separators (`---`). Find the separator that comes immediately after the section ending with the bolded line *"Well-defined, high-volume, privacy-sensitive tasks are the real goldmine."* (or whatever the section's closing emphasis is). The new section gets inserted *after* this separator.

If the file structure has changed since the spec was written, locate the section by its heading: search for `## Where Local AI Excels` and find the next `---` separator after it.

- [ ] **Step 2: Insert the new section immediately after the separator**

Insert this content between the "Where Local AI Excels" section's closing `---` and the next section that follows:

```markdown
## Where local AI *wins* (not just where it doesn't lose)

The "matches cloud on focused tasks" framing above is true and useful. It is also defensive. There are tasks where local AI doesn't just match cloud — it *outperforms* it, for structural reasons rather than incidental ones.

**Creative work, because variance > precision.** Frontier models are trained to produce safe, average outputs. Ask 50 of them to write a story about a boy and a dragon and you get 50 stories with the same shape. Local small models, with a [variance-engineering harness](the-loco-thesis), compete on creative tasks because their imprecision *becomes variance*, and variance is what creativity needs. We're not trying to make small models precise — we're channelling what they already do.

**Verified offloading, where conversation beats delegation.** Cognitive offloading without verification is surrender. With verification, it's amplification. Frontier APIs typically don't bother surfacing the seams: you get a confident answer and the loop closes. A [good harness](the-loco-thesis) makes the verification cheap — surfacing uncertainty, exposing tool outputs, maintaining conversation state so you can push back without re-explaining. Local AI plus a good harness gives the human a verification loop frontier APIs don't.

**Frontier-equivalent UX, on hardware you own.** Frontier *capability* and frontier *experience* are separable. The tools users want — NotebookLM-style document chat, Claude-style coding assistance, voice, image generation — can be delivered by [a stack you control](the-loco-thesis). LocoPuente exists to prove this. The argument isn't "local is good enough." The argument is "local is the right shape for the use case."

---
```

(Note the trailing `---` — preserve the separator pattern of the file.)

- [ ] **Step 3: Verify the site builds**

```bash
npm run build 2>&1 | tail -10
```

Expected: build succeeds. Three new links to `the-loco-thesis` resolve cleanly.

- [ ] **Step 4: Commit**

```bash
git add src/content/docs/why-local-ai.md
git commit -m "why-local-ai: add 'where local wins' offensive section"
```

---

### Task 5: Edit `research.md` — framing line + Principles column

**Files:**
- Modify: `src/content/docs/research.md`

- [ ] **Step 1: Read the current intro to locate insertion point**

```bash
head -20 src/content/docs/research.md
```

Expected: shows the title, frontmatter, and an intro paragraph beginning *"LocoLab's research explores how local AI can support education..."*.

- [ ] **Step 2: Insert the framing line under the existing intro**

In `src/content/docs/research.md`, find the existing intro paragraph (currently one paragraph ending *"...published papers become public with links to the full text."*). Add a new paragraph immediately after it:

```markdown
Each paper enacts one or more of the lab's [five principles](the-loco-thesis). The artifacts behind these papers — built but not yet published — live in [findings](findings).
```

- [ ] **Step 3: Add a "Principles" column to the Active table**

Find the existing Active table:

```markdown
| Paper | Description | Status |
|-------|-------------|--------|
| **Cognitive Strategy Transfer** | Framework for understanding how cognitive strategies transfer across AI-assisted learning contexts (4-paper series) | In progress |
| **DSR AI Education Simulation** | Design science research on AI-powered education simulations | In progress |
| **Keep Asking — Study 1: Does the Nudge Work?** | Using frontier models, test whether a conversational nudge shifts students from passive delegation to active conversation and improves task outcomes | In progress |
| **Keep Asking — Study 2: Does Conversation Compensate for Model Quality?** | Test whether nudged students using a weak local model can match un-nudged students using a frontier model — reframing AI equity as a habits problem | Planned (pending Study 1) |
```

Replace with the same table plus a "Principles" column:

```markdown
| Paper | Description | Status | Principles |
|-------|-------------|--------|------------|
| **Cognitive Strategy Transfer** | Framework for understanding how cognitive strategies transfer across AI-assisted learning contexts (4-paper series) | In progress | conversation; vary |
| **DSR AI Education Simulation** | Design science research on AI-powered education simulations | In progress | conversation; methodological |
| **Keep Asking — Study 1: Does the Nudge Work?** | Using frontier models, test whether a conversational nudge shifts students from passive delegation to active conversation and improves task outcomes | In progress | conversation |
| **Keep Asking — Study 2: Does Conversation Compensate for Model Quality?** | Test whether nudged students using a weak local model can match un-nudged students using a frontier model — reframing AI equity as a habits problem | Planned (pending Study 1) | conversation; vary |
```

- [ ] **Step 4: Add a "Principles" column to the Planned table**

Find the existing Planned table:

```markdown
| Paper | Description |
|-------|-------------|
| **PCIe Multi-GPU Inference Scaling** | Does VRAM tier or architecture generation matter more? GTX vs RTX scaling comparison on consumer hardware ([experiment design](https://lococonvoy.org/docs/tiered-inference-experiment/)) |
| **Context Length Effects on Small Language Models** | How context window size affects small language model performance on consumer hardware |
| **Perceived Intelligence vs Token Rate** | Relationship between perceived AI intelligence and token generation speed |
```

Replace with the same table plus a "Principles" column:

```markdown
| Paper | Description | Principles |
|-------|-------------|------------|
| **PCIe Multi-GPU Inference Scaling** | Does VRAM tier or architecture generation matter more? GTX vs RTX scaling comparison on consumer hardware ([experiment design](https://lococonvoy.org/docs/tiered-inference-experiment/)) | engineer |
| **Context Length Effects on Small Language Models** | How context window size affects small language model performance on consumer hardware | specialize |
| **Perceived Intelligence vs Token Rate** | Relationship between perceived AI intelligence and token generation speed | methodological |
```

- [ ] **Step 5: Verify the site builds and tables render**

```bash
npm run build 2>&1 | tail -10
```

Expected: build succeeds.

- [ ] **Step 6: Commit**

```bash
git add src/content/docs/research.md
git commit -m "research: link to thesis + findings; tag papers with enacted principles"
```

---

### Task 6: Edit `audience.md` — one connective sentence per persona

**Files:**
- Modify: `src/content/docs/audience.md`

The file has six personas (in this order): Budget Rebel, Tinkerer, Researcher, Educator, Vault, Scrapper. Each currently ends with a `**Your entry points:**` bulleted list. Add a new sentence after each persona's entry-points list, before the next `---` separator.

- [ ] **Step 1: Read the file to confirm persona order and structure**

```bash
grep -n '^## ' src/content/docs/audience.md
```

Expected: six matching lines (each persona is an `## ` heading with an emoji prefix). The order should be: Budget Rebel, Tinkerer, Researcher, Educator, Vault, Scrapper.

- [ ] **Step 2: Add connective sentence after Budget Rebel's entry points**

In `src/content/docs/audience.md`, find the Budget Rebel section. Immediately after the third `[AI Landscape](ai-landscape)` bullet and before the next `---` separator, add:

```markdown
And the [bridge](the-loco-thesis) is built for you specifically — frontier-equivalent tools without frontier costs is the bridge's whole job.
```

- [ ] **Step 3: Add connective sentence after Tinkerer's entry points**

After the Tinkerer's `[Getting Started](getting-started)` bullet and before the next `---` separator, add:

```markdown
The harness is the part you'll most enjoy taking apart — see [the thesis](the-loco-thesis) for why the engineering around the model matters more than the model.
```

- [ ] **Step 4: Add connective sentence after Researcher's entry points**

After the Researcher's `[Research](research)` bullet and before the next `---` separator, add:

```markdown
Our [methodology](the-loco-thesis) is laid out in the thesis: honest baselines, surfaced uncertainty, status markers on every claim. And [findings](findings) shows you what's measured, what's claimed, and what would invalidate each.
```

- [ ] **Step 5: Add connective sentence after Educator's entry points**

After the Educator's `[Why Local AI](why-local-ai)` bullet and before the next `---` separator, add:

```markdown
The "[conversation, not delegation](the-loco-thesis)" principle is the pedagogical heart of the lab — it's what the Cognitive Strategy Transfer and Keep Asking research threads are about, and why the rehearsal environments are designed the way they are.
```

- [ ] **Step 6: Add connective sentence after Vault's entry points**

After the Vault's `[Why Local AI](why-local-ai)` bullet and before the next `---` separator, add:

```markdown
Local AI is not just "private by policy" but [private by architecture](the-loco-thesis) — the bridge synthesises capability and privacy in a single stack you own.
```

- [ ] **Step 7: Add connective sentence after Scrapper's entry points**

After the Scrapper's `[Economics of Local Training](economics-of-local-training)` bullet and before the next `---` separator (or before the closing "Not sure where to start?" section if it follows directly), add:

```markdown
The whole "[engineer before hardware](the-loco-thesis)" principle was built for you. Five `llama.cpp` flags + system RAM letting an eight-year-old GTX 1060 run a 30-billion-parameter MoE model is the kind of finding the floor produces.
```

- [ ] **Step 8: Verify the site builds and the file structure is preserved**

```bash
npm run build 2>&1 | tail -10
grep -c '^## ' src/content/docs/audience.md
```

Expected: build succeeds; second command returns `6` (still six persona sections, no accidental restructure).

- [ ] **Step 9: Commit**

```bash
git add src/content/docs/audience.md
git commit -m "audience: connective tissue from each persona to relevant principle"
```

---

## Phase 3: Final integration

### Task 7: Final integrity check

**Files:** none modified — verification only.

- [ ] **Step 1: Build the entire site clean**

```bash
npm run build 2>&1 | tail -20
```

Expected: build succeeds with no errors and no broken-link warnings. Note the page count — should be one or two higher than the Phase 0 baseline (two new pages, modulo Astro's index/redirect page count).

- [ ] **Step 2: Verify all cross-links resolve**

```bash
# Check that the new pages exist in the build output
ls dist/the-loco-thesis/index.html dist/findings/index.html 2>&1
```

Expected: both files exist.

```bash
# Quick scan for unresolved internal links (Starlight typically logs these as warnings)
npm run build 2>&1 | grep -iE '(broken|warning|missing|not found|unresolved)' | head -20
```

Expected: empty (or only known/unrelated warnings). If real broken links surface, locate the source markdown and fix.

- [ ] **Step 3: Spot-check the homepage hero block via dev server**

```bash
npm run dev &
DEV_PID=$!
sleep 5
curl -s http://localhost:4321/ 2>&1 | grep -iE '(deliberate|secondhand|different bet|five principles)' | head -5
kill $DEV_PID 2>/dev/null
wait 2>/dev/null
```

Expected: matching lines including the new "different bet" subhead and the new "five principles" card. (If the dev server uses a different port — Starlight's default is `4321`; check `astro.config.mjs` if needed — adjust the URL.)

- [ ] **Step 4: Verify no stale "student" references in the changed home-page cards**

```bash
grep -n 'student' src/content/docs/index.mdx
```

Expected: no output. (Spec required dropping student references from the index cards; Tasks 3 already did this. This step confirms.)

Also scan the *new* pages for any accidental "student" framing:

```bash
grep -n 'student' src/content/docs/the-loco-thesis.md src/content/docs/findings.md
```

Expected: no output.

- [ ] **Step 5: Confirm the commit log tells a clean story**

```bash
git log --oneline ae57a90..HEAD
```

Expected: 6 commits — one per task (Tasks 1-6), in order. No spurious "fix typo" or "amend" commits.

- [ ] **Step 6: If everything is clean, no further commit needed**

If steps 1-5 all pass, this phase has nothing to commit. The plan is complete.

If steps 1-5 surface anything (broken link, build warning, stale reference), make the targeted fix, run `npm run build` again, and commit:

```bash
git add <fixed-file>
git commit -m "Final integrity sweep: <what was fixed>"
```

---

## Out of scope for this plan (parking lot)

These are documented in the spec's parking-lot section and are **not** in this plan:

- **Visual diagram of the four-axis stack** — a new SVG/PNG image could supplement the existing 3-pillar image; defer until empirical results from MoE+RAM and harness work mature.
- **Per-principle deep-dive pages** — if `the-loco-thesis.md` grows over time, individual principles might warrant their own pages.
- **Translation to Spanish** — separate project.
- **Update the index.mdx hero image (`lab.svg`)** to reflect the bridge framing visually — design work, separate from this content update.
- **External-facing pitch deck or one-pager** — separate artifact.
- **Footer / about-this-site updates** — defer.

---

## Implementer notes

- **The site is Astro/Starlight.** Internal links use Starlight's slug convention: `[label](slug)` where `slug` is the filename without `.md` and without a `docs/` prefix. Examples in the existing `audience.md`: `[ai-landscape](ai-landscape)`, `[research](research)`. Anchor links like `[heading](page#anchor)` work after auto-slugification of the heading text.
- **Heading slugs.** Starlight auto-generates anchors from heading text. The thesis doc uses headings like `## Engineer before hardware`, which slugify to `#engineer-before-hardware`. The audience.md and why-local-ai.md links to `the-loco-thesis` (without an anchor) target the page itself; the cross-links in the thesis closing use specific anchors.
- **Build, don't lint.** There is no markdown lint configured. The build (`npm run build`) is the validation. If it succeeds, the content is structurally valid for Starlight.
- **No `student` references in changed home-page cards or new pages.** The user explicitly broadened away from student-specific framing on the home page; the privacy and educational arguments live elsewhere (in `audience.md`'s Educator persona, in `why-local-ai.md` once that's read).
- **Commit per task, not per file.** Each task ends in one commit; six commits total across Tasks 1-6, with Task 7 only committing if the integrity sweep finds something to fix.
- **The findings page is a living document.** Don't try to make it complete or polished at launch — its job is to track what's actually built/measured/published, with status markers showing maturity. As the moe-budget runs land and the Keep Asking studies execute, entries move down the status ladder.
- **Voice check while writing.** The site uses second person sparingly and avoids hype. The thesis can be confident but not preachy. No buzzwords ("game-changing", "revolutionary"). Each principle should be defensible against a hostile reviewer. If a sentence sounds like marketing copy, rewrite it as a measurable claim.
- **The `running` status on LocoPuente** in findings.md is intentional — it's the same operational maturity as `measured` (working in production), but `running` is more accurate for a service rather than an experiment.
