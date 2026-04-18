---
title: "Meet the Lab"
---

LocoLabo is the umbrella research initiative -- several sub-projects running across seven machines. None of them are new. All were sourced secondhand. Hardware was acquired opportunistically -- the right capability at the right price, not a planned procurement.

The naming follows a Spanish thread: Colmena (hive), Tortuga (turtle), Poco (a little), Hormiga (ant), Puente (bridge), Hidra (hydra), and Búho (owl). The hive runs RTX-era benchmarking at the tier floors, the turtle holds the pre-RTX legacy fleet and wakes slowly when called, the little one connects you to all of them, the ant keeps the floor honest on minimal hardware, the bridge carries students to the stack through the LocoPuente PoC and the LocoEnsayo rehearsal chatbots, the hydra runs many heads in parallel on full-bandwidth PCIe for multi-GPU research, server GPU benchmarking, and onboarding every new card into the lab, and the owl works quietly through the night on adapter training.

**Sub-projects under LocoLabo:**

- **LocoLLM** (Búho) -- adapter training on the V100 32 GB; dedicated single-card training and inference
- **LocoBench** (Colmena + Tortuga + Hormiga + Hidra) -- benchmarking platform; Colmena covers RTX-era consumer tiers, Tortuga covers pre-RTX tiers, Hormiga anchors the SFF floor, Hidra covers the server GPU tiers
- **LocoConvoy** (Hidra) -- multi-GPU architecture experiments on full-bandwidth PCIe x16, on an open frame for rapid card swaps
- **LocoPuente** (Puente) -- student-facing BridgeAI PoC: primary LLM, cited search, image generation, voice, research tooling, all on the Ryzen 5 2600 + RTX 3090 24 GB
- **LocoEnsayo** (Puente) -- most rehearsal chatbots (CloudCore Networks, Pinnacle Tours, TalkBuddy backend) now co-reside with the LocoPuente stack on Puente
- **LocoLabo coordination** (Poco) -- remote access and Apple Silicon testing across all sub-projects

---

## Poco

**MacBook M1 -- Remote Terminal and Apple Silicon Testbed**

| | |
|---|---|
| **Chip** | Apple M1 |
| **Memory** | 16 GB unified (shared CPU/GPU) |
| **Storage** | 256 GB SSD |
| **OS** | macOS |
| **Role** | LocoLabo coordination -- remote access into all sub-projects, Apple Silicon compatibility testing |

Poco means "a little" in Spanish. It doesn't do the heavy lifting -- it's how you reach the machines that do.

Day to day it's a remote terminal. SSH into Colmena for inference, benchmarking, and overnight training jobs, monitor progress, pull results. Portable and works from anywhere on the network.

Its secondary role is Apple Silicon compatibility testing. LocoLLM needs to run on hardware students actually own, and a significant proportion carry MacBooks. Poco validates that installation, Ollama inference, and adapter loading all work cleanly on Apple Silicon with unified memory. A base M1 with 16 GB represents a reasonable lower bound for that user group.

Apple's MLX framework supports LoRA adapter training natively via `mlx_lm.lora`, so Poco can also verify the training-to-deployment pipeline on Apple hardware when needed. Memory bandwidth is 68 GB/s -- slow compared to the rest of the lab -- but functional.

**Best at:** Remote access. Validating the student experience on consumer Apple hardware.

---

## Colmena

**WEIHO 8-GPU Enclosed Chassis -- RTX-Era LocoBench Benchmarking**

| | |
|---|---|
| **Chassis** | WEIHO 8-GPU enclosed mining rig (72x42x18cm, steel, blue lid) |
| **Motherboard** | Intel LGA1155, B75/H61 chipset |
| **CPU** | Intel i3-3220 (Ivy Bridge, dual core) |
| **GPUs** | 3x GTX 1060 6 GB, 3x RTX 2060 Super 8 GB, RTX 4060 Ti 16 GB |
| **Memory** | 8 GB DDR3 SODIMM (board maximum) |
| **Storage** | 128 GB mSATA (OS) + WD Scorpio Blue 750 GB SATA (model storage via `OLLAMA_MODELS`) |
| **PSU** | Integrated 2000-3300W unit |
| **Cooling** | 4x 120mm case fans (Arctic P12 PWM) + 80mm PSU fan (Arctic P8 Max, 3D-printed 60-to-80mm adapter) |
| **GPU slots** | 8 native PCIe slots, no risers needed |
| **OS** | Ubuntu 22.04 LTS |
| **Form** | Enclosed chassis |
| **Role** | LocoBench -- RTX-era tier benchmarking |

