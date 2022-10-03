import random


def guess(x):
    rand_num = random.randint(1, x)
    guess = 0
    while guess != rand_num:
        print(rand_num)
        guess = int(input(f"Guess a number between 1 and {str(x)}: "))
        if guess < rand_num:
            print("Sorry your number was too low. Guess again")
        elif guess > rand_num:
            print("Sorry your number was too high. Guess again")
    print(f"Yay!! You guessed the number {str(rand_num)} correctly 😀")

guess(10)
