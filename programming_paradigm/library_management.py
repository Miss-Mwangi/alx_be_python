class Book:
    """Represents a single book in the library."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successfully checked out
        return False  # Already checked out

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successfully returned
        return False  # Already returned

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

class Library:
    """Manages a collection of books."""
    def __init__(self):
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"Checked out: {title}")
                    return
        print(f"Book '{title}' is not available or does not exist.")

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"Returned: {title}")
                    return
        print(f"Book '{title}' is not currently checked out or does not exist.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
