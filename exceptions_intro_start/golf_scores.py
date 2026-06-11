print("Golf Score Calculator")
count = 0
total_score = 0
# removed active variable

while True:
    user_input = input("What was your most recent golf score? (enter 'quit' to stop) ")
    if user_input == 'quit': # quit if the user enters 'quit'
        break
    else: # add the score to the total and increment the count
        try:
            total_score += int(user_input)
        except ValueError as e:
            print(f'Please enter a valid integer. ({e})')
        else:
            count += 1

# use the average.

try:
    average = total_score / count
except ZeroDivisionError:
    print("You didn't enter any scores!")
else:
    print(f"Your average golf score is {average}.")

