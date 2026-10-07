import pytest
from flask import Flask
from flask_socketio import SocketIO, emit
from threading import Thread
import time
import requests
from main import app, ConcreteSubject, CurrencyObserver

@pytest.fixture
def client():
    """Фикстура для тестирования Flask-приложения."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def socketio_client():
    """Фикстура для тестирования WebSocket соединений."""
    socketio = SocketIO(app, cors_allowed_origins="*")
    return socketio.test_client(app)

def test_index_page(client):
    """Проверяет, что главная страница загружается корректно."""
    response = client.get('/')
    assert response.status_code == 200
    assert '<h1>Курсы обмена валют</h1>'.encode('utf-8') in response.data

def test_currency_observer_updates():
    """Проверяет, что наблюдатели получают обновления от субъекта."""
    subject = ConcreteSubject()

    # Mock для отправки данных
    class TestObserver:
        def init(self):
            self.data = None

        def update(self, data):
            self.data = data

    observer = TestObserver()
    subject.attach(observer)

    # Пример обновления данных
    test_data = {'USD': {'name': 'Доллар США', 'value': '75.00'}}
    subject._rate_data = test_data
    subject.notify()

    assert observer.data == test_data

def test_fetch_rates():
    """Проверяет, что курсы валют корректно запрашиваются из API."""
    subject = ConcreteSubject()

    # Запускаем поток для имитации fetch_rates
    def mock_fetch():
        time.sleep(1)  # Задержка для эмуляции работы
        subject._rate_data = {'USD': {'name': 'Доллар США', 'value': '75.00'}}
        subject.notify()

    thread = Thread(target=mock_fetch, daemon=True)
    thread.start()

    # Подключаем наблюдателя
    class TestObserver:
        def init(self):
            self.data = None

        def update(self, data):
            self.data = data

    observer = TestObserver()
    subject.attach(observer)

    thread.join()  # Ждем завершения потока
    assert observer.data == {'USD': {'name': 'Доллар США', 'value': '75.00'}}