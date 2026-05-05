student_grades = [88, 65, 91, 72, 98]

print("Our student grades are: ")
print(student_grades)

print("Our student grades sorted are: ")
student_grades.sort(reverse=True)
print(student_grades)

# Let's add 100 to the student grades.
student_grades.append(100)
student_grades.insert(2,50)
print("After we've added grades, the new list is: ")
print(student_grades)

# Let's remove a few items from the list.
student_grades.pop(3) # remove at index 2
student_grades.remove(98) # remove the value 98 from the list.
print("After we've removed grades, the new list is: ")
print(student_grades)

# Show students the value error on the next line.
# student_grades.remove(9001)

print("Has a student got a perfect grade?")
print(100 in student_grades)
print("Has a student gotten a 0 in the course?")
print(0 in student_grades)

# pop() returns the removed item; remove() does not.
removed_grade = student_grades.pop()
print("The grade we removed was:", removed_grade)

# Safely remove an item using `in` as a guard.
grade_to_remove = 50
if grade_to_remove in student_grades:
    student_grades.remove(grade_to_remove)
    print(grade_to_remove, "was removed from the list.")
else:
    print(grade_to_remove, "is not in the list, nothing to remove.")

# More list methods — fresh list to keep output clean.
student_grades = [88, 65, 91, 72, 88, 98]
print("Number of grades:", len(student_grades))
print("Index of 91:", student_grades.index(91))
print("Times 88 appears:", student_grades.count(88))
student_grades.clear()
print("After clear:", student_grades)