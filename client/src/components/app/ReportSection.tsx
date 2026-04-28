import React from 'react';
import { Box, Typography, Card, CircularProgress, Stack } from '@mui/material';
import AssignmentIcon from '@mui/icons-material/Assignment';
import CheckCircleOutlinedIcon from '@mui/icons-material/CheckCircleOutlined';
import { cardStyles, reportSectionContainerStyles, reportContentStyles } from '../../styles/app';

interface ReportSectionProps {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  reportData: any | null;
  isLoading?: boolean;
  loadingMessage?: string;
}

const ReportSection: React.FC<ReportSectionProps> = ({ reportData, isLoading, loadingMessage }) => {
  if (isLoading) {
    return (
      <Box sx={reportSectionContainerStyles}>
        <CircularProgress size={40} color="primary" sx={{ mb: 2 }} />
        <Typography variant="body1" color="text.secondary">
          {loadingMessage || 'Analyzing pull request...'}
        </Typography>
      </Box>
    );
  }

  if (!reportData) {
    return (
      <Box sx={reportSectionContainerStyles}>
        <AssignmentIcon sx={{ fontSize: 48, color: 'text.secondary', mb: 2, opacity: 0.5 }} />
        <Typography variant="body1" color="text.secondary">
          Submit a Pull Request URL to view the analysis report.
        </Typography>
      </Box>
    );
  }

  return (
    <Card sx={cardStyles} elevation={0}>
      <Stack sx={{ alignItems: "center", spacing: "1.5", mb: 1, direction: "row" }}>
        <CheckCircleOutlinedIcon color="primary" />
        <Typography variant="h6" sx={{ fontWeight: 600 }}>
          Analysis Complete
        </Typography>
      </Stack>
      <Typography variant="body2" color="text.secondary" gutterBottom>
        Structural impact report generated successfully.
      </Typography>
      
      <Box sx={reportContentStyles}>
        <Typography variant="body2" component="pre" sx={{ m: 0, fontFamily: 'monospace', fontSize: '0.85rem' }}>
          {JSON.stringify(reportData, null, 2)}
        </Typography>
      </Box>
    </Card>
  );
};

export default ReportSection;
