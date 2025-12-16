text = input()
nospace = text.replace(' ', '')
print(f"Количество пробелов: {text.count(' ')}, количество других символов:{len(nospace)}")