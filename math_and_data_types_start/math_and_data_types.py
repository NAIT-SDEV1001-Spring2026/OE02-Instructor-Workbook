name = "Alice"
print(f"Hello {name}")

# learning about numbers
days_until_assignment_due = 17  # int
assignment_completion_percentage = 25.5  # float
print(f"Assign due in {days_until_assignment_due} days")
print(f"Assignment completion: {assignment_completion_percentage}%")

print("==============================")
# Learning about Math

# subtraction example
days_playing_video_games = 2
days_until_due_running_total = days_until_assignment_due - days_playing_video_games
print(f"Days spent playing video games: {days_playing_video_games}")
print(f"Assignment due in: {days_until_assignment_due - days_playing_video_games} days")

# addition example
time_machine_days_added = 3
# augmented assignment operator
# automatically + what is to the right of the = to what is to the left
# Just one example
days_until_due_running_total += time_machine_days_added
print(f"Days added by the time machine: {time_machine_days_added}")
print(
    f"Assignment due in: {days_until_assignment_due + time_machine_days_added} days (only time machine)"
)

# combined example
print(
    f"Assignment Due in: {days_until_assignment_due - days_playing_video_games + time_machine_days_added} days"
)

# multiplication Example
time_warp_multiplier = 2
days_until_due_running_total = days_until_due_running_total * time_warp_multiplier
print(f"Time Warp Multiplier: {time_warp_multiplier}")
print(f"Assignment due in: {days_until_due_running_total} percieved total days")

# Division Example
slowing_spell_divisor = 7
print(f"Instructor Typing slowly spell {slowing_spell_divisor} times")
days_until_due_running_total = days_until_due_running_total // slowing_spell_divisor
print(
    f"Results of the divisions using the slowing spell is {days_until_due_running_total} days!"
)

# Modulus Example
days_even_or_odd = days_until_due_running_total % 2
# reassigning the value as true or false by checking if the days_even_or_odd is equal to 0
days_even_or_odd = days_even_or_odd == 0
print(f"The total days remaining is even, this is {days_even_or_odd}!")

## Exponent Example
days_until_due_running_total = days_until_due_running_total**2
print(
    f"Days until due with a special squaring power is: {days_until_due_running_total} days!"
)

## Lets put it all together!
days_until_assignment_due_total = (
    (days_until_assignment_due - days_playing_video_games + time_machine_days_added)
    * time_warp_multiplier
    // slowing_spell_divisor
) ** 2

print(
    f"Putting it all together the final due date is: {days_until_assignment_due_total} days!"
)
