import requests
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Asegúrate de que el nombre de la variable esté entre comillas
api_key = os.getenv("API_KEY")

url = "https://app.stelorder.com/app/clients/"
headers = {
    "accept": "application/json; charset=utf-8",
    "APIKEY": api_key,
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
