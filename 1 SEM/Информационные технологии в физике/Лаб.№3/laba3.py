import matplotlib.pyplot as plt
import numpy as np
import pylab

v0 = 200
a = np.radians(58)
a1 = np.pi / 12  # 15
a2 = np.pi / 6  # 30
a3 = np.pi / 4  # 45
g = 9.8
t = 0
t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0
t6 = 0
# ПУНКТ 1
x1 = []
y1 = []

plt.figure(figsize=(16, 9))
pylab.style.use('ggplot')

for t in np.arange(0, 34.7, 0.1):
    x = v0 * np.cos(a) * t
    y = v0 * np.sin(a) * t - (g * t ** 2) / 2
    x1.append(x)
    y1.append(y)
pylab.subplot(2, 2, 1)
pylab.plot(x1, y1, color='orange')
pylab.title('Задание 1, Пункт 1')
pylab.text(3650, 200, 'S = 3666m', color='orange', size='8')

# Y
x2 = [0, 0]
y2 = [0, 1500]
pylab.plot(x2, y2, color='black')

# X
x3 = [0, 4000]
y3 = [0, 0]
pylab.plot(x3, y3, color='black')

# стрелка для X
x4 = [3930, 4000, 3930]
y4 = [50, 0, -50, ]
pylab.plot(x4, y4, color='black')

# стрелка для Y
x5 = [-40, 0, 40]
y5 = [1450, 1500, 1450]
pylab.plot(x5, y5, color='black')
# Подпись для осей
pylab.text(-100, 1500, 'Y', size='10')
pylab.text(4010, -30, 'X', size='10')

# ПУНКТ 2
# Угол 15 синий
x6 = []
y6 = []
for t1 in np.arange(0, 10.6, 0.1):
    x = v0 * np.cos(a1) * t1
    y = v0 * np.sin(a1) * t1 - (g * t1 ** 2) / 2
    x6.append(x)
    y6.append(y)
pylab.subplot(2, 2, 2)
pylab.plot(x6, y6, color='blue')
pylab.title('Задание 1, Пункт 2')
pylab.text(1400, 160, 'α = 15°', size=10, color='blue')
pylab.text(2040, 95, 'S=2039m', size=10, color='blue')
# угол 30 оранжевый
x7 = []
y7 = []
for t2 in np.arange(0, 20.5, 0.1):
    x = v0 * np.cos(a2) * t2
    y = v0 * np.sin(a2) * t2 - (g * t2 ** 2) / 2
    x7.append(x)
    y7.append(y)
pylab.subplot(2, 2, 2)
pylab.plot(x7, y7, color='orange')
pylab.title('Задание 1, Пункт 2')
pylab.text(2000, 550, 'α = 30°', size=10, color='orange')
pylab.text(2600, 480, 'S=3532m', size=10, color='orange')
# угол 45 красный
x8 = []
y8 = []
for t3 in np.arange(0, 28.9, 0.1):
    x = v0 * np.cos(a3) * t3
    y = v0 * np.sin(a3) * t3 - (g * t3 ** 2) / 2
    x8.append(x)
    y8.append(y)
pylab.subplot(2, 2, 2)
pylab.plot(x8, y8, color='red')
pylab.title('Задание 1, Пункт 2')
pylab.text(3200, 800, 'α = 45°', size=10, color='red')
pylab.text(3500, 600, 'S=4078m', size=10, color='red')
# Y
x9 = [0, 0]
y9 = [0, 1090]
pylab.plot(x9, y9, color='black')
# X
x10 = [0, 4150]
y10 = [0, 0]
pylab.plot(x10, y10, color='black')
# Стрелка для Y
x11 = [-40, 0, 40]
y11 = [1040, 1090, 1040]
pylab.plot(x11, y11, color='black')
# Стрелка для Х
x12 = [4100, 4150, 4100]
y12 = [20, 0, -20]
pylab.plot(x12, y12, color='black')
# Подпись для осей
pylab.text(-90, 1090, 'Y', size='10')
pylab.text(4180, 0, 'X', size='10')
# Задание 2
# угол 45 красный  h = 0
x13 = []
y13 = []
for t4 in np.arange(0, 28.9, 0.1):
    x = v0 * np.cos(a3) * t4
    y = v0 * np.sin(a3) * t4 - (g * t4 ** 2) / 2
    x13.append(x)
    y13.append(y)
pylab.subplot(2, 2, 3)
pylab.plot(x13, y13, color='red')
pylab.title('Задание 2')
# h = 250
x14 = []
y14 = []
for t5 in np.arange(0, 30.6, 0.1):
    x = v0 * np.cos(a3) * t5
    y = v0 * np.sin(a3) * t5 - (g * t5 ** 2) / 2
    x14.append(x)
    y14.append(y)
    x15 = x14
    y15 = [i + 250 for i in y14]
pylab.subplot(2, 2, 3)
pylab.plot(x15, y15, color='orange')
# h = 500
x16 = []
y16 = []
for t6 in np.arange(0, 32.1, 0.1):
    x = v0 * np.cos(a3) * t6
    y = v0 * np.sin(a3) * t6 - (g * t6 ** 2) / 2
    x16.append(x)
    y16.append(y)
    x17 = x16
    y17 = [i + 500 for i in y16]
pylab.subplot(2, 2, 3)
pylab.plot(x17, y17, color='gray')
# h = 700
x18 = []
y18 = []
for t7 in np.arange(0, 33.2, 0.1):
    x = v0 * np.cos(a3) * t7
    y = v0 * np.sin(a3) * t7 - (g * t7 ** 2) / 2
    x18.append(x)
    y18.append(y)
    x19 = x18
    y19 = [i + 700 for i in y18]
pylab.subplot(2, 2, 3)
pylab.plot(x19, y19, color='blue')
# X
x20 = [0, 4850]
y20 = [0, 0]
pylab.plot(x20, y20, color='black')
# Y
x21 = [0, 0]
y21 = [0, 1800]
pylab.plot(x21, y21, color='black')
# Стрелка для Y
x22 = [-40, 0, 40]
y22 = [1740, 1800, 1740]
pylab.plot(x22, y22, color='black')
# Стрелка для Х
x22 = [4780, 4850, 4780]
y22 = [30, 0, -30]
pylab.plot(x22, y22, color='black')
# Подпись для осей
pylab.text(-90, 1800, 'Y', size='10')
pylab.text(4870, 0, 'X', size='10')
# Подписи h
pylab.text(3000, 1500, 'h = 700m', color='blue')
plt.show()
