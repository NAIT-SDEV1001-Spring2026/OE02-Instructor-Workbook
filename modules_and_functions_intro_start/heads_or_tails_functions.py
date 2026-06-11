import random

def get_coin_flip():
    # heads will be 0 and tails will be 1
    random_number = random.randint(0, 1)
    if random_number == 0:
        print("The coin flip was: heads")
        return "h"
    else:
        print("The coin flip was: tails")
        return "t"

def get_user_guess():
    while True:
        user_input = input("Guess the coin flip! Enter heads or tails (h/t): ")
        if user_input == 'h' or user_input == 't':
            break
        else:
            print("Invalid input. Please type only 'h' or 't'.")
    
    return user_input


user_guess = get_user_guess()

random_flip = get_coin_flip()

if (random_flip == user_guess):
    print("you guessed correct!")
else:
    print("you guessed wrong!")
