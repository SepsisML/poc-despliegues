from fastapi import FastAPI
from app.api.v1 import prediction
from app.models.loader import load_model

app = FastAPI(title="Medical Prediction API")

# Cargar modelo al iniciar
load_model("models/gbdt_model.pkl")

# Incluir rutas
app.include_router(prediction.router)
