---
title: "How It Started"
---

LocoLabo has two origin stories. One is institutional. The other is personal. They converged.

---

## The Policy

The university where LocoLabo began, like many institutions, restricted the use of frontier cloud AI models for teaching and assessment. No ChatGPT. No Claude. No API calls with student data. The reasons were legitimate -- privacy, sovereignty, governance -- and the effect was a hard constraint: if students were going to use AI, it had to run locally.

That story is told elsewhere on this site. It explains the *institutional* motivation. But it doesn't explain why a lecturer ended up with six machines, twenty-five GPUs, and a research programme built on secondhand hardware.

That part started with eBay.

---

## The Cards That Didn't Work

Before LocoLabo had a name, before there were projects or research questions, there were three GPUs bought on impulse and curiosity: two Tesla K80s and a Tesla K40.

The logic was straightforward. Data centre GPUs were appearing on the secondhand market at prices that seemed too good to ignore. The K80 was a dual-GPU card -- 2x 12 GB of VRAM on a single board. The K40 had 12 GB and had been a workhorse for scientific computing. If local inference was the plan, these looked like bargains.

They weren't.

The K80 and K40 are Kepler architecture -- CUDA compute capability 3.5 and 3.7. Modern inference frameworks either don't support them or run so slowly that the experience is unusable. The cards are physically large, power-hungry, and generate enough heat to warm a small room. They taught an important lesson: not all VRAM is equal, and cheap does not mean useful.

The K80s and K40 are retired from inference duty. They may yet find a second life as home compute nodes, but for the questions that became LocoLabo, they were a dead end.

A productive dead end, as it turned out.

---

## The P100

The K80 failure narrowed the search. What was the oldest, cheapest data centre GPU that could actually run modern inference frameworks? The answer, in late 2024, was the Tesla P100.

Pascal architecture. CUDA compute capability 6.0. 16 GB of HBM2 with 732 GB/s bandwidth. No tensor cores -- that came with Volta -- but enough compute and memory bandwidth to run quantised models at acceptable speeds. Readily available on eBay as data centres retired them.

The purchase raised a question that turned out to be more interesting than the card itself:

**Was that actually worth it?**

Not philosophically. Practically. For someone with $180 and a need to run inference locally, was a secondhand P100 a good buy? How did it compare to a consumer GTX 1060 at half the VRAM? To a used RTX 2060 Super at a similar price point? If you already had a gaming PC with a 1050 Ti, was the P100 worth the upgrade, or should you save for an RTX 3060?

There was no good answer. The benchmarks that existed tested models under ideal conditions on current-generation hardware. Nobody was systematically testing what local LLM inference actually looked like on the kind of hardware that real people -- students, hobbyists, educators at under-resourced institutions -- could actually afford.

So the decision was to build the answer.

That question became **LocoBanco**.

---

## The Machine That Was Already Running

While the GPU questions were forming, something else was already underway.

A desktop machine -- later named Cerebro -- had been running AI-powered simulation websites for several courses. Students interacted with simulated organisations for assessments: conducting audits, gathering requirements, interviewing stakeholders. The simulations ran on Ollama, served over the local network, access-controlled with bearer keys. It worked. Students used it. The courses ran.

That system became **LocoEnsayo**.

The naming came later, as did the formal research framing. But the practical reality -- a local machine serving AI-powered educational simulations to students -- predated the lab. LocoEnsayo didn't emerge from a research proposal. It emerged from a semester that needed simulation tools and a machine that could run them.

---

## The Questions That Multiplied

Cerebro had two RTX 2060 Supers. Running Ollama for multiple concurrent student sessions raised practical questions about multi-GPU utilisation. Then additional GPUs started arriving -- a 1060 here, a 3060 there, the P100 -- and the questions sharpened.

How does inference across two RTX 2060 Supers compare to a single 16 GB card? Is load balancing across mismatched GPUs worthwhile, or does the slowest card become the bottleneck? If you have three 8 GB cards, can you effectively simulate a 24 GB card through tensor parallelism, or does PCIe bandwidth kill the advantage?

These were not theoretical questions. They were the direct consequence of having a growing collection of secondhand GPUs and needing to know what configurations actually worked.

That line of inquiry became **LocoConvoy**.

---

## The Specialist Hypothesis

Meanwhile, a parallel question was developing from the educational side. The simulation tools worked, but the models were general-purpose. A 4B generalist model did a reasonable job across many tasks, but it was noticeably weaker on domain-specific work -- marketing terminology, security audit procedures, accounting standards.

The hypothesis: rather than waiting for a larger general model to fit in the same VRAM budget, what if you trained small specialist adapters -- one for each domain -- and routed queries to the right specialist? A swarm of cheap specialists instead of one expensive generalist.

That became **LocoLLM**.

---

## The Agent Question

The final project emerged from watching the broader AI landscape. Agentic AI systems -- OpenClaw, Claude Code, Karpathy's autoresearch -- were demonstrating what models could do when given tools and reasoning loops. But they all assumed frontier models with hundreds of billions of parameters.

The question was natural: how far could you get with a 4B model, the right scaffolding, and a constrained action space? Could a small local model productively participate in an agent loop, or was there a hard capability floor?

Nobody had studied this systematically at the sub-7B scale. The experiment matrix was designed so that every row was a self-contained research contribution -- suitable for a student project or publication.

That became **LocoAgente**.

---

## The Thread

Looking back, every project traces to the same impulse: a practical question that nobody had answered for the hardware people actually have.

- **K80s and K40:** Can data centre cards do local inference? (No -- but asking led to the P100.)
- **P100:** Was buying this worth it? (No good answer existed -- so: LocoBanco.)
- **Cerebro:** Can a local machine serve AI simulations to students? (Yes -- so: LocoEnsayo.)
- **Multiple GPUs:** What happens when you coordinate cheap cards? (Nobody had measured it -- so: LocoConvoy.)
- **Domain tasks:** Can specialists beat generalists at the same VRAM budget? (Plausible -- so: LocoLLM.)
- **Agent loops:** Can small models think in loops? (Unknown at this scale -- so: LocoAgente.)

Each project exists because the previous one surfaced a question it couldn't answer. The institutional policy restriction created the need for local AI. The hardware experiments created the questions. Together they explain why a teaching-focused, one-person lab ended up with a research programme in applied AI infrastructure.

The P100 is still in the fleet. It sits in Colmena's seventh slot, running adapter training jobs. It is almost certainly in the final published LocoBanco results -- the card that started the question deserves to be part of the answer.

---

*LocoLabo did not begin with a plan. It began with a restriction, a bad purchase, and a better question.*
