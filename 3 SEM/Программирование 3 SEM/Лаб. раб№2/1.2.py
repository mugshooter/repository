import math
import statistics

def convert_precision(tolerance):
    """
    Функция принимает значение допуска и возвращает порядок величины.
    Например, для 1e-6 она вернет 6.
    """
    return abs(math.floor(math.log10(tolerance)))

def calculate (sym, *args, tolerance=1e-6):
    """
    Функция выполняет арифметическую операцию над числами.
    Возможные операции: "+", "-", "*", "/", "medium - среднее значение", "variance - дисперсия",
    "std_deviation - стандартное отклонение", "median - медиана", 
    "q2 - второй квартиль", "q3 - q1 - межквартильный размах".
    Результат округляется до порядка величины, указанного параметром tolerance.
    """
    if not all(isinstance(arg, (int, float)) for arg in args):
        return "Ошибка в операндах"
    
    precision = convert_precision(tolerance)
    
    if sym =="+":
        return round(sum(args), precision)
    elif sym =="-":
        return round(args[0] - sum(args[1:]), precision)
    elif sym =="*":
        result = 1
        for arg in args:
            result *= arg
        return round(result, precision)
    elif sym =="/":
        if 0 in args[1:]:
            return "Деление на 0 невозможно"
        else:
            result = args[0]
            for arg in args[1:]:
                result /= arg
            return round(result, precision)
    elif sym == "medium":
        return round(statistics.mean(args), precision)
    elif sym == "variance":
        return round(statistics.variance(args), precision)
    elif sym == "std_deviation":
        return round(statistics.stdev(args), precision)
    elif sym in ["median", "q2"]:
        return round(statistics.median(args), precision)
    elif sym == "q3 - q1":
        q1 = round(statistics.quantiles(args, n=4)[0], precision)
        q3 = round(statistics.quantiles(args, n=4)[2], precision)
        return q3 - q1
    else:
        return "Оператор не поддерживается"

def test_sum_two_int():
    assert calculate("+", 1, 2) == 3
    print("test_sum_two_int passed")
    
def test_minus_neg_n():
    assert calculate("-", 10, 5, 3) == 2
    print("test_minus_neg_n passed")
    
def test_div_by_zero():
    assert calculate("/", 10, 0) == "Деление на 0 невозможно"
    print("test_div_by_zero passed")
    
def test_sum_two_float():
    assert calculate("+", 1.5, 2.5, tolerance=1e-2) == 4.00
    print("test_sum_two_float passed")
    
def test_op2_invalid_type():
    assert calculate("+", 1, "2") == "Ошибка в операндах"
    print("test_op2_invalid_type passed")
    
def test_op1_invalid_type():
    assert calculate("+", "1", 2) == "Ошибка в операндах"
    print("test_op1_invalid_type passed")

def test_convert_precision():
    assert convert_precision(1e-6) == 6
    print("test_convert_precision passed")
    
def test_calculate_with_tolerance():
    assert calculate("+", 1.123456, 2.123456, tolerance=1e-3) == 3.247
    print("test_calculate_with_tolerance passed")
    
# Run the tests
test_sum_two_int()
test_minus_neg_n()
test_div_by_zero()
test_sum_two_float()
test_op2_invalid_type()
test_op1_invalid_type()
test_convert_precision()
test_calculate_with_tolerance()


# Ввод данных
sym = input("Введите символ операции (+, -, *, /, medium, variance, std_deviation, median, q2, q3 - q1): ")
args = list(map(float, input("Введите числа через пробел: ").split()))
tolerance = float(input("Введите точность вычислений (например, 1e-6): "))

# Вычисление и вывод результата
result = calculate(sym, *args, tolerance=tolerance)
print(result)
