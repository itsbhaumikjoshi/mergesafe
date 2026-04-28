import React, { useMemo } from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

import { extractVerdicts, extractRecommendations, parseSymbol } from "../../helpers";
import {
  RISK_CONFIG,
  BANNER_MSG,
  reportWrapperSx,
  prBadgeSx,
  riskBannerSx,
  riskDotSx,
  metricsGridSx,
  metricCardSx,
  sectionTitleSx,
  symbolCardSx,
  chipSx,
  verdictSx,
  heatmapTableSx,
  tableHeadCellSx,
  tableBodyCellSx,
  depthBarTrackSx,
  recItemSx,
  recNumSx,
  layerBadgeSx,
  riskPillSx,
} from '../../styles/app';

export type RiskLevel = 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';

export interface BlastData {
  changed_symbols: string[];
  direct_callers?: Record<string, string[]>;
  transitive: Record<string, string[]>;
  depths: Record<string, number>;
  layers_crossed?: Record<string, string[]>;
  risk_scores: Record<string, RiskLevel>;
  overall_risk: RiskLevel;
}

export interface BlastRadiusReportProps {
  prNumber: number | string;
  blastData: BlastData;
  reportText: string;
}

const RiskPill: React.FC<{ risk: RiskLevel }> = ({ risk }) => (
  <Box component="span" sx={riskPillSx(risk)}>{risk}</Box>
);

const LayerBadge: React.FC<{ layer: string }> = ({ layer }) => (
  <Box component="span" sx={layerBadgeSx}>{layer}</Box>
);

const SectionTitle: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <Box sx={sectionTitleSx}>{children}</Box>
);

const MetricCard: React.FC<{ label: string; value: React.ReactNode }> = ({ label, value }) => (
  <Box sx={metricCardSx}>
    <Typography sx={{ fontSize: '0.7rem', color: 'text.secondary', mb: 0.5 }}>
      {label}
    </Typography>
    <Box sx={{ fontSize: '1.4rem', fontWeight: 500, color: 'text.primary' }}>
      {value}
    </Box>
  </Box>
);

const Chip: React.FC<{ label: string }> = ({ label }) => (
  <Box component="span" sx={chipSx}>{label}</Box>
);

