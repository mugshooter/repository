import math
import statistics
import unittest

# Функция для конвертации точности
def convert_precision(tolerance):
    return abs(math.floor(math.log10(tolerance)))

# Функция калькулятора с обработкой исключений
def calculate(sym, *args, tolerance=1e-6):
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise ValueError("Ошибка в операндах")
    
    precision = convert_precision(tolerance)
    
    try:
        if sym == "+":
            return round(sum(args), precision)
        elif sym == "-":
            return round(args[0] - sum(args[1:]), precision)
        elif sym == "*":
            result = math.prod(args)
            return round(result, precision)
        elif sym == "/":
            result = args[0]
            for arg in args[1:]:
                if arg == 0:
                    raise ZeroDivisionError("Деление на 0 невозможно")
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
            raise ValueError("Оператор не поддерживается")
    except Exception as e:
        raise e

# Класс для модульного тестирования с unittest
class TestCalculator(unittest.TestCase):
    def test_sum_two_int(self):
        self.assertEqual(calculate("+", 1, 2), 3)
    
    def test_minus_neg_n(self):
        self.assertEqual(calculate("-", 10, 5, 3), 2)
    
    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate("/", 10, 0)
    
    def test_sum_two_float(self):
        self.assertEqual(calculate("+", 1.5, 2.5, tolerance=1e-2), 4.00)
    
    def test_op2_invalid_type(self):
        with self.assertRaises(ValueError):
            calculate("+", 1, "2")
    
    def test_op1_invalid_type(self):
        with self.assertRaises(ValueError):
            calculate("+", "1", 2)
    
    def test_convert_precision(self):
        self.assertEqual(convert_precision(1e-6), 6)
    
    def test_calculate_with_tolerance(self):
        self.assertEqual(calculate("+", 1.123456, 2.123456, tolerance=1e-3), 3.247)

# Запуск тестов, если файл запущен как основная программа
if __name__ == '__main__':
    unittest.main()
