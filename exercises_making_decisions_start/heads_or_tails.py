import random

user_guess = input("Guess the coin flip! Enter heads or tails (h/t): ")
coin_flip = random.randint(0, 1)

if coin_flip == 0:
    flip_result = "heads"
else:
    flip_result = "tails"

print(f"The coin flip was: {flip_result}")

if flip_result == "heads" and user_guess == "h":
    print("you guessed correct!")
elif flip_result == "heads" and user_guess == "t":
    print("you guessed wrong!")
elif flip_result == "tails" and user_guess == "t":
    print("you guessed correct!")
else:
    print("you guessed wrong!")