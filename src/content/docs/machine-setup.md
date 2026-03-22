---
title: "Machine Setup"
---

Every lab machine runs Ubuntu 22.04 LTS minimal server, provisioned by **LocoBase** — a menu-driven setup kit that handles everything from NVIDIA drivers to CUDA toolkit to Ollama to the tmux dashboard on the TTY.

**Repository:** [github.com/michael-borck/loco-base](https://github.com/michael-borck/loco-base)

## Quick start

```bash
sudo apt install git
git clone https://github.com/michael-borck/loco-base.git
cd loco-base
sudo -E bash install.sh
```

Select your machine from the menu, choose "Fresh Install", and everything runs with sensible defaults. No config file editing required.

## What it installs

| Layer | Components |
|-------|------------|
| **OS branding** | Plymouth boot splash, custom MOTD with ASCII art, two-line bash prompt with machine emoji |
| **Dashboard** | tmux auto-launch on TTY with configurable panes (htop, cmatrix, pipes.sh, GPU stats, etc.) |
| **NVIDIA** | Drivers (configurable version), CUDA 12.4 toolkit |
| **AI stack** | Ollama, Docker + NVIDIA Container Toolkit, Node.js LTS, HuggingFace CLI |
| **Security** | UFW firewall (deny inbound, allow SSH), fail2ban, lm-sensors + fancontrol |
| **Post-install** | GitHub/SSH key setup, Claude Code CLI, dashboard reconfiguration, fan curves |

## Relationship to loco-* projects

LocoBase is the **foundation layer**. It provisions a bare machine into a working lab node with GPU compute, Ollama, and Docker ready. Individual projects build on top:

- **loco-bench** — clone after loco-base, runs benchmarks using Ollama + CUDA
- **loco-llm** — clone after loco-base, trains and serves adapters via Ollama
- **loco-convoy** — clone after loco-base, runs multi-GPU experiments via vLLM
- **loco-ensayo** — clone after loco-base, deploys CloudCore API via Docker

Each project has its own setup that assumes loco-base is already in place.

## Machine lookup

The installer knows the lab fleet by name. Selecting a machine auto-configures the emoji, prompt, MOTD header, and ASCII art:

| Machine | Spanish | Emoji |
|---------|---------|-------|
| cerebro | brain | 🧠 |
| colmena | beehive | 🐝 |
| hormiga | ant | 🐜 |
| pulpo | octopus | 🐙 |
| tortuga | turtle | 🐢 |

Custom machine names are also supported for machines outside the lab fleet.

## Workflows

- **Fresh Install** — full provisioning from minimal Ubuntu server
- **Fix Drift** — idempotent re-run to restore expected state
- **Full Reset** — strip to minimal server (removes desktop environments, snaps, unnecessary services)
- **Post-Install** — GitHub auth, Claude Code, fan curves, dashboard config
- **Individual Script** — re-run any single setup step (NVIDIA, MOTD, hardening, etc.)

See the [loco-base README](https://github.com/michael-borck/loco-base) for full documentation.
