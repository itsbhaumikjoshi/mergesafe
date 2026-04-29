export const parseSymbol = (full: string): { file: string; name: string; layer: string } => {
  const parts = full.split('::');
  const file = parts[0];
  const name = parts.slice(1).join('::') || file.split('/').pop() || full;
  const layer = file.includes('services')
    ? 'service'
    : file.includes('controllers')
    ? 'controller'
    : file.includes('repositories')
    ? 'repository'
    : file.includes('adapters')
    ? 'adapter'
    : file.includes('helpers')
    ? 'helper'
    : file.includes('parsers')
    ? 'parser'
    : file.includes('constants')
    ? 'constant'
    : 'other';
  return { file, name, layer };
}

export const extractVerdicts = (raw: string):Record<string, string> => {
  const verdicts: Record<string, string> = {};
  const blocks = raw.split(/###\s+\d+\.\s+/);
  blocks.slice(1).forEach((block) => {
    const firstLine = block.split('\n')[0].trim();
    const match = block.match(/\*\*Verdict\*\*:?\s*(.+)/);
    if (firstLine && match) verdicts[firstLine] = match[1].trim();
  });
  return verdicts;
}

export const extractRecommendations = (raw: string):string[] => {
  const match = raw.match(/### Merge Recommendations\n([\s\S]*?)(?=###|$)/);
  if (!match) return [];
  return match[1]
    .trim()
    .split('\n')
    .filter((l) => /^\d+\./.test(l.trim()))
    .map((l) => l.replace(/^\d+\.\s*/, '').trim());
}

export const stripMarkdown = (text: string): string => {
  return text.replace(/\*\*(.+?)\*\*/g, '$1');
}