Colmena means "hive" in Spanish. Many workers under one roof, doing the same kind of work at different scales.

Colmena is the RTX-era benchmarking platform. Every VRAM tier from the RTX 2000 generation forward is represented at or near its floor card, giving honest baselines that readers with better hardware can only improve on. The matched-trio arrangement (3x RTX 2060 Super 8 GB) also means repeat measurements at a single tier to discipline variance, and the floor of each consumer tier is visible directly without swapping cards.

The i3-3220 CPU and 8 GB RAM ceiling exist by design. The CPU's job is to boot the OS and manage the PCIe bus. Over-speccing the host would make Colmena a worse benchmark instrument -- it measures GPU capability on modest hardware, which is what most users actually have.

**GPU lineup:**

| Card | VRAM | Bandwidth | Architecture | Tensor Cores | Role |
|------|------|-----------|-------------|--------------|------|
| GTX 1060 6 GB x3 | 6 GB each | 192 GB/s | Pascal | No | 6 GB tier (Pascal, no Tensor Cores); bridges into Tortuga's pre-RTX coverage |
| RTX 2060 Super 8 GB x3 | 8 GB each | 448 GB/s | Turing | Yes | 8 GB RTX-era floor; matched trio for variance discipline |
| RTX 4060 Ti 16 GB | 16 GB | 288 GB/s | Ada Lovelace | Yes | 16 GB consumer floor -- documents the memory-bus penalty |

Multi-GPU experiments live on Hidra, where full-bandwidth PCIe x16 slots isolate the interconnect variable cleanly. Adapter training lives on Búho, where the V100 32 GB on a dedicated machine eliminates contention. Colmena's job is reproducible RTX-era tier benchmarking.

**Best at:** RTX-era LocoBench tier benchmarking. Repeat-measurement discipline via the matched 2060 Super trio. Modest-host, GPU-first results that readers can extrapolate from.

---

## Tortuga

**WEIHO 8-GPU Enclosed Chassis -- Pre-RTX Legacy Tier Benchmarking**

| | |
|---|---|
| **Chassis** | WEIHO 8-GPU enclosed mining rig |
| **GPUs** | GTX 950 2 GB, GTX 960 4 GB, GTX 1050 Ti 4 GB, GTX 1060 3 GB, GTX 1060 6 GB, GTX 980 Ti 6 GB, GTX Titan X 12 GB (7 cards) |
| **OS** | Ubuntu 22.04 LTS |
| **Form** | Enclosed chassis |
| **Role** | LocoBench -- pre-RTX legacy tier benchmarking; powered on for benchmark runs only |
| **Notes** | No Tensor Cores across entire fleet. Slot 4 occupied by PCIe NVMe (M.2 SATA bandwidth conflict). |

Tortuga means "turtle" in Spanish. It moves at its own pace and wakes only when called.

Tortuga holds every GPU tier that predates the RTX era -- Pascal, Maxwell, and the Maxwell-era Titan X that punched above its weight for years. The machine is not running continuously. It powers on for benchmarking sessions and goes back to sleep. This is deliberate: the hardware is well-understood, the results are reproducible, and there's no reason to keep it warm between runs.

The fleet covers a wide arc of consumer hardware history. The GTX 950 represents the genuine floor -- 2 GB VRAM, Maxwell architecture, what a budget builder was likely to have in 2015-2016. The Titan X at the other end of the rack represents 12 GB Maxwell-era compute, still capable for its age. The GTX 980 Ti is a similar wildcard -- 6 GB Maxwell-era bandwidth, faster in some workloads than modern 6 GB budget cards.

None of these cards have Tensor Cores. That's the defining characteristic of the Tortuga fleet: inference runs on standard CUDA cores only. Comparing Tortuga results against RTX cards isolates exactly what Tensor Core acceleration contributes at each VRAM tier.

**GPU fleet -- pre-RTX coverage:**

