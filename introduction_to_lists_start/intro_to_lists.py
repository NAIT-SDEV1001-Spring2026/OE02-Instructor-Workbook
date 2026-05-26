# our grocery list.
groceries = ['lettuce', 'tomatoes', 'bread', 'milk', 'chicken', 'apples']
print("Our grocery list is: ", groceries)

print("the first item in our grocery list is:", groceries[0])
print("the third item in our grocery list is:", groceries[2])

groceries[0] = 'romaine lettuce'
groceries[2] = 'baguette'

print("The modified grocery list is: ", groceries)

print("The first three items in our list are:", groceries[0:3])
print("The last two items in our list are:", groceries[-2:])
print(f"The grocery list has {len(groceries)} items.")