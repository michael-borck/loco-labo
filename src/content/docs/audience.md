---
title: "Are You Loco Enough?"
description: Who LocoLab is for — six personas, six entry points into the lab's work.
---

LocoLab is not for everyone. It is for people who want to understand what local AI can actually do — and are willing to get their hands dirty finding out.

If any of these sound like you, welcome to the lab.

---

## 💰 The Budget Rebel

You refuse to pay per-token for something your own hardware can do. You've done the math on API costs and it offends you. You'd rather spend a weekend setting up a local stack than sign up for another subscription you'll resent.

**Your entry points:**
- [LocoPuente](https://locopuente.org) — a full local AI service stack on hardware you own and control
- [LocoLLM](https://locollm.org) — a routed specialist model that runs free on consumer GPUs
- [AI Landscape](ai-landscape) — honest comparison of local vs cloud options, including cheap API paths

And the [bridge](the-loco-thesis) is built for you specifically — frontier-equivalent tools without frontier costs is the bridge's whole job. See [The Local AI Opportunity](the-local-ai-opportunity) for the longer argument: why the meter is unsustainable, and what that opens up.

---

## 🤖 The Tinkerer

You want to understand how LLMs actually work by cracking them open and rewiring the internals. Reading about fine-tuning is not enough. You want to train a real adapter, measure whether it helped, and understand why.

**Your entry points:**
- [LocoLLM](https://locollm.org) — adapter training, evaluation harnesses, and a router you can improve
- [LocoBench](https://locobench.org) — systematic benchmarking infrastructure to measure what you built
- [Getting Started](getting-started) — technical foundations: inference, VRAM, quantisation, the full stack

The harness is the part you'll most enjoy taking apart — see [the thesis](the-loco-thesis) for why the engineering around the model matters more than the model.

---

## 🔬 The Researcher

You need reproducible local inference for experiments. You want to test whether specialist routing actually beats a generalist on scoped tasks — and publish honest results either way. You are not interested in vibes.

**Your entry points:**
- [LocoBench](https://locobench.org) — VRAM-tier benchmarking with real hardware, real cards, honest baselines
- [LocoConvoy](https://lococonvoy.org) — multi-GPU parallelism experiments on consumer PCIe hardware
- [LocoAgente](https://locoagente.org) — agentic scaffolding research: can small models think in loops?
- [Research](research) — active and planned studies across the lab

Our [methodology](the-loco-thesis) is laid out in the thesis: honest baselines, surfaced uncertainty, status markers on every claim. And [findings](findings) shows you what's measured, what's claimed, and what would invalidate each.

---

## 🏫 The Educator

You teach AI, computing, or a professional discipline and want a real project your students can contribute to. Not a toy demo. Real infrastructure that grows with every cohort. You also want rehearsal environments where students practise professional skills before they face the real thing.

**Your entry points:**
- [LocoEnsayo](https://locoensayo.org) — AI-populated rehearsal environments: security audits, requirements gathering, difficult conversations
- [LocoLLM](https://locollm.org) — a teaching and research framework students build by contributing adapters, benchmarks, and routing improvements
- [Why Local AI](why-local-ai) — the case for local AI in education and institutional contexts

The "[conversation, not delegation](the-loco-thesis)" principle is the pedagogical heart of the lab — it's what the Cognitive Strategy Transfer and Keep Asking research threads are about, and why the rehearsal environments are designed the way they are. For the future-of-careers angle, [The Local AI Opportunity](the-local-ai-opportunity) lays out the small-business and consulting openings the next generation of operators is walking into.

---

## 🔐 The Vault

Your data does not leave your machine. Period. Medical notes, legal research, personal journals, proprietary code, student assessment work — local inference is not a convenience, it is the only acceptable path. You do not need to be convinced. You need the stack to work.

**Your entry points:**
- [LocoPuente](https://locopuente.org) — local AI services for institutions and individuals who cannot or will not use cloud inference
- [AI Landscape](ai-landscape) — why "private by policy" is not the same as "private by architecture"
- [Why Local AI](why-local-ai) — data sovereignty, compliance, and the structural argument for local inference

Local AI is not just "private by policy" but [private by architecture](the-loco-thesis) — the bridge synthesises capability and privacy in a single stack you own.

---

## ⚙ The Scrapper

You know the best gear does not make the best work. A $150 secondhand GPU and sharp training data might just surprise you. You are assembling capability from what is available, and you want to know exactly where the floor is.

**Your entry points:**
- [LocoBench](https://locobench.org) — floor-representative benchmarks: worst card per VRAM tier, honest baselines
- [GPU Inventory](https://locobench.org/docs/gpu-inventory/) — the actual secondhand fleet running these experiments
- [Economics of Local Training](economics-of-local-training) — what local AI actually costs to build and run

The whole "[engineer before hardware](the-loco-thesis)" principle was built for you. Five `llama.cpp` flags + system RAM letting an eight-year-old GTX 1060 run a 30-billion-parameter MoE model is the kind of finding the floor produces. And once you know where the floor is, [The Local AI Opportunity](the-local-ai-opportunity) maps out who needs that capability — small accounting firms, regional legal practices, local consultancies — and what the work of building it for them actually looks like.

---

## Not sure where to start?

If you are new to local AI entirely, [Getting Started](getting-started) covers the technical foundations without assuming prior knowledge. If you want to understand the broader landscape before committing to anything, [AI Landscape](ai-landscape) gives an honest comparison of every option — including the ones that are better than LocoLab for your use case.

Loco by name. Serious by intent.
