from scipy.stats import shapiro

intervals = [(190, 200), (200, 210), (210, 220), (220, 230), (230, 240), (240, 250)]
xi = [195, 205, 215, 225, 235, 245] 
ni = [10, 26, 56, 64, 30, 14] 

data = []
for i in range(len(intervals)):
    data.extend([xi[i]] * ni[i])

statistic, p_value = shapiro(data)

print("Проверка нулевой гипотезы о нормальном распределении прочности:")
print(f"Интервалы прочности: {intervals}")
print(f"Средние значения интервалов (xi): {xi}")
print(f"Частоты (ni): {ni}")

print("\n Результаты проверки :")
print(f"Статистика критерия: {statistic}")
print(f"P-значение: {p_value}")

alpha = 0.001
print(f"\nУровень значимости (alpha): {alpha}")
if p_value < alpha:
    print("Отвергаем нулевую гипотезу: данные не имеют нормальное распределение.")
else:
    print("Не отвергаем нулевую гипотезу: данные имеют нормальное распределение.")
