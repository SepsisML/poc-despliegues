import numpy as np
from pymongo import MongoClient
from fastapi import HTTPException
from app.models.model_loader import get_model
from app.database.mongo import MONGO_URI, get_db
from app.api.v1.constants import EXPECTED_KEYS
def predict_from_input(input_data):
    try:
        features = [getattr(input_data, key) for key in EXPECTED_KEYS]
        if len(features) < len(EXPECTED_KEYS):
            raise HTTPException(status_code=400, detail="Faltan algunos features")
        features_array = np.array(features).reshape(1, -1)
        model = get_model()
        prediction = model.predict(features_array)
        return {
            "prediction": int(prediction[0]),
            "patient": "Not specified",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def predict_from_mongo(data):
    try:
        db = get_db()
        collection = db['SepsisTraining']["DataPacientes"]
        query = {"Paciente": data.patient, "Hora": data.hour}
        projection = {key: 1 for key in EXPECTED_KEYS}
        records = list(collection.find(query, projection))

        if not records:
            raise HTTPException(
                status_code=404,
                detail=f"No records found for patient {data.patient} at hour {data.hour}"
            )

        model = get_model()
        record = records[0]  # tomar el primero

        features = [record.get(key, -9999) for key in EXPECTED_KEYS]
        features_array = np.array(features).reshape(1, -1)
        prediction_result = model.predict(features_array)

        return {
            "patient": data.patient,
            "prediction": int(prediction_result[0])
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))