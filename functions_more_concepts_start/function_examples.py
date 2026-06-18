def pet_info(name, breed):
    print(f'Your pet is a {breed} and their name is {name}.')

animal = ('Fluffy', 'parrot')
pet_info(*animal)

pet = {"name": "Fred", "breed": "Cat"}
pet_info(**pet)