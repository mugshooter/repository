
import numpy as np
import pylab

r = 9
E = 3
x1 = []
y1 = []

x5 = [0, 0]
y5 = [0, 3]
pylab.plot(x5, y5, color='black')

x6 = [0, 0.35]
y6 = [0, 0]
pylab.plot(x6, y6, color='black')
x2 = []
y2 = []

x_str = [0.343, 0.35, 0.343]
y_str = [0.05, 0, -0.05]
pylab.plot(x_str, y_str, color='black')

x1_srt = [-0.002, 0, 0.002]
y1_str = [2.9, 3, 2.9]
pylab.plot(x1_srt, y1_str, color='black')
for R in np.arange(0, 500):
    I = E / (R + r)
    U = E - I * r
    x1.append(I)
    y1.append(U)

for R1 in np.arange(0, 500):
    I1 = E / (R1 + r)
    P = E * I1
    x2.append(I1)
    y2.append(P)

x3 = []
y3 = []

for R2 in np.arange(0, 500):
    I2 = E / (R2 + r)
    P_full = E * I2 - I2 ** 2 * r
    x3.append(I2)
    y3.append(P_full)

x4 = []
y4 = []
for R3 in np.arange(0, 500):
    I3 = E / (R3 + r)
    P = E * I3
    P1_full = E * I3 - I3 ** 2 * r
    n = P1_full / P
    x4.append(I3)
    y4.append(n)
pylab.plot(x4, y4, color='gray')
pylab.text(0.05, 1, 'η(I)')
pylab.plot(x3, y3, color='orange')
pylab.text(0.16, 0.3, 'Pп(I)')
pylab.plot(x2, y2, color='red')
pylab.text(0.3, 1.1, 'P(I)')
pylab.plot(x1, y1, color='blue')
pylab.text(0.16, 1.75, 'U(I)')
pylab.text(0.351, 0, 'I')
pylab.text(-0.01, 3, 'U, P, Pп, η')
pylab.show()
