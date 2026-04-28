export const formContainerStyles = {
  display: 'flex',
  flexDirection: 'column',
  gap: 2.5,
  width: '100%',
  mt: 2,
};

export const submitButtonStyles = {
  py: 1.5,
  fontSize: '1rem',
  fontWeight: 600,
  mt: 1,
};

export const googleButtonStyles = {
  py: 1.25,
  fontSize: '1rem',
  fontWeight: 500,
  backgroundColor: 'rgba(255, 255, 255, 0.05)',
  color: 'text.primary',
  border: '1px solid rgba(255, 255, 255, 0.12)',
  '&:hover': {
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
  },
};

export const dividerStyles = {
  my: 2,
  '&::before, &::after': {
    borderColor: 'divider',
  },
};
