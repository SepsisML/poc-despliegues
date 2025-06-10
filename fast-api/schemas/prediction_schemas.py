from pydantic import BaseModel
from typing import Optional

class PredictionRequest(BaseModel):
    _id: Optional[str] = None
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
    BaseExcess: float
    HCO3: float
    FiO2: float
    pH: float
    PaCO2: float
    SaO2: float
    AST: float
    BUN: float
    Alkalinephos: float
    Calcium: float
    Chloride: float
    Creatinine: float
    Bilirubin_direct: float
    Glucose: float
    Lactate: float
    Magnesium: float
    Phosphate: float
    Potassium: float
    Bilirubin_total: float
    TroponinI: float
    Hct: float
    Hgb: float
    PTT: float
    WBC: float
    Fibrinogen: float
    Platelets: float

    # Demographics / Metadata
    Age: float
    Gender: float
    Unit1: float
    Unit2: float
    HospAdmTime: float
    ICULOS: float
    SepsisLabel: float
    Hora: float
    Paciente: str
    HospitalName: str
    Day: float

class PatientHourRequest(BaseModel):
    patient: str
    hour: str

class PredictionResponse(BaseModel):
    prediction: int
    patient: str