| Card | VRAM | Bandwidth | Architecture | Notes |
|------|------|-----------|-------------|-------|
| GTX 950 | 2 GB | 105 GB/s | Maxwell | Absolute floor; 2 GB VRAM severely limits model selection |
| GTX 960 | 4 GB | 112 GB/s | Maxwell | Entry 4 GB tier |
| GTX 1050 Ti | 4 GB | 112 GB/s | Pascal | 4 GB Pascal floor; direct comparison to Hormiga |
| GTX 1060 3 GB | 3 GB | 192 GB/s | Pascal | Unusual tier -- 3 GB sits between 2 GB and 4 GB floors |
| GTX 1060 6 GB | 6 GB | 192 GB/s | Pascal | 6 GB Pascal floor |
| GTX 980 Ti | 6 GB | 336 GB/s | Maxwell | Legacy high-end; bandwidth outlier for its VRAM tier |
| GTX Titan X | 12 GB | 336 GB/s | Maxwell | Maxwell 12 GB; counterpoint to RTX 3060 12 GB Ampere |

**Best at:** Pre-RTX benchmarking. Documenting the no-Tensor-Core inference baseline. Showing students what older hardware can still accomplish -- and where it falls short.

---

## Hormiga

**Lenovo ThinkCentre M710s -- Minimum Viable Inference Node**

| | |
|---|---|
| **Chassis** | Lenovo ThinkCentre M710s (SFF) |
| **CPU** | Intel Core i5 7th Gen (Kaby Lake) |
| **GPU** | NVIDIA GeForce GTX 1050 Ti LP 4 GB |
| **OS** | Ubuntu 22.04 LTS |
| **Role** | Minimum viable inference node, reference testing |

Hormiga means "ant" in Spanish. Small, low-profile, and gets the job done.

The ThinkCentre M710s is a small form factor machine -- a standard SFF chassis that won't accept a full-height GPU. The 1050 Ti LP (low-profile) is the right card for the right slot: Pascal architecture, 4 GB GDDR5, 112 GB/s memory bandwidth. 4 GB VRAM is the binding constraint. It runs quantised 7B models at Q4 -- tightly, but it runs them.

The question Hormiga answers is whether a node at the low end of the capability range can still serve useful inference. If a Q4_K_M model loads and runs here, it runs on comparable consumer hardware. The ThinkCentre form factor is familiar to anyone in an office or educational institution -- exactly the kind of machine a department already owns and might press into service.

Ubuntu 22.04 LTS matches the rest of the fleet. Same CUDA toolkit, same driver stack, same Ollama installation path. The 1050 Ti LP shares its VRAM tier and bandwidth profile with Tortuga's GTX 1050 Ti, making cross-machine comparisons between SFF and open-chassis deployments straightforward.

**Best at:** Validating inference on constrained hardware. Representing what a department's existing PC can actually run.

---

## Puente

**Ryzen 5 2600 Desktop -- LocoPuente PoC and LocoEnsayo Host**

| | |
|---|---|
| **Chassis** | Desktop tower |
| **CPU** | AMD Ryzen 5 2600 |
| **GPU** | NVIDIA RTX 3090 24 GB (single card) |
| **OS** | Ubuntu 22.04 LTS |
| **Role** | LocoPuente "closing the gap" PoC; LocoEnsayo AI rehearsal host (CloudCore Networks, Pinnacle Tours, TalkBuddy backend) |

Puente means "bridge" in Spanish. It bridges students to the lab's stack -- one machine, one card, one URL, everything they need.

Puente is the student-facing host. The 24 GB of VRAM on the RTX 3090 lets LLM inference, image generation, voice services, and the LocoEnsayo chatbots all co-reside on one card with comfortable headroom.

**LocoPuente (BridgeAI) PoC.** Puente runs the full local-AI stack described in `locopuente-project-brief.md`: Ollama, Open WebUI, Perplexica, SearXNG, AnythingLLM for domain RAG, Open Notebook AI, Speaches for STT/TTS, ComfyUI for image generation, and the custom research-consent chat interface. The PoC demonstrates that the BridgeAI service model works on hardware that costs less than a single semester of commercial AI subscriptions for a cohort of students.

**LocoEnsayo rehearsal platform.** The rehearsal platform that lets students practice real-world professional scenarios now lives on the same machine. Rehearsal, not simulation. The distinction matters: simulation implies a technical model; rehearsal implies preparation for doing the real thing. A student doesn't simulate a security audit -- they rehearse one, then go do it for real.

LocoEnsayo currently runs three scenarios on Puente:

