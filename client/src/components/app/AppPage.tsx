import { useState } from 'react';
import { Box, Container, Typography, Button, Snackbar, Alert } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import { pageContainerStyles, headerStyles } from '../../styles/app';
import PRInput from './PRInput';
import { useSSEPipeline } from './SSEHandler';
import StepperContainer from './StepperContainer';
import { logout } from '../../adapters/backend';

const AppPage = () => {
  const { user, setUser } = useAuth();
  const { steps, prNumber, activeStep, isProcessing, startPipeline } = useSSEPipeline();
  const navigate = useNavigate();
  const [error, setError] = useState<string | null>(null);

  const handleAnalyzePR = (url: string) => {
    startPipeline(url);
  };

  const handleLogout = async () => {
    try {
      await logout();
      setUser(null);
      navigate('/');
    } catch (err: any) {
      setError(err.message || 'Failed to logout. Please try again.');
    }
  };

  const goHome = async () => {
    navigate('/');
  };

  const handleCloseError = () => {
    setError(null);
  };

  return (
    <Box sx={{ ...pageContainerStyles, position: 'relative' }}>
      <Container maxWidth="md">
        <Button 
          variant="text" 
          color="inherit" 
          onClick={goHome}
          sx={{ position: 'absolute', top: { xs: 15, md: 25 }, left: { xs: 15, md: 25 }, borderColor: 'rgba(255,255,255,0.2)' }}
        >
          Home
        </Button>
        <Button 
          variant="text" 
          color="inherit" 
          onClick={handleLogout}
          sx={{ position: 'absolute', top: { xs: 15, md: 25 }, right: { xs: 15, md: 25 }, borderColor: 'rgba(255,255,255,0.2)' }}
        >
          Logout
        </Button>
        <Box sx={headerStyles}>
          <Typography variant="h3" component="h1" gutterBottom sx={{ fontWeight: 700 }}>
            Welcome, {user?.firstName} {user?.lastName}
          </Typography>
          <Typography variant="subtitle1" color="text.secondary">
            Ready to analyze your pull requests?
          </Typography>
        </Box>

        <PRInput onSubmit={handleAnalyzePR} isLoading={isProcessing} user={user} />
        <StepperContainer prNumber={prNumber} steps={steps} activeStep={activeStep} />
      </Container>

      <Snackbar open={Boolean(error)} autoHideDuration={6000} onClose={handleCloseError}>
        <Alert onClose={handleCloseError} severity="error" sx={{ width: '100%' }}>
          {error}
        </Alert>
      </Snackbar>
    </Box>
  );
};

export default AppPage;


