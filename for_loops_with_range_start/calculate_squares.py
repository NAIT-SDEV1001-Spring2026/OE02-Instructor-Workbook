# Only save the start value when it is an integer
while True:
    try:
        start_value = int(input('Enter the value to start at: '))
        break
    except ValueError:
        print('Invalid input. You must provide an integer.')

# Only save the stop value when it is an integer
while True:
    try:
        stop_value = int(input('Enter the value to stop at: '))
        break
    except ValueError:
        print('Invalid input. You must provide an integer.')

step_choice = input('Would you like to add a step value? (Y/N): ')

if step_choice == 'Y':
    # Only save the step value when it is an integer
    while True:
        try:
            step_value = int(input('Enter the value for steps: '))
            break
        except ValueError:
            print('Invalid input. You must provide an integer.')

print("Calculating squares for the provided range:")

# If using a negative step to go backwards, the start value must be higher
# than the stop value
for number in range(start_value,stop_value,step_value):
    print(f'iteration: {number} has a square of {number ** 2}')