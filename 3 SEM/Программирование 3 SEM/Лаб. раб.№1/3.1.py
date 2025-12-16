#Функция проводит арифметическую операцию над двумя числами. Возможные операции "+" ,"-","","/"
def calculate (a,b, sym):
    if not isinstance(a, (int, float)):
        return "Ошибка в первом операнде"
    if not isinstance(b, (int, float)):
        return "Ошибка во втором операнде"
    
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

#Тест
def test_sum_two_int():
    assert calculate(1, 2, "+") == 3, "Неверная сумма"
    print("test_sum_two_int passed")

def test_minus_neg_n():
    assert calculate(1, -1, "-") == 2, "Вычитание отрицательных чисел (по сути - сложение)"
    print("test_minus_neg_n passed")

def test_div_by_zero():
    assert calculate(10, 0, "/") == "Деление на 0 невозможно", "Деление на ноль"
    print("test_div_by_zero passed")

def test_sum_two_float():
    assert calculate(1.0, 1.0, "+") == 2.0, "Неверная сумма чисел с плавающей точкой"
    print("test_sum_two_float passed")

def test_op2_invalid_type():
    assert calculate(1, "0","+") == "Ошибка во втором операнде", "тип операнда int или float"
    print("test_op2_invalid_type passed")

def test_op1_invalid_type():
    assert calculate("1", 0,"+") == "Ошибка в первом операнде", "тип операнда int или float"
    print("test_op1_invalid_type passed")
#Тест
test_sum_two_int()
test_minus_neg_n()
test_div_by_zero()
test_sum_two_float()
test_op2_invalid_type()
test_op1_invalid_type()

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
sym = input("Введите символ операции (+, -, *, /): ")


result = calculate(a, b, sym)
print(result)