import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://locolabo.org',
  base: '/docs',
  integrations: [
    starlight({
      title: 'LocoLab',
      description: 'Frontier AI on a Budget. Crazy, Right?',
      favicon: '/favicon.svg',
      logo: {
        alt: 'LocoLab',
        src: './src/assets/lab.svg',
        replacesTitle: false,
      },
      social: [
        { icon: 'external', label: 'Home', href: 'https://locolabo.org' },
        { icon: 'github', label: 'GitHub', href: 'https://github.com/michael-borck/loco-lab' },
      ],
      customCss: ['./src/styles/custom.css'],
      sidebar: [
        {
          label: 'Lab Overview',
          items: [
            { label: 'Meet the Lab', slug: 'meet-the-lab' },
            { label: 'Are You Loco Enough?', slug: 'audience' },
            { label: 'Meet the Team', slug: 'meet-the-team' },
            { label: 'Machine Setup', slug: 'machine-setup' },
            { label: 'FAQ', slug: 'faq' },
          ],
        },
        {
          label: 'Research',
          items: [
            { label: 'Papers & Projects', slug: 'research' },
          ],
        },
        {
          label: 'Projects',
          items: [
            { label: 'LocoLLM', link: 'https://locollm.org' },
            { label: 'LocoBench', link: 'https://locobench.org' },
            { label: 'LocoConvoy', link: 'https://lococonvoy.org' },
            { label: 'LocoEnsayo', link: 'https://locoensayo.org' },
            { label: 'LocoAgente', link: 'https://locoagente.org' },
            { label: 'LocoPuente', link: 'https://locopuente.org' },
          ],
        },
        {
          label: 'Local AI Foundations',
          items: [
            { label: 'Why Local AI', slug: 'why-local-ai' },
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
    }),
  ],
});
