import { useState } from 'react';

import { scanTarget } from './api';
import Dashboard from './components/Dashboard';
import ResultsViewer from './components/ResultsViewer';
import TargetForm from './components/TargetForm';

export default function App() {
  const [status, setStatus] = useState('Ready');
  const [result, setResult] = useState(null);

  const handleSubmit = async (target) => {
    setStatus('Running scan...');
    try {
      const response = await scanTarget(target);
      setResult(response);
      setStatus('Scan complete');
    } catch {
      setStatus('Scan failed');
    }
  };

  return (
    <main>
      <h1>AEGIS-FALL</h1>
      <Dashboard status={status} />
      <TargetForm onSubmit={handleSubmit} />
      <ResultsViewer result={result} />
    </main>
  );
}
