from flask import Flask, request, jsonify
from model import predict

app = Flask (__name__) #Inicializamos la API

@app.route("/")
def home():
    return {
        "mensaje": "API de prediccion de ataque cardiaco",
        "descripcion": "Esta API recibe datos de salud de un paciente y devuelve una predicción de riesgo de ataque cardíaco usando un modelo de Machine Learning",
        "endpoint": "/predict",
        "metodo": "POST"
    }

@app.route("/predict", methods=["POST"])
def predict_endpoint():

    data = request.get_json(silent=True)

    if not data:
        data = {
            "Sex": "Male",
            "AgeCategory": "Age 60-64",
            "GeneralHealth": "Good",
            "PhysicalHealthDays": 0,
            "MentalHealthDays": 0,
            "LastCheckupTime": "Within past year",
            "PhysicalActivities": "Yes",
            "SleepHours": 7,
            "RemovedTeeth": "None",
            "HadAngina": "No",
            "HadStroke": "No",
            "HadCOPD": "No",
            "HadDiabetes": "No",
            "HadKidneyDisease": "No",
            "HadArthritis": "No",
            "HadSkinCancer": "No",
            "AlcoholDrinkers": "Yes",
            "SmokerStatus": "Never smoked",
            "DifficultyWalking": "No",
            "DifficultyDressingBathing": "No",
            "DifficultyErrands": "No",
            "DeafOrHardOfHearing": "No",
            "BlindOrVisionDifficulty": "No",
            "DifficultyConcentrating": "No",
            "WeightInKilograms": 80,
            "CovidPos": "No",
            "ChestScan": "No",
            "PneumoVaxEver": "Yes",
            "State": "California"
        }

    result = predict(data)

    return jsonify({
        "prediction": result
    })