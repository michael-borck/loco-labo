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
