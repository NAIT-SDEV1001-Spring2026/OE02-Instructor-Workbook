from journal_app import read_journal

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        return None

def write_file(filename, text):
    with open(filename, 'a') as f:
        f.write(text + "\n")

filename = "todo.txt"
while True:
    action = input("Add (a), Read (r), or Quit (q)? ").lower()
    if action == "a":
        item = input("Enter a to-do item: ")
        # If not [string] will also catch blank input when used with .strip() which removes leading and trailing white spaces
        if not item.strip():
            print("Please enter a todo item, cannot be blank.")
        else:
            write_file(filename, item)
    elif action == "r":
        lines = read_file(filename)
        if lines is None:
            print('No todo list entries to show.')
        else:
            for line in lines:
                print("-", line.strip())
    elif action == "q":
        break
    else:
        print("Invalid option. Please enter a, r, or q.")