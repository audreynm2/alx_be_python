class Book:
    """Base class for all books."""

    def __init__(self, title, author):
        """Initialize the title and author."""
        self.title = title
        self.author = author


class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title, author, file_size):
        """Initialize title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    """Derived class representing a printed book."""

    def __init__(self, title, author, page_count):
        """Initialize title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    """Class representing a collection of books (composition)."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books with their details."""
        for book in self.books:
            if isinstance(book, EBook):
                print(
                    f"EBook: {book.title} by {book.author}, "
                    f"File Size: {book.file_size}KB"
                )
            elif isinstance(book, PrintBook):
                print(
                    f"PrintBook: {book.title} by {book.author}, "
                    f"Page Count: {book.page_count}"
                )
            else:
                print(f"Book: {book.title} by {book.author}")
