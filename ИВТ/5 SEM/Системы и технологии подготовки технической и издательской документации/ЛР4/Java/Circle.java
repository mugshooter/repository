/**
 * Класс для представления круга.
 */
public class Circle implements Shape {
    private double radius;

    /**
     * Создает круг с указанным радиусом.
     *
     * @param radius радиус круга
     */
    public Circle(double radius) {
        this.radius = radius;
    }

    /**
     * Вычисляет площадь круга.
     *
     * @return площадь круга
     */
    @Override
    public double area() {
        return Math.PI * radius * radius;
    }

    /**
     * Вычисляет периметр круга (длину окружности).
     *
     * @return периметр круга
     */
    @Override
    public double perimeter() {
        return 2 * Math.PI * radius;
    }
}
