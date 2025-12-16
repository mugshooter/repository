import pytest
from main import calculate, convert_precision  # Импортируем функции из вашего основного файла

def test_sum_two_int():
    assert calculate("+", 1, 2) == 3

def test_minus_neg_n():
    assert calculate("-", 10, 5, 3) == 2

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate("/", 10, 0)

def test_sum_two_float():
    assert calculate("+", 1.5, 2.5, tolerance=1e-2) == 4.00

def test_op2_invalid_type():
    with pytest.raises(ValueError):
        calculate("+", 1, "2")

def test_op1_invalid_type():
    with pytest.raises(ValueError):
        calculate("+", "1", 2)

def test_convert_precision():
    assert convert_precision(1e-6) == 6

def test_calculate_with_tolerance():
    assert calculate("+", 1.123456, 2.123456, tolerance=1e-3) == 3.247
