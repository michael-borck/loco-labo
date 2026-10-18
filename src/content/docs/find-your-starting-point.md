---
title: "Find Your Starting Point"
description: A short interactive guide to where in LocoLabo to start, based on what pulls you in, what hardware you have, and what you actually want to do next.
---

LocoLabo has six active projects and several supporting docs. Three short questions, and we'll point you at the one to start with — plus which of the others fit alongside.

<div id="loco-wizard"></div>

<style>
  #loco-wizard {
    margin: 2rem 0 3rem;
  }
  .lw-card {
    background: var(--sl-color-bg-nav, var(--sl-color-bg));
    border: 1px solid var(--sl-color-gray-5);
    border-radius: 0.5rem;
    padding: 1.5rem 1.75rem;
    margin-bottom: 1rem;
  }
  .lw-step {
    font-family: var(--sl-font-system-mono);
    font-size: 0.75rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--sl-color-gray-3);
    margin-bottom: 0.5rem;
  }
  .lw-question {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--sl-color-white);
    margin: 0 0 1.25rem;
    line-height: 1.4;
  }
  .lw-options {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }
  .lw-option {
    text-align: left;
    width: 100%;
    background: var(--sl-color-bg);
    border: 1px solid var(--sl-color-gray-5);
    color: var(--sl-color-text);
    padding: 0.85rem 1rem;
    border-radius: 0.375rem;
    font-size: 0.95rem;
    line-height: 1.45;
    cursor: pointer;
    transition: border-color 0.12s, background 0.12s, transform 0.06s;
    font-family: inherit;
  }
  .lw-option:hover {
    border-color: var(--sl-color-accent);
    background: var(--sl-color-accent-low);
  }
  .lw-option:active {
    transform: translateY(1px);
  }
  .lw-controls {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 1rem;
    font-size: 0.875rem;
  }
  .lw-controls button {
    background: none;
    border: none;
    color: var(--sl-color-text-accent);
    cursor: pointer;
    font: inherit;
    padding: 0.25rem 0;
  }
  .lw-controls button:hover {
    text-decoration: underline;
  }
  .lw-result-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 1rem;
    margin-bottom: 0.75rem;
    flex-wrap: wrap;
  }
  .lw-persona {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--sl-color-white);
    margin: 0;
  }
  .lw-persona-emoji {
    margin-right: 0.4rem;
  }
  .lw-retake {
    background: none;
    border: none;
    color: var(--sl-color-text-accent);
    cursor: pointer;
    font: inherit;
    font-size: 0.875rem;
    padding: 0.25rem 0;
  }
  .lw-retake:hover {
    text-decoration: underline;
  }
  .lw-persona-description {
    color: var(--sl-color-gray-2);
    margin: 0 0 1.5rem;
    line-height: 1.6;
  }
  .lw-section-label {
    font-family: var(--sl-font-system-mono);
    font-size: 0.7rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--sl-color-gray-3);
    margin: 1.5rem 0 0.5rem;
  }
  .lw-primary-card {
    background: var(--sl-color-accent-low);
    border: 1px solid var(--sl-color-accent);
    border-radius: 0.5rem;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1rem;
  }
  .lw-primary-card h3 {
    margin: 0 0 0.4rem;
    font-size: 1.15rem;
  }
  .lw-primary-card h3 a {
    color: var(--sl-color-white);
  }
  .lw-primary-card p {
    margin: 0;
    color: var(--sl-color-gray-2);
    line-height: 1.5;
  }
  .lw-secondary-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 0.5rem;
    margin-bottom: 1rem;
  }
  @media (min-width: 50rem) {
    .lw-secondary-grid {
      grid-template-columns: 1fr 1fr;
    }
  }
  .lw-secondary-card {
    background: var(--sl-color-bg);
    border: 1px solid var(--sl-color-gray-5);
    border-radius: 0.375rem;
    padding: 0.85rem 1rem;
  }
  .lw-secondary-card strong a {
    color: var(--sl-color-white);
  }
  .lw-secondary-card p {
    margin: 0.25rem 0 0;
    font-size: 0.9rem;
    color: var(--sl-color-gray-3);
    line-height: 1.45;
  }
  .lw-hardware-note {
    background: var(--sl-color-bg);
    border-left: 3px solid var(--sl-color-accent);
    padding: 0.6rem 0.9rem;
    margin: 1rem 0;
    font-size: 0.9rem;
    color: var(--sl-color-gray-2);
    line-height: 1.5;
  }
  .lw-read-first {
    margin-top: 1.5rem;
    font-size: 0.95rem;
  }
</style>

