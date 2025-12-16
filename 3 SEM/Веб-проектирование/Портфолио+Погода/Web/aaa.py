import requests

def get_weather(city):
    base_url = f'https://wttr.in/{city.replace(" ", "+")}?format=%C+%t'

    response = requests.get(base_url)
    data = response.text.strip()

    if response.status_code == 404 or 'Sorry,' in data:
        return 'Город не найден.'

    formatted_data = data.split(' ')
    weather_description = formatted_data[1]
    temperature = formatted_data[2]

    return f'Сейчас в городе {city} {weather_description}. Температура: {temperature}.'

def main():
    city = input('Введите название города: ')
    weather = get_weather(city)

    print(weather)

if __name__ == '__main__':
    main()