from LibraryManager import LibraryManager


library = LibraryManager()

books_data = [
    ('Operating Systems: Three Easy Pieces', 'Remzi H. Arpaci-Dusseau', 'Arpaci-Dusseau', '1st', 2020, '978-1600077929'),
    ('Introduction to Algorithms', 'Thomas H. Cormen', 'MIT Press', '4th', 2022, '978-0262038448'),
    ('Machine Learning Yearning', 'Andrew Ng', 'Self-Published', 'N/A', 2022, '978-0999735204'),
    ('Deep Learning with Python', 'François Chollet', 'Manning Publications', '1st', 2021, '978-1617294433'),
    ('Data Structures and Algorithm Analysis in C++', 'Mark Allen Weiss', 'Pearson', '4th', 2021, '978-0132847377'),
   
]


for book in books_data:
    library.add_book(*book)

# Remove a book
library.remove_book('978-0999735204')

# Retrieve details of a book
book_details = library.retrieve_book('978-1600077929')
print("Book Details:", book_details)

# Search for books by title
search_results = library.search_books(title='Machine Learning')
print("Search Results by Title:", search_results)

# Search for books by author
search_results = library.search_books(author='Thomas H. Cormen')
print("Search Results by Author:", search_results)

# List all books in the library
all_books = library.list_books()
print("All Books:", all_books)

# Update a book's details
library.update_book('978-1600077929', title='Operating Systems: Modern Perspectives')

# Check availability of a book
is_available = library.check_availability('978-1600077929')
print("Is book available?", is_available)
