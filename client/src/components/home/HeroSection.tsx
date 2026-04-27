import { Box, Typography, Button, Container, Stack } from '@mui/material';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import ShieldIcon from '@mui/icons-material/Shield';
import { heroSectionStyles, heroTitleStyles, heroSubtitleStyles, sectionSubtitleStyles } from '../../styles/home';

interface HeroSectionProps {
  onOpenAuth: () => void;
}

const HeroSection = ({ onOpenAuth }: HeroSectionProps) => {
  return (
    <Box sx={heroSectionStyles}>
      <Container maxWidth="lg">
        <Box sx={{ display: "flex", justifyContent: "center", mb: 4 }}>
          <Box
            sx={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: 1,
              px: 2,
              py: 0.75,
              borderRadius: 8,
              border: '1px solid rgba(16, 185, 129, 0.3)',
              backgroundColor: 'rgba(16, 185, 129, 0.05)',
              color: 'primary.main',
              fontWeight: 600,
              fontSize: '0.875rem',
            }}
          >
            <ShieldIcon fontSize="small" />
            <span>Pre-Merge Impact Analysis</span>
          </Box>
        </Box>
        <Typography variant="h1" sx={heroTitleStyles}>
          Merge Pull Requests Safely
        </Typography>
        <Box sx={{ display: 'flex', justifyContent: 'center' }}>
          <Typography variant="subtitle1" sx={heroSubtitleStyles}>
            This project analyzes code changes in a repository to determine which parts of the system may be affected before merging a pull request.
          </Typography>
        </Box>
        <Stack
          direction={{ xs: 'column', sm: 'row' }}
          spacing={2}
          sx={{
            justifyContent: 'center',
            zIndex: 1,
            position: 'relative'
          }}
        >
          <Button
            variant="contained"
            color="primary"
            size="large"
            onClick={onOpenAuth}
            endIcon={<ArrowForwardIcon />}
            sx={{ px: 4, py: 1.5, fontSize: '1.125rem' }}
          >
            Get Started
          </Button>
        </Stack>
        <Typography variant="subtitle1" sx={sectionSubtitleStyles}>
          Manual PR reviews miss transitive dependencies. This project aims to make impact analysis explicit and reliable.
        </Typography>
      </Container>
    </Box>
  );
};

export default HeroSection;
