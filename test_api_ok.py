import requests

url = "https://TU-URL.onrender.com/predict"

data = {
    "Sex": "Male",
    "AgeCategory": "Age 60-64",
    "GeneralHealth": "Good"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())