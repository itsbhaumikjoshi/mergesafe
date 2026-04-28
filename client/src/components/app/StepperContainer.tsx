import React from 'react';
import { 
  Stepper, 
  Step, 
  StepLabel, 
  StepContent, 
  Paper, 
  Typography 
} from '@mui/material';
import type { StepData } from './SSEHandler';
import { StepItem } from './StepItem';

interface StepperContainerProps {
  steps: StepData[];
  activeStep: number;
  prNumber: number;
}

const StepperContainer: React.FC<StepperContainerProps> = ({ steps, activeStep, prNumber }) => {
  if (steps.every(s => s.status === 'pending') && activeStep === 0) {
    return null;
  }

  return (
    <Paper sx={{ p: 4, mt: 4, borderRadius: 2, bgcolor: 'background.paper', border: '1px solid', borderColor: 'divider' }} elevation={0}>
      <Typography variant="h6" gutterBottom sx={{ mb: 4, fontWeight: 600 }}>
        Analysis Progress
      </Typography>
      
      <Stepper activeStep={activeStep} orientation="vertical">
        {steps.map((step) => {
          const isError = step.status === 'error';
          
          return (
            <Step key={step.id} expanded={true}>
              <StepLabel 
                error={isError}
                optional={
                  isError ? (
                    <Typography variant="caption" color="error">Failed</Typography>
                  ) : step.status === 'completed' ? (
                    <Typography variant="caption" color="success.main">Completed</Typography>
                  ) : null
                }
              >
                <Typography variant="subtitle1" sx={{ fontWeight: step.status === 'loading' ? 600 : 400 }}>
                  {step.label}
                </Typography>
              </StepLabel>
              <StepContent>
                <StepItem step={step} steps={steps} prNumber={prNumber} />
              </StepContent>
            </Step>
          );
        })}
      </Stepper>
    </Paper>
  );
};

export default StepperContainer;
