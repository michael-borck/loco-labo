---
title: "Meet the Lab"
---

LocoLabo is the umbrella research initiative -- five sub-projects running across six machines. None of them are new. All were sourced secondhand. Hardware was acquired opportunistically -- the right capability at the right price, not a planned procurement.

The naming follows a Spanish thread: Colmena (hive), Tortuga (turtle), Poco (a little), Hormiga (ant), Cerebro (brain), and Pulpo (octopus). The hive coordinates many workers and carries the heavy training loads, the turtle holds the legacy fleet and wakes slowly when called, the little one connects you to all of them, the ant keeps the floor honest on minimal hardware, the brain runs the rehearsal, and the octopus grabs new cards, tests them, and passes them on to their permanent home.

**Five sub-projects under LocoLabo:**

- **LocoLLM** (Colmena) -- infrastructure, architecture research, adapter training
- **LocoBench** (Tortuga + Hormiga) -- benchmarking platform, community results
- **LocoConvoy** (Colmena) -- multi-GPU architecture experiments: load balancing, Mixture of Agents, vLLM tensor parallelism
- **LocoEnsayo** (Cerebro) -- authentic assessment rehearsal platform, runs CloudCore Networks, Pinnacle Tours, TalkBuddy
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

**WEIHO 8-GPU Enclosed Chassis -- Multi-GPU Experiments and Training Server**

| | |
|---|---|
| **Chassis** | WEIHO 8-GPU enclosed mining rig (72x42x18cm, steel, blue lid) |
| **Motherboard** | Intel LGA1155, B75/H61 chipset |
| **CPU** | Intel i3-3220 (Ivy Bridge, dual core) |
| **GPUs** | 3x GTX 1060 6 GB, 3x RTX 2060 Super 8 GB, Tesla P100 16 GB HBM2 (arriving) |
| **Memory** | 8 GB DDR3 SODIMM (board maximum) |
| **Storage** | 128 GB mSATA (OS) + WD Scorpio Blue 750 GB SATA (model storage via `OLLAMA_MODELS`) |
| **PSU** | Integrated 2000-3300W unit |
| **Cooling** | 4x 120mm case fans (Arctic P12 PWM) + 80mm PSU fan (Arctic P8 Max, 3D-printed 60-to-80mm adapter) |
| **GPU slots** | 8 native PCIe slots, no risers needed |
| **OS** | Ubuntu 22.04 LTS |
| **Form** | Enclosed chassis |
| **Role** | LocoConvoy multi-GPU architecture research, LocoLLM inference and adapter training |

Colmena means "hive" in Spanish. Multiple workers, one coordinated system.

Colmena is the multi-GPU experimentation platform. The GPU lineup pairs two matched trios -- 3x GTX 1060 6 GB (Pascal, no Tensor Cores) and 3x RTX 2060 Super 8 GB (Turing, Tensor Cores) -- enabling direct generational comparisons of multi-GPU scaling strategies. The Tesla P100 16 GB HBM2 handles adapter training duties.

The i3-3220 CPU and 8 GB RAM ceiling exist by design. The CPU's job is to boot the OS and manage the PCIe bus. Over-speccing the host system would make Colmena a worse research instrument -- it measures GPU capability on modest hardware, which is what most users actually have.

Colmena has two roles in priority order:

**1. Multi-GPU architecture research (LocoConvoy).** The matched trios enable three distinct research tracks: independent-worker load balancing, Mixture of Agents across cards, and vLLM tensor parallelism experiments. The GTX 1060 trio (18 GB pooled, no Tensor Cores) versus the RTX 2060 Super trio (24 GB pooled, with Tensor Cores) is a direct generational comparison of pooled VRAM performance on PCIe-connected consumer hardware.

**2. Fine-tuning (LocoLLM).** The Tesla P100's 16 GB of HBM2 at 732 GB/s enables full 16-bit LoRA rather than 4-bit QLoRA, longer context windows (4096-8192 tokens), larger batch sizes, and higher LoRA ranks. Pascal architecture (compute capability 6.0) doesn't have Tensor Cores, so training runs through standard CUDA cores using vanilla PEFT or HuggingFace Trainer rather than Unsloth. Expect roughly 2-3x slower wall-clock time than a 2060 Super running Unsloth QLoRA for an equivalent job. A three-hour Unsloth run on a 2060 Super becomes a six-to-eight-hour PEFT run on the P100. That's an overnight job, not a multi-day one.

**GPU lineup:**

