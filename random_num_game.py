import random

num = random.randint(1, 20)
attempts = 0
guess = None

while num != guess:
    guess = int(input("Enter a number between 1 and 20: "))
    attempts += 1
    print(attempts)
    if num > guess:
        print("Guess is lower than the random numbe 0 ")
    elif num < guess:
        print("Guess is higher than the random number")
    else:
        if attempts <= 5:
            print("You won the game")
        else:
            print("You must guess the number within 5 attempts to win")
