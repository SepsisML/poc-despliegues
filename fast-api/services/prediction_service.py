import numpy as np
from pymongo import MongoClient
from fastapi import HTTPException
from app.models.loader import get_model
from app.constants import expected_keys, MONGO_URI

def predict_from_input(input_data):
    try:
        features = [getattr(input_data, key) for key in expected_keys]
        if len(features) < len(expected_keys):
            raise HTTPException(status_code=400, detail="Faltan algunos features")
        features_array = np.array(features).reshape(1, -1)
        model = get_model()
        prediction = model.predict(features_array)
        return {
            "prediction": int(prediction[0]),
            "patient": input_data.Paciente,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def predict_from_mongo(data):
    try:
        db = get_db()
        collection = db['SepsisTraining']

        query = {"Paciente": data.patient, "Hora": float(data.hour)}
        projection = {key: 1 for key in expected_keys}
        records = list(collection.find(query, projection))

        if not records:
            raise HTTPException(
                status_code=404,
                detail=f"No records found for patient {data.patient} at hour {data.hour}"
            )

        model = get_model()
        record = records[0]  # tomar el primero

        features = [record.get(key, -9999) for key in expected_keys]
        features_array = np.array(features).reshape(1, -1)
        prediction_result = model.predict(features_array)

        return {
            "patient": data.patient,
            "prediction": int(prediction_result[0])
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))