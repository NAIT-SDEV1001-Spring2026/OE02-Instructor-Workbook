# Still need to import another class when we reference that class
from library_tools.book import Book


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        return f"{self.name}"
    
    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print(f"Current books in the {self}:")
        if len(self.books) == 0:
            print("No books in our library")
        for book in self.books:
            print(f"- {book}")
    
    # defined title and said it MUST be a string with : str
    # -> tells the method what MUST be returned
    # Book | None tells the method the return must be a Book OR Nothing
    def find_book(self, title: str) -> Book | None:
        for book in self.books:
            if book.title == title:
                return book
        return None
