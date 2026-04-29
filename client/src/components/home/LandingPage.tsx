import { useState, useEffect } from 'react';
import { Box, Snackbar, Alert } from '@mui/material';
import { useSearchParams } from 'react-router-dom';
import { containerStyles } from '../../styles/home';
import HeroSection from './HeroSection';
import ProblemSolutionSection from './ProblemSolutionSection';
import HowItWorksSection from './HowItWorksSection';
import TechnicalEdgeSection from './TechnicalEdgeSection';
import AuthModal from './AuthModal';

const LandingPage = () => {
  const [isAuthModalOpen, setIsAuthModalOpen] = useState(false);
  const [searchParams, setSearchParams] = useSearchParams();
  const [errorMsg, setErrorMsg] = useState<string | null>(null);
  const [showError, setShowError] = useState(false);

  useEffect(() => {
    const error = searchParams.get('error');
    if (error) {
      setErrorMsg(error);
      setShowError(true);
      
      // Clean up the URL param
      const newParams = new URLSearchParams(searchParams);
      newParams.delete('error');
      setSearchParams(newParams, { replace: true });
    }
  }, [searchParams, setSearchParams]);
  
  const handleOpenAuthModal = () => {
    setIsAuthModalOpen(true);
  };

  const handleCloseAuthModal = () => {
    setIsAuthModalOpen(false);
  };

  const handleCloseError = () => {
    setShowError(false);
  };

  return (
    <>
      <Box sx={containerStyles}>
        <HeroSection onOpenAuth={handleOpenAuthModal} />
        <ProblemSolutionSection />
        <HowItWorksSection />
        <TechnicalEdgeSection />
      </Box>
      <AuthModal 
        open={isAuthModalOpen} 
        onClose={handleCloseAuthModal} 
        defaultMode="login" 
      />
      <Snackbar 
        open={showError} 
        autoHideDuration={10000} 
        onClose={handleCloseError}
        anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
      >
        <Alert onClose={handleCloseError} severity="error" variant="filled" sx={{ width: '100%' }}>
          {errorMsg}
        </Alert>
      </Snackbar>
    </>
  );
};

export default LandingPage;
