import joblib
import threading

_model_lock = threading.Lock()
_current_model = None
_model_path = "app/model_store/gbdt_model.pkl"

def load_model(path: str = None):
    global _current_model, _model_path
    if path:
        _model_path = path
    with open(_model_path, "rb") as f:
        model = joblib.load(f)
    with _model_lock:
        _current_model = model

def get_model():
    with _model_lock:
        return _current_model
