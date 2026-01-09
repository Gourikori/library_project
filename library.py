class Library:
    def __init__(self):
        """Initialize an empty library."""
        self.books = []

    def add_book(self, title: str) -> str:
        """Add a book to the library."""
        if title in self.books:
            return "Book already exists"
        self.books.append(title)
        return "Book added"

    def remove_book(self, title: str) -> str:
        """Remove a book from the library."""
        if title in self.books:
            self.books.remove(title)
            return "Book removed"
        return "Book not found"

    def list_books(self):
        """List all books in the library."""
        return list(self.books)
