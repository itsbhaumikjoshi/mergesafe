import type { SxProps, Theme } from '@mui/material';

export const pageContainerStyles: SxProps<Theme> = {
  minHeight: '100vh',
  backgroundColor: 'background.default',
  pt: { xs: 6, md: 10 },
  pb: { xs: 6, md: 10 },
};

export const headerStyles: SxProps<Theme> = {
  mb: 6,
  mt: 4,
  textAlign: 'left',
};

export const cardStyles: SxProps<Theme> = {
  p: { xs: 3, md: 4 },
  mb: 4,
  backgroundColor: 'background.paper',
  borderRadius: 2,
  border: '1px solid',
  borderColor: 'divider',
  boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
};

export const prInputContainerStyles: SxProps<Theme> = {
  display: 'flex',
  flexDirection: { xs: 'column', md: 'row' },
  alignItems: 'flex-start',
  gap: 2,
};

export const reportSectionContainerStyles: SxProps<Theme> = {
  p: { xs: 4, md: 6 },
  minHeight: 250,
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  justifyContent: 'center',
  border: '1px dashed',
  borderColor: 'divider',
  borderRadius: 2,
  backgroundColor: 'rgba(255, 255, 255, 0.02)',
  textAlign: 'center',
};

export const reportContentStyles: SxProps<Theme> = {
  mt: 3,
  p: 3,
  bgcolor: '#0a0a0a',
  borderRadius: 2,
  border: '1px solid',
  borderColor: 'divider',
  overflowX: 'auto',
};
