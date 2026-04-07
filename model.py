import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "heart_attack_model_01.pkl")

model = None

def predict(features: dict):

    global model

    if model is None:
        model = joblib.load(model_path)

    df = pd.DataFrame([features])

    prediction = model.predict(df)

    return int(prediction[0])

