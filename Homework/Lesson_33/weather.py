import requests

API_KEY = "f185a351f58657e70101e22572034c6a"                    # мій API ключ
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",                                      # температура в °C
        "lang": "ua"                                            # українська мова
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return f"Помилка! Не вдалося отримати дані ({response.status_code})."

    data = response.json()

    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    desc = data["weather"][0]["description"].capitalize()

    return (
        f"Погода у місті {city}:\n"
        f"Температура: {temp}°C\n"
        f"Відчувається як: {feels}°C\n"
        f"Вологість: {humidity}%\n"
        f"Опис: {desc}"
    )

if __name__ == "__main__":
    city_name = input("Введіть назву міста: ")
    print(get_weather(city_name))