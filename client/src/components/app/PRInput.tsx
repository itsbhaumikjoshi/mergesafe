import React, { useEffect, useState } from 'react';
import { Box, TextField, Button, CircularProgress, Typography, Card, Alert } from '@mui/material';
import AnalyticsIcon from '@mui/icons-material/Analytics';
import { prInputContainerStyles, cardStyles } from '../../styles/app';
import type { User } from '../../adapters/types';

interface PRInputProps {
  onSubmit: (url: string) => void;
  user: User | null;
  isLoading: boolean;
}

const PRInput: React.FC<PRInputProps> = ({ onSubmit, user, isLoading }) => {
  const [url, setUrl] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (url.trim()) {
      onSubmit(url.trim());
    }
  };

  useEffect(() => {
    if(user?.email === import.meta.env.VITE_TEST_EMAIL) {
      setUrl("https://github.com/mock/test/pull/123");
    }
  }, [user]);

  return (
    <Card sx={cardStyles} elevation={0}>
      <Box sx={{ mb: 4 }}>
        <Typography variant="h5" component="h2" gutterBottom sx={{ fontWeight: 600, display: 'flex', alignItems: 'center', gap: 1.5 }}>
          <AnalyticsIcon color="primary" />
          Analyze Pull Request
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Enter the URL of a GitHub Pull Request to generate a comprehensive structural impact report.
        </Typography>
        {user?.email === import.meta.env.VITE_TEST_EMAIL && (
          <Alert severity="info" sx={{ mt: 2, mb: 1, borderRadius: 2 }}>
            You are logged in with dev credentials. Only dummy responses will be shown.
          </Alert>
        )}
      </Box>

      <Box component="form" onSubmit={handleSubmit} sx={prInputContainerStyles}>
        <TextField
          fullWidth
          label="GitHub Pull Request URL"
          variant="outlined"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="https://github.com/owner/repo/pull/123"
          disabled={isLoading}
          slotProps={{
            input: {
              sx: { bgcolor: 'background.default' }
            }
          }}
        />
        <Button
          type="submit"
          variant="contained"
          color="primary"
          size="large"
          disabled={!url.trim() || isLoading}
          sx={{ minWidth: 160, height: 56 }}
        >
          {isLoading ? <CircularProgress size={24} color="inherit" /> : 'Run Analysis'}
        </Button>
      </Box>
    </Card>
  );
};

export default PRInput;
