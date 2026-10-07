import warnings
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model, ensemble
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Игнорирование предупреждений
warnings.simplefilter(action='ignore', category=FutureWarning)

# Загрузка данных
df = pd.read_csv('ex1data2.txt', sep=',')

# Разделение на тренировочные и тестовые данные
train, test = train_test_split(df, test_size=0.2, random_state=42)

# Предобработка данных (удаление пропусков, если есть)
def preprocess_data(df):
    df = df.dropna()
    return df.select_dtypes(include=['number'])

train = preprocess_data(train)
test = preprocess_data(test)

# Разделение на признаки и целевую переменную
target_variable = 'cost'
X_train = train.drop(target_variable, axis=1)
y_train = train[target_variable]
X_test = test.drop(target_variable, axis=1)
y_test = test[target_variable]

# Обучение линейной регрессии
linear_model = linear_model.LinearRegression()
linear_model.fit(X_train, y_train)

# Обучение случайного леса
rf_model = ensemble.RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)

# Предсказания
linear_pred = linear_model.predict(X_test)
rf_pred = rf_model.predict(X_test)

# Оценка качества
print("Линейная регрессия:")
print(f"MAE: {mean_absolute_error(y_test, linear_pred):.2f}")
print(f"RMSE: {mean_squared_error(y_test, linear_pred)**0.5:.2f}")
print(f"R²: {r2_score(y_test, linear_pred):.2f}\n")

print("Случайный лес:")
print(f"MAE: {mean_absolute_error(y_test, rf_pred):.2f}")
print(f"RMSE: {mean_squared_error(y_test, rf_pred)**0.5:.2f}")
print(f"R²: {r2_score(y_test, rf_pred):.2f}")

# Визуализация
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(y_test, linear_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.title('Линейная регрессия')
plt.xlabel('Реальная стоимость')
plt.ylabel('Предсказанная стоимость')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(y_test, rf_pred, alpha=0.5, color='orange')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.title('Случайный лес')
plt.xlabel('Реальная стоимость')
plt.ylabel('Предсказанная стоимость')
plt.grid(True)

plt.tight_layout()
plt.show()

# Сравнение метрик
metrics = ['MAE', 'RMSE', 'R²']
linear_metrics = [
    mean_absolute_error(y_test, linear_pred),
    mean_squared_error(y_test, linear_pred)**0.5,
    r2_score(y_test, linear_pred)
]

rf_metrics = [
    mean_absolute_error(y_test, rf_pred),
    mean_squared_error(y_test, rf_pred)**0.5,
    r2_score(y_test, rf_pred)
]

x = range(len(metrics))
plt.figure(figsize=(10, 5))
plt.bar(x, linear_metrics, width=0.4, label='Линейная регрессия')
plt.bar([i + 0.4 for i in x], rf_metrics, width=0.4, label='Случайный лес')
plt.xticks([i + 0.2 for i in x], metrics)
plt.title('Сравнение метрик')
plt.ylabel('Значение')
plt.legend()
plt.grid(True, axis='y', linestyle='--')
plt.show()