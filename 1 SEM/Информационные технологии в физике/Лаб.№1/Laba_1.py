import numpy as np
import matplotlib.pyplot as plt
import pylab

print('Enter time slot')
D = int(input())  # промежуток времени на основании которого будет выведена траектория движения планет
# Входные данные по Земле
rY = 149600000
TY = 365
wY = np.pi * 2 / TY
# Входные данные по Марсу
rM = 228000000
TM = 687
wM = np.pi * 2 / TM

t1 = 0
t2 = 0
t3 = 0
t4 = 0

# Входные данные по Венере
rV = 108000000
TV = 224.7
wV = np.pi * 2 / TV
# Входные данные по Сатурну
r_Saturn = 1430_000_000
T_Saturn = 10585
w_Saturn = np.pi * 2 / T_Saturn
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []

plt.figure(figsize=(16, 9))
pylab.style.use('ggplot')

# МАРС ЗЕМЛЯ
while t1 <= D:
    x = rM * np.cos(wM * t1) - rY * np.cos(wY * t1)
    y = rM * np.sin(wM * t1) - rY * np.sin(wY * t1)
    t1 += 6
    x1.append(x)
    y1.append(y)
pylab.subplot(2, 2, 1)
pylab.plot(x1, y1)
pylab.title('Марс относительно Земли')
# ВЕНЕРА ЗЕМЛЯ
while t2 <= D:
    x = rV * np.cos(wV * t2) - rY * np.cos(wY * t2)
    y = rV * np.sin(wV * t2) - rY * np.sin(wY * t2)
    t2 += 6
    x2.append(x)
    y2.append(y)
pylab.subplot(2, 2, 2)
pylab.plot(x2, y2,)
pylab.title('Венера относительно Земли')

# Сатурн ЗЕМЛЯ
while t3 <= D:
    x = r_Saturn * np.cos(w_Saturn * t3) - rY * np.cos(wY * t3)
    y = r_Saturn * np.sin(w_Saturn * t3) - rY * np.sin(wY * t3)
    t3 += 6
    x3.append(x)
    y3.append(y)
pylab.subplot(2, 2, 3)
pylab.plot(x3, y3)
pylab.title('Сатурн относительно Земли')

# ВЕНЕРА Марс
while t4 <= D:
    x = rV * np.cos(wV * t4) - rM * np.cos(wM * t4)
    y = rV * np.sin(wV * t4) - rM * np.sin(wM * t4)
    t4 += 6
    x4.append(x)
    y4.append(y)
pylab.subplot(2, 2, 4)
pylab.plot(x4, y4)
pylab.title('Венера относительно Марса')

pylab.show()
