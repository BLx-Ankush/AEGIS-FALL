export default function ResultsViewer({ result }) {
  if (!result) {
    return <p>No scan results yet.</p>;
  }

  return (
    <div>
      <h3>Results for {result.target}</h3>
      <ul>
        {result.findings.map((finding) => (
          <li key={finding}>{finding}</li>
        ))}
      </ul>
    </div>
  );
}
