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