import { Box, Typography, Container, Grid, Card, CardContent } from '@mui/material';
import WarningAmberIcon from '@mui/icons-material/WarningAmber';
import DoneAllIcon from '@mui/icons-material/DoneAll';
import RuleIcon from '@mui/icons-material/Rule';
import AnalyticsIcon from '@mui/icons-material/Analytics';
import { sectionContainerStyles, cardStyles, iconContainerStyles } from '../../styles/home';

const ProblemSolutionSection = () => {
  return (
    <Box sx={sectionContainerStyles} id="solution">
      <Container maxWidth="lg">
        {/* <Typography variant="h2" sx={sectionTitleStyles}>
          Stop Guessing the Impact
        </Typography> */}

        <Grid container spacing={4}>
          <Grid size={{ xs: 12, md: 6 }}>
            <Card sx={cardStyles}>
              <CardContent>
                <Box
                  sx={{
                    ...iconContainerStyles,
                    color: 'secondary.main',
                    backgroundColor: 'rgba(245, 158, 11, 0.1)'
                  }}
                >
                  <WarningAmberIcon fontSize="large" />
                </Box>
                <Typography component="h4" variant="h4" sx={{ fontWeight: 600, mb: 2 }}>
                  The Problem
                </Typography>
                <Typography variant="body1" sx={{ color: 'text.secondary', mb: 2 }}>
                  Modern repositories have many interconnected functions and modules.
                  When a developer modifies a function, it is hard to identify:
                </Typography>
                <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1, mb: 2 }}>
                  <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 1.5 }}>
                    <Typography variant="body2" color="text.secondary">
                      1. Which functions depend on it?
                    </Typography>
                  </Box>
                  <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 1.5 }}>
                    <Typography variant="body2" color="text.secondary">
                      2. How far does the impact propagate?
                    </Typography>
                  </Box>
                </Box>
                <Typography variant="body1" sx={{ color: 'text.secondary' }}>
                  As a result, pull request reviews may miss indirect dependencies, causing regressions.
                </Typography>
              </CardContent>
            </Card>
          </Grid>

          <Grid size={{ xs: 12, md: 6 }}>
            <Card sx={cardStyles}>
              <CardContent>
                <Box
                  sx={{
                    ...iconContainerStyles,
                    color: 'primary.main',
                    backgroundColor: 'rgba(16, 185, 129, 0.1)'
                  }}
                >
                  <DoneAllIcon fontSize="large" />
                </Box>
                <Typography component="h4" variant="h4" sx={{ fontWeight: 600, mb: 2 }}>
                  The Solution
                </Typography>
                <Typography variant="body1" sx={{ color: 'text.secondary', mb: 2 }}>
                  The project builds a function-level dependency graph of the repository and uses it to analyze pull requests.
                </Typography>
                <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                  <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 1.5 }}>
                    <RuleIcon color="primary" />
                    <Typography variant="body2" color="text.secondary">
                      <strong>Static Phase:</strong> Scans the repository and identifies all functions, classes, and methods.
                    </Typography>
                  </Box>
                  <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 1.5 }}>
                    <AnalyticsIcon color="primary" />
                    <Typography variant="body2" color="text.secondary">
                      <strong>Dynamic Phase:</strong> Parses incoming PRs, traverses the call graph, and generates a human-readable blast radius report.
                    </Typography>
                  </Box>
                </Box>
              </CardContent>
            </Card>
          </Grid>
        </Grid>
      </Container>
    </Box>
  );
};

export default ProblemSolutionSection;
