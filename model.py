import joblib #Lo usamos para cargar modelos entrenados guardados en archivos .pkl
import numpy as np
import pandas as pd

model = joblib.load("heart_attack_model_01.pkl") #Cargamos el modelo

def predict(features: dict):

    df = pd.DataFrame([features])      


    prediction = model.predict(df)

    return int(prediction[0])

