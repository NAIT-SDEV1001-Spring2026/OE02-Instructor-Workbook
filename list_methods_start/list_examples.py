# books = ["1984", "Brave New World", "Fahrenheit 451"]

# print("Books to read:")
# for book in books:
#     print(f"Don't forget to read: {book}")


# months = ["January", "February", "March"]
# winter_months = ("December", "January", "February")

# months[0] = "April"

# for month in months:
#     if month in winter_months:
#         print(f"{month} is a winter month")
#     else:
#         print(f"{month} is not a winter month")

# students = ["Alice", "Bob", "Charlie"]

# for idx, student in enumerate(students):
#     print(f"Student {idx + 1}: {student}")

# numbers = [1, 2, 3, 4, 5]
# for n in numbers:
#     if n % 2 == 0:
#         continue # Skip even numbers
#     print(f"Odd number: {n}")

pets = ["dog", "cat", "parrot", "hamster"]
for pet in pets:
    if pet == "parrot":
        print("Found a parrot! Stopping search.")
        break
    print(f"Checked: {pet}")