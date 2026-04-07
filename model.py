import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "heart_attack_model_01.pkl")

model = None

# Orden correcto de columnas
columns = [
    "State","Sex","GeneralHealth","PhysicalHealthDays","MentalHealthDays",
    "LastCheckupTime","PhysicalActivities","SleepHours","RemovedTeeth",
    "HadAngina","HadStroke","HadCOPD","HadDiabetes","HadKidneyDisease",
    "HadArthritis","HadSkinCancer","AlcoholDrinkers","SmokerStatus",
    "DifficultyWalking","DifficultyDressingBathing","DifficultyErrands",
    "DeafOrHardOfHearing","BlindOrVisionDifficulty","DifficultyConcentrating",
    "AgeCategory","WeightInKilograms","CovidPos","ChestScan","PneumoVaxEver"
]

def predict(features: dict):

    global model

    # Cargar modelo solo una vez
    if model is None:
        model = joblib.load(model_path)

    df = pd.DataFrame([features])

    # Asegurar orden correcto
    df = df[columns]

    prediction = model.predict(df)

    return int(prediction[0])
