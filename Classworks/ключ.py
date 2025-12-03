import requests

API_KEY = "f185a351f58657e70101e22572034c6a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": "Kyiv",
    "appid": API_KEY
}

response = requests.get(BASE_URL, params=params)
print(response.status_code)
print(response.text)