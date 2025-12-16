import numpy as np
from tabulate import tabulate

def cholesky_decomposition(matrix):
    n = len(matrix)
    L = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i+1):
            if i == j:
                sum_term = sum(L[i][k] ** 2 for k in range(j))
                L[i][j] = np.sqrt(matrix[i][i] - sum_term)
            else:
                sum_term = sum(L[i][k] * L[j][k] for k in range(j))
                L[i][j] = (matrix[i][j] - sum_term) / L[j][j]
    
    return L

def forward_substitution(L, b):
    n = len(b)
    y = np.zeros(n)
    
    for i in range(n):
        y[i] = (b[i] - sum(L[i][j] * y[j] for j in range(i))) / L[i][i]
    
    return y

def backward_substitution(L_transpose, y):
    n = len(y)
    x = np.zeros(n)
    
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(L_transpose[i][j] * x[j] for j in range(i+1, n))) / L_transpose[i][i]
    
    return x

# Пример задания матрицы
A = np.array([
    [5, 7, 6, 5, 23],
    [7, 10, 8, 7, 32],
    [6, 8, 10, 9, 33],
    [5, 7, 9, 10, 31]
], dtype=float)

print("Матрица А:")
print(tabulate(A, tablefmt="fancy_grid"))

# Метод Холецкого
L = cholesky_decomposition(A[:, :-1])
print("Матрица L:")
print(tabulate(L, tablefmt="fancy_grid"))

# Прямой ход
b = A[:, -1]
y = forward_substitution(L, b)
print("Правая часть м. A:")
print(y)

# Обратный ход
L_transpose = L.transpose()
x = backward_substitution(L_transpose, y)
print("Решение СЛУ:")
print(x)
