class Library:
    def __init__(self):
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
        return self.books


def main():
    lib = Library()
    while True:
        print("\n=== Library Menu ===")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            title = input("Enter book title: ").strip()
            print(lib.add_book(title))
        elif choice == "2":
            title = input("Enter book title: ").strip()
            print(lib.remove_book(title))
        elif choice == "3":
            print("Books in library:", lib.list_books())
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()