inventory = {"apples": 0,  "oranges": 0, "bananas": 0}
purchases = ["apples", "bananas", "apples", "oranges", "apples"]
for item in purchases:
    inventory[item] += 1

print("Inventory:")
for fruit, count in sorted(inventory.items()):
    print(f"{fruit.title()}: {count}")