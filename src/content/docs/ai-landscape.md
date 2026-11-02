---
title: "AI Landscape"
---

LocoLLM does not exist in isolation. Students and educators have a growing set of options for accessing AI, from free cloud tiers to fully local tools. This document maps the options honestly so users can make informed choices, including the choice not to use LocoLLM.

A project that pretends its alternatives do not exist is selling something. We are not selling anything.

## Free and Low-Cost Cloud Options

These are the tools most students will encounter first. Many are good. Some are very good.

### Free Tiers

| Provider | Free Offering | Strengths | Limitations |
|----------|--------------|-----------|-------------|
| **Google Gemini** | Generous free tier, education accounts | Excellent capability, large context, multimodal | Rate-limited; depends on Google's pricing decisions |
| **ChatGPT (OpenAI)** | Free GPT-4o-mini access | Strong general capability, familiar interface | Capped usage, reduced features vs paid |
| **Claude (Anthropic)** | Free tier available | Strong reasoning, long context | Usage limits, requires account |
| **Microsoft Copilot** | Free with Microsoft account | Integrated with Office/Edge ecosystem | Quality varies, tied to Microsoft ecosystem |
| **GitHub Copilot** | Free for verified students | Excellent for code | Requires GitHub Education verification |
| **Google Colab** | Free GPU notebooks | GPU access for training/inference | Session limits, queue times, runtime disconnections |

**Honest assessment:** For a student who needs general AI assistance, free Gemini managed carefully is hard to beat as of early 2026. LocoLLM does not pretend otherwise. If a student has reliable internet and their free tier meets their needs, they should use it.

### Cheap API Access

| Service | What It Offers | Approximate Cost |
|---------|---------------|-----------------|
| **OpenRouter** | Aggregated access to many models, some free | Free models available; paid models from $0.10/M tokens |
| **Anthropic Haiku** | Fast, capable, cheap | ~$0.25/M input tokens |
| **GPT-4o-mini** | Strong quality at low cost | ~$0.15/M input tokens |
| **Gemini Flash** | Fast inference, competitive quality | ~$0.075/M input tokens |
| **Groq** | Extremely fast inference | Free tier available; paid from $0.05/M tokens |

**Honest assessment:** For students comfortable with APIs, cheap models like Haiku, GPT-4o-mini, and Gemini Flash are competitive and often superior to any 4B local model on general tasks. The barrier is technical (understanding API keys, endpoints, billing) and financial (even cheap adds up over a semester of heavy use).

### What Is Changing

Free tiers are not guaranteed. As the financial realities of inference compute become clearer:

- Providers are tightening free-tier limits and degrading free-tier model quality
- "Free" often means "free until we have enough users to justify charging"
- Student-specific programmes (GitHub Education, Google for Education) are the most stable but require institutional partnerships
- Free tiers are a user-acquisition strategy, and their long-term availability is not guaranteed

That is the economics, and it means any curriculum built entirely on free cloud AI is one pricing change away from disruption.

## GPU Rental: Self-Hosted in the Cloud

This is the option most comparisons miss. Between "use someone else's model via subscription" and "run your own model on your own hardware" sits a third path: rent GPU hardware and run your own model on it.

This is categorically different from subscribing to ChatGPT or Claude. You are not accessing an AI provider's model through their API. You are renting raw compute, deploying Ollama or llama.cpp yourself, and running an open-weight model of your choosing. Your data goes to your rented server, not through any AI company's inference infrastructure.

### Why This Matters

