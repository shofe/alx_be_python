# Base Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}"
    
    def __str__(self):
        return self.get_details


# Derived Class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__ (self):
        return f"{super().get_details()}, File Size: {self.file_size}MB"


    def __str__(self):
        return self.get_details

# Derived Class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().get_details()}, Pages: {self.page_count}"


    def __str__(self):
        return self.get_details

# Composition Class: Library
class Library:
    def __init__(self):
        self.books = []  # stores instances of Book, EBook, and PrintBook

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print("A book has been added.")
        else:
            print("Only instances of Book or its subclasses can be added.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nLibrary Collection:")
            for book in self.books:
                print(book.get_details())