<script>
(function () {
  const root = document.getElementById('loco-wizard');
  if (!root) return;

  const questions = [
    {
      key: 'pull',
      label: 'Question 1 of 3',
      prompt: 'What pulls you in?',
      options: [
        { value: 'budget_rebel', text: "I'm tired of paying per-token for things my hardware could do." },
        { value: 'tinkerer',     text: "I want to crack models open and rewire how they work." },
        { value: 'researcher',   text: "I need reproducible experiments and honest baselines." },
        { value: 'educator',     text: "I teach, and I want students contributing to real infrastructure." },
        { value: 'vault',        text: "My data does not leave my machine — period." },
        { value: 'scrapper',     text: "I'm assembling capability from secondhand parts on a tight budget." },
        { value: 'operator',     text: "I run a small or medium organisation and need AI tools that work for my team — pragmatic, reliable, accountable." },
        { value: 'builder',      text: "I'm building a product on top of local AI — I need stable inference and adapters, not raw research." },
        { value: 'skeptic',      text: "I haven't decided local AI is ready — I want stress-tested claims and honest negative results before committing." }
      ]
    },
    {
      key: 'hardware',
      label: 'Question 2 of 3',
      prompt: "What's your hardware situation?",
      options: [
        { value: 'none',     text: "None or unsure — I'd start by reading." },
        { value: 'old',      text: "An older or secondhand card (4–6 GB)." },
        { value: 'consumer', text: "One consumer GPU (8–12 GB)." },
        { value: 'multi',    text: "Multiple GPUs or a high-VRAM workstation." },
        { value: 'server',   text: "Access to a server or shared infrastructure." }
      ]
    },
    {
      key: 'next',
      label: 'Question 3 of 3',
      prompt: "What's the next concrete thing you want?",
      options: [
        { value: 'service',    text: "A working local AI service I can use day-to-day." },
        { value: 'specialist', text: "A specialist model I trained or routed myself." },
        { value: 'measure',    text: "Measured results comparing approaches." },
        { value: 'teach',      text: "Teaching material or a project students can contribute to." },
        { value: 'map',        text: "An honest map of what's possible before I commit." }
      ]
    }
  ];

  const projectInfo = {
    puente:      { name: 'LocoPuente',                  url: 'https://locopuente.org',                    line: 'A full local AI service stack on hardware you own and control — frontier-equivalent UX, no metering.' },
    llm:         { name: 'LocoLLM',                     url: 'https://locollm.org',                       line: 'Adapter training, routing, and a specialist-model framework you can extend.' },
    bench:       { name: 'LocoBanco',                   url: 'https://locobanco.org',                     line: 'VRAM-tier benchmarking with real cards and honest baselines — what each tier can actually do.' },
    muse:        { name: 'LocoMusa',                    url: 'https://locomusa.org',                      line: 'Thinking-partner benchmark: which local model is best to ideate, reframe, and converse with — pairwise-judged against frontier anchors.' },
    convoy:      { name: 'LocoConvoy',                  url: 'https://lococonvoy.org',                    line: 'Multi-GPU parallelism experiments on consumer PCIe hardware.' },
    agente:      { name: 'LocoAgente',                  url: 'https://locoagente.org',                    line: 'Agentic scaffolding research: can small models do useful work in multi-turn loops?' },
    ensayo:      { name: 'LocoEnsayo',                  url: 'https://locoensayo.org',                    line: 'AI-populated rehearsal environments where students practise professional skills before facing the real thing.' },
    landscape:   { name: 'AI Landscape',                url: '/ai-landscape/',                       line: 'Honest comparison of local vs cloud options, including the cases where cloud is the right call.' },
    why:         { name: 'Why Local AI',                url: '/why-local-ai/',                       line: 'The structural argument: data sovereignty, compliance, and "private by architecture" rather than "private by policy".' },
    start:       { name: 'Getting Started',             url: '/getting-started/',                    line: 'Technical foundations — inference, VRAM, quantisation, and the rest of the stack.' },
    research:    { name: 'Research',                    url: '/research/',                           line: 'Active and planned studies across the lab, with status markers on every claim.' },
    inventory:   { name: 'GPU Inventory',               url: 'https://locobanco.org/gpu-inventory/', line: 'The actual secondhand fleet running these experiments — what was bought, what it cost, what it can do.' },
    econ:        { name: 'Economics of Local Training', url: '/economics-of-local-training/',        line: 'What local AI actually costs to build and run — capital, electricity, time.' },
    opportunity: { name: 'The Local AI Opportunity',    url: '/the-local-ai-opportunity/',           line: 'The strategic argument: who benefits from local AI, why now, and what building it for them actually looks like.' },
    findings:    { name: 'Findings',                    url: '/findings/',                           line: 'What is measured, what is claimed, and what would invalidate each — the lab\'s honest record.' }
  };

  const personas = {
    budget_rebel: {
      name: 'The Budget Rebel',
      emoji: '💰',
      description: "You refuse to pay per-token for something your own hardware can do. You'd rather spend a weekend on a local stack than sign up for another subscription you'll resent.",
      projects: ['puente', 'llm', 'landscape'],
      thesisHash: 'bridge-experience-locally',
      thesisLabel: 'Bridge experience, locally',
      q3Map: { service: 'puente', specialist: 'llm', measure: 'landscape', teach: 'llm', map: 'landscape' }
    },
    tinkerer: {
      name: 'The Tinkerer',
      emoji: '🤖',
      description: "You want to understand how LLMs work by cracking them open and rewiring the internals. Reading about fine-tuning is not enough — you want to train an adapter, measure whether it helped, and understand why.",
      projects: ['llm', 'bench', 'start'],
      thesisHash: 'specialize-and-harness',
      thesisLabel: 'Specialize and harness',
      q3Map: { service: 'llm', specialist: 'llm', measure: 'bench', teach: 'llm', map: 'start' }
    },
    researcher: {
      name: 'The Researcher',
      emoji: '🔬',
      description: "You need reproducible local inference for experiments. You want to test whether specialist routing actually beats a generalist on scoped tasks — and publish honest results either way.",
      projects: ['bench', 'muse', 'agente', 'convoy', 'research'],
      thesisHash: 'map-the-floor-honestly',
      thesisLabel: 'Map the floor honestly (methodology)',
      q3Map: { service: 'convoy', specialist: 'agente', measure: 'bench', teach: 'research', map: 'research' }
    },
    educator: {
      name: 'The Educator',
      emoji: '🏫',
      description: "You teach AI, computing, or a professional discipline and want a real project your students can contribute to. Not a toy demo — real infrastructure that grows with every cohort.",
      projects: ['ensayo', 'llm', 'why'],
      thesisHash: 'conversation-not-delegation',
      thesisLabel: 'Conversation, not delegation',
      q3Map: { service: 'ensayo', specialist: 'llm', measure: 'llm', teach: 'ensayo', map: 'why' }
    },
    vault: {
      name: 'The Vault',
      emoji: '🔐',
      description: "Your data does not leave your machine. Period. Local inference is not a convenience for you — it is the only acceptable path. You don't need convincing; you need the stack to work.",
      projects: ['puente', 'landscape', 'why'],
      thesisHash: 'bridge-experience-locally',
      thesisLabel: 'Bridge experience, locally',
      q3Map: { service: 'puente', specialist: 'puente', measure: 'landscape', teach: 'why', map: 'landscape' }
    },
    scrapper: {
      name: 'The Scrapper',
      emoji: '⚙',
      description: "You know the best gear does not make the best work. A $150 secondhand GPU and sharp training data might just surprise you. You're assembling capability from what is available.",
      projects: ['bench', 'inventory', 'econ'],
      thesisHash: 'engineer-before-hardware',
      thesisLabel: 'Engineer before hardware',
      q3Map: { service: 'inventory', specialist: 'bench', measure: 'bench', teach: 'econ', map: 'econ' }
    },
    operator: {
      name: 'The Operator',
      emoji: '🏢',
      description: "You run a small or medium organisation — a clinic, a firm, a consultancy, a school department. You need AI tools that work for your team without sending client data to someone else's machine, and without an enterprise licence that costs more than your hardware. Pragmatic, reliable, accountable.",
      projects: ['puente', 'opportunity', 'landscape'],
      thesisHash: 'bridge-experience-locally',
      thesisLabel: 'Bridge experience, locally',
      q3Map: { service: 'puente', specialist: 'puente', measure: 'landscape', teach: 'opportunity', map: 'opportunity' }
    },
    builder: {
      name: 'The Builder',
      emoji: '🛠️',
      description: "You ship products. Local AI is a backend in your own software — an app, a service, a tool you're putting into people's hands. You don't need to train models from scratch; you need a stable inference layer, adapters that fit your domain, and a harness that keeps working when you turn around.",
      projects: ['llm', 'agente', 'puente', 'landscape'],
      thesisHash: 'specialize-and-harness',
      thesisLabel: 'Specialize and harness',
      q3Map: { service: 'puente', specialist: 'llm', measure: 'agente', teach: 'llm', map: 'landscape' }
    },
    skeptic: {
      name: 'The Skeptic',
      emoji: '📋',
      description: "You haven't decided local AI is ready. You've heard the hype, you've heard the dismissals, and you want neither. You want stress-tested claims, honest negative results, and an evaluator-friendly path through what's measured versus what's still hoped for.",
      projects: ['findings', 'bench', 'landscape'],
      thesisHash: 'map-the-floor-honestly',
      thesisLabel: 'Map the floor honestly (methodology)',
      q3Map: { service: 'landscape', specialist: 'bench', measure: 'bench', teach: 'findings', map: 'landscape' }
    }
  };

  const hardwareNotes = {
    none:     "No hardware yet? Lead with the reading. Hardware decisions land easier once you know what you'd want it to do.",
    old:      "Older cards (4–6 GB) are LocoLabo's natural habitat — much of the floor work is built specifically for hardware in this range.",
    consumer: "An 8–12 GB consumer card runs Qwen3-4B comfortably and reaches most of the lab's work directly.",
    multi:    "Multi-GPU on consumer PCIe is exactly LocoConvoy's territory — worth a look even if it isn't your starting point.",
    server:   "Shared infrastructure changes the calculus. LocoPuente's deployment notes cover LAN-served setups specifically."
  };

  const state = { step: 0, answers: {} };

  function render() {
    if (state.step < questions.length) {
      renderQuestion(questions[state.step]);
    } else {
      renderResult();
    }
  }

  function renderQuestion(q) {
    const back = state.step > 0
      ? '<button type="button" data-action="back">← Back</button>'
      : '<span></span>';
    const reset = state.step > 0
      ? '<button type="button" data-action="reset">Start over</button>'
      : '<span></span>';

    root.innerHTML = `
      <div class="lw-card">
        <div class="lw-step">${q.label}</div>
        <h2 class="lw-question">${q.prompt}</h2>
        <div class="lw-options">
          ${q.options.map(o => `<button type="button" class="lw-option" data-value="${o.value}">${o.text}</button>`).join('')}
        </div>
        <div class="lw-controls">${back}${reset}</div>
      </div>
    `;

    root.querySelectorAll('.lw-option').forEach(btn => {
      btn.addEventListener('click', () => {
        state.answers[q.key] = btn.dataset.value;
        state.step += 1;
        render();
      });
    });
    const backBtn = root.querySelector('[data-action="back"]');
    if (backBtn) backBtn.addEventListener('click', () => { state.step -= 1; render(); });
    const resetBtn = root.querySelector('[data-action="reset"]');
    if (resetBtn) resetBtn.addEventListener('click', () => { state.step = 0; state.answers = {}; render(); });
  }

  function renderResult() {
    const persona = personas[state.answers.pull];
    if (!persona) { state.step = 0; render(); return; }

    const primaryId = persona.q3Map[state.answers.next] || persona.projects[0];
    const secondaryIds = persona.projects.filter(id => id !== primaryId).slice(0, 2);
    const primary = projectInfo[primaryId];
    const note = hardwareNotes[state.answers.hardware] || '';

    const secondaryHtml = secondaryIds.map(id => {
      const p = projectInfo[id];
      return `
        <div class="lw-secondary-card">
          <strong><a href="${p.url}">${p.name}</a></strong>
          <p>${p.line}</p>
        </div>`;
    }).join('');

    root.innerHTML = `
      <div class="lw-card">
        <div class="lw-result-header">
          <h2 class="lw-persona"><span class="lw-persona-emoji">${persona.emoji}</span>You're ${persona.name.toLowerCase()}</h2>
          <button type="button" class="lw-retake" data-action="reset">↻ Retake</button>
        </div>
        <p class="lw-persona-description">${persona.description}</p>

        ${note ? `<div class="lw-hardware-note">${note}</div>` : ''}

        <div class="lw-section-label">Start here</div>
        <div class="lw-primary-card">
          <h3><a href="${primary.url}">${primary.name}</a></h3>
          <p>${primary.line}</p>
        </div>

        <div class="lw-section-label">Also relevant</div>
        <div class="lw-secondary-grid">${secondaryHtml}</div>

        <div class="lw-read-first">
          <strong>Read first:</strong> <a href="/the-loco-thesis/#${persona.thesisHash}">${persona.thesisLabel}</a> — the principle most relevant to where you're starting.
        </div>
      </div>
    `;

    const resetBtn = root.querySelector('[data-action="reset"]');
    if (resetBtn) resetBtn.addEventListener('click', () => { state.step = 0; state.answers = {}; render(); });
  }

  render();
})();
</script>

---

## Skip the wizard?

If you'd rather browse directly:

- **[All nine personas in detail](/audience/)** — the full audience page this wizard draws from
- **[The thesis](/the-loco-thesis/)** — the five principles the projects sit on
- **[Findings](/findings/)** — what's measured, what's claimed, and what would invalidate each
- **[Research](/research/)** — active and planned studies across the lab
