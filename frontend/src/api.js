export async function scanTarget(target) {
  const response = await fetch('/scan', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ target })
  });

  if (!response.ok) {
    throw new Error('Scan request failed');
  }

  return response.json();
}
