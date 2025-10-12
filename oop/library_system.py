class Book:
    """Base class for all books."""

    def __init__(self, title, author):
        """Initialize the title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title, author, file_size):
        """Initialize title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the ebook."""
        return (
            f"EBook: {self.title} by {self.author}, "
            f"File Size: {self.file_size}KB"
        )


class PrintBook(Book):
    """Derived class representing a printed book."""

    def __init__(self, title, author, page_count):
        """Initialize title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the print book."""
        return (
            f"PrintBook: {self.title} by {self.author}, "
            f"Page Count: {self.page_count}"
        )


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
            print(book)
