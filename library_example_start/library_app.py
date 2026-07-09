from library_tools.book import Book
from library_tools.library import Library

if __name__ == '__main__':
    print('Welcome to out library App')
    print('--------------------------')
    library = Library("Edmonton Public Library")
    library.list_books()
    print('--------------------------')
    book = Book('The Lord of the Rings', "J.R.R. Tolkien", 1000)
    bookTwo = Book("The Wheel of Time", "Robert Jordan", 690)
    bookThree = Book("The Way of Kings", "Brandon Sanderson", 1200)
    bookFour = Book("Mistborn", "Brandon Sanderson", 640)
    library.add_book(book)
    library.add_book(bookTwo)
    library.add_book(bookThree)
    library.add_book(bookFour)
    library.list_books()
    result = library.find_book('Mistborn')
    if result is None:
        print('Book not Found')
    else:
        print(f"Found: {result}")

    result = library.find_book('Not a Book')
    if result is None:
        print('Book not Found')
    else:
        print(f"Found: {result}")