**CloudCore Networks** (server-side, running on Puente) -- a fictional IT company populated with AI chatbot employees, each with unique backstories, roles, and institutional knowledge. Students read the CloudCore website, navigate the organisation, and interview virtual employees to extract requirements, conduct security assessments, or understand business problems -- the same cognitive and professional work they would do in a real engagement, in a space where mistakes are safe and scenarios are repeatable. IT, security, web design, and business analysis contexts.

**Pinnacle Tours** (server-side, running on Puente) -- a second fictional company with a broader business flavour. Where CloudCore skews toward IT-facing disciplines, Pinnacle Tours opens LocoEnsayo to marketing, operations, HR, customer experience, and general management scenarios.

**TalkBuddy** (client-side Electron app, Puente provides the Ollama backend) -- conversation rehearsal for the scenarios that can't be scripted around a fictional company. Firing someone. Delivering bad news. Conflict resolution. A doctor explaining a difficult diagnosis. A social worker in a crisis conversation. TalkBuddy puts students in those conversations before they face them for real, with real-time speech recognition and synthesis so the rehearsal feels like an actual conversation rather than a chat interface. Available as desktop, Docker, and server installations. [github.com/michael-borck/talk-buddy](https://github.com/michael-borck/talk-buddy)

Puente also serves as the Ollama backend for the wider LocoLabo client-app ecosystem: **StuddyBuddy** (study companion) and **Career Compass** (careers guidance) both point at Puente for local inference alongside TalkBuddy. One backend, many apps -- each app ships as its own client but shares the inference and voice services on Puente.

The architectural split is worth noting: CloudCore, Pinnacle Tours, and the LocoPuente web stack are server-side -- students connect via browser to Puente. TalkBuddy, StuddyBuddy, and Career Compass are local client apps the student installs, pointing at Puente (or a cloud endpoint) for Ollama inference and Speaches for STT/TTS. The RTX 3090's 24 GB VRAM gives Puente enough headroom to serve multiple concurrent sessions across both deployment patterns.

**Best at:** Hosting the full LocoPuente stack and the LocoEnsayo rehearsal suite on one machine. Running CloudCore Networks and Pinnacle Tours server-side. Providing the Ollama backend for TalkBuddy, StuddyBuddy, and Career Compass client installations.

---

## Búho

**X99 Single-Xeon Workstation -- Dedicated Inference and LocoLLM Adapter Training**

| | |
|---|---|
| **Motherboard** | X99 single-socket, LGA2011-3 |
| **CPU** | Intel Xeon (E5 series) |
| **Memory** | 32 GB DDR4 |
| **GPU** | Tesla V100 32 GB HBM2 |
| **OS** | Ubuntu 22.04 LTS |
| **Role** | Dedicated AI inference; LocoLLM adapter training; potential full fine-tuning |

Búho means "owl" in Spanish. Patient, nocturnal, a specialist at the one thing it does.

Búho is the lab's dedicated training and inference station. One machine, one card, one purpose. The V100 32 GB runs without competing for PCIe lanes, CPU cycles, or thermal headroom. Where Colmena works through its bench runs across the consumer-card fleet and Hidra swaps cards in and out for server benchmarking and multi-GPU experiments, Búho sits quietly and works through the night on adapter-training runs.

The V100 32 GB is a few generations old -- Volta, 2017 -- but it remains excellent at the specific job asked of it: first-generation Tensor Cores enable mixed-precision training that the P100 and P40 cannot accelerate, 900 GB/s of HBM2 bandwidth still outruns most consumer cards, and 32 GB of VRAM allows longer context windows, larger batch sizes, and higher LoRA ranks than any 16 GB server card. Adapter training runs that take overnight on the P100 complete in a fraction of the time on Búho. The machine doesn't need to be the newest card in the lab; it needs to be left alone to do its work.

Búho has two primary workloads:

**LocoLLM adapter training.** The core training workflow for LocoLLM specialists runs on Búho. Adapter training uses Unsloth for QLoRA where supported, and vanilla PEFT / HuggingFace Trainer for higher-precision work on the Volta path. Training runs typically run overnight; the dedicated-machine arrangement means no contention with benchmarking or multi-GPU experiments.

**Dedicated inference.** Between training runs, Búho serves as a single-card inference node for workloads that need the full 32 GB without shared access -- longer context windows, 30B-class quantised models, KV-cache-heavy workloads that don't fit on the 16 GB tier elsewhere in the fleet.

Beyond adapter training, Búho has the capacity for full-precision fine-tuning of smaller models (3B-7B class) if a research question ever requires it. That is a forward-looking capability, not a primary use case. LocoLLM itself remains an adapter-training project.

