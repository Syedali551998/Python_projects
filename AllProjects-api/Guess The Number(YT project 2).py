import random

def guess(x):
    random_numbers = random.randint(1,x)
    guess = 0
    while guess!=random_numbers:
        guess = int(input("Guess a Number between 1 to 20:"))
        if guess<random_numbers:
            print('Sorry, Guess again. Too low')
        elif guess>random_numbers:
            print('Sorry, guess again. Too high')
    print(f"Congrats! You have guessed the number{random_numbers} correctly")
guess(20)