| Card | VRAM | Bandwidth | Architecture | Tensor Cores | Role |
|------|------|-----------|-------------|--------------|------|
| GTX 1060 6 GB x3 | 6 GB each | 192 GB/s | Pascal | No | Multi-GPU pooling (18 GB); pre-RTX scaling baseline |
| RTX 2060 Super 8 GB x3 | 8 GB each | 448 GB/s | Turing | Yes | Multi-GPU pooling (24 GB); RTX-era scaling testbed |
| Tesla P100 16 GB | 16 GB | 732 GB/s | Pascal | No | Fine-tuning, high-fidelity LoRA (arriving) |

**Multi-GPU operating modes:**

*Load balancer:* Multiple Ollama instances behind an nginx or FastAPI router distributing requests round-robin. Increases concurrent throughput with no quality tradeoff. Relevant for multi-user AnythingLLM sessions.

*Mixture of Agents (MoA):* Two cards act as proposers, generating independent responses to the same query at slightly different temperatures. A third card acts as aggregator, synthesising the two outputs into a final response. Quality improvements are most noticeable on reasoning tasks. See [arxiv.org/abs/2406.04692](https://arxiv.org/abs/2406.04692).

*Speculative decoding:* A small draft model on one card generates candidate tokens rapidly. A larger verifier model on another card accepts or rejects token batches. Net result is lower latency from the large model. Supported natively by llama.cpp via `--model-draft`.

*vLLM tensor parallelism:* Matched cards (GTX 1060 x3 or RTX 2060 Super x3) pool VRAM across PCIe. Enables models larger than any single card's VRAM. PCIe bandwidth becomes the primary bottleneck, making the cross-generational comparison the central research question.

**Best at:** Multi-GPU architecture experiments. Cross-generational pooling research. Overnight adapter training on the P100.

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

## Cerebro

**Ryzen 5 2600 Desktop -- LocoEnsayo Rehearsal Host**

| | |
|---|---|
| **Chassis** | Desktop tower |
| **CPU** | AMD Ryzen 5 2600 |
| **GPU** | 2x RTX 2060 Super 8 GB |
| **OS** | Ubuntu 22.04 LTS |
| **Role** | LocoEnsayo -- AI simulation host (CloudCore Networks, Pinnacle Tours, TalkBuddy) |

Cerebro means "brain" in Spanish. It runs the thinking behind LocoEnsayo.

Cerebro is the dedicated host for LocoEnsayo -- the rehearsal platform that lets students practice real-world professional scenarios before they encounter the real thing. Rehearsal, not simulation. The distinction matters: simulation implies a technical model; rehearsal implies preparation for doing the real thing. A student doesn't simulate a security audit -- they rehearse one, then go do it for real.

LocoEnsayo currently runs three scenarios:

**CloudCore Networks** (server-side, running on Cerebro) -- a fictional IT company populated with AI chatbot employees, each with unique backstories, roles, and institutional knowledge. Students read the CloudCore website, navigate the organisation, and interview virtual employees to extract requirements, conduct security assessments, or understand business problems -- the same cognitive and professional work they would do in a real engagement, in a space where mistakes are safe and scenarios are repeatable. IT, security, web design, and business analysis contexts.

**Pinnacle Tours** (server-side, running on Cerebro) -- a second fictional company with a broader business flavour. Where CloudCore skews toward IT-facing disciplines, Pinnacle Tours opens LocoEnsayo to marketing, operations, HR, customer experience, and general management scenarios. Same server-side architecture on Cerebro, different organisational context.

**TalkBuddy** (client-side Electron app, Cerebro provides the Ollama backend) -- conversation rehearsal for the scenarios that can't be scripted around a fictional company. Firing someone. Delivering bad news. Conflict resolution. A doctor explaining a difficult diagnosis. A social worker in a crisis conversation. TalkBuddy puts students in those conversations before they face them for real, with real-time speech recognition and synthesis so the rehearsal feels like an actual conversation rather than a chat interface. Available as desktop, Docker, and server installations. [github.com/michael-borck/talk-buddy](https://github.com/michael-borck/talk-buddy)

The architectural split is worth noting: CloudCore and Pinnacle Tours are server-side -- students connect via browser to Cerebro. TalkBuddy is a local Electron app the student installs, pointing at Cerebro (or a cloud endpoint) for Ollama inference and Speaches for STT/TTS. Two RTX 2060 Supers give Cerebro enough headroom to serve multiple concurrent sessions across both deployment patterns.

**Best at:** Hosting the full LocoEnsayo rehearsal suite. Running CloudCore Networks and Pinnacle Tours server-side. Providing the Ollama backend for TalkBuddy client installations.

---

## Pulpo

**B250 Mining Board -- Overflow, GPU Onboarding, and Ad Hoc Experiments**

| | |
|---|---|
| **Chassis** | B250 mining board, open air |
| **GPUs** | RTX 3060 12 GB |
| **Location** | TBD |
| **Role** | Overflow, GPU onboarding/testing, ad hoc experiments |

Pulpo means "octopus" in Spanish. It grabs new cards, tests them, and passes them on to their permanent home.

Pulpo is the staging ground. New cards arrive here first for burn-in, driver validation, and compatibility testing before being assigned to Colmena, Tortuga, or wherever they're needed. Between onboarding runs, the RTX 3060 12 GB makes it a capable ad hoc experiment node -- enough VRAM for meaningful inference work without tying up a dedicated research machine.

The open-air B250 mining board format makes GPU swaps trivial. No case to open, no cable management -- slot a card, power on, test. That's the point.

**Best at:** GPU onboarding and testing. Overflow capacity. Quick experiments that don't warrant disrupting a production machine.

---

## Fleet at a Glance

| Machine | Sub-project(s) | GPU(s) | VRAM | Primary Role |
|---------|----------------|--------|------|--------------|
| **Colmena** (WEIHO 8-GPU) | LocoConvoy / LocoLLM | GTX 1060 6GB x3, RTX 2060 Super x3, Tesla P100† | 6/8/16 GB | Multi-GPU experiments, adapter training |
| **Tortuga** (WEIHO 8-GPU) | LocoBench | GTX 950/960/1050Ti/1060 3GB/1060 6GB/980Ti/Titan X | 2-12 GB | Pre-RTX legacy benchmarking (powered on for runs only) |
| **Cerebro** (Ryzen 5 2600) | LocoEnsayo | 2x RTX 2060 Super | 2x 8 GB | AI simulation host (CloudCore, Pinnacle Tours, TalkBuddy) |
| **Hormiga** (ThinkCentre M710s) | LocoBench | GTX 1050 Ti LP | 4 GB | Minimum viable inference node, SFF reference testing |
| **Pulpo** (B250 open air) | -- | RTX 3060 12 GB | 12 GB | Overflow, GPU onboarding/testing, ad hoc experiments |
| **Poco** (MacBook M1) | LocoLabo | Apple M1 GPU | 16 GB unified | Remote terminal, Apple Silicon testing |

†Arriving

---

## Hardware Notes

The specific hardware here isn't prescriptive. The P100 needs a PCIe x16 slot, adequate power, and airflow over a passively cooled card. Colmena doesn't require this exact GPU lineup -- any PCIe cards work. Hormiga doesn't require a ThinkCentre -- any low-profile CUDA card with 4 GB in any SFF chassis fits the role. Pulpo doesn't require a B250 board -- any open-air or spare chassis with a free PCIe slot serves the staging role.

What matters for replication is capability tier, not specific parts. Match the VRAM range and CUDA support, source whatever is available locally at the time.

**Why Nvidia only?** The entire local LLM toolchain -- Ollama, llama.cpp, PyTorch, bitsandbytes, Unsloth -- targets CUDA first. AMD's ROCm stack exists and is improving, but driver support is narrower, community troubleshooting is thinner, and the tooling friction is meaningfully higher. Intel Arc is earlier still. For a lab that needs to work reliably with minimal sysadmin overhead, CUDA is the only practical choice today.

The secondhand market reinforces this. The cryptocurrency mining boom flooded resale channels with Nvidia consumer cards at accessible prices. AMD equivalents at the same VRAM tiers are rarer and less standardised. And the overwhelming majority of users running local LLMs on consumer hardware are on Nvidia -- LocoBench floor cards need to represent what people actually have.

Apple Silicon is the exception, and Poco covers that path via Metal and MLX. If ROCm matures to the point where an AMD card is a genuine drop-in for Ollama inference, it becomes a candidate for a Colmena slot. That day isn't today.

The lab exists at this price point deliberately. Frontier model access on premium hardware -- cloud APIs, Apple Silicon, high-end workstations -- is available, but it concentrates AI capability around cost. A lab built from secondhand consumer hardware makes the same workflows accessible to anyone willing to learn the stack. Smaller models on modest hardware are genuinely useful for exploration, brainstorming, and iteration. That use case doesn't require a frontier model and doesn't require expensive hardware. It requires understanding what you're doing -- which is the point of the lab.
