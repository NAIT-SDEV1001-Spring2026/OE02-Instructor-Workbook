concert_name = input("What is the name of the concert tonight? ")
has_ticket = input("Do you have a ticket? (y/n) ")
if has_ticket == 'y':
    ticket_type = input("What type of ticket do you have? (VIP or Standard) ")

if not has_ticket == 'y':
    print("You need a ticket to get in, sorry!")
elif concert_name == "Taylor Swift" and ticket_type == "VIP":
    print("You're in the right place!")
    print("Have fun VIP!")
elif concert_name == "Taylor Swift" and ticket_type == "Standard":
    print("You're in the right place!")
    print("Enjoy the show!")
elif concert_name == "Rise Against":
    print("That concert is next door")
elif concert_name == "Taylor Swift":
    print("This Code will never run.")
else:
    print("This is not the concert you are looking for")


# number_input = input("Give me a number between 1 and 10: ")

# if int(number_input) >= 7:
#     print("High Score!")
# elif int(number_input) >= 4:
#     print("Medium Score!")
# elif int(number_input) >= 3:
#     print("Weird Score!")
# else:
#     print("Low Score!")