Thirty-two gigabytes of system RAM matches the VRAM and provides headroom for dataset preprocessing and tokeniser operations without swapping. The single-socket X99 platform is sufficient -- the GPU does the work, the CPU manages it.

**Best at:** Uninterrupted overnight adapter training. Single-card inference at the 32 GB tier. Being the quiet, patient specialist that does one thing well.

---

## Hidra

**X99 Dual-Xeon Open Frame -- LocoConvoy Multi-GPU, Server GPU Benchmarking, GPU Onboarding**

| | |
|---|---|
| **Motherboard** | X99 MD8 dual-socket kit, LGA2011-3 |
| **CPU** | 2x Intel Xeon E5-2680 v4 (14 cores / 28 threads each; 28C / 56T total, Broadwell-EP) |
| **Memory** | DDR4 ECC |
| **GPU slots** | 4x PCIe x16 (full electrical width, dual-CPU lane provisioning) |
| **Chassis** | Open frame |
| **Server GPUs** | Tesla V100 16 GB HBM2, Tesla P100 16 GB HBM2; Tesla M40 24 GB and Tesla P40 incoming |
| **Consumer rotation** | GTX 1070, RTX 3050, RTX 3060 12 GB (onboarding + small-card benchmarks) |
| **OS** | Ubuntu 22.04 LTS |
| **Role** | LocoConvoy multi-GPU experiments; LocoBench server GPU benchmarking; GPU onboarding for every new card in the lab |

Hidra means "hydra" in Spanish. Many heads, each doing its own thing, sharing one body.

Hidra does three jobs on the same open-frame workstation. The four full-width PCIe x16 slots, the dual-CPU lane provisioning, and the easy card-swap access are the reason all three can co-locate.

**LocoConvoy multi-GPU experiments.** Where Colmena's mining-oriented board trades PCIe width for slot count, Hidra runs four slots at full x16. For experiments where PCIe bandwidth dominates -- vLLM tensor parallelism, cross-card KV-cache traffic, pipeline-parallel inference -- Hidra provides the uncrippled interconnect that a mining board cannot.

**Server GPU benchmarking.** The Tesla M40, P40, P100, and V100 family all pass through Hidra for LocoBench runs at their native VRAM tiers. The open-frame chassis accepts the passive-cooled datacenter form factor better than Colmena's enclosed mining rig, and the full x16 slots mean the benchmark reflects the card rather than the slot. Currently installed: V100 16 GB (Volta, Tensor Cores, HBM2 at 900 GB/s) and P100 16 GB (Pascal, HBM2 at 732 GB/s). Incoming: M40 24 GB (Maxwell, floor of the 24 GB server tier) and P40 24 GB (Pascal with CC 6.1, full modern inference stack at 24 GB).

**GPU onboarding.** Every new card in the lab -- consumer or datacenter, current generation or deprecated -- arrives on Hidra first for burn-in, driver validation, and compatibility testing before being assigned to its permanent home. The open-frame chassis is the reason. No case to open, no cable management, no thermal envelope to respect for a brief characterisation run -- slot a card, power on, test, move it on.

Dual E5-2680 v4s give Hidra something the rest of the fleet lacks: real CPU. Twenty-eight cores and fifty-six threads handle data preprocessing, multi-process inference orchestration, and vLLM's Python overhead without the CPU ever becoming the bottleneck -- which is exactly what you want when the research question is about GPU scaling. DDR4 ECC and the full lane count on both sockets round out the platform.

**Multi-GPU operating modes (LocoConvoy research tracks):**

*Load balancer:* Multiple Ollama instances behind an nginx or FastAPI router distributing requests round-robin. Increases concurrent throughput with no quality tradeoff. Relevant for multi-user AnythingLLM sessions.

