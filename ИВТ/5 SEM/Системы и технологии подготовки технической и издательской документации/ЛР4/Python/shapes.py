class Rectangle:
    """
    Класс для представления прямоугольника.
    """

    def __init__(self, width, height):
        """
        Инициализация прямоугольника.

        Args:
            width (float): Ширина прямоугольника.
            height (float): Высота прямоугольника.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Returns:
            float: Площадь прямоугольника.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Returns:
            float: Периметр прямоугольника.
        """
        return 2 * (self.width + self.height)


class Circle:
    """
    Класс для представления круга.
    """

    def __init__(self, radius):
        """
        Инициализация круга.

        Args:
            radius (float): Радиус круга.
        """
        self.radius = radius

    def area(self):
        """
        Вычисляет площадь круга.

        Returns:
            float: Площадь круга.
        """
        return 3.14 * self.radius ** 2

    def perimeter(self):
        """
        Вычисляет длину окружности.

        Returns:
            float: Длина окружности.
        """
        return 2 * 3.14 * self.radius
