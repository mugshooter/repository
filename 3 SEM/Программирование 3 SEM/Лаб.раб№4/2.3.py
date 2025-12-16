import matplotlib.pyplot as plt
import numpy as np

# Функции для 1 окна
def tanh(x):
    return np.tanh(x)

# Функция котангенса
def coth(x):
    return 1/np.tanh(x)

# Функция для второго окна
def f(x):
    return x**2 + 2*x + 1

# Создаем массив значений x
x = np.linspace(-10, 10, 1000)
# Первое окно
plt.figure (1)

plt.subplot(221)
plt.plot(x, tanh(x))
plt.title('tanh(x)')

plt.subplot(222)
plt.plot(x, coth(x))
plt.title('coth(x)')
# Второе окно
plt.figure (2)

plt.plot(x, f(x))
plt.title('f(x)')

plt.show()
