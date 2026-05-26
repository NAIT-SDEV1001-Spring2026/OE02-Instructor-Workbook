# animals = ['cat', 'dog', 'rabbit']
# print("First animal:", animals[0])
# print("Last animal:", animals[-1])
# print("Middle animal:", animals[1])
# animals[1] = 'more cats!'
# print("Middle animal:", animals[1])

letters = ['a', 'b', 'c', 'd', 'e']
print("First three letters:", letters[:3])
print("Last two letters:", letters[-2:])
print("Middle letters:", letters[1:4])
print("List Length:", len(letters))
# Remember len is 5 here, but the highest index is 4 cause the counting starts at 0
print("This be broke:", letters[len(letters)])
print("This not broke:", letters[len(letters)-1])
