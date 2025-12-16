import matplotlib.pyplot as plt
import pandas as pd
import json

def visualise_data(json_data):
    if json_data:
        data = json.loads(json_data)
        city_name = data['city']
        
        # Даты и температуры
        dates = [entry['dt'] for entry in data['temperatures']]
        temps = [entry['temp'] for entry in data['temperatures']]
        
        # Преобразуем временные метки
        dates = pd.to_datetime(dates, unit='s')
        
        # Создаем scatter plot
        plt.figure(figsize=(10, 6))
        plt.subplot(1, 2, 1)
        plt.scatter(dates, temps)
        plt.title(f"Температура за последние 5 дней в {city_name}")
        plt.xlabel("Дата")
        plt.ylabel("Температура (°C)")
        
        # Добавляем box plot
        plt.subplot(1, 2, 2)
        plt.boxplot(temps, vert=False)
        plt.title("Диаграмма ящика с усами")
        plt.xlabel("Температура (°C)")
        
        plt.tight_layout()
        plt.show()
