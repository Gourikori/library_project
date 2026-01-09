from typing import List

class Library:
    def __init__(self):
        """Initialize an empty library."""
        self.books: List[str] = []

    def add_book(self, title: str) -> str:
        """Add a book to the library (case-insensitive duplicate check)."""
        normalized_title = title.strip().lower()
        # Use a list comprehension to compare case-insensitively
        if normalized_title in [book.lower() for book in self.books]:
            return "Book already exists"
        # Store the cleaned original title
        cleaned_title = title.strip()
        if not cleaned_title:
            return "Invalid title"
        self.books.append(cleaned_title)
        return "Book added"

    def remove_book(self, title: str) -> str:
        """Remove a book from the library (case-insensitive)."""
        normalized_title = title.strip().lower()
        for idx, book in enumerate(self.books):
            if book.lower() == normalized_title:
                # Remove by index to avoid issues while iterating
                self.books.pop(idx)
                return "Book removed"
        return "Book not found"

    def list_books(self) -> List[str]:
        """List all books in the library."""
        return list(self.books)  # return a copy


def main():
    lib = Library()
    while True:
        print("\n=== Library Menu ===")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()
        if choice == "1":
            title = input("Enter book title: ").strip()
            print(lib.add_book(title))
        elif choice == "2":
            title = input("Enter book title: ").strip()
            print(lib.remove_book(title))
        elif choice == "3":
            books = lib.list_books()
            if books:
                print("Books in library:", books)
            else:
                print("Library is empty.")
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1–4.")


if __name__ == "__main__":
    main()
