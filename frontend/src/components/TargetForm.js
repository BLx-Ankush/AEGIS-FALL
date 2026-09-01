import { useState } from 'react';

export default function TargetForm({ onSubmit }) {
  const [target, setTarget] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (!target.trim()) {
      return;
    }
    onSubmit(target.trim());
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={target}
        onChange={(event) => setTarget(event.target.value)}
        placeholder="example.com"
      />
      <button type="submit">Scan</button>
    </form>
  );
}
