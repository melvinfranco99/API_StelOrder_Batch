import requests
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Asegúrate de que el nombre de la variable esté entre comillas
api_key = os.getenv("API_KEY")

url = "https://app.stelorder.com/app/clients/"
# Añadir la APIKEY como un parámetro de consulta
url_con_api_key = f"{url}?APIKEY={api_key}"

headers = {
    "accept": "application/json; charset=utf-8",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

# Imprimir el enlace para acceder en el navegador
print(f"Puedes acceder a la API en: {url_con_api_key}")
