import React from 'react';
import { 
  Typography, 
  Box, 
  Accordion, 
  AccordionSummary, 
  AccordionDetails,
  CircularProgress
} from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import type { StepData } from './SSEHandler';
import BlastRadiusReport from './BlastRadiusReport';

interface StepItemProps {
  step: StepData;
  steps: StepData[];
  prNumber: number;
}

export const StepItem: React.FC<StepItemProps> = ({ step, steps, prNumber }) => {
  const { id, status, message, data, error } = step;

  const renderData = () => {
    if (!data) return null;

    if (id === 'ai_report' && typeof data === 'string') {
      const blastStep = steps?.find(s => s.id === 'blast_radius');
      const blastData = blastStep?.data;
      return (
        <BlastRadiusReport
          prNumber={prNumber}
          blastData={blastData || {
            changed_symbols: [],
            transitive: {},
            depths: {},
            risk_scores: {},
            overall_risk: 'LOW'
          }}
          reportText={data}
        />
      );
    }

    if (id === 'nodes' && Array.isArray(data)) {
      return (
        <Box sx={{ mt: 2, display: 'flex', flexDirection: 'column', gap: 1 }}>
          <Typography variant="subtitle2" color="text.secondary">Discovered Nodes:</Typography>
          <Box sx={{ p: 2, bgcolor: '#121212', borderRadius: 1, maxHeight: 200, overflow: 'auto' }}>
            {data.map((node, i) => {
              const parts = typeof node === 'string' ? node.split("::") : [JSON.stringify(node)];
              return (
                <Typography key={i} variant="body2" sx={{ fontFamily: 'monospace', color: 'primary.light' }}>
                  {parts.join(" → ")}
                </Typography>
              );
            })}
          </Box>
        </Box>
      );
    }

    return (
      <Accordion sx={{ mt: 2, bgcolor: 'background.paper', border: '1px solid', borderColor: 'divider' }} elevation={0}>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography variant="body2" color="text.secondary">JSON Data (for developers’ reference only)</Typography>
        </AccordionSummary>
        <AccordionDetails sx={{ bgcolor: '#0a0a0a', overflowX: 'auto', p: 2 }}>
          <Typography variant="body2" component="pre" sx={{ m: 0, fontFamily: 'monospace', fontSize: '0.75rem', color: '#e0e0e0' }}>
            {JSON.stringify(data, null, 2)}
          </Typography>
        </AccordionDetails>
      </Accordion>
    );
  };

  return (
    <Box sx={{ mt: 1, mb: 2 }}>
      {status === 'loading' && (
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, mb: 1 }}>
          <CircularProgress size={20} thickness={5} />
          <Typography variant="body2" color="text.secondary">{message || 'Processing...'}</Typography>
        </Box>
      )}
      
      {status === 'error' && (
        <Typography variant="body2" color="error" sx={{ fontWeight: 600 }}>
          {error}
        </Typography>
      )}

      {status === 'completed' && renderData()}
    </Box>
  );
};
