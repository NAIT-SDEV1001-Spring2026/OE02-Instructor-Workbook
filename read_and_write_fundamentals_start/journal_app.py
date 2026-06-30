# Journal Application
def read_journal(file_path):
    """Read the journal entries from a file."""
    try:
        with open(file_path, 'r') as file:
            # option 1: read all of the file at once
            entries = file.readlines()
        return entries
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except PermissionError:
        print(f"Error: You do not have permission to access {file_path}.")
    except IsADirectoryError:
        print(f"Error: {file_path} is a directory not a file.")
    except OSError as error:
        print(f"Error: Count not read the file ({error})")
    return None

def write_journal(file_path, entry):
    """Write a journal entry to a file."""
    clean_entry = entry.strip()
    if not clean_entry:
        print("Error: Cannot save an empty entry")
    else:
        try:
            with open(file_path, 'a') as file:  # 'a' mode to append
                file.write(F"{entry}\n")
        except PermissionError:
            print(f"Error: You do not have permission to access {file_path}.")
        except IsADirectoryError:
            print(f"Error: {file_path} is a directory not a file.")
        except OSError as error:
            print(f"Error: Count not read the file ({error})")
    
def main():
    file_path = 'journal.txt'
    while True:
        action = input("Do you want to (r)ead the journal or (w)rite a new entry? (q to quit): ").lower()
        if action == "r":
            entries = read_journal(file_path)
            if entries != None:
                print(f'Journal Entries of {file_path}: \n')
                for index, entry in enumerate(entries):
                    print(f"{index + 1}. {entry}")
        elif action == "w":
            new_entry = input("Enter your journal entry: ")
            write_journal(file_path, new_entry)
        elif action == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
        

if __name__ == "__main__":
    main()