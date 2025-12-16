from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import random


arr = [5.1, 5.2, 5.1, 5.3, 5.2, 5.1, 5.2, 5.3, 5.4, 5.2, 5.3, 5.4, 5.5, 5.4, 5.3, 5.2, 5.3, 5.4, 5.5, 5.4]

print("Массив: ", arr)
arr.sort()
n = len(arr)

k = 1 + 1.4*np.log(n)
print("Количество интервалов k =", k)

a, b = arr[0], arr[-1]

d = (b - a) / k
print("Длина интервала d =", d)

det = Counter(arr)
x, y = [], []
for char in det:
    x.append(char)
    y.append(det[char])


plt.subplot(2, 1, 2)
plt.grid(True)
plt.plot(x, y)
plt.plot([arr[0], arr[-1]], [0, 0], color='black')

plt.subplot(2, 1, 1)
plt.grid(True)
plt.hist(arr, color='skyblue', edgecolor='black')

plt.show()