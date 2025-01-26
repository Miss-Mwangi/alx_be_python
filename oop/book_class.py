class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the book's title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to print a message when the book is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation of the book in a user-friendly format."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation to recreate the book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
