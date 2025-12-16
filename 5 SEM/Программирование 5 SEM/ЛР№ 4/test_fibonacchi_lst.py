import pytest
from fibonacchi_lst import FibonacchiLst


def test_fibonacchi_lst_basic():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    fib_iterator = FibonacchiLst(lst)
    result = list(fib_iterator)
    assert result == [0, 1, 2, 3, 5, 8, 1], f"Expected [0, 1, 2, 3, 5, 8, 1], but got {result}"


def test_fibonacchi_lst_no_fib_elements():
    lst = [4, 6, 10]
    fib_iterator = FibonacchiLst(lst)
    result = list(fib_iterator)
    assert result == [], f"Expected [], but got {result}"

def test_fibonacchi_lst_only_fib_elements():
    lst = [0, 1, 2, 3, 5, 8]
    fib_iterator = FibonacchiLst(lst)
    result = list(fib_iterator)
    assert result == [0, 1, 2, 3, 5, 8], f"Expected [0, 1, 2, 3, 5, 8], but got {result}"


def test_fibonacchi_lst_large_input():
    lst = [i for i in range(1000)]
    fib_iterator = FibonacchiLst(lst)
    result = list(fib_iterator)
    expected = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
    assert result == expected, f"Expected {expected}, but got {result}"

if __name__ == "__main__":
    pytest.main()
