import joblib
import pandas as pd
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(BASE_DIR, "heart_attack_model_01.pkl")

# Cargar modelo UNA VEZ al iniciar
model = joblib.load(model_path)

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

    # Convertir a DataFrame
    df = pd.DataFrame([features])

    # Asegurar orden correcto
    df = df[columns]

    # Predicción
    prediction = model.predict(df)

    return int(prediction[0])
