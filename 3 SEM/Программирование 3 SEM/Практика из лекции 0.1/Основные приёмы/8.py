n = int(input("Введите количество дней: "))
years = n // 365
months = (n - years * 365) // 30
days = (n - years * 365 - months * 30)
print(f'Годы: {years} Месяцы: {months} Дни: {days}')