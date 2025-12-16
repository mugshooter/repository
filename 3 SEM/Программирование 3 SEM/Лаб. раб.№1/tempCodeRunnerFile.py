def calculate (a,b, sym):#Функция проводит арифметическую операцию над двумя числами. Возможные операции "+" ,"-","*","/"
    if sym =="+":
        return a + b
    elif sym =="-":
        return a - b
    elif sym =="*":
        return a * b
    elif sym =="/":
        if b ==0:
            return "Деление на 0 невозможно"
        else:
            return a/b
    else:
        return "Оператор не поддерживается"


def test_sum_two_int():
    assert calculate(1, 2, "+") == 3, "Неверная сумма"


def test_minus_neg_n():
    assert calculate(1, -1, "-") == 2, "Вычитание отрицательных чисел (по сути - сложение)"


def test_div_by_zero():
    assert calculate(10, 0, "/") == "деление на ноль невозможно", "Деление на ноль"


def test_sum_two_float():
    assert calculate(1.0, 1.0, "+") == 2.0, "Неверная сумма чисел с плавающей точкой"


def test_op2_invalid_type():
    assert calculate(1, "0","+") == "ошибка во втором операнде", "тип операнда int или float"


def test_op1_invalid_type():
    assert calculate("1", 0,"+") == "ошибка в первом операнде", "тип операнда int или float"
#Тест
#test_sum_two_int()
#test_minus_neg_n()
#test_div_by_zero()
#test_sum_two_float()
#test_op2_invalid_type()
#test_op1_invalid_type()

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
sym = input("Введите символ операции (+, -, *, /): ")

result = calculate(a, b, sym)
print(result)
