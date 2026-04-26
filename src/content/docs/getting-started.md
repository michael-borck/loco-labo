---
title: "Getting Started with Local AI"
---

This guide covers the technical foundations of local AI inference and a practical pathway to building real skills. Start here if you are new to running models locally.

---

## Part 1 — Technical Foundations

### What is Inference?

AI has two phases: **training** (building the model from data — requires massive compute clusters, months of time, enormous cost) and **inference** (using the pre-built model to generate responses — runs on your own hardware).

When you run a model locally, you are doing inference only. You are leveraging a brain that someone else trained, on your own machine, at your own pace, with your own data. This is what makes local AI accessible: you do not need to recreate the training process, only to run the result.

### Why GPUs?

Large language models are fundamentally **matrices of numbers**. Generating a single token requires billions of mathematical operations across these matrices. GPUs are built for exactly this: they contain thousands of small parallel processors designed for matrix multiplication, whereas CPUs are designed for complex sequential logic.

| | CPU | GPU |
|--|-----|-----|
| Architecture | Few powerful cores, sequential | Thousands of small cores, parallel |
| AI role | Orchestration, OS management | Matrix calculation (inference) |
| Limitation for AI | Too slow for large matrix math | Constrained by VRAM capacity |

### The VRAM Rule

The critical constraint in local inference is **VRAM** (Video RAM) — the high-speed memory on your GPU. The model's weights must fit entirely in VRAM to run at useful speed. The rule is simple:

> **2 bytes per parameter at 16-bit precision**

A 7B model needs ~14 GB; a 70B model needs ~140 GB. Most consumer GPUs have 8–24 GB, which is why quantisation matters.

Beyond the model weights, you also need VRAM for the **KV Cache** — the pre-calculated vectors that store conversation context. If the cache has nowhere to go, the context window collapses. The model should occupy no more than 70–75% of your VRAM to leave room for meaningful context.

### Quantisation

Quantisation compresses model weights by reducing numerical precision — from 16-bit floats down to 8-bit, 4-bit, or lower. This trades a small amount of quality for a large reduction in memory footprint.

| Precision | 70B model VRAM | Quality |
|-----------|---------------|---------|
| 16-bit | 140 GB | Full |
| 8-bit | ~70 GB | Near-full |
| 4-bit (Q4_K_M) | ~35 GB | Good — industry standard |
| 3-bit | ~26 GB | Noticeably degraded |

**Q4_K_M is the default for most situations.** It fits large models on consumer hardware while retaining most capability. The GGUF format (from Llama.cpp) is the standard quantised format — when pulling models from Hugging Face, filter by GGUF.

### Unified Memory — Breaking the VRAM Wall

Standard discrete GPUs (NVIDIA RTX series) have fixed VRAM — 8, 16, or 24 GB on consumer cards. To get more, you pay enterprise prices ($7,000+ for 48 GB).

**Unified Memory Architecture (UMA)** breaks this. Systems like Apple M-series or AMD Strix Halo (Ryzen AI 395) share a single pool of high-speed RAM between CPU, GPU, and NPU. A 128 GB unified memory machine makes ~108 GB available for inference — matching expensive enterprise discrete VRAM for $2,100–$2,500.

On Linux with AMD Strix Halo, configure GTT settings to allocate 108 GB to the GPU and reserve 20 GB for the OS. Exceeding this causes kernel panics under load.

---

## Part 2 — Your Learning Pathway

### Why Learn This Now?

The numbers are striking: 84% of developers use AI tools daily, but only 18% are involved in building the systems that make those tools work. Most are consuming cloud APIs. Very few understand local deployment.

The industries that need local AI most — healthcare, finance, defense, legal — cannot use public cloud APIs. Their data cannot leave the building. They need engineers who understand inference, quantisation, hardware tuning, and private deployment. This skill set does not yet have a formal curriculum. That is the opportunity.

### The Zero-Cost Starter Stack

You do not need to buy hardware immediately. Start with what you have:

| Tool | Purpose |
|------|---------|
| **LM Studio** | Download and run models with a GUI; built-in inference server |
| **Ollama** | CLI-based model management; API server for integrations |
| **Open WebUI** | Browser-based chat interface connecting to Ollama |
| **Continue.dev** | VS Code / JetBrains extension — local Copilot experience |
| **Qwen or Llama 3 (7B–14B Q4)** | Capable models that run on modest hardware |

Even on a laptop with integrated graphics or a modest GPU, you can run 7B models at Q4 and get a real sense of what local inference feels like, where it excels, and where it hits limits.

### Milestone 1 — Build a Local Co-pilot

Set up a local code autocomplete system:

1. Install **LM Studio** (or Ollama)
2. Download a Qwen or CodeLlama model (7B or 14B at Q4)
3. Connect **Continue.dev** in VS Code, pointing to `localhost:11434`

This is not just about free code completions. You will learn to observe **inference latency**, spot **hallucination patterns**, and understand how local models behave under hardware constraints. That observational knowledge is what distinguishes someone who has actually run inference from someone who has only read about it.

### Milestone 2 — Build a Private Pipeline

Create a project that runs entirely on private infrastructure:

- A local RAG (Retrieval-Augmented Generation) system for private documents
- A Whisper-based transcription pipeline for meeting audio
- A document summarisation tool for internal files

These "boring" pipelines are the high-value enterprise use cases. Well-defined, reliable, private, high-volume — exactly what organisations pay for. Document your setup and performance observations. That documentation is a portfolio piece.

### Milestone 3 — Understand the Limits

Run LocoBench on your hardware to get real throughput numbers. Then deliberately hit the limits:

- Fill the context window to see what happens
- Try agentic tasks with multiple tools — observe where the model loses coherence
- Compare Q4 vs Q8 on the same task

Knowing where local models fail, and being able to articulate why, is more valuable to a hiring manager than a generic AI certification.

### Career Paths

**Backend engineers**: your Docker and orchestration skills translate directly. Focus on RAG — connecting local models to private company data sources. Build a portfolio demonstrating you can handle sensitive data requirements.

**Students and self-taught developers**: start with the zero-cost stack, document everything, benchmark your setup. Proof that you understand inference behaviour is more valuable than proof you can call an API.

**DevOps/MLOps**: this is your fastest path to an AI role. Edge AI deployments need the same skills as any infrastructure work — deployment, monitoring, scaling — applied to model weights instead of application containers.

---

## The Big Picture

Local AI is not about replacing cloud AI. It is about developing a skill set that:

- Gives you direct experience with how these systems actually work
- Positions you for the parts of the market that cannot use cloud APIs
- Prepares you for the edge AI wave, where models run on constrained devices by default
- Lets you contribute to or benefit from open-weight model improvements without paying a subscription

The models improve continuously. Hardware you run today will run better models in six months. The skill you build now transfers to whatever comes next.

---

*Next steps: [Why Local AI](why-local-ai.md) for the broader context. [Hardware Selection](https://github.com/michael-borck/loco-puente/blob/main/HARDWARE.md) for deployment decisions. [LocoBench](https://github.com/michael-borck/loco-bench) for benchmarks on your hardware.*
