---
title: "The Economics of Local Training"
---

LocoLab runs on secondhand hardware. This document puts real numbers to the question of whether that makes financial sense compared to cloud GPU rental, API inference, or buying new equipment.

All figures use Australian dollars (AUD) and Perth electricity rates (Synergy Home Plan A1, ~$0.31/kWh).

---

## The Fleet

The lab runs five machines across three roles:

- **LocoLLM** (Colmena) — infrastructure, architecture research, adapter training
- **LocoBench** (Colmena + Tortuga) — benchmarking platform, community results
- **LocoConvoy** (Colmena) — multi-GPU architecture experiments: load balancing, Mixture of Agents, vLLM tensor parallelism

Colmena runs 24/7. Tortuga is on-call — powered on for benchmark runs, powered off the rest of the time. Two 8-GPU boxes, but only one drawing power continuously.

---

## Power Draw

Colmena runs 24/7. Most of the time it's idle (SSH available, Ollama loaded, waiting for work). Inference and training runs push power draw up significantly but only for a few hours at a time. Tortuga powers on for benchmarking sessions and goes back to sleep.

**Estimated draw by state:**

| Machine | Idle | Active Load | Duty Cycle |
|---|---|---|---|
| **Colmena** (WEIHO 8-GPU, 4 GPUs + P100) | ~120W | ~400W (inference/training) | 24/7 |
| **Tortuga** (WEIHO 8-GPU, 7 legacy GPUs) | ~150W | ~500W (benchmarking) | On-call (~10 hrs/week) |

*Note: Colmena estimates are based on typical TDP values for installed cards, with idle and inference scaling factors applied. Power draw will increase as additional cards are installed. Tortuga estimates are conservative — older Maxwell/Pascal cards draw less under inference than RTX-era equivalents. Real-world measurements will replace these estimates once available.*

---

## Annual Electricity Cost

Colmena runs 24/7. Two scenarios: a conservative one where the machine is under training load half the time, and a lighter one that reflects more typical usage patterns. Tortuga is estimated separately based on on-call usage.

**Colmena — 50% active / 50% idle (conservative):**

| Machine | Average Draw | Annual kWh | Annual Cost |
|---|---|---|---|
| **Colmena** | ~320W | 2,803 kWh | ~$869 AUD |

**Colmena — 25% active / 75% idle (more typical):**

| Machine | Average Draw | Annual kWh | Annual Cost |
|---|---|---|---|
| **Colmena** | ~190W | 1,664 kWh | ~$516 AUD |

**Tortuga — on-call (~10 hours/week, fully active when on):**

| Machine | Average Draw | Annual Hours | Annual kWh | Annual Cost |
|---|---|---|---|---|
| **Tortuga** | ~400W | ~520 hrs | ~208 kWh | ~$64 AUD |

**Combined lab electricity: roughly $580-930 AUD per year.**

That's a real cost. It's not free. But keeping Tortuga on-call rather than running it 24/7 means the second 8-GPU box adds minimal overhead. Two boxes spanning Maxwell through Ampere, one always-on and one waking only when needed. The question is what you get for that cost, and what the alternatives cost.

---

## Cost Per Training Run

| Scenario | Duration | Energy | Electricity Cost |
|---|---|---|---|
| Colmena: one adapter via PEFT overnight (P100) | 8 hours | 3.4 kWh | ~$1.05 AUD |
| Colmena: inference session (1 card, 2 hours) | 2 hours | 0.35 kWh | ~$0.11 AUD |

A semester of adapter development (roughly 20 training runs across student groups) adds ~$21 AUD in marginal electricity on top of the idle baseline. Benchmarking on Tortuga adds marginal cost only when the machine is powered on — a four-hour benchmark session costs roughly $0.50 in electricity. CloudCore inference runs on Cerebro independently.

---

## Compared to Cloud GPU Rental

Cloud GPU pricing for a comparable 16 GB card (A4000/V100 class) on platforms like RunPod, Lambda, or Vast.ai runs roughly $0.75-1.15 AUD per hour.

| | Local (Colmena P100) | Cloud GPU |
|---|---|---|
| 8-hour training run | ~$1.05 electricity | ~$6-9 rental |
| 20 runs per semester | ~$21 electricity | ~$120-180 rental |
| 60 runs per year (3 semesters) | ~$63 electricity | ~$360-540 rental |

Cloud wins on per-watt efficiency. Local wins on per-dollar cost by a factor of 6-8x for training, even before accounting for the idle power draw.

But the cloud comparison understates the local advantage in three ways.

