import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState([]);
  const [prediction, setPrediction] = useState(null);

  useEffect(() => {
    // Cargar datos históricos desde el backend
    fetch('/api/data')
      .then((res) => res.json())
      .then((data) => setData(data.series));
  }, []);

  const handlePredict = () => {
    // Llamar al endpoint de predicción
    fetch('/api/predict')
      .then((res) => res.json())
      .then((pred) => setPrediction(pred.prediction));
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>AI Prediction Dashboard</h1>
        <button onClick={handlePredict}>Generate Prediction</button>
        {prediction !== null && <h2>Predicted Value: {prediction}</h2>}
        <h2>Historical Data</h2>
        <ul>
          {data.map((point, index) => (
            <li key={index}>Period {point.x}: {point.y}</li>
          ))}
        </ul>
      </header>
    </div>
  );
}

export default App;
