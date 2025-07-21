from pydantic import BaseModel
from typing import Optional

class PredictionRequest(BaseModel):
    # Vital signs
    HR: float
    O2Sat: float
    Temp: float
    SBP: float
    MAP: float
    DBP: float
    Resp: float
    EtCO2: float

    # Lab results
    pH: float
    PaCO2: float
    AST: float
    BUN: float
    Alkalinephos: float
    Chloride: float
    Creatinine: float
    Lactate: float
    Magnesium: float
    Potassium: float
    Bilirubin_total: float
    PTT: float
    WBC: float
    Fibrinogen: float
    Platelets: float

    # Demographics
    Age: float
    ICULOS: float
    Gender: float

class PatientHourRequest(BaseModel):
    patient: str
    hour: str

class PredictionResponse(BaseModel):
    prediction: int
    patient: str