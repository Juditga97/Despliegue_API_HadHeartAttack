from model import predict

features = {
"State": "California",
"Sex": "Male",
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
"AgeCategory": "Age 60-64",
"WeightInKilograms": 80,
"CovidPos": "No",
"ChestScan": "No",
"PneumoVaxEver": "Yes"
}

resultado = predict(features)

print("Predicción:", resultado)