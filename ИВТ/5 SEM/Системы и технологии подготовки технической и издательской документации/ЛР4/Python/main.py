from shapes import Rectangle, Circle
from utils import print_shape_info

def main():
    """
    Основная функция программы. Создает объекты фигур и выводит их параметры.
    """
    rect = Rectangle(5, 10)
    circ = Circle(7)

    print_shape_info(rect)
    print_shape_info(circ)

if __name__ == "__main__":
    main()
