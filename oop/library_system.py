# Base class - Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

# Derived class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author) # Call the __init__ of the base class (Book)
        self.file_size = file_size # EBook specific attribure

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author) #Call the __init__ of the base class (Book)
        self.page_count = page_count #PrintBook specific attribute

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Composition class - Library
class Library:
    def __init__(self):
        self.books = [] # List to store books (Book, EBook, PrintBook instances)

    def add_book(self, book):
        self.books.append(book) # Add a book to the Library

    def list_books(self):
        for book in self.books:
            print(book) # Print the details of each book in the Library
