import requests
import json
from datetime import datetime

def get_weather_data(place, api_key=None):
    if api_key is None:
        raise ValueError("API key is required")

    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Ошибка при получении данных для {place}")
        return json.dumps({"city": place, "temperatures": []}, ensure_ascii=False, indent=4)

    data = response.json()
    
    temperatures = []
    for forecast in data['list']:
        # Преобразуем UNIX время в читабельный формат
        dt = datetime.fromtimestamp(forecast['dt'])
        if dt.hour == 12:  # Выбираем данные для полудня
            temperatures.append({
                "dt": forecast['dt'],
                "temp": forecast['main']['temp']
            })
    
    result = {
        "city": place,
        "temperatures": temperatures
    }
    return json.dumps(result, ensure_ascii=False, indent=4)