First, cloud hours are use-it-or-lose-it. When a student is iterating on dataset formatting, debugging a training script, or just thinking about their approach, the cloud meter is running. Locally, that iteration happens on an idle machine at ~130W. The "time spent not training" is nearly free locally and expensive on the cloud.

Second, cloud access introduces dependency. If the provider changes pricing, discontinues an instance type, or has an outage during assignment week, you have no fallback. The machines under the desk don't go away.

Third, the lab's benchmarking role is difficult and expensive to replicate in the cloud. LocoBench needs runs across a range of VRAM tiers -- 2 GB, 4 GB, 6 GB, 8 GB, and 12 GB cards running the same model at the same quantisation level to produce comparable results. Between Colmena (RTX era) and Tortuga (pre-RTX), the lab covers every meaningful consumer tier. Cloud providers don't offer low-end consumer GPUs. The smallest widely available cloud GPU is typically a T4 (16 GB) or A4000 (16 GB). There is no cloud equivalent of a GTX 950, GTX 1050 Ti, or GTX 1650 -- the hardware that represents the floor of what students and departments actually own. You can choose VRAM size in the cloud, but only from the middle of the range upward.

Approximating the lab's benchmarking setup in the cloud would require renting multiple GPU instances simultaneously — and even then, the right hardware isn't available. A rough estimate using RunPod community pricing (March 2026):

| Cloud GPU | VRAM | Hourly Rate (AUD) | Closest Lab Card |
|---|---|---|---|
| T4 | 16 GB | ~$0.35 | None -- no cloud equivalent below 16 GB |
| RTX A4000 | 16 GB | ~$0.45 | None -- overshoots the 8 GB tier |
| RTX 3090 | 24 GB | ~$0.55 | None -- overshoots the 12 GB tier |

A four-hour benchmarking session across three cloud instances would cost ~$5-6 AUD. Running that weekly over a semester (12 weeks) adds ~$60-72 AUD. And the results wouldn't be directly comparable to consumer hardware anyway -- different architectures, different memory bandwidth profiles, no persistent card identity for longitudinal tracking.

The real issue isn't cost, it's validity. LocoBench exists to answer the question "what can a student run on hardware they can actually get?" Cloud GPUs don't answer that question. The 2 GB floor on Tortuga, the 4-8 GB sweet spot across both boxes, and the specific bandwidth characteristics of consumer Maxwell through Ampere cards are the point. That data can only come from the actual hardware, which is part of what makes the benchmarking exercise a genuine research contribution rather than a replication of existing cloud benchmarks.

---

## Compared to New Hardware

The efficiency criticism often takes the form: "Why not just buy a modern GPU? An RTX 4090 trains faster per watt."

True. It also costs $3,000-4,000 AUD for the card alone, plus a system to put it in. Call it $5,000-6,000 AUD for a modern training workstation. A new enterprise-grade server with an A-series GPU starts well above that.

**Return on investment framing:**

The lab's annual electricity cost is roughly $580-930 AUD. A new workstation that halved the power consumption (generous assumption) would save perhaps $290-465 AUD per year in electricity. At a purchase price of $5,000-6,000 AUD, the payback period on the capital expenditure is **11-20 years** in electricity savings alone.

And new hardware has running costs too. It still draws power. A modern GPU under training load still pulls 300-450W. The idle draw might be lower, but the training draw is comparable or higher. You're paying $5,000+ upfront to save $500/year in power, on equipment that will itself be outdated in 3-5 years.

Meanwhile, the secondhand market continues to offer capable hardware at low cost. Patience and willingness to hunt for deals is the only requirement. The same class of GPUs and servers that the lab uses are still available on eBay, Facebook Marketplace, and surplus dealers. Prices remain accessible for anyone willing to look.

**The AI hardware inflation factor:**

The economics are actually getting more favourable for secondhand buyers, not less. AI data centre demand is driving up prices across the board for new components. NAND flash prices have more than doubled in the past six months. GPU prices remain inflated at every tier. DRAM and even hard drives are affected. New hardware is getting more expensive to acquire, while the secondhand market for previous-generation enterprise equipment remains largely unaffected by that demand.

---

## Data Sovereignty and Ownership

When you train on cloud infrastructure, your training data transits external networks and resides on hardware you don't own. For a university research project handling case study data, student work, or anything adjacent to sensitive domains, that creates compliance requirements.

When you run inference through a commercial API, every query leaves your network. For students working with business scenarios, client data in case studies, or health-adjacent content in related programs, local inference avoids that data flow entirely.

