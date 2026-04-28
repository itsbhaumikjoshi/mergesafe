import type { SxProps, Theme } from '@mui/material';
import type { RiskLevel } from '../../components/app/BlastRadiusReport';

export const RISK_CONFIG: Record<RiskLevel, {
  bannerBg: string;
  bannerBorder: string;
  bannerText: string;
  pillBg: string;
  pillText: string;
  dotColor: string;
  barColor: string;
}> = {
  CRITICAL: {
    bannerBg: 'rgba(239, 68, 68, 0.12)',
    bannerBorder: 'rgba(239, 68, 68, 0.35)',
    bannerText: '#fca5a5',
    pillBg: 'rgba(239, 68, 68, 0.18)',
    pillText: '#fca5a5',
    dotColor: '#ef4444',
    barColor: '#ef4444',
  },
  HIGH: {
    bannerBg: 'rgba(245, 158, 11, 0.12)',
    bannerBorder: 'rgba(245, 158, 11, 0.35)',
    bannerText: '#fcd34d',
    pillBg: 'rgba(245, 158, 11, 0.18)',
    pillText: '#fcd34d',
    dotColor: '#f59e0b',
    barColor: '#f59e0b',
  },
  MEDIUM: {
    bannerBg: 'rgba(59, 130, 246, 0.12)',
    bannerBorder: 'rgba(59, 130, 246, 0.35)',
    bannerText: '#93c5fd',
    pillBg: 'rgba(59, 130, 246, 0.18)',
    pillText: '#93c5fd',
    dotColor: '#3b82f6',
    barColor: '#3b82f6',
  },
  LOW: {
    bannerBg: 'rgba(16, 185, 129, 0.10)',
    bannerBorder: 'rgba(16, 185, 129, 0.30)',
    bannerText: '#6ee7b7',
    pillBg: 'rgba(16, 185, 129, 0.15)',
    pillText: '#6ee7b7',
    dotColor: '#10b981',
    barColor: '#10b981',
  },
};

export const BANNER_MSG: Record<RiskLevel, string> = {
  CRITICAL: 'Critical risk — multiple architectural layers affected. Do not merge without full test coverage.',
  HIGH: 'High risk — significant transitive impact detected across layers.',
  MEDIUM: 'Medium risk — some transitive impact. Review callers before merging.',
  LOW: 'Low risk — limited blast radius. Standard review process applies.',
};

export const reportWrapperSx: SxProps<Theme> = {
  py: 3,
  maxWidth: 800,
};

export const prBadgeSx: SxProps<Theme> = {
  fontSize: '0.7rem',
  fontFamily: 'monospace',
  color: 'text.secondary',
  mb: 1.5,
  letterSpacing: '0.04em',
};

export const riskBannerSx = (risk: RiskLevel): SxProps<Theme> => ({
  display: 'flex',
  alignItems: 'center',
  gap: 1.5,
  p: '14px 18px',
  borderRadius: 2,
  border: `1px solid ${RISK_CONFIG[risk].bannerBorder}`,
  bgcolor: RISK_CONFIG[risk].bannerBg,
  mb: 3,
});

export const riskDotSx = (risk: RiskLevel): SxProps<Theme> => ({
  width: 8,
  height: 8,
  borderRadius: '50%',
  bgcolor: RISK_CONFIG[risk].dotColor,
  flexShrink: 0,
});

export const metricsGridSx: SxProps<Theme> = {
  display: 'grid',
  gridTemplateColumns: 'repeat(auto-fit, minmax(120px, 1fr))',
  gap: 1.5,
  mb: 3,
};

export const metricCardSx: SxProps<Theme> = {
  bgcolor: 'background.paper',
  border: '1px solid rgba(255,255,255,0.05)',
  borderRadius: 2,
  p: '14px 16px',
};

export const sectionTitleSx: SxProps<Theme> = {
  fontSize: '0.7rem',
  fontWeight: 500,
  color: 'text.secondary',
  letterSpacing: '0.07em',
  textTransform: 'uppercase',
  mb: 1.5,
  pb: 0.75,
  borderBottom: '1px solid rgba(255,255,255,0.08)',
};

export const symbolCardSx: SxProps<Theme> = {
  bgcolor: 'background.paper',
  border: '1px solid rgba(255,255,255,0.07)',
  borderRadius: 2,
  p: '14px 16px',
  mb: 1.25,
};

export const chipSx: SxProps<Theme> = {
  fontFamily: 'monospace',
  fontSize: '0.65rem',
  px: 1,
  py: 0.4,
  borderRadius: 1,
  bgcolor: 'rgba(255,255,255,0.05)',
  color: 'text.secondary',
  border: '1px solid rgba(255,255,255,0.08)',
  wordBreak: 'break-all',
  display: 'inline-block',
};

export const verdictSx: SxProps<Theme> = {
  fontSize: '0.72rem',
  color: 'text.secondary',
  borderLeft: '2px solid rgba(255,255,255,0.12)',
  pl: 1.25,
  mt: 1.25,
  lineHeight: 1.6,
};

export const heatmapTableSx: SxProps<Theme> = {
  width: '100%',
  borderCollapse: 'collapse' as const,
};

export const tableHeadCellSx: SxProps<Theme> = {
  textAlign: 'left',
  p: '8px 10px',
  color: 'text.secondary',
  fontWeight: 500,
  fontSize: '0.72rem',
  borderBottom: '1px solid rgba(255,255,255,0.08)',
};

export const tableBodyCellSx = (isLast: boolean): SxProps<Theme> => ({
  p: '10px 10px',
  verticalAlign: 'top',
  borderBottom: isLast ? 'none' : '1px solid rgba(255,255,255,0.06)',
});

export const depthBarTrackSx: SxProps<Theme> = {
  height: 5,
  borderRadius: 2,
  bgcolor: 'rgba(255,255,255,0.06)',
  overflow: 'hidden',
  mt: 0.5,
  minWidth: 60,
};

export const recItemSx: SxProps<Theme> = {
  display: 'flex',
  gap: 1.25,
  p: '10px 14px',
  borderRadius: 2,
  bgcolor: 'rgba(255,255,255,0.04)',
  mb: 1,
  fontSize: '0.8rem',
  lineHeight: 1.6,
  color: 'text.primary',
  border: '1px solid rgba(255,255,255,0.05)',
};

export const recNumSx: SxProps<Theme> = {
  fontSize: '0.68rem',
  fontWeight: 600,
  color: 'text.secondary',
  minWidth: 20,
  mt: 0.2,
  flexShrink: 0,
};

export const layerBadgeSx: SxProps<Theme> = {
  fontSize: '0.6rem',
  px: 0.85,
  py: 0.3,
  borderRadius: 10,
  fontWeight: 500,
  bgcolor: 'rgba(255,255,255,0.06)',
  color: 'text.secondary',
  border: '1px solid rgba(255,255,255,0.09)',
  whiteSpace: 'nowrap',
  display: 'inline-block',
};

export const riskPillSx = (risk: RiskLevel): SxProps<Theme> => ({
  fontSize: '0.65rem',
  fontWeight: 600,
  px: 1.25,
  py: 0.35,
  borderRadius: 10,
  letterSpacing: '0.04em',
  bgcolor: RISK_CONFIG[risk].pillBg,
  color: RISK_CONFIG[risk].pillText,
  display: 'inline-block',
  lineHeight: 1.6,
});