import joblib
import numpy as np
from config import MODEL_PATH

model = joblib.load(MODEL_PATH)

def ml_score(tx):
    features = np.array([[
        tx.amount,
        int(tx.country != tx.home_country),
        int(tx.device_new)
    ]])

    return float(model.predict_proba(features)[0][1])
