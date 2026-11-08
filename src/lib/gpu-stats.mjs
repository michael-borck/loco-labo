// Reconciled GPU counts from the canonical registry, shared by the registry page
// and the homepage stats strip so the two can never disagree.
import data from '@locolabo/theme/gpus.json';

const has = (r, p) => r.projects.includes(p);
const total = (rows, f = (r) => r.count) => rows.reduce((n, r) => n + f(r), 0);

export const machinesOf = (r) => [...new Set([r.banco_machine, r.group].filter(Boolean))];

export function gpuStats(cards = data.cards) {
  const banco = cards.filter((r) => has(r, 'LocoBanco'));
  const fosil = cards.filter((r) => has(r, 'LocoFósil'));
  const shared = cards.filter((r) => has(r, 'LocoBanco') && has(r, 'LocoFósil'));

  const fleet = total(banco.filter((r) => r.status === 'installed'));
  const relicCards = total(fosil);
  const relicDevices = total(fosil, (r) => r.count * (r.device_count ?? 1));
  const sharedCount = total(shared);

  return {
    owned: fleet + relicCards - sharedCount,
    devices: fleet + relicDevices - sharedCount,
    fleet,
    unassigned: total(cards.filter((r) => machinesOf(r).includes('Unassigned'))),
    relicCards,
    relicDevices,
  };
}

export const cards = data.cards;
