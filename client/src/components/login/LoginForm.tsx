import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Box, TextField, Button, Typography, Divider, Alert, CircularProgress } from '@mui/material';
import GoogleIcon from '@mui/icons-material/Google';
import { formContainerStyles, submitButtonStyles, googleButtonStyles, dividerStyles } from '../../styles/login';
import { login, fetchUserData } from '../../adapters/backend';
import { useAuth } from '../../context/AuthContext';

interface LoginFormProps {
  onSwitchToRegister: () => void;
}

const LoginForm = ({ onSwitchToRegister }: LoginFormProps) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const { setUser } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);
    try {
      await login({ email, password });
      const user = await fetchUserData();
      setUser(user);
      navigate('/app');
    } catch (err: any) {
      setError(err.message || 'An error occurred during login');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={formContainerStyles}>
      {error && (
        <Alert severity="error" sx={{ mb: 2 }}>
          {error}
        </Alert>
      )}
      <TextField
        fullWidth
        label="Email"
        type="email"
        variant="outlined"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />
      <TextField
        fullWidth
        label="Password"
        type="password"
        variant="outlined"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      />
      
      <Button
        type="submit"
        variant="contained"
        color="primary"
        fullWidth
        sx={submitButtonStyles}
        disabled={isLoading}
      >
        {isLoading ? <CircularProgress size={24} color="inherit" /> : 'Login'}
      </Button>

      <Divider sx={dividerStyles}>OR</Divider>

      <Button
        variant="outlined"
        fullWidth
        startIcon={<GoogleIcon />}
        sx={googleButtonStyles}
      >
        Login with Google
      </Button>

      <Button
        variant="outlined"
        color="secondary"
        fullWidth
        sx={{ mt: 1, textTransform: 'none', fontWeight: 600 }}
        onClick={async () => {
          setEmail('dev@test.com');
          setPassword('password');
          setIsLoading(true);
          setError(null);
          try {
            await login({ email: 'dev@test.com', password: 'password' });
            const user = await fetchUserData();
            setUser(user);
            navigate('/app');
          } catch (err: any) {
            setError(err.message || 'An error occurred during login');
          } finally {
            setIsLoading(false);
          }
        }}
        disabled={isLoading}
      >
        Login with Dev Creds
      </Button>

      <Box sx={{ textAlign: 'center', mt: 2 }}>
        <Typography variant="body2" color="text.secondary">
          Don't have an account?{' '}
          <Button 
            variant="text" 
            color="primary" 
            onClick={onSwitchToRegister}
            sx={{ p: 0, minWidth: 'auto', textTransform: 'none', fontWeight: 600 }}
          >
            Register
          </Button>
        </Typography>
      </Box>
    </Box>
  );
};

export default LoginForm;
