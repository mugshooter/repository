def create_magic_square(n):
    if n % 2 == 1:
        # Метод Сиамского квадрата для нечётных порядков
        magic_square = [[0] * n for _ in range(n)]
        row, col = 0, n // 2
        for num in range(1, n * n + 1):
            magic_square[row][col] = num
            new_row, new_col = (row - 1) % n, (col + 1) % n
            if magic_square[new_row][new_col]:
                row += 1
            else:
                row, col = new_row, new_col
        return magic_square
    elif n % 4 == 0:
        # Метод Страшея для чётно-чётных порядков
        magic_square = [[(i * n) + j + 1 for j in range(n)] for i in range(n)]
        for i in range(n // 4):
            for j in range(n // 4):
                magic_square[i][j] = n * n + 1 - magic_square[i][j]
                magic_square[i][n - j - 1] = n * n + 1 - magic_square[i][n - j - 1]
                magic_square[n - i - 1][j] = n * n + 1 - magic_square[n - i - 1][j]
                magic_square[n - i - 1][n - j - 1] = n * n + 1 - magic_square[n - i - 1][n - j - 1]
        return magic_square
    else:
        # Метод для чётно-нечётных порядков (например, 10×10)
        magic_square = [[0] * n for _ in range(n)]
        quadrant_size = n // 2
        quadrant = create_magic_square(quadrant_size)
        for i in range(quadrant_size):
            for j in range(quadrant_size):
                magic_square[i][j] = quadrant[i][j]
                magic_square[i][j + quadrant_size] = quadrant[i][j] + 2 * (quadrant_size ** 2)
                magic_square[i + quadrant_size][j] = quadrant[i][j] + 3 * (quadrant_size ** 2)
                magic_square[i + quadrant_size][j + quadrant_size] = quadrant[i][j] + quadrant_size ** 2
        return magic_square

def calculate_magic_constant(n):
    return n * (n ** 2 + 1) // 2

def is_magic_square(square, n):
    magic_constant = calculate_magic_constant(n)
    
    # Проверка строк
    for row in square:
        if sum(row) != magic_constant:
            return False
    
    # Проверка столбцов
    for col in range(n):
        if sum(square[row][col] for row in range(n)) != magic_constant:
            return False
    
    # Проверка главной диагонали
    if sum(square[i][i] for i in range(n)) != magic_constant:
        return False
    
    # Проверка побочной диагонали
    if sum(square[i][n - i - 1] for i in range(n)) != magic_constant:
        return False
    
    return True

def print_magic_square(square):
    for row in square:
        print(" ".join("{:3}".format(num) for num in row))

def main():
    n = int(input("Введите размер магического квадрата (n): "))
    if n < 3:
        print("Магический квадрат невозможен для n < 3.")
        return
    
    magic_square = create_magic_square(n)
    print("\nМагический квадрат:")
    print_magic_square(magic_square)
    
    magic_constant = calculate_magic_constant(n)
    print("\nМагическая константа: {}".format(magic_constant))
    
    if is_magic_square(magic_square, n):
        print("Квадрат является магическим.")
    else:
        print("Квадрат НЕ является магическим.")

if __name__ == "__main__":
    main()
