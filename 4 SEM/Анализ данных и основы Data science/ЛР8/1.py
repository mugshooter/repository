import numpy as np

# Ввод данных
n = int(input('Введите размерность квадратной матрицы: '))

# Матрица X
matrix_X = np.array([[int(input(f"Введите элемент [{i+1}][{j+1}] матрицы X: ")) for j in range(n)] for i in range(n)])

# Матрица Y
matrix_Y = np.array([[int(input(f"Введите элемент [{i+1}][{j+1}] матрицы Y: ")) for j in range(1)] for i in range(n)])

# Вывод матриц X и Y
print("\nВведенная матрица X:\n", matrix_X)
print("\nВведенная матрица Y:\n", matrix_Y)

# Матрица X^T
matrix_XT = matrix_X.T

# Перемножение C = X^T * X
matrix_C = np.dot(matrix_XT, matrix_X)

# Перемножение Y1 = X^T * Y
matrix_Y1 = np.dot(matrix_XT, matrix_Y)

# Обратная матрица C (C^-1)
obratnay_C = np.round(np.linalg.inv(matrix_C), 5)

# Нахождение матрицы А (коэффициенты)
matrix_A = np.round(np.dot(obratnay_C, matrix_Y1), 5)

# Вывод результатов
print("\nМатрица X^T:\n", matrix_XT)
print("\nПеремножение X^T и X (C):\n", matrix_C)
print("\nПеремножение X^T и Y (Y1):\n", matrix_Y1)
print("\nОбратная матрица C (C^-1):\n", obratnay_C)
print("\nМатрица с коэффициентами a:\n", matrix_A)
