# Only save the start value when it is an integer
def get_int_from_user(message):
    while True:
        try:
            user_input = int(input(f'{message}'))
            break
        except ValueError:
            print('Invalid input. You must provide an integer.')
    return user_input 

start_value = get_int_from_user('Enter the value to start at: ')

stop_value = get_int_from_user('Enter the value to stop at: ')

step_choice = input('Would you like to add a step value? (Y/N): ')

if step_choice == 'Y':
    step_value = get_int_from_user('Enter the value for steps: ')

print("Calculating squares for the provided range:")

# If using a negative step to go backwards, the start value must be higher
# than the stop value
for number in range(start_value,stop_value,step_value):
    print(f'iteration: {number} has a square of {number ** 2}')