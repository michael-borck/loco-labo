---
title: "What We've Discovered"
description: The artifacts behind each principle, with status markers — a living research notebook that evolves as work matures.
---

LocoLabo claims [five principles](the-loco-thesis). Below are the artifacts, built, measured, or in progress, that those claims rest on. Each entry has a status marker borrowed from [research](research) (where papers carry similar markers):

- `claim`: position taken, not yet built
- `architecture`: designed and specced, implementation pending
- `built`: implementation shipped, not yet measured at scale
- `measured`: empirical results, not yet published
- `published`: paper or report public

This page evolves. Items move down the status ladder as work matures. Failed claims stay on the page with their evidence.

---

## Engineer before hardware

### Qwen3-30B-A3B at reading speed on a GTX 1060 6GB

- **Status:** `architecture`
- **Claim:** five `llama.cpp` flags (`--n-cpu-moe`, `--no-mmap`, `--mlock`, `--cache-type-k q4_0`, `--cache-type-v q3_0`) plus 24-64GB of system RAM let a $80 used GTX 1060 run Qwen3-30B-A3B at ~17 tokens/sec
- **Artifacts:** [LocoBanco MoE-on-a-budget design spec](https://locobanco.org); implementation plan; Python harness library (33+ passing tests covering config loading, server boot, llama-bench wrapper, hardware fingerprinting); 17 cell configs across 4 VRAM tiers ready to run
- **What would invalidate:** if measured `tg128` < 10 tok/s on the 1060 with the optimised preset, or if the article's claim doesn't replicate

---

## Specialize and harness

### LocoAgente conversational harness: Phase 1

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
- **What would invalidate:** if the four strategies all collapse to the same output distribution on small models, that is, if engineered framing doesn't channel variance through the model, the principle is just an aesthetic claim

---

## Conversation, not delegation

### `Variant` + `Uncertainty` verification contract

- **Status:** `built`
- **Claim:** every harness output carries a rationale and surfaced uncertainty (load-bearing `flags` + `verification_hooks`; auxiliary `confidence`); singular outputs are forbidden at the primitive level; the human's verification loop is cheap because the harness does the prep work
- **Artifacts:** `Variant` and `Uncertainty` dataclasses in `harness/core.py`; XML tag parser enforcing required `<text>` and `<rationale>`; `CalibrationLog` recording user picks/rejects/edits as JSONL for downstream analysis
- **What would invalidate:** if users routinely ignore the `verification_hooks` field (the harness produces hooks but they're not the right hooks), the principle is performative rather than functional

### [Keep Asking](https://keep-asking.locolabo.org): Study 1: Does the Nudge Work?

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
