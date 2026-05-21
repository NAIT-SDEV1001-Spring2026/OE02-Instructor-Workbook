letter_grade = input("Enter your letter grade (eg: A, B+, C-): ")

letter_grade = letter_grade.upper()

match letter_grade:
    case "A" | "A+" | "A-":
        gpa = 4.0
    case "B" | "B+" | "B-":
        gpa = 3.3
    case "C" | "C+" | "C-":
        gpa = 2.5
    case "D":
        gpa = 2.0
    case "F":
        gpa = 1.0
    case _:
        print("Could not determine numeric grade.")
        gpa = 0.0

print(f"Your GPA is {gpa}")