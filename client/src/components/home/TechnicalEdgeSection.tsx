import { Box, Typography, Container, Grid, Card, CardContent } from '@mui/material';
import MemoryIcon from '@mui/icons-material/Memory';
import AccountTreeIcon from '@mui/icons-material/AccountTree';
import TerminalIcon from '@mui/icons-material/Terminal';
import { sectionContainerStyles, sectionTitleStyles, sectionSubtitleStyles, cardStyles, iconContainerStyles } from '../../styles/home';

const TechnicalEdgeSection = () => {
  return (
    <Box sx={sectionContainerStyles} id="features">
      <Container maxWidth="lg">
        <Typography variant="h2" sx={sectionTitleStyles}>
          The Technical Edge
        </Typography>
        <Typography variant="subtitle1" sx={sectionSubtitleStyles}>
          Built for modern, dynamic languages. MergeSafe solves the hardest problems in static analysis.
        </Typography>

        <Grid container spacing={4}>
          <Grid size={{ xs: 12, md: 4 }}>
            <Card sx={cardStyles}>
              <CardContent>
                <Box sx={iconContainerStyles}>
                  <MemoryIcon fontSize="large" />
                </Box>
                <Typography component="h5" variant="h5" sx={{ fontWeight: 600, mb: 2 }}>
                  Symbol Resolution
                </Typography>
                <Typography variant="body2" color="text.secondary" component="div">
                  Function calls are resolved using:
                  <Box component="ul" sx={{ my: 1, pl: 2.5 }}>
                    <li>import statements</li>
                    <li>file-local definitions</li>
                    <li>global symbol indexing</li>
                  </Box>
                  Ambiguous matches are ignored to avoid incorrect results.
                </Typography>
              </CardContent>
            </Card>
          </Grid>

          <Grid size={{ xs: 12, md: 4 }}>
            <Card sx={cardStyles}>
              <CardContent>
                <Box sx={iconContainerStyles}>
                  <AccountTreeIcon fontSize="large" />
                </Box>
                <Typography component="h5" variant="h5" sx={{ fontWeight: 600, mb: 2 }}>
                  Call Graph Representation
                </Typography>
                <Typography variant="body2" color="text.secondary" component="div">
                  The system builds a deterministic call graph:
                  <Box sx={{ my: 1.5, p: 1, bgcolor: 'action.hover', borderRadius: 1, fontFamily: 'monospace', fontSize: '0.8125rem' }}>
                    callee → list of callers
                  </Box>
                  Each node is uniquely identified as:
                  <Box sx={{ mt: 1.5, p: 1, bgcolor: 'action.hover', borderRadius: 1, fontFamily: 'monospace', fontSize: '0.8125rem' }}>
                    file_path::function<br />
                    file_path::class::method
                  </Box>
                </Typography>
              </CardContent>
            </Card>
          </Grid>

          <Grid size={{ xs: 12, md: 4 }}>
            <Card sx={cardStyles}>
              <CardContent>
                <Box sx={iconContainerStyles}>
                  <TerminalIcon fontSize="large" />
                </Box>
                <Typography component="h5" variant="h5" sx={{ fontWeight: 600, mb: 2 }}>
                  Handling Real-World Code
                </Typography>
                <Typography variant="body2" color="text.secondary" component="div">
                  <Box component="ul" sx={{ m: 0, pl: 2.5 }}>
                    <li>Works with partially qualified function calls.</li>
                    <li>Handles imports and aliases.</li>
                    <li>Skips unresolved or external dependencies.</li>
                    <li>Avoids incorrect edges in ambiguous cases.</li>
                  </Box>
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        </Grid>
      </Container>
    </Box>
  );
};

export default TechnicalEdgeSection;
