import React, { useState, useEffect } from 'react';
import './App.css';

const API_BASE_URL = `http://${window.location.hostname}:8000`;

function App() {
  const [historicalData, setHistoricalData] = useState([]);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`${API_BASE_URL}/api/data`)
      .then(res => {
        if (!res.ok) throw new Error('La respuesta de la red no fue exitosa');
        return res.json();
      })
      .then(data => {
        setHistoricalData(data);
        setLoading(false);
      })
      .catch(error => {
        console.error("Error al cargar datos históricos:", error);
        setError("No se pudieron cargar los datos históricos. Verifique que el backend esté funcionando.");
        setLoading(false);
      });
  }, []);

  const handlePredict = () => {
    setPrediction(null);

    const requestBody = {
      model: "ARIMA",
      numCandidates: 3
    };

    fetch(`${API_BASE_URL}/api/predict`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(requestBody),
    })
      .then(res => res.json())
      .then(pred => setPrediction(pred))
      .catch(error => {
        console.error("Error al generar la predicción:", error);
        setError("No se pudo generar la predicción.");
      });
  };

  if (loading) return <div className="App"><h1>Cargando datos...</h1></div>;
  if (error) return <div className="App"><h1 style={{color: 'red'}}>Error</h1><p>{error}</p></div>;

  return (
    <div className="App">
      <header className="App-header">
        <h1>AI Prediction Dashboard</h1>
      </header>
      <main>
        <section className="prediction-section">
          <h2>Generar Nueva Predicción</h2>
          <button onClick={handlePredict}>Generar Predicción</button>
          {prediction && (
            <div className="prediction-result">
              <h3>Resultado de la Predicción:</h3>
              <p><strong>Modelo Utilizado:</strong> {prediction.modelUsed}</p>
              <p><strong>Candidatos Sugeridos:</strong> {prediction.candidates.join(', ')}</p>
              <p><strong>Puntuación de Confianza:</strong> {prediction.confidenceScore}</p>
            </div>
          )}
        </section>
        <section className="data-section">
          <h2>Datos Históricos</h2>
          <div className="table-container">
            <table>
              <thead>
                <tr>
                  <th>FECHA</th>
                  <th>MD</th>
                  <th>TD</th>
                  <th>NC</th>
                </tr>
              </thead>
              <tbody>
                {historicalData.map((row, index) => (
                  <tr key={index}>
                    <td>{row.FECHA}</td>
                    <td>{row.MD}</td>
                    <td>{row.TD}</td>
                    <td>{row.NC}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
