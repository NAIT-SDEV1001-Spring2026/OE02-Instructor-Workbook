from library_tools.book import Book
from library_tools.library import Library

if __name__ == '__main__':
    print('Welcome to out library App')
    print('--------------------------')
    library = Library("Edmonton Public Library")
    book = Book('The Lord of the Rings', "J.R.R. Tolkien", 1000)
    library.add_book(book)
    library.list_books
