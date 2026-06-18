def make_pizza(*toppings, size=None, crust=None, **kwargs):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with " +
          crust + " crust.")
    print("The toppings are:")
    # note here that toppings is a tuple that you can loop through
    # you can also insert a breakpoint here to see exactly what it is.
    for topping in toppings:
        print("- " + topping)

    if kwargs:
        print("Special instructions for the pizza are:")
        for key, value in kwargs.items():
            print(f' - {key}: {value}')
    
if __name__ == "__main__":
    make_pizza('cheese', size=16, crust='thin', cheese="double")
    make_pizza('pepperoni', 'mushroom', crust='thick', size=12)
    make_pizza('pineapple', 'ham', 'ricotta', size=18, crust='medium', ham="extra", ricotta="extra")