# numbers = list(range(1,6))
# numbers_range = range(1,6)

# counter = 1
# while counter <= 3:
#     print(f"Attempt {counter}")
#     counter += 1

# print("Enter numbers to add. Type 'done' to finish.")
# total = 0
# while True:
#     value = input("Enter a number: ")
#     if value == "done":
#         break
#     total += int(value)
# print(f"Total sum: {total}")

count = 0
total = 0
more_scores = True
while more_scores:
    score = input("Enter a test score (or 'q' to quit): ")
    if score == "q":
        more_scores = False
    total += int(score)
    count += 1
if count > 0:
    print("Average score:", total / count)
else:
    print("No scores entered.")