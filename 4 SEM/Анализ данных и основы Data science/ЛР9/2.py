import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from scipy.stats import pearsonr

# Исходные данные
years = np.array([1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998])
potato_production = np.array([70, 79, 83, 85, 68, 71, 81, 77, 83, 76, 81, 86, 70, 92, 70, 83, 92, 95, 107])

# а) Построение графика временного ряда
plt.figure(figsize=(10, 5))
plt.plot(years, potato_production, marker='o')
plt.title('а) График временного ряда валового сбора картофеля')
plt.xlabel('Год')
plt.ylabel('Валовой сбор, тыс.т')
plt.grid(True)
plt.show()

# б) Расчет коэффициента автокорреляции первого порядка
autocorr = pearsonr(potato_production[:-1], potato_production[1:])[0]
print("б) Коэффициент автокорреляции первого порядка:", autocorr)

# в) Определение типа уравнения тренда и расчет его параметров
# Поскольку на графике виден некоторый тренд, будем использовать линейную регрессию для его аппроксимации
data = pd.DataFrame({'Year': years, 'Production': potato_production})

data['Year_Num'] = np.arange(1, len(data) + 1)

model = np.polyfit(data['Year_Num'], data['Production'], 1)

trend_slope = model[0]
trend_intercept = model[1]

print("в) Параметры тренда (slope, intercept):", trend_slope, trend_intercept)

# г) Интерпретация параметров тренда и выводы
if trend_slope > 0:
    trend_interpretation = "Валовой сбор картофеля увеличивается с течением времени."
elif trend_slope < 0:
    trend_interpretation = "Валовой сбор картофеля уменьшается с течением времени."
else:
    trend_interpretation = "Валовой сбор картофеля не изменяется со временем."

print("г) Интерпретация параметров тренда и выводы:", trend_interpretation)
