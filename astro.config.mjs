import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { loco, relatedItems } from '@locolabo/theme';

export default defineConfig({
  site: 'https://locolabo.org',
  integrations: [
    starlight(
      loco({
        project: 'loco-labo',
        title: 'LocoLabo',
        description: 'A self-funded lab mapping what AI can do on hardware people already own.',
        home: 'https://locolabo.org',
        github: 'loco-labo',
        labo: false,
        related: false,
        accent: { low: '#0a1628', main: '#3b82f6', high: '#bfdbfe' },
        customCss: ['./src/styles/hub.css'],
        logo: {
          alt: 'LocoLabo',
          src: './src/assets/art/icon.png',
          replacesTitle: false,
        },
        sidebar: [
          {
            label: 'Lab Overview',
            items: [
              { label: 'Quests', slug: 'quests' },
              { label: 'Meet the Lab', slug: 'meet-the-lab' },
              { label: 'Origin Story', slug: 'origin-story' },
              { label: 'The Loco Thesis', slug: 'the-loco-thesis' },
              { label: 'Are You Loco Enough?', slug: 'audience' },
              { label: 'Find Your Starting Point', slug: 'find-your-starting-point' },
              { label: 'Meet the Team', slug: 'meet-the-team' },
              { label: 'Machine Setup', slug: 'machine-setup' },
              { label: 'GPU Registry', slug: 'gpu-registry' },
              { label: 'FAQ', slug: 'faq' },
            ],
          },
          {
            label: 'Research',
            items: [
              { label: 'Papers & Projects', slug: 'research' },
              { label: 'Findings', slug: 'findings' },
              { label: 'LocoNotas', link: 'https://loconotas.org' },
              { label: 'Research (borck.dev)', link: 'https://research.borck.dev' },
            ],
          },
          {
            label: 'Projects',
            items: relatedItems('loco-labo'),
          },
          {
            label: 'Local AI Foundations',
            items: [
              { label: 'Why Local AI', slug: 'why-local-ai' },
              { label: 'The Local AI Opportunity', slug: 'the-local-ai-opportunity' },
              { label: 'Getting Started', slug: 'getting-started' },
            ],
          },
          {
            label: 'General Reference',
            items: [
              { label: 'Economics of Local Training', slug: 'economics-of-local-training' },
              { label: 'AI Landscape', slug: 'ai-landscape' },
              { label: 'Nvidia GPU Reference', slug: 'nvidia-gpu-reference' },
              { label: 'Ollama Model Guide', slug: 'ollama-model-guide' },
              { label: 'Local LLM Tools', slug: 'local-llm-tools' },
              { label: 'Learning How LLMs Work', slug: 'learning-how-llms-work' },
            ],
          },
        ],
      })
    ),
  ],
});
