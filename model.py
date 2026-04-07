import joblib
import pandas as pd
import os

# Obtener la ruta del directorio actual
BASE_DIR = os.path.dirname(__file__)

# Construir la ruta completa del modelo
model_path = os.path.join(BASE_DIR, "heart_attack_model_01.pkl")

# Cargar el modelo
model = joblib.load(model_path)

def predict(features: dict):

    df = pd.DataFrame([features])

    prediction = model.predict(df)

    return int(prediction[0])

