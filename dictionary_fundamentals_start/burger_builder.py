# burger dictionary
burger = {
    'patties': 1,
    'patty_type': 'beef',
    'cheese': True,
    'toppings': ['lettuce', 'tomato', 'onion', 'pickles', 'ketchup', 'mustard'],
    'bun': 'sesame seed'
}

# change the values!
burger['patties'] = 2
burger['cheese'] = False
burger['toppings'].append('relish')

print('Here is what is in your burger. Enjoy!')
print(f'{burger['patties']} {burger['patty_type']} patties are on your burger.')
print(f'Your burger has a {burger["bun"]} bun.')
if burger['cheese']:
    print('Cheese is on your burger.')
else:
    print('No cheese on your burger.')

print('Here is a list of the topping selected:')
for topping in burger['toppings']:
    print(f'- {topping}')

print(f'You must really like {burger['toppings'][0]}, cause you picked it first!')

gluten_allergy = burger.get('gluten_allergy', False)
if gluten_allergy:
    print('We have removed the gluten from your burger!')

if 'tomato_allergy' in burger:
    if burger['tomato_allergy']:
        print("We have removed the tomatoes from the burger.")
    else:
        print('We have added tomatoes to the burger.')

burger_menu = {
    "classic" : { "price": 8.99, "calories": 650 },
    "veggie" : { "price": 7.99, "calories": 450 }
}

print(f'Would you like this as a classic burger for ${burger_menu["classic"]['price']}?')