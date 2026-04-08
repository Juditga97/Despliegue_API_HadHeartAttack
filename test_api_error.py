import requests

url = " https://despliegue-api-hadheartattack.onrender.com/predict"

# Caso 1: vacío
response = requests.post(url, json={})
print("Vacío:", response.json())

# Caso 2: tipo incorrecto
response = requests.post(url, json={"Sex": 123})
print("Tipo incorrecto:", response.json())