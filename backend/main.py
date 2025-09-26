from fastapi import FastAPI
from typing import List, Dict, Any
from pydantic import BaseModel, Field

app = FastAPI()

# --- BASE DE DATOS EN MEMORIA (Tus datos históricos reales) ---

historical_data = [
    {"FECHA": "2024-10-31", "MD": 97, "TD": 85, "NC": 47},
    {"FECHA": "2024-10-30", "MD": 59, "TD": 44, "NC": 74},
    {"FECHA": "2024-10-29", "MD": 31, "TD": 69, "NC": 34},
    {"FECHA": "2024-10-28", "MD": 26, "TD": 58, "NC": 15},
    {"FECHA": "2024-10-27", "MD": 9, "TD": 73, "NC": 83},
    {"FECHA": "2024-10-26", "MD": 60, "TD": 63, "NC": 7},
    {"FECHA": "2024-10-25", "MD": 75, "TD": 36, "NC": 63},
    {"FECHA": "2024-10-24", "MD": 32, "TD": 21, "NC": 79},
    {"FECHA": "2024-10-23", "MD": 27, "TD": 64, "NC": 48},
    {"FECHA": "2024-10-22", "MD": 41, "TD": 99, "NC": 82},
    {"FECHA": "2024-10-21", "MD": 37, "TD": 23, "NC": 2},
    {"FECHA": "2024-10-20", "MD": 87, "TD": 60, "NC": 70},
    {"FECHA": "2024-10-19", "MD": 36, "TD": 53, "NC": 77},
    {"FECHA": "2024-10-18", "MD": 95, "TD": 20, "NC": 73},
    {"FECHA": "2024-10-17", "MD": 78, "TD": 74, "NC": 76},
    {"FECHA": "2024-10-16", "MD": 60, "TD": 14, "NC": 48},
    {"FECHA": "2024-10-15", "MD": 56, "TD": 23, "NC": 65},
    {"FECHA": "2024-10-14", "MD": 85, "TD": 15, "NC": 37},
    {"FECHA": "2024-10-13", "MD": 88, "TD": 27, "NC": 58},
    {"FECHA": "2024-10-12", "MD": 13, "TD": 27, "NC": 39},
    {"FECHA": "2024-10-11", "MD": 41, "TD": 33, "NC": 48},
    {"FECHA": "2024-10-10", "MD": 62, "TD": 83, "NC": 50},
    {"FECHA": "2024-10-09", "MD": 65, "TD": 12, "NC": 7},
    {"FECHA": "2024-10-08", "MD": 32, "TD": 43, "NC": 74},
    {"FECHA": "2024-10-07", "MD": 43, "TD": 88, "NC": 2},
    {"FECHA": "2024-10-06", "MD": 11, "TD": 21, "NC": 0},
    {"FECHA": "2024-10-05", "MD": 14, "TD": 66, "NC": 94},
    {"FECHA": "2024-10-04", "MD": 93, "TD": 95, "NC": 80},
    {"FECHA": "2024-10-03", "MD": 57, "TD": 52, "NC": 72},
    {"FECHA": "2024-10-02", "MD": 97, "TD": 9, "NC": 32},
    {"FECHA": "2024-10-01", "MD": 54, "TD": 35, "NC": 26}
]


# --- MODELOS DE DATOS PARA LAS PETICIONES (INPUTS) ---

class PredictionRequest(BaseModel):
    model: str = Field(..., example="ARIMA")
    numCandidates: int = Field(..., ge=1, example=3)
    # Puedes añadir más campos como hyperparameters y dateRange aquí en el futuro


# --- ENDPOINTS DE LA API ---

@app.get("/")
def read_root():
    return {"message": "AI Prediction API está funcionando!"}

@app.get("/api/data", response_model=List[Dict[str, Any]])
def get_historical_data():
    """Devuelve todos los datos históricos disponibles."""
    return historical_data

@app.post("/api/predict", response_model=Dict[str, Any])
def generate_prediction(request: PredictionRequest):
    """
    Recibe una configuración y devuelve una predicción de ejemplo.
    Por ahora, siempre devuelve los mismos 3 candidatos.
    """
    print(f"Recibida petición para predecir con el modelo: {request.model}")
    print(f"Número de candidatos solicitados: {request.numCandidates}")

    # --- AQUÍ IRÁ LA LÓGICA DEL MODELO DE IA REAL ---
    # Por ahora, devolvemos una respuesta fija de ejemplo.
    
    prediction_result = {
        "modelUsed": request.model,
        "candidates": [42, 53, 98],
        "confidenceScore": 0.85,
        "message": f"Predicción de ejemplo generada para el modelo {request.model}."
    }
    
    return prediction_result