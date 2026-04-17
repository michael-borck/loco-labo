---
title: "LocoLab"
subtitle: "Frontier AI on a Budget. Crazy, Right?"
---

# LocoLab

> *Frontier AI on a budget. Crazy, right?*

LocoLab is an applied AI research lab at Curtin University's School of Marketing and Management. We study what local AI can actually do on modest hardware -- and build tools that put that capability in the hands of educators, students, and organisations that can't or won't send their data to the cloud.

The work is deliberate. The hardware is secondhand. The models are small. The questions are serious.

---

## Where This Started

It didn't start with a research grant or a GPU cluster. It started with a restriction.

Curtin University, like many institutions, prohibited the use of frontier cloud AI models for teaching and assessment. No ChatGPT. No Claude. No API calls with student data. The reasons are legitimate: student privacy obligations, data sovereignty requirements, ethics approvals that don't contemplate third-party processing, and the straightforward governance problem of sending assessment work to a commercial provider whose data practices you don't fully control.

The obvious response was to stop. The response that produced LocoLab was to build alternatives.

The first outputs were privacy-first desktop applications -- local, offline, built around Ollama for inference, with BYOK (Bring Your Own Key) options for users who wanted to make their own choices about cloud access. No data leaves the machine by default. No institutional exposure. No API costs. The student controls the tool; the institution controls the policy.

Building those tools surfaced something more interesting than a technical solution. Working with small local models -- genuinely constrained, genuinely imprecise compared to frontier alternatives -- forced a rethink of what AI was actually for in an educational context.

The answer became **Conversation, not Delegation**.

Delegating a task to AI -- asking it to write your essay, solve your problem, produce your output -- requires frontier-level factual precision and reasoning. You are trusting the model's answer. Small models are legitimately worse at this, and the trust is harder to justify.

Conversing with AI -- using it to brainstorm, ideate, iterate, challenge your assumptions, and amplify your thinking -- requires something different. It requires a model that responds coherently and keeps up with your reasoning. It does not require GPT-4. A 7B model running locally on a secondhand GPU does this well. And critically, it keeps the human thinking rather than replacing the thinking.

That reframe transformed the institutional restriction from a constraint into a pedagogical position. Small local models are not a compromise. For the most educationally valuable use of AI -- amplifying student thinking rather than replacing it -- they are the right tool. The privacy and governance benefits are real and additional.

LocoLab exists to study, document, and extend that position.

---

## Why Local AI Matters

The gap between frontier AI and local AI is widening. GPT-4, Claude, Gemini -- powerful, accessible, and for many users and institutions, unavailable in practice.

The barriers are not always financial. They are often principled:

**Data sovereignty** -- governments, health organisations, and defence-adjacent institutions operate under data residency requirements that prohibit cloud processing of sensitive information regardless of cost. Local inference is not a workaround; it is the only compliant path.

**Student and research privacy** -- assessment submissions, conversation transcripts, interaction logs, and unpublished research findings carry privacy obligations. Many institutional ethics approvals do not contemplate third-party cloud processing. Running inference locally keeps that data on-premises by design.

**Institutional governance** -- an institution that sends student work to a commercial AI provider has made a policy decision with legal and reputational implications. Local inference makes that decision unnecessary.

**Economic access** -- ongoing API costs are real for individuals, small organisations, and institutions in lower-income contexts. Local inference removes the per-query cost entirely once hardware is in place.

**The "Conversation not Delegation" case** -- for the most valuable educational uses of AI, frontier precision is not required. Brainstorming, ideation, iteration, and critical dialogue benefit from a model that responds coherently, not one that responds with authority. Local small models are sufficient for this. The fact that they are also private, local, and free to run is not a consolation -- it is the point.

We are not mapping the floor of what AI can do because we cannot afford the ceiling. We are mapping the floor because most people live there, and nobody is documenting it honestly.

---

## The Projects

### LocoLLM
*Routed swarm of tiny specialist models*

The flagship project. Rather than running one large general-purpose model, LocoLLM routes queries to small specialist models -- each adapter-trained for a narrow domain -- and composes their outputs. The hypothesis is that a coordinated swarm of cheap, local specialists can outperform a single generalist on real domain tasks.

No cloud. No API keys. Just your hardware doing more than you would expect.

**Hardware:** Condor (X99 single-Xeon, V100 32 GB HBM2 -- dedicated adapter-training and single-card inference)

**Key questions:** Can specialist routing recover quality lost to model size? What routing strategies work on PCIe-connected multi-GPU hardware without NVLink? How much adapter training is needed for a specialist to meaningfully outperform a generalist on domain tasks?

---

### LocoBench
*VRAM tier benchmarking across GPU generations*

