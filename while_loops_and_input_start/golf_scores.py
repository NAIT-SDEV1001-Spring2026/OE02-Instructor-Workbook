print("Golf Score Calculator")
total = 0
count = 0
# active = True

while True:
    score = input("What was your most recent golf score? (enter 'q' to quit): ")
    if score == 'q':
        # active = False
        break
    else:
        count += 1
        total += int(score)

average = int(total)/count
print(f"Your average golf score is {average}.")