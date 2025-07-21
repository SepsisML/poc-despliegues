from fastapi import APIRouter, HTTPException, Query
from app.schemas.prediction_schemas import PredictionRequest, PatientHourRequest, PredictionResponse
from app.services.prediction_service import predict_from_input, predict_from_mongo
from app.models.model_loader import load_model
import os

router = APIRouter(prefix="/predict", tags=["Prediction"])

@router.post("", response_model= PredictionResponse, summary="Full Patient Prediction")
async def predict(input_data: PredictionRequest):
    return predict_from_input(input_data)

@router.post("/by-patient", response_model= PredictionResponse, summary="Prediction from database")
async def predict_by_patient(data: PatientHourRequest):
    return predict_from_mongo(data)

@router.post("/reload-model", summary="Reload model from path")
def reload_model_endpoint(path: str = Query(..., description="Path to model .pkl file")):
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Modelo no encontrado")
    load_model(path)
    return {"message": f"Modelo recargado desde {path}"}
