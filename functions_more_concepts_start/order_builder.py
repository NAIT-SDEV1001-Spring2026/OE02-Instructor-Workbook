from pizza import make_pizza

if __name__ == "__main__":
    ordering_pizza = True
    pizzas = []
    while ordering_pizza:
        ordering = input("Are you done ordering pizzas? (y/n): ")
        if ordering == "y":
            ordering_pizza = False
            continue
        #get the size and crust
        size = int(input("What size pizza would you like? (12, 16, 18): "))
        crust = input("What type of crust would you like? (thin, medium, thick): ")
        #get the toppings:
        toppings = []
        topping = input("What topping would you like? (enter 'done' when finished): ")
        while topping != "done":
            toppings.append(topping)
            topping = input("What topping would you like? (enter 'done' when finished): ")
        # get the special requests.
        special_requests = {}
        while True:
            # show each topping with a number next to it
            print("\nYour toppings:")
            for number, name in enumerate(toppings, start=1):
                print(str(number) + ". " + name)
            
            choice = input("Which topping do you want to modify? (enter the number or 'done'): ")
            if choice == 'done':
                break

            # the user types 1, 2, 3... but list position start at 0
            # so subtract 1 to find the toppings index and get the right topping
            index = int(choice) - 1

            # make sure the number id actually on the list
            if index < 0 or index >= len(toppings):
                print("That number isn't on the list. Try again.")
                continue

            chosen_topping = toppings[index]

            amount = input("How much? (light, extra, double): ")
            special_requests[chosen_topping] = amount

        pizza = {
            "toppings": toppings,
            "size": size,
            "crust": crust,
            "special_requests": special_requests
        }
        pizzas.append(pizza)

    for pizza in pizzas:
        make_pizza(
            *pizza["toppings"],
            size=pizza["size"],
            crust=pizza["crust"],
            **pizza["special_requests"]
        )