A systematic benchmark of LLM inference across every consumer GPU VRAM tier, from 2 GB to 24 GB, from Maxwell to Blackwell. Each tier is represented by the worst-in-class card -- the floor, not the ceiling. If it runs here, it runs on your card.

LocoBench documents two things mainstream benchmarks ignore: throughput (tokens per second at the tier floor) and quality retention (what you actually get at each tier and quantisation level). The GSM8K cliff -- where mathematical reasoning degrades sharply below certain quantisation levels despite acceptable perplexity scores -- is an example of the kind of finding that only emerges when you run the full tier stack rather than cherry-picking hardware.

The sub-4 GB tiers are included deliberately. Most inference guides assert a "4 GB minimum" as received wisdom. LocoBench will show the data behind that claim -- where the quality cliff is steep, where it is gradual, and what an adapter-trained small model can recover at the floor.

**Hardware:** Colmena (RTX-era tiers) + Tortuga (pre-RTX legacy tiers) + Hormiga (reference floor node)

**Key questions:** Where exactly is the quality cliff? What is the minimum viable hardware for useful inference on real tasks? Do adapter-trained small models recover quality that quantisation removes? Does the "Conversation not Delegation" use case hold up empirically at the 2-4 GB tier?

**Community:** Results are designed to be reproducible. A single GPU owner can run the same harness and submit results. The benchmark matrix expands beyond what any single lab can cover.

---

### LocoConvoy
*Multi-GPU parallelism on consumer hardware*

Consumer NVLink is dead. Every multi-GPU configuration available to most users runs over PCIe -- which means the constraints are real, documented, and representative of what the community actually has.

LocoConvoy studies three architectures on that hardware: load balancing (multiple Ollama instances behind a router for concurrent throughput), Mixture of Agents (proposer cards and an aggregator card for quality improvements on reasoning tasks), and speculative decoding (a fast draft model passes token candidates to a slower verifier for latency reduction). PCIe bandwidth as the bottleneck is a feature of the methodology, not a limitation to work around -- worst-case results on realistic hardware are honest results.

**Hardware:** Hidra (X99 dual-Xeon open frame, 4x PCIe x16 slots for uncrippled interconnect)

**Key questions:** What does multi-GPU coordination actually deliver on PCIe hardware? When does MoA quality improvement justify the latency cost? Can vLLM tensor parallelism across cheap cards usefully simulate higher VRAM tiers?

---

### LocoEnsayo
*Authentic rehearsal environments for professional education*

Ensayo means rehearsal in Spanish. That is the point.

Students cannot develop professional skills by reading case studies -- they need to practice. A security student should conduct a real audit before doing one for a real organisation. A marketing student should handle a difficult client before facing one professionally. A hospitality student should manage a complaint escalation before it is their job on the line.

LocoEnsayo builds AI-populated organisations that students can interrogate, interview, audit, and negotiate with. Each persona has a backstory, a role, and information constraints -- they know what their character knows and no more. The organisation has structure, culture, and problems the student needs to surface through conversation. The scenario is not a quiz. It is a rehearsal.

Currently deployed: **CloudCore Networks** -- an IT services firm used for security audits, requirements gathering, and systems analysis units. **Pinnacle Tours** -- a hospitality and tourism organisation opening scenario coverage across marketing, management, and service design units. **TalkBuddy** -- conversation rehearsal for high-stakes professional scenarios.

The platform extends to high-stakes conversation practice that is too risky or expensive to run with real people: HR termination conversations, clinicians delivering difficult diagnoses, lawyers advising under pressure, managers navigating conflict. Local inference is not just convenient here -- it is required. Student interaction data in sensitive scenarios must not leave the institution. No cloud API makes that guarantee credibly.

BYOK options allow instructors and students who want frontier model access for specific scenarios to bring their own keys without the institution taking on the data governance exposure. The architecture supports choice without mandating risk.

**Hardware:** Puente (Ryzen 5 2600 with a single RTX 3090 24 GB; host for both LocoEnsayo and the LocoPuente BridgeAI PoC)

**Disciplines:** Information Systems, Marketing, Management, Tourism, Hospitality, Accounting, Supply Chain

**Key questions:** Does rehearsal in an AI-populated organisation transfer to real professional contexts? Can scenario generation replace expensive case study licensing at scale? What design principles produce authentic rather than toy interactions? How does local inference quality affect the credibility of the rehearsal experience?

---

### LocoAgente
*Can small models think in loops?*

Agente means agent in Spanish. The question is whether one can work.

Modern agentic AI systems -- OpenClaw, Claude Code, Karpathy's autoresearch -- assume frontier models with hundreds of billions of parameters. LocoAgente asks: how far can you get with a 4B model, the right scaffolding strategies, and a constrained action space?

