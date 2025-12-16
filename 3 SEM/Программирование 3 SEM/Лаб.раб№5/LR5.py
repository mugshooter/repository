import random
import time
from pymongo import MongoClient

# 1.1
class RandomNumberIterator:
    def __init__(self, count, range_start, range_end):
        self.count = count
        self.range_start = range_start
        self.range_end = range_end
        self.generated_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated_count < self.count:
            self.generated_count += 1
            return random.randint(self.range_start, self.range_end)
        else:
            raise StopIteration

# 1.2
def random_number_generator(count, range_start, range_end):
    for _ in range(count):
        yield random.randint(range_start, range_end)

# 1.3
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def add_ten_generator(numbers):
    for number in numbers:
        yield number + 10

# 1.4
def find_country(city, country_dict):
    for country, cities in country_dict.items():
        if city in cities:
            return country
    return "Страна не найдена"

# 2.1
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.perf_counter()
        self.interval = self.end - self.start
        print(f"Время выполнения: {self.interval} секунд")

# 2.2
class BatchCalculatorContextManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def calculate(self, expression):
        try:
            return eval(expression)
        except Exception as e:
            return e

2.3
class MongoDBContextManager:
    def __init__(self, hostname="localhost", port=27017, username=None, password=None):
        self.mongo_client = MongoClient(hostname, port, username=username, password=password)

    def __enter__(self):
        return self.mongo_client

    def __exit__(self, exc_type, exc_value, traceback):
        self.mongo_client.close()

# Пример использования 
if __name__ == "__main__":
    # 1.1 и 1.2
    random_iterator = RandomNumberIterator(5, 1, 10)
    for number in random_iterator:
        print(number)

    for number in random_number_generator(5, 1, 10):
        print(number)

    # 1.3
    fib_numbers = fibonacci_generator(10)
    for number in add_ten_generator(fib_numbers):
        print(number)

    # 1.4
    country_dict = {
        "Россия": ["Москва", "Санкт-Петербург"],
        "Франция": ["Париж", "Марсель"],
    }
    cities_to_find = ["Москва", "Марсель", "Берлин"]
    for city in cities_to_find:
        print(f"{city} находится в стране {find_country(city, country_dict)}")

    # 2.1
    with Timer():
        fib_numbers = fibonacci_generator(1000000)
        for _ in fib_numbers:
            pass

    # 2.2
    with BatchCalculatorContextManager('calculations.txt') as bcm:
        for line in bcm.file:
            result = bcm.calculate(line.strip())
            print(f"{line.strip()} = {result}")

    # 2.3
    with MongoDBContextManager(username="myUserAdmin", password="abc123") as client:
        db = client.myshinynewdb
        user_collection = db.user
        ada_lovelace = user_collection.find_one({'age': 205})
        print(ada_lovelace)