const BlastRadiusReport: React.FC<BlastRadiusReportProps> = ({
  prNumber,
  blastData,
  reportText,
}) => {
  const {
    changed_symbols,
    transitive,
    depths,
    risk_scores,
    overall_risk,
    direct_callers = {},
  } = blastData;

  const risk = overall_risk;

  const totalAffected = useMemo(
    () => Object.values(transitive).reduce((acc, arr) => acc + arr.length, 0),
    [transitive]
  );

  const maxDepth = useMemo(
    () => Math.max(...Object.values(depths), 1),
    [depths]
  );

  const verdicts = useMemo(() => extractVerdicts(reportText), [reportText]);
  const recommendations = useMemo(() => extractRecommendations(reportText), [reportText]);

  const sortedSymbols = useMemo(
    () =>
      [...changed_symbols].sort(
        (a, b) => (transitive[b]?.length || 0) - (transitive[a]?.length || 0)
      ),
    [changed_symbols, transitive]
  );

  const affectedControllers = useMemo(() => {
    const all = Object.values(transitive).flat();
    return [...new Set(all)].filter((s) => parseSymbol(s).layer === 'controller');
  }, [transitive]);

  return (
    <Box sx={reportWrapperSx}>

      <Box sx={prBadgeSx}>PR #{prNumber}</Box>

      <Box sx={riskBannerSx(risk)}>
        <Box sx={riskDotSx(risk)} />
        <Typography sx={{ fontSize: '0.8rem', color: RISK_CONFIG[risk].bannerText, lineHeight: 1.5 }}>
          <Box component="strong">{risk} risk</Box> — {BANNER_MSG[risk]}
        </Typography>
      </Box>

      <Box sx={metricsGridSx}>
        <MetricCard label="Changed symbols" value={changed_symbols.length} />
        <MetricCard label="Transitively affected" value={totalAffected} />
        <MetricCard label="Max ripple depth" value={Math.max(...Object.values(depths), 0)} />
        <MetricCard
          label="Overall risk"
          value={<Box sx={{ mt: 0.5 }}><RiskPill risk={risk} /></Box>}
        />
      </Box>

      <Box sx={{ mb: 3 }}>
        <SectionTitle>Changed symbols</SectionTitle>

        {changed_symbols.map((sym) => {
          const { file, name, layer } = parseSymbol(sym);
          const r = risk_scores[sym] || 'LOW';
          const affected = transitive[sym] || [];
          const callers = direct_callers[sym] || [];
          const verdict = verdicts[sym] || '';

          return (
            <Box key={sym} sx={symbolCardSx}>

              <Box sx={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: 1, mb: 1.25 }}>
                <Box>
                  <Typography sx={{ fontFamily: 'monospace', fontSize: '0.72rem', lineHeight: 1.5, wordBreak: 'break-all', color: 'text.primary' }}>
                    {name}
                  </Typography>
                  <Typography sx={{ fontSize: '0.65rem', fontFamily: 'monospace', color: 'text.secondary', mt: 0.3 }}>
                    {file}
                  </Typography>
                </Box>
                <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: 0.75, flexShrink: 0 }}>
                  <RiskPill risk={r} />
                  <LayerBadge layer={layer} />
                </Box>
              </Box>

              {callers.length > 0 && (
                <Box sx={{ mb: 1 }}>
                  <Typography sx={{ fontSize: '0.65rem', color: 'text.secondary', mb: 0.5 }}>
                    Direct callers:
                  </Typography>
                  <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.75 }}>
                    {callers.map((c) => <Chip key={c} label={parseSymbol(c).name} />)}
                  </Box>
                </Box>
              )}

              {affected.length > 0 ? (
                <Box>
                  <Typography sx={{ fontSize: '0.65rem', color: 'text.secondary', mb: 0.5 }}>
                    Transitively affects {affected.length} symbol{affected.length !== 1 ? 's' : ''}:
                  </Typography>
                  <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.75 }}>
                    {affected.map((a) => <Chip key={a} label={parseSymbol(a).name} />)}
                  </Box>
                </Box>
              ) : (
                <Typography sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>
                  No transitive callers — isolated change
                </Typography>
              )}

              {verdict && <Box sx={verdictSx}>{verdict}</Box>}
            </Box>
          );
        })}
      </Box>

      <Box sx={{ mb: 3 }}>
        <SectionTitle>Blast radius heatmap</SectionTitle>
        <Box sx={{ overflowX: 'auto' }}>
          <Box component="table" sx={heatmapTableSx}>
            <Box component="thead">
              <Box component="tr">
                {['Symbol', 'Affected', 'Depth', 'Layer', 'Risk'].map((h) => (
                  <Box component="th" key={h} sx={tableHeadCellSx}>{h}</Box>
                ))}
              </Box>
            </Box>
            <Box component="tbody">
              {sortedSymbols.map((sym, i) => {
                const { name, layer } = parseSymbol(sym);
                const r = risk_scores[sym] || 'LOW';
                const affectedCount = (transitive[sym] || []).length;
                const depth = depths[sym] || 0;
                const pct = maxDepth > 0 ? (depth / maxDepth) * 100 : 0;
                const isLast = i === sortedSymbols.length - 1;
                const cellSx = tableBodyCellSx(isLast);

                return (
                  <Box component="tr" key={sym}>
                    <Box component="td" sx={{ ...cellSx, fontFamily: 'monospace', fontSize: '0.65rem', wordBreak: 'break-all' as const }}>
                      {name}
                    </Box>
                    <Box component="td" sx={{ ...cellSx, fontSize: '0.85rem', fontWeight: 500 }}>
                      {affectedCount}
                    </Box>
                    <Box component="td" sx={cellSx}>
                      <Typography sx={{ fontSize: '0.85rem', color: 'text.primary' }}>{depth}</Typography>
                      <Box sx={depthBarTrackSx}>
                        <Box sx={{ height: '100%', borderRadius: 2, width: `${Math.max(pct, 5)}%`, bgcolor: RISK_CONFIG[r].barColor }} />
                      </Box>
                    </Box>
                    <Box component="td" sx={cellSx}>
                      <LayerBadge layer={layer} />
                    </Box>
                    <Box component="td" sx={cellSx}>
                      <RiskPill risk={r} />
                    </Box>
                  </Box>
                );
              })}
            </Box>
          </Box>
        </Box>
      </Box>

      <Box sx={{ mb: 3 }}>
        <SectionTitle>User-facing impact</SectionTitle>
        {affectedControllers.length === 0 ? (
          <Typography sx={{ fontSize: '0.8rem', color: 'text.secondary', fontStyle: 'italic' }}>
            None identified — no controller-layer symbols in blast radius.
          </Typography>
        ) : (
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
            {affectedControllers.map((sym) => {
              const { name, file } = parseSymbol(sym);
              return (
                <Box key={sym} sx={{ bgcolor: 'rgba(245,158,11,0.08)', border: '1px solid rgba(245,158,11,0.25)', borderRadius: 2, p: '10px 14px' }}>
                  <Typography sx={{ fontFamily: 'monospace', fontSize: '0.72rem', color: '#fcd34d' }}>{name}</Typography>
                  <Typography sx={{ fontSize: '0.65rem', color: 'rgba(252,211,77,0.55)', mt: 0.3 }}>{file}</Typography>
                </Box>
              );
            })}
          </Box>
        )}
      </Box>

      <Box sx={{ mb: 3 }}>
        <SectionTitle>Merge recommendations</SectionTitle>
        {recommendations.length === 0 ? (
          <Typography sx={{ fontSize: '0.8rem', color: 'text.secondary', fontStyle: 'italic' }}>
            No recommendations generated.
          </Typography>
        ) : (
          <Box component="ol" sx={{ listStyle: 'none', p: 0, m: 0 }}>
            {recommendations.map((rec, i) => (
              <Box component="li" key={i} sx={recItemSx}>
                <Box sx={recNumSx}>{i + 1}</Box>
                <Box component="span">{rec}</Box>
              </Box>
            ))}
          </Box>
        )}
      </Box>

    </Box>
  );
};

export default BlastRadiusReport;
