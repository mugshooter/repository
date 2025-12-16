import matplotlib.pyplot as plt
import numpy as np
import pylab

print('Введите  значение m')
m = int(input()) # Входные данные для построения графиков зависимости 
g = 9.8
αс = np.radians(30)
μс = 0.5
F1max=0 # Переменная для нахождения максимальной силы трения
F1min=1000 # Переменная для нахождения минимальной силы трения
F2max=0
F2min=1000
αmax=0
αmin=90
μmax=0
μmin=1
print('Введите начальное значение μ(от 0 до 1)')
μ1=int(input())
print('Введите конечное значение μ(от 0 до 1)')
μ2=int(input())
print('Введите начальное значение α(от 0 до 90)')
α1=int(input())
print('Введите конечное значение α(от 0 до 90)')
α2=int(input())

x1,y1,x2,y2,x3,y3,x4,y4,x5,y5 = [],[],[],[],[],[],[],[],[],[] # Массивы для построения графиков зависимости


plt.figure(figsize=(16, 9))
pylab.style.use('ggplot')


for α in range(α1, α2+1): # Высчитываем координаты для построения графика зависимости силы трения от угла наклонной плоскости
    α = np.radians(α) # Значение угла наклонной плоскости в радианах
    F1 = μс * m * g * np.cos(α) # Значение силы трения
    α = np.degrees(α) # Преобразование угла наклонной плоскости в градусах для корректного отображения точек на графика
    if F1>F1max: # вычисление максимального значения силы трения при угле α
        F1max=F1
        αmax=α
    if F1<F1min: # вычисление минимального значения силы трения при угле α
        F1min=F1
        αmin=α
        
    x1.append(α) # Занесение значений в массив
    y1.append(F1) # Занесение значений в массив
    
pylab.subplot(1, 2, 1) # Расположение графика на окне вывода
pylab.plot(x1, y1, color='blue') # Построение графика, используя точки из массивов x1 и y1
pylab.title('Fтр(α)') # Вывод текста над графиком

x2 = [0, 0] # Построение оси x             
y2 = [0, max(y1)+1]
pylab.plot(x2, y2, color='black') 

x3 = [0, max(x1)+10] # Построение оси y
y3 = [0, 0]
pylab.plot(x3, y3, color='black')

x4 = [max(x1)+7.5, max(x1)+10, max(x1)+7.5] 
y4 = [0.1, 0, -0.1]
pylab.plot(x4, y4, color='black')

x5 = [-1, 0, 1]
y5 = [max(y1)+0.4, max(y1)+1, max(y1)+0.4]
pylab.plot(x5, y5, color='black')

pylab.text(-6, max(y1)+1, 'Fтр', size='11')
pylab.text(max(x1)+9.5, -0.4, 'α', size='13')


x6,y6,x7,y7,x8,y8,x9,y9,x10,y10 = [],[],[],[],[],[],[],[],[],[]


for μ in np.arange(μ1, μ2+0.02, 0.02):
    F2 = μ * m * g * np.cos(αс)
    if F2>F2max:
        F2max=F2
        μmax=μ
    if F2<F2min:
        F2min=F2
        μmin=μ
    x6.append(μ)
    y6.append(F2)

pylab.subplot(1, 2, 2)
pylab.plot(x6, y6, color='blue')
pylab.title('Fтр(μ)')

x7 = [0, 0]
y7 = [0, max(y6)+1]
pylab.plot(x7, y7, color='black')

x8 = [0, max(x6)+0.1]
y8 = [0, 0]
pylab.plot(x8, y8, color='black')

x9 = [max(x6)+0.05, max(x6)+0.1, max(x6)+0.05]
y9 = [0.15, 0, -0.15]
pylab.plot(x9, y9, color='black')

x10 = [-0.01, 0, 0.01]
y10 = [max(y6)+0.3, max(y6)+1, max(y6)+0.3]
pylab.plot(x10, y10, color='black')

pylab.text(-0.07, max(y6)+0.48, 'Fтр', size='11')
pylab.text(max(x6)+0.08, -0.55, 'μ', size='13')
print ('Fтр принимает максимальное значение', F1max,'H при угле α = ',αmax)
print ('Fтр принимает минимальное значение', F1min,'H при угле α = ',αmin)
print ('Fтр принимает максимальное значение', F2max,'H коэффициенте трения μ = ',μmax)
print ('Fтр принимает минимальное значение', F2min,'H коэффициенте трения μ = ',μmin)

pylab.show()
