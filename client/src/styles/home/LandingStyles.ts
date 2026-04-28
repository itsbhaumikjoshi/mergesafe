import type { SxProps, Theme } from '@mui/material';

export const containerStyles: SxProps<Theme> = {
  minHeight: '100vh',
  backgroundColor: 'background.default',
  color: 'text.primary',
  display: 'flex',
  flexDirection: 'column',
  overflowX: 'hidden',
};

export const heroSectionStyles: SxProps<Theme> = {
  pt: { xs: 12, md: 20 },
  pb: { xs: 8, md: 16 },
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  textAlign: 'center',
  position: 'relative',
  '&::before': {
    content: '""',
    position: 'absolute',
    top: 0,
    left: '50%',
    transform: 'translateX(-50%)',
    width: '100%',
    height: '100%',
    background: 'radial-gradient(circle at top center, rgba(16, 185, 129, 0.15) 0%, transparent 60%)',
    zIndex: 0,
    pointerEvents: 'none',
  },
};

export const heroTitleStyles: SxProps<Theme> = {
  fontWeight: 800,
  mb: 3,
  background: 'linear-gradient(135deg, #ffffff 0%, #a1a1aa 100%)',
  WebkitBackgroundClip: 'text',
  WebkitTextFillColor: 'transparent',
  zIndex: 1,
};

export const heroSubtitleStyles: SxProps<Theme> = {
  color: 'text.secondary',
  maxWidth: '800px',
  mb: 6,
  zIndex: 1,
};

export const sectionContainerStyles: SxProps<Theme> = {
  py: { xs: 10, md: 14 },
  position: 'relative',
};

export const sectionTitleStyles: SxProps<Theme> = {
  fontWeight: 700,
  mb: 0,
  textAlign: 'center',
};

export const sectionSubtitleStyles: SxProps<Theme> = {
  color: 'text.secondary',
  textAlign: 'center',
  maxWidth: '800px',
  mx: 'auto',
  mb: 8,
  mt: 10,
};

export const cardStyles: SxProps<Theme> = {
  height: '100%',
  display: 'flex',
  flexDirection: 'column',
  p: 4,
  transition: 'transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out',
  '&:hover': {
    boxShadow: '0 10px 30px -10px rgba(16, 185, 129, 0.15)',
    borderColor: 'primary.main',
  },
};

export const iconContainerStyles: SxProps<Theme> = {
  display: 'inline-flex',
  p: 1.5,
  borderRadius: 2,
  backgroundColor: 'rgba(16, 185, 129, 0.1)',
  color: 'primary.main',
  mb: 3,
};

export const flowContainerStyles: SxProps<Theme> = {
  display: 'flex',
  flexDirection: { xs: 'column', md: 'row' },
  justifyContent: 'space-between',
  alignItems: 'center',
  position: 'relative',
  mt: 8,
};

export const stepStyles: SxProps<Theme> = {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  textAlign: 'center',
  maxWidth: { xs: '100%', md: '200px' },
  mb: { xs: 6, md: 0 },
  position: 'relative',
  zIndex: 1,
};

export const stepNumberStyles: SxProps<Theme> = {
  width: 48,
  height: 48,
  borderRadius: '50%',
  backgroundColor: 'primary.main',
  color: 'primary.contrastText',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
  fontWeight: 'bold',
  fontSize: '1.25rem',
  mb: 2,
  boxShadow: '0 0 20px rgba(16, 185, 129, 0.4)',
};

export const connectorStyles: SxProps<Theme> = {
  display: { xs: 'none', md: 'block' },
  position: 'absolute',
  top: 24,
  left: 0,
  right: 0,
  height: 2,
  background: 'linear-gradient(90deg, rgba(16, 185, 129, 0) 0%, rgba(16, 185, 129, 0.5) 50%, rgba(16, 185, 129, 0) 100%)',
  zIndex: 0,
};

export const ctaSectionStyles: SxProps<Theme> = {
  py: { xs: 12, md: 16 },
  textAlign: 'center',
  background: 'linear-gradient(180deg, transparent 0%, rgba(16, 185, 129, 0.05) 100%)',
  borderTop: '1px solid rgba(255, 255, 255, 0.05)',
};
