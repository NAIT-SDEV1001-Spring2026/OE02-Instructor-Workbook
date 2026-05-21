import random

# Generate a random integer between a range
random_number = random.randint(1, 100)

# Get the user input
user_input = input("Guess a number between 1 and 100: ")
user_guess = int(user_input)

print(F"user guess: {user_guess}")
high_low_input = input("Do you think you are higher or lower than the number? (h/l): ")

print(F"random number: {random_number}")

if user_guess == random_number:
    result = "correct"
elif user_guess >= random_number + 10:
    result = "way high"
elif user_guess <= random_number - 10:
    result = "way low"
elif user_guess > random_number:
    result = "high"
elif user_guess < random_number:
    result = "low"
else:
    result = "error"


if result == "high" and high_low_input == "h":
    print("You are correct, it's high!")
elif result == "way high" and high_low_input == "h":
    print("You are correct, it was way too high!")
elif result == "low" and high_low_input == "l":
    print("You are correct, it's low!")
elif result == "way low" and high_low_input == "l":
    print("You are correct, it was way too low!")
else:
    print("You are wrong, and this is rigged... :(")

# if user_guess == random_number:
#     print("You guessed the number!")
# elif user_guess >= random_number + 10:
#     print("You were way higher than the number!")
# elif user_guess <= random_number - 10:
#     print("You were way lower than the number!")
# elif user_guess > random_number:
#     print("You were higher than the number!")
# elif user_guess > random_number:
#     print("You were lower than the number!")
# else:
#     print("Sorry, I couldn't compute that :(")