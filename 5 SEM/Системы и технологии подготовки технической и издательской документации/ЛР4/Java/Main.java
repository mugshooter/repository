/**
 * Основной класс программы, который демонстрирует работу с фигурами.
 */
public class Main {
    public static void main(String[] args) {
        Rectangle rect = new Rectangle(5, 10);
        Circle circ = new Circle(7);

        printShapeInfo(rect);
        printShapeInfo(circ);
    }

    /**
     * Выводит информацию о фигуре.
     *
     * @param shape Объект фигуры.
     */
    public static void printShapeInfo(Shape shape) {
        System.out.println("Площадь: " + shape.area());
        System.out.println("Периметр: " + shape.perimeter());
    }
}