| | Managed AI (ChatGPT, Claude) | GPU Rental (RunPod, etc.) | Local Inference |
|--|-----|-----|-----|
| Data sovereignty | No: processed by provider | Yes: your server, your model | Yes: never leaves device |
| Subscription model | Yes | No: pay for compute time used | No |
| Hardware required | None | None | Yes |
| Model choice | Provider's models only | Any open-weight model | Any open-weight model |
| Availability | Requires internet | Requires internet | Works offline |
| VRAM ceiling | Unlimited (provider's) | As high as you rent | Limited to your hardware |

### Providers

| Provider | Notes |
|----------|-------|
| **RunPod** | Best GPU-per-dollar for AI workloads. Spot (cheap, interruptible) and on-demand. Straightforward setup. |
| **Vast.ai** | Peer-to-peer GPU marketplace: cheapest option, variable reliability. Good for short burst jobs. |
| **Lambda Labs** | Reserved instances, more predictable than spot markets. Good for longer-running deployments. |
| **Paperspace** | Clean interface, good for students. Gradient notebooks lower the setup barrier. |
| **AWS / GCP / Azure** | Enterprise SLAs and compliance, significantly higher cost. Relevant for institutional deployments. |

### When It Makes Sense

- You need more VRAM than your hardware provides (e.g., want to run a 70B model without buying a $2,000 machine)
- You want a persistent server accessible to multiple users or from multiple locations
- You are evaluating whether local inference is worth the hardware investment: rent first, buy later
- You need burst compute for a specific project without committing to hardware

### The Honest Trade-off

GPU rental gives you data sovereignty and model choice without upfront hardware cost. The trade-off is ongoing compute cost: it is not free to leave a rented GPU instance running. For a student who uses it occasionally for a few hours at a time, RunPod spot instances can be surprisingly cheap. For a persistent always-on server, costs accumulate.

**Honest assessment:** For students who cannot run capable models on their own hardware and are uncomfortable with the data implications of managed AI subscriptions, a RunPod spot instance running Ollama is a practical and principled middle path. It is also useful for experimenting with larger models before deciding whether to invest in hardware.

## Local Inference Tools

LocoLLM is not the only way to run models locally. The local AI ecosystem is maturing rapidly, and several tools are excellent.

### Model Runners

| Tool | What It Does | Strengths | Limitations |
|------|-------------|-----------|-------------|
| **Ollama** | Local model serving with simple CLI | Dead simple setup, wide model support, active community | Single model focus, no routing or adapters |
| **LM Studio** | GUI for downloading and running local models | Beautiful interface, model discovery, easy setup | macOS/Windows focus, less scriptable |
| **llama.cpp** | Low-level inference engine | Maximum control, best performance tuning | Requires technical comfort with CLI |
| **Jan** | Local AI assistant with chat interface | Clean UX, offline-first, open source | Newer project, smaller ecosystem |
| **LocalAI** | OpenAI-compatible local API server | Drop-in replacement for OpenAI API, supports many backends | More complex setup, aimed at developers |

### Chat Interfaces

| Tool | What It Does | Strengths | Limitations |
|------|-------------|-----------|-------------|
| **Open WebUI** | Web-based chat interface for local models | Feature-rich, supports Ollama backend, RAG, multi-user | Requires running a separate server |
| **AnythingLLM** | Desktop app for local AI with document ingestion | Good RAG support, workspace concept, multiple LLM backends | Heavier resource usage |
| **Msty** | Lightweight local AI chat | Clean interface, low resource usage, ~5-10 tok/s on CPU | Limited advanced features |
| **GPT4All** | Desktop chat with local models | Simple installation, curated model library | Less flexible than Ollama ecosystem |

**Honest assessment:** A student who installs Ollama and runs Qwen3-4B with a thoughtful system prompt gets roughly 80% of what LocoLLM aims to provide, with dramatically less complexity. If their needs are "brainstorm, draft, iterate, think out loud," that is probably sufficient. Msty deserves particular mention: it provides a polished chat experience with CPU-viable models at 5-10 tokens per second, which is usable for conversation-style interaction.

## Where LocoLLM Fits

Given all of the above, LocoLLM needs to be clear about what it adds and what it does not.

### What LocoLLM Is Not

- **Not a model runner.** Ollama and llama.cpp handle inference. LocoLLM orchestrates on top of them.
- **Not a chat interface.** Open WebUI and Msty are better pure chat tools. LocoLLM is a system, not a UI.
- **Not a competitor to free-tier frontier models.** On general tasks, free Gemini or ChatGPT will outperform LocoLLM's 4B base. We do not pretend otherwise.
- **Not a product (yet).** It is a teaching and research framework that happens to produce a usable tool.

### What LocoLLM Adds

- **Specialist routing.** No other local tool automatically dispatches queries to domain-specific trained adapters. Whether this adds meaningful value over a single generalist is an open research question (see [The Router Question](known-challenges.md#the-router-question)), but it is the core differentiator.
- **Systematic evaluation.** Every adapter must prove it beats the base model. No vibes. This evaluation infrastructure does not exist in any of the tools listed above.
- **Inference stacking.** RE2 prompting and self-consistency voting are free on local inference and expensive via API. LocoLLM applies these systematically.
- **A research framework.** The semester-based contribution model, the evaluation gates, and the benchmark infrastructure produce replicable findings, not a chatbot.
- **Benchmark data.** Systematic benchmarking of quantized small models on consumer hardware fills a genuine gap in the literature. This data has value independent of whether anyone uses the LocoLLM CLI.

### The Honest Positioning

LocoLLM's value proposition:

1. **For students:** A local AI tool that works without internet, without rate limits, without cost, and without sending your work to a third party. Use free tiers when they are available. Use LocoLLM when they are not, or when you need unlimited iteration.

2. **For student contributors:** A real engineering project where you learn adapter training, evaluation, data curation, routing, and system design by building something that works. The learning is in the building, not in the using.

3. **For researchers:** Benchmark data and methodology for quantized small models that does not exist elsewhere. Routing experiments under hard constraints. Publishable findings regardless of whether the results are positive or negative.

4. **For anyone who cares about dependency:** A small demonstration that useful AI capability does not require a subscription to a company that might change its terms tomorrow. It is a proof of concept, not a revolution.

## Recommendations for Students

Here is what LocoLLM recommends, without the marketing gloss:

1. **Start with free tiers.** Google Gemini's free offering is excellent. Use it. Learn prompting, learn to evaluate output critically, develop AI literacy. This costs nothing and teaches the most important skill: working *with* AI, not *for* AI.

2. **Learn about local options.** Install Ollama. Try a small model. Understand what runs on your hardware. This builds technical literacy and gives you a fallback when cloud services are unavailable or rate-limited.

3. **Use cheap APIs when free tiers are insufficient.** Haiku, GPT-4o-mini, and Gemini Flash are remarkable value. If you have a small budget, these stretch further than subscriptions.

4. **Consider GPU rental if you care about sovereignty but lack the hardware.** A RunPod spot instance running Ollama costs a few cents per hour and gives you full model choice and data control without buying a GPU. Useful for trying larger models, running a persistent shared server, or evaluating whether local inference is worth a hardware investment.

6. **Use LocoLLM when it makes sense.** Use it when you need unlimited local inference with no cost anxiety, when you are contributing as a learning exercise, when you care about privacy, or when you want to understand adapter training and routing by building the system yourself.

7. **Do not use LocoLLM because you think you should.** If free Gemini meets your needs, use free Gemini. The goal is student capability, not project adoption.

## The Bigger Picture

AI is moving fast. Tools that are cutting-edge today may be commoditised or deprecated within a year. Free tiers may get more generous or may tighten. Local models will get better. New tools will emerge.

LocoLLM's bet is that local capability retains value even as cloud capability improves, for practical reasons:

- **Provider terms change.** Pricing, rate limits, and model availability are not under the user's control. Local inference is.
- **Privacy is structural, not policy-based.** Local inference cannot leak what it does not send.
- **Understanding how AI works** by building it creates technical skills that a hosted service does not develop.
- **Offline capability matters** for users with unreliable connectivity or in environments where cloud access is restricted.

Whether that bet pays off is an empirical question. Anyone evaluating LocoLLM can see the full picture and make their own informed decision.
