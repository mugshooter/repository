n = int(input())
seconds = n % (24 * 3600)
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60
print(f'Часы: {hours} Минуты: {minutes} Секунды: {seconds}')