---
title: "Frequently Asked Questions"
---

---

## The Cloud Question

### Why not just use the cloud?

Two of the lab's three core roles cannot be done in the cloud at any price. [LocoBench](https://locobench.org) requires consumer GPUs from 2 GB to 24 GB -- GTX 950s, GTX 1050 Tis, RTX 2060 Supers. No cloud provider offers those cards. The lowest tier widely available is a T4 at 16 GB. Multi-GPU architecture research with consumer Turing and Ampere cards is similarly unavailable. Only inference serving is straightforwardly replicable in the cloud.

For the work that *could* be done in the cloud, local is 6-8x cheaper per training run. See [Economics of Local Training](economics-of-local-training.md) for the full numbers.

### Is this just a cost-saving exercise?

No. Cost matters -- the lab runs for under $1,000 AUD per year in electricity -- but the primary argument is capability, not frugality. The research questions LocoBench asks ("what can a student run on a $150 secondhand GPU?") can only be answered on that actual hardware. The data doesn't exist in the cloud because the hardware doesn't exist in the cloud.

The privacy argument is equally structural. Student assessment data, conversation transcripts, and rehearsal scenarios never leave the machine. Not by policy -- by architecture.

---

## The Hardware

### Why secondhand hardware?

Three reasons. First, it's what students and small institutions actually have -- research on consumer floor hardware is only valid if it runs on consumer floor hardware. Second, the secondhand market for previous-generation GPUs remains accessible while new hardware prices are inflated by AI data centre demand. Third, the capital outlay is low enough that anyone can replicate the setup. The entire lab was assembled for well under $2,000 AUD.

### Can I replicate this?

Yes. The minimum viable setup is one machine with a CUDA-capable GPU and 4+ GB VRAM running Ubuntu, Ollama, and llama.cpp. A secondhand desktop with a GTX 1050 Ti will get you started for under $200 AUD. The [Machine Setup](machine-setup.md) guide covers the installation path.

For benchmarking, any consumer Nvidia GPU works. For fine-tuning, you want 16 GB VRAM -- a Tesla P100 can be sourced secondhand for $150-250 AUD. For multi-GPU experiments, a mining chassis like the WEIHO 8-GPU rig accepts any PCIe card without risers.

### Why Nvidia only?

The entire local LLM toolchain -- Ollama, llama.cpp, PyTorch, bitsandbytes, Unsloth -- targets CUDA first. AMD's ROCm stack is improving but driver support is narrower and community troubleshooting is thinner. Intel Arc is earlier still. For a lab that needs to work reliably with minimal sysadmin overhead, CUDA is the only practical choice today. Apple Silicon is the exception, covered via Metal and MLX on Poco.

### How much does it cost to run?

Colmena (always-on, 8-GPU box): $500-870 AUD per year. Tortuga (on-call benchmarking, 8-GPU box): ~$64 AUD per year. Combined: roughly $580-930 AUD per year. A single training run costs about $1.05 in electricity. A semester of adapter development adds ~$21. See [Economics of Local Training](economics-of-local-training.md) for the breakdown.

---

## The Models

### Do small models actually work?

For delegation -- asking the model to produce a finished answer you trust without checking -- small models are measurably worse than frontier alternatives. That is honest and documented.

For conversation -- brainstorming, ideation, iteration, challenging your assumptions, rehearsing professional scenarios -- small models are sufficient. The interaction requires a model that responds coherently and keeps up with your reasoning, not one that responds with authority. A 4B model running locally does this well. This is the "Conversation, not Delegation" position that underpins the lab's work.

### Why not just use a bigger model locally?

You can. A 7B or 13B model on an RTX 3090 will outperform a 4B model on a GTX 1050 Ti. But the research question is about the floor, not the ceiling. What is the minimum viable hardware for useful inference? Where exactly does quality degrade? What can fine-tuning recover at the bottom of the range? Those questions only have answers if you run the full tier stack.

---

## The Projects

### Why five projects instead of one?

Different research questions require different methodologies and different hardware. [LocoLLM](https://locollm.org) studies whether specialist routing compensates for model size. [LocoBench](https://locobench.org) maps inference quality across every consumer VRAM tier. [LocoConvoy](https://lococonvoy.org) tests multi-GPU architectures on PCIe hardware. [LocoEnsayo](https://locoensayo.org) builds rehearsal environments for professional education. They share infrastructure and philosophy but produce distinct research outputs.

### What is LocoLabo then?

LocoLabo is the umbrella -- the lab itself, not a software project. It coordinates the sub-projects, hosts the shared documentation ([Meet the Lab](meet-the-lab.md), [Economics](economics-of-local-training.md), [GPU Reference](nvidia-gpu-reference.md)), and provides the public-facing site at [locolabo.org](https://locolabo.org).

### Who is this for?

Educators who want to use AI in teaching without sending student data to the cloud. Researchers studying local AI on consumer hardware. Students building the system as part of their learning. Small organisations and departments that need AI capability without subscription costs or cloud dependencies. Anyone curious about what the floor of consumer AI hardware can actually do.

---

## Research and Reproducibility

### Is this real research or a hobby project?

Real research. The lab sits within Curtin University's School of Marketing and Management. The work targets peer-reviewed venues including ACIS and the Australasian Journal of Information Systems. LocoLLM and LocoEnsayo follow design science research methodology. LocoBench produces reproducible community benchmarks.

### Can reviewers verify the results?

Yes -- that's the point. Every result runs on hardware you can buy on eBay for under $200 AUD. If a paper claims "routed 4-bit specialists achieve X% of GPT-4 performance on these tasks," any reviewer can verify it on their own machine. The consumer hardware constraint is a limitation that doubles as a methodological strength.
