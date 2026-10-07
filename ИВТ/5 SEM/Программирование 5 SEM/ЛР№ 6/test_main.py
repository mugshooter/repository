import pytest
from main import CurrenciesList, ConcreteDecoratorJSON, ConcreteDecoratorCSV
import json


def test_currencies_list_valid_structure():
    """
    Проверяет, что возвращаемый результат соответствует ожидаемой структуре.
    """
    currencies = CurrenciesList()
    result = currencies.get_currencies(['R01035', 'R01335'])

    assert isinstance(result, dict), "Результат должен быть словарем"
    for char_code, info in result.items():
        assert isinstance(char_code, str), "Код валюты должен быть строкой"
        assert isinstance(info, dict), "Информация о валюте должна быть словарем"
        assert 'name' in info, "Информация должна содержать ключ 'name'"
        assert 'rate' in info, "Информация должна содержать ключ 'rate'"
        assert isinstance(info['rate'], tuple), "Курс должен быть представлен в виде кортежа"
        assert len(info['rate']) == 2, "Курс должен содержать целую и дробную части"


def test_currencies_list_empty_request():
    """
    Проверяет, что при пустом списке ID возвращается пустой словарь.
    """
    currencies = CurrenciesList()
    result = currencies.get_currencies([])
    assert result == {}, "Для пустого списка ID должен возвращаться пустой словарь"


def test_currencies_list_invalid_structure():
    """
    Проверяет, что обработка неправильных ID валют не ломает структуру результата.
    """
    currencies = CurrenciesList()
    result = currencies.get_currencies(['INVALID_ID'])
    assert isinstance(result, dict), "Результат должен быть словарем"
    assert result == {}, "Для несуществующих ID результат должен быть пустым словарем"


def test_json_decorator_output_format():
    """
    Проверяет, что JSON-декоратор возвращает корректно форматированный JSON.
    """
    currencies = CurrenciesList()
    json_decorator = ConcreteDecoratorJSON(currencies)
    result = json_decorator.get_currencies(['R01035', 'R01335'])

    try:
        data = json.loads(result)
        assert isinstance(data, dict), "Результат JSON-декоратора должен быть словарем после парсинга"
    except json.JSONDecodeError:
        pytest.fail("JSON-декоратор вернул некорректный JSON")


def test_currencies_list_invalid_url_handling():
    """
    Проверяет, что метод корректно обрабатывает недоступный URL.
    """
    currencies = CurrenciesList()
    currencies_list_invalid_url = 'http://invalid.url'

    try:
        result = currencies.get_currencies(['R01035', 'R01335'])
        assert isinstance(result, dict), "Результат должен быть словарем даже при ошибке запроса"
    except Exception:
        pytest.fail("Метод должен корректно обрабатывать ошибки запросов")