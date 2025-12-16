def guess_number(goal,min,max):
    n=0
    while min <= max:
        guess = (min+max)//2
        n += 1
        if guess == goal:
            return guess, n
        elif guess < goal:
            min = guess + 1
        else:
            max = guess -1
    return None, n



goal = 42
min = 1
max = 100
guess, n = guess_number(goal, min, max)
print(f"Угаданное число: {guess}, количество попыток: {n}")
