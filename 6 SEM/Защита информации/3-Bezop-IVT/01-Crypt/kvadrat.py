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
        # Метод для чётно-нечётных порядков (10×10)
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

# Пример использования
n = 4
magic_square = create_magic_square(n)
for row in magic_square:
    print(row)

