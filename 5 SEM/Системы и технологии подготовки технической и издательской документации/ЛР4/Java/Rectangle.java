/**
 * Класс для представления прямоугольника.
 */
public class Rectangle implements Shape {
    private double width;
    private double height;

    /**
     * Создает прямоугольник с указанными размерами.
     *
     * @param width  ширина прямоугольника
     * @param height высота прямоугольника
     */
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    /**
     * Вычисляет площадь прямоугольника.
     *
     * @return площадь прямоугольника
     */
    @Override
    public double area() {
        return width * height;
    }

    /**
     * Вычисляет периметр прямоугольника.
     *
     * @return периметр прямоугольника
     */
    @Override
    public double perimeter() {
        return 2 * (width + height);
    }
}
