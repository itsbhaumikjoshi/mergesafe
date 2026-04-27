import { useState } from 'react';
import { ThemeProvider, CssBaseline, Box } from '@mui/material';
import { theme, containerStyles } from '../../styles/home';
import HeroSection from './HeroSection';
import ProblemSolutionSection from './ProblemSolutionSection';
import HowItWorksSection from './HowItWorksSection';
import TechnicalEdgeSection from './TechnicalEdgeSection';
import AuthModal from './AuthModal';

const LandingPage = () => {
  const [isAuthModalOpen, setIsAuthModalOpen] = useState(false);
  
  const handleOpenAuthModal = () => {
    setIsAuthModalOpen(true);
  };

  const handleCloseAuthModal = () => {
    setIsAuthModalOpen(false);
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
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
    </ThemeProvider>
  );
};

export default LandingPage;
