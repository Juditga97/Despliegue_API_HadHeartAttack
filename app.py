from flask import Flask, request, jsonify
from model import predict

app = Flask (__name__) #Inicializamos la API

@app.route("/")
def home():
    return {
        "mensaje": "API de prediccion de ataque cardiaco",
        "endpoint": "/predict",
        "metodo": "POST",
        "descripcion": "Envia los datos de salud de un paciente en formato JSON para obtener una prediccion"
    }

@app.route("/predict", methods=["POST"])
def predict_endpoint():

    try:
        data = request.get_json() #Recibimos los datos

        if not data:
            return jsonify({"error": "No hay data disponible"}), 400

        result = predict(data)

        return jsonify({
            "prediction": result
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)


