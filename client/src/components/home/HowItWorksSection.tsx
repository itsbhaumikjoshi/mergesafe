import { Box, Typography, Container } from '@mui/material';
import { sectionContainerStyles, sectionTitleStyles, sectionSubtitleStyles, flowContainerStyles, stepStyles, stepNumberStyles, connectorStyles } from '../../styles/home';

const HowItWorksSection = () => {
  const steps = [
    { num: 1, title: 'Crawl Repository', desc: 'Traverse the repository (via GitHub API) and collect all Python files.' },
    { num: 2, title: 'Build Call Graph', desc: 'Parse each file using tree-sitter to extract function, class, and method.' },
    { num: 3, title: 'Parse PR Diffs', desc: 'Parse pull request diffs to identify modified functions, classes, or methods.' },
    { num: 4, title: 'Compute Impact', desc: 'Traverse the call graph to identify all direct and indirect dependents of modified symbols.' },
    { num: 5, title: 'Generate Report', desc: 'Deliver a clear, human-readable blast radius report directly to the PR.' },
  ];

  return (
    <Box sx={{ ...sectionContainerStyles, backgroundColor: 'rgba(0,0,0,0.2)' }} id="how-it-works">
      <Container maxWidth="lg">
        <Typography variant="h2" sx={sectionTitleStyles}>
          How It Works
        </Typography>
        <Typography variant="subtitle1" sx={sectionSubtitleStyles}>
          From static repository analysis to dynamic pull request evaluation.
        </Typography>

        <Box sx={flowContainerStyles}>
          <Box sx={connectorStyles} />
          {steps.map((step, index) => (
            <Box key={index} sx={stepStyles}>
              <Box sx={stepNumberStyles}>{step.num}</Box>
              <Typography component="h6" variant="h6" sx={{ fontWeight: 600, mb: 1 }}>
                {step.title}
              </Typography>
              <Typography variant="body2" color="text.secondary">
                {step.desc}
              </Typography>
            </Box>
          ))}
        </Box>
      </Container>
    </Box>
  );
};

export default HowItWorksSection;
