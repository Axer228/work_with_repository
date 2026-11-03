import random

number = random.randint(1, 100)

attempts = 0
while True:
    guess = int(input("Ваша догадка: "))
    attempts += 1
    if guess < number:
        print("Больше")
    elif guess > number:
        print("Меньше")
    else:
        print("Угадал!")
        print("Попыток:", attempts)
        break