*Mixture of Agents (MoA):* Two cards act as proposers, generating independent responses to the same query at slightly different temperatures. A third card acts as aggregator, synthesising the two outputs into a final response. Quality improvements are most noticeable on reasoning tasks. See [arxiv.org/abs/2406.04692](https://arxiv.org/abs/2406.04692).

*Speculative decoding:* A small draft model on one card generates candidate tokens rapidly. A larger verifier model on another card accepts or rejects token batches. Net result is lower latency from the large model. Supported natively by llama.cpp via `--model-draft`.

*vLLM tensor parallelism:* Matched cards pool VRAM across PCIe. Enables models larger than any single card's VRAM. PCIe bandwidth becomes the primary bottleneck, which is precisely why these experiments live on Hidra's full x16 interconnect -- isolating the bandwidth variable is the central research question.

**Best at:** Full-bandwidth multi-GPU research across load balancing, MoA, speculative decoding, and tensor parallelism. Rapid GPU onboarding on open-frame hardware.

---

## Fleet at a Glance

| Machine | Sub-project(s) | GPU(s) | VRAM | Primary Role |
|---------|----------------|--------|------|--------------|
| **Colmena** (WEIHO 8-GPU) | LocoBench | GTX 1060 6GB x3, RTX 2060 Super x3, RTX 4060 Ti 16GB | 6/8/16 GB | RTX-era consumer tier benchmarking |
| **Tortuga** (WEIHO 8-GPU) | LocoBench | GTX 950/960/1050Ti/1060 3GB/1060 6GB/980Ti/Titan X | 2-12 GB | Pre-RTX legacy benchmarking (powered on for runs only) |
| **Puente** (Ryzen 5 2600) | LocoPuente / LocoEnsayo | RTX 3090 24 GB | 24 GB | Student-facing BridgeAI stack and rehearsal chatbots |
| **Búho** (X99 single Xeon) | LocoLLM | Tesla V100 32 GB | 32 GB | Dedicated adapter training and single-card inference |
| **Hormiga** (ThinkCentre M710s) | LocoBench | GTX 1050 Ti LP | 4 GB | Minimum viable inference node, SFF reference testing |
| **Hidra** (X99 dual Xeon, open frame) | LocoConvoy / LocoBench | V100 16 GB, P100 16 GB; M40, P40 incoming; GTX 1070, RTX 3050, RTX 3060 12 GB rotation | 4x PCIe x16 | Multi-GPU experiments, server GPU benchmarking, GPU onboarding |
| **Poco** (MacBook M1) | LocoLabo | Apple M1 GPU | 16 GB unified | Remote terminal, Apple Silicon testing |

†Arriving

---

## Hardware Notes

The specific hardware here isn't prescriptive. The P100 needs a PCIe x16 slot, adequate power, and airflow over a passively cooled card. Colmena doesn't require this exact GPU lineup -- any PCIe cards work. Hormiga doesn't require a ThinkCentre -- any low-profile CUDA card with 4 GB in any SFF chassis fits the role. Hidra doesn't require an X99 board specifically -- any dual-CPU or HEDT platform with multiple full-x16 slots in an accessible open frame fills the same role. Búho doesn't require X99 either -- any workstation that can host a V100 32 GB with adequate cooling and enough system RAM to preprocess training data is sufficient. Puente doesn't require a Ryzen 5 2600 -- any desktop with enough PCIe and power budget for a 24 GB consumer flagship fits the PoC role.

What matters for replication is capability tier, not specific parts. Match the VRAM range and CUDA support, source whatever is available locally at the time.

**Why Nvidia only?** The entire local LLM toolchain -- Ollama, llama.cpp, PyTorch, bitsandbytes, Unsloth -- targets CUDA first. AMD's ROCm stack exists and is improving, but driver support is narrower, community troubleshooting is thinner, and the tooling friction is meaningfully higher. Intel Arc is earlier still. For a lab that needs to work reliably with minimal sysadmin overhead, CUDA is the only practical choice today.

The secondhand market reinforces this. The cryptocurrency mining boom flooded resale channels with Nvidia consumer cards at accessible prices. AMD equivalents at the same VRAM tiers are rarer and less standardised. And the overwhelming majority of users running local LLMs on consumer hardware are on Nvidia -- LocoBench floor cards need to represent what people actually have.

Apple Silicon is the exception, and Poco covers that path via Metal and MLX. If ROCm matures to the point where an AMD card is a genuine drop-in for Ollama inference, it becomes a candidate for a Colmena slot. That day isn't today.

The lab exists at this price point deliberately. Frontier model access on premium hardware -- cloud APIs, Apple Silicon, high-end workstations -- is available, but it concentrates AI capability around cost. A lab built from secondhand consumer hardware makes the same workflows accessible to anyone willing to learn the stack. Smaller models on modest hardware are genuinely useful for exploration, brainstorming, and iteration. That use case doesn't require a frontier model and doesn't require expensive hardware. It requires understanding what you're doing -- which is the point of the lab.