The project investigates three tracks. Track A ports Karpathy's autoresearch loop to run with local small models as the agent brain -- the simplest possible agent (one file, one metric, automatic evaluation). Track B extends to task-specific agents (data analysis, code review, documentation). Track C is the core research contribution: a systematic comparison of scaffolding strategies (chain-of-thought, RE2, self-consistency voting, constrained action spaces, agent adapters) and whether they compound across multi-step loops differently than they do for single-turn tasks.

The key insight is that errors compound in loops. A model that is 90% accurate per turn is only 59% accurate over 5 turns. Scaffolding strategies that barely matter for single questions might be critical for agent loops. Nobody has studied this systematically at the sub-7B scale.

Every experiment after the frontier baseline runs free on local hardware. The experiment matrix is designed so each row is a self-contained research contribution suitable for a student project or publication.

**Hardware:** Shared with LocoLLM fleet (same base model, same adapters)

**Key questions:** Can a 4B model make productive decisions in an agent loop? Which scaffolding strategies compound most effectively across multiple reasoning steps? Is it more effective to make the agent smarter (better prompting) or to make the task simpler (constrained action spaces)? Where is the hard capability floor for small-model agents?

---

## The Lab

LocoLab runs on seven machines, all sourced secondhand. The entire fleet was assembled opportunistically -- the right capability at the right price, not a planned procurement.

| Machine | Role | Key Hardware |
|---------|------|-------------|
| **Colmena** | LocoBench RTX-era tier benchmarking | WEIHO 8-GPU enclosed chassis, GTX 1060 6GB x3, RTX 2060 Super x3, RTX 4060 Ti 16GB, Tesla P100 16 GB |
| **Condor** | LocoLLM adapter training, dedicated single-card inference | X99 single-Xeon, 32 GB DDR4, Tesla V100 32 GB HBM2 |
| **Tortuga** | LocoBench pre-RTX legacy benchmarking | WEIHO 8-GPU enclosed chassis, GTX 950 through Titan X |
| **Puente** | LocoPuente BridgeAI PoC + LocoEnsayo chatbots | Ryzen 5 2600, RTX 3090 24 GB (single card) |
| **Hormiga** | Minimum viable inference node | ThinkCentre M710s, GTX 1050 Ti LP 4 GB |
| **Hidra** | LocoConvoy multi-GPU experiments, GPU onboarding | X99 MD8 dual-Xeon (2x E5-2680 v4), DDR4 ECC, 4x PCIe x16, open frame; GTX 1070, RTX 3050, RTX 3060 12 GB + onboarding rotation |
| **Poco** | Remote terminal, Apple Silicon testing | MacBook M1, 16 GB unified memory |

The naming follows a Spanish thread -- Colmena (hive), Condor (condor), Tortuga (turtle), Puente (bridge), Hormiga (ant), Hidra (hydra), Poco (a little). All Linux machines run Ubuntu 22.04 LTS minimal server, CUDA throughout, Ollama for inference, llama.cpp under the hood.

---

## Research Output

LocoLab produces:

**LocoBench results** -- reproducible benchmarks across the VRAM tier stack, published openly for community extension. Standardised hardware reporting and a shared results format mean any GPU owner can contribute.

**Architecture papers** -- LocoLLM routing strategies and LocoConvoy multi-GPU experiments, targeting ACIS and the Australasian Journal of Information Systems IS Education section.

**Design science papers** -- LocoEnsayo as a DSR contribution. Authentic rehearsal environments as an IS education design principle with applications across business disciplines and beyond.

**Open tooling** -- harnesses, scenario frameworks, prompt libraries, and configuration templates published so others can replicate without starting from scratch. Privacy-first by default. BYOK where appropriate.

---

## The Philosophy

The institutional restriction that started this was not an obstacle. It was a clarification.

It forced the question: what is AI actually for in an education context? The answer -- amplifying thinking, not replacing it -- turned out to be better served by local small models than by frontier alternatives. Not because the small models are better. Because the constraint produced a better question.

That is the LocoLab disposition. Constraints surface optimisations that comfortable resources conceal. Secondhand hardware, small models, and honest baselines produce research that the A100 crowd is not doing -- not because they could not, but because the question only becomes visible from the floor.

We are not claiming small models match frontier models. We are claiming that for a large class of genuinely useful tasks -- educational brainstorming, professional rehearsal, domain-specific assistance, privacy-sensitive applications -- they are sufficient, local, and free to run. Documenting that honestly, at scale, and reproducibly is a contribution worth making.

The work is reproducible. The hardware is accessible. The findings are for everyone who needs to know what the floor actually looks like.

Loco by name. Serious by intent.

---

*LocoLab -- Information Systems, School of Marketing and Management, Curtin University, Perth, Western Australia.*
