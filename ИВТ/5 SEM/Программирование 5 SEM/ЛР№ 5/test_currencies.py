import pytest
from decimal import Decimal
from main import CurrenciesLst  # Импортируем основной модуль

def test_get_currencies_valid_ids():
    """Тест для проверки получения данных по валидным ID валют."""
    cl = CurrenciesLst()
    result = cl.get_currencies(['R01035', 'R01335'])

    assert len(result) > 0, "Список валют должен содержать данные"
    
    gbp = cl.get_valute('GBP')
    assert gbp['GBP'] is not None, "Данные по GBP должны быть получены"
    assert 'Фунт стерлингов' in gbp['GBP'][0], "Название валюты GBP неверно"

    kzt = cl.get_valute('KZT')
    assert kzt['KZT'] is not None, "Данные по KZT должны быть получены"
    assert 'Тенге' in kzt['KZT'][0], "Название валюты KZT неверно"

def test_get_currencies_invalid_id():
    """Тест для проверки обработки некорректного ID валюты."""
    cl = CurrenciesLst()
    result = cl.get_valute('R9999')
    assert result == {'R9999': None}, "Некорректный ID валюты должен возвращать None"

def test_add_valute():
    """Тест для проверки добавления новой валюты."""
    cl = CurrenciesLst()
    cl.add_valute('USD', 'Доллар США', '98,7565')
    usd = cl.get_valute('USD')

    assert usd['USD'] is not None, "Данные по USD должны быть добавлены"
    assert usd['USD'][0] == 'Доллар США', "Название валюты USD неверно"
    assert Decimal(usd['USD'][1][0] + '.' + usd['USD'][1][1]) == Decimal('99.7565'), "Курс валюты USD неверен"

def test_visualize_currencies(mocker):
    """Тест для проверки визуализации курсов валют."""
    cl = CurrenciesLst()
    cl.add_valute('USD', 'Доллар США', '98,7565')
    cl.add_valute('EUR', 'Евро', '104,2543')

    mocker.patch("matplotlib.pyplot.show")  # Патчим plt.show() чтобы не отображать график
    cl.visualize_currencies()
    
    # Проверяем, что визуализация выполняется без ошибок
    assert True

if __name__ == "__main__":
    pytest.main()