Running locally means:
- No data processing agreements to negotiate
- No per-query costs that scale with student numbers
- No dependency on a specific provider's continued availability or pricing
- Compliance with data sovereignty requirements by default

Australian Privacy Act reforms, sector-specific data handling requirements, and university ethics frameworks are relevant context here. Local architectures simplify compliance, though they are not the only way to achieve it.

**Hardware sovereignty:**

There is a broader point beyond data privacy. Owning the hardware means owning the research capability. Cloud providers can change pricing, deprecate instance types, impose usage policies, or simply disappear. A lab that depends entirely on rented infrastructure has no fallback when any of those things happen. The machines under the desk don't require an account, a credit card, or a terms-of-service agreement. They don't throttle, they don't expire, and nobody else decides what you're allowed to run on them. For a research lab exploring how small models behave on constrained hardware, that independence isn't a convenience -- it's a precondition. The research questions LocoLLM asks can only be answered on hardware you control.

---

## The Real Comparison

| | Local Lab (Annual) | Cloud GPU (Annual) | New Workstation |
|---|---|---|---|
| **Capital cost** | Already acquired | $0 | $5,000-6,000 |
| **Electricity** | ~$580-930 | N/A | ~$500-700 (estimated) |
| **Compute rental** | $0 | $360-540+ | $0 |
| **API inference** | $0 | Scales with usage | $0 |
| **Data sovereignty** | Complete | Provider-dependent | Complete |
| **Availability** | 24/7 (Colmena) + on-call (Tortuga) | Subject to availability | 24/7, no booking |
| **Consumer GPU benchmarking** | Native (2 boxes, Maxwell through Ampere) | Not possible | Possible (single card) |
| **Multi-GPU architecture research** | Native (3+ matched cards) | Not comparable | Limited by slot count |
| **VRAM tier coverage** | 2-24 GB across 14 GPUs | 16 GB+ only | Single card |
| **Payback period** | Already past | Never (recurring) | 11-20 years |

The local lab's electricity cost is comparable to a modern workstation. It costs far less than cloud rental. The two-box architecture — Colmena always-on for research and inference, Tortuga on-call for legacy benchmarking — gives the lab complete VRAM tier coverage from 2 GB Maxwell through 24 GB Ampere while keeping the power bill under $1,000 per year. Cerebro remains active for CloudCore Networks with a dedicated 2060 Super. The hardware investment has already been made, at prices that are increasingly difficult to replicate for new equipment but remain available in the secondhand market for patient buyers.

**What the cloud cannot do at any price:**

"Just do it in the cloud" is a reasonable default for many workloads. It is not a reasonable default here. Two of the lab's three core roles are not available in the cloud at any price:

- **LocoBench** requires consumer GPUs from 2 GB to 24 GB across Maxwell, Pascal, Turing, and Ampere architectures. Cloud providers do not offer consumer-grade cards below 16 GB. The lowest tier widely available is the T4 (16 GB). There is no cloud instance with a GTX 950, GTX 1050 Ti, GTX 1060, or RTX 2060 Super. The benchmark data that LocoBench produces -- "what can a student run on a $150 secondhand GPU?" -- can only come from that actual hardware. Colmena covers the RTX era, Tortuga covers pre-RTX. Between them, every meaningful consumer VRAM tier is represented. This is not a cost problem. The capability does not exist in the cloud.

- **Multi-GPU architecture research** with consumer Turing and Ampere cards is similarly unavailable. You could rent T4s, but they're a different architecture with different memory bandwidth answering a different question. The research value is in understanding what works on hardware people actually have.

Only the third role -- inference serving and adapter training -- is straightforwardly replicable in the cloud. That's the role where the cost comparison above applies. For the other two, the comparison isn't "local is cheaper than cloud." It's "local is the only option."

---

## Summary

Running one 8-GPU box 24/7 and a second on-call costs roughly $580-930 AUD per year in electricity. That's the honest number.

For that, you get unlimited training runs, unlimited inference, complete data sovereignty, zero recurring subscription costs, VRAM tier coverage from 2 GB to 24 GB across four GPU architectures, and full reproducibility on hardware anyone can acquire secondhand.

The on-call model works. Tortuga adds ~$64 per year to the electricity bill while giving the lab complete pre-RTX benchmarking coverage. Two 8-GPU boxes, 14 GPUs across the full consumer range, under $1,000 per year in power.

The question isn't whether the lab is power-efficient. It isn't, compared to current-generation hardware. The question is whether the total cost of ownership -- capital expenditure, electricity, independence, and control -- makes sense compared to the alternatives.

It does.
