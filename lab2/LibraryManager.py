# LibraryManager.py

class LibraryManager:
    def __init__(self):
        self.books = {}  # Dictionary to store books with ISBN as the key

    def add_book(self, title, author, publisher, volume, year, isbn):
        """Add a book to the library."""
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
        else:
            self.books[isbn] = {
                'title': title,
                'author': author,
                'publisher': publisher,
                'volume': volume,
                'year': year,
                'isbn': isbn
            }
            print(f"Book with ISBN {isbn} added successfully.")

    def remove_book(self, isbn):
        """Remove a book from the library by its ISBN."""
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} removed successfully.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def retrieve_book(self, isbn):
        """Retrieve and display the details of a book using its ISBN."""
        book = self.books.get(isbn)
        if book:
            return book
        else:
            print(f"Book with ISBN {isbn} not found.")
            return None

    def search_books(self, title=None, author=None):
        """Search for books by title or author."""
        results = []
        for book in self.books.values():
            if (title and title.lower() in book['title'].lower()) or (author and author.lower() in book['author'].lower()):
                results.append(book)
        return results

    def list_books(self):
        """List all books currently in the library."""
        return list(self.books.values())

    def update_book(self, isbn, **kwargs):
        """Update the details of an existing book."""
        if isbn in self.books:
            self.books[isbn].update(kwargs)
            print(f"Book with ISBN {isbn} updated successfully.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def check_availability(self, isbn):
        """Check if a book is available in the library by its ISBN."""
        return isbn in self.books
