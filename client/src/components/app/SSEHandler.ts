import { useState, useCallback } from 'react';

export interface StepData {
  id: string;
  label: string;
  status: 'pending' | 'loading' | 'completed' | 'error';
  message?: string;
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  data?: any;
  error?: string;
}

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export const PIPELINE_STEPS = [
  { id: 'nodes', loadingStatus: 'FETCHING_PR_NODES', successStatus: 'FOUND_PR_NODES', label: 'Fetch PR Nodes' },
  { id: 'repo', loadingStatus: 'CRAWLING_REPO', successStatus: 'CRAWLED_REPO', label: 'Crawl Repository' },
  { id: 'blast_radius', loadingStatus: 'COMPUTING_BLAST_RADIUS', successStatus: 'COMPUTED_BLAST_RADIUS', label: 'Compute Blast Radius' },
  { id: 'ai_report', loadingStatus: 'COMPUTING_GEN_AI_REPORT', successStatus: 'COMPUTED_GEN_AI_REPORT', label: 'Create LLM Report' }
];

export const useSSEPipeline = () => {
  const [steps, setSteps] = useState<StepData[]>([]);
  const [activeStep, setActiveStep] = useState(0);
  const [prNumber, setPrNumber] = useState(0);
  const [isProcessing, setIsProcessing] = useState(false);

  const startPipeline = useCallback((url: string) => {
    const urlParts = url.match(/github\.com\/([^/]+)\/([^/]+)\/pull\/(\d+)/);
    if (!urlParts) {
      alert("Invalid GitHub PR URL. Expected format: https://github.com/owner/repo/pull/123");
      return;
    }
    const [, owner, repo, pr_number] = urlParts;

    setIsProcessing(true);
    setActiveStep(0);
    setSteps([]);
    setPrNumber(Number(pr_number));

    const eventSource = new EventSource(`${API_BASE_URL}/get_blast_radius/${owner}/${repo}/${pr_number}`, {
      withCredentials: true
    });

    eventSource.onmessage = (event) => {
      try {
        const payload = JSON.parse(event.data);

        setSteps(currentSteps => {
          const newSteps = [...currentSteps];

          if (payload.error) {
            if (newSteps.length > 0) {
              const firstIdx = 0;
              newSteps[firstIdx].status = 'error';
              newSteps[firstIdx].error = payload.error;
              setActiveStep(firstIdx);
            } else {
              newSteps.unshift({
                id: 'error',
                label: 'Error',
                status: 'error',
                error: payload.error
              });
              setActiveStep(0);
            }
            setIsProcessing(false);
            eventSource.close();
            return newSteps;
          }

          const status = payload.status;
          
          if (payload.message) {
            const def = PIPELINE_STEPS.find(s => s.loadingStatus === status);
            if (def) {
              const existingIdx = newSteps.findIndex(s => s.id === def.id);
              if (existingIdx === -1) {
                newSteps.unshift({
                  id: def.id,
                  label: def.label,
                  status: 'loading',
                  message: payload.message
                });
                setActiveStep(0);
              } else {
                newSteps[existingIdx].status = 'loading';
                newSteps[existingIdx].message = payload.message;
                setActiveStep(existingIdx);
              }
            }
          } else {
            const def = PIPELINE_STEPS.find(s => s.successStatus === status);
            if (def) {
              const existingIdx = newSteps.findIndex(s => s.id === def.id);
              if (existingIdx !== -1) {
                newSteps[existingIdx].status = 'completed';
                if (status === 'FOUND_PR_NODES') {
                  newSteps[existingIdx].data = payload.nodes;
                } else if (status === 'CRAWLED_REPO') {
                  newSteps[existingIdx].data = payload.content;
                } else if (status === 'COMPUTED_BLAST_RADIUS') {
                  newSteps[existingIdx].data = payload.res;
                } else if (status === 'COMPUTED_GEN_AI_REPORT') {
                  newSteps[existingIdx].data = payload.gen_ai_report;
                  setIsProcessing(false);
                  eventSource.close();
                }
                setActiveStep(0);
              }
            }
          }

          return newSteps;
        });

      } catch (err) {
        console.error("Error parsing SSE data", err);
      }
    };

    eventSource.onerror = (err) => {
      console.error("SSE Error:", err);
      setSteps(currentSteps => {
        const newSteps = [...currentSteps];
        if (newSteps.length > 0) {
          const firstIndex = 0;
          if (newSteps[firstIndex].status === 'loading') {
            newSteps[firstIndex].status = 'error';
            newSteps[firstIndex].error = 'Connection lost. Please try again.';
            setActiveStep(firstIndex);
          }
        }
        return newSteps;
      });
      setIsProcessing(false);
      eventSource.close();
    };

  }, []);

  return { steps, prNumber, activeStep, isProcessing, startPipeline };
};
