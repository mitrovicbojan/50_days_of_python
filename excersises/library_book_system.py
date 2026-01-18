'''
Library Book System

Create two classes: Book and Library.

Book

Attributes: title, author, is_checked_out (default False).
Methods: check_out(), return_book(), __str__().

Library

Attribute: books → list of Book objects.
Methods:
add_book(book) → adds book to library.
list_books() → prints all books with status.
check_out_book(title) → finds book by title and marks it as checked out.
return_book(title) → finds book by title and marks it as returned.
'''

class Book:
    def __init__(self, title, author, is_checked_out=False):
        self.title = title
        self.author = author
        self.is_checked_out = is_checked_out

    def check_out(self):
        self.is_checked_out = True
        return self.is_checked_out
        
    def return_book(self):
        self.is_checked_out = False
        return self.is_checked_out
        
    def __str__(self):
        book_details = f"Title: {self.title}\nAuthor: {self.author}\nIs checked out: {self.is_checked_out}\n"
        return book_details
        
        
class Library:
    def __init__(self, books):
        self.books = books if books is not None else []
        
    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be added.")
        self.books.append(book)
        
    def list_books(self):
        return [
            {"Title": book.title, 
             "Author": book.author, 
             "Checked-out": book.is_checked_out} for book in self.books
        ]
    
    def check_out_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_checked_out == False:
                    book.check_out()
                    return True
                else:
                    return False
        return False
        
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_checked_out == True:
                    book.return_book()
                    return True
                else:
                    return False
        return False
    
    def available_books(self):
        available = []
        for book in self.books:
            if book.is_checked_out == False:
                available.append({"Title": book.title,"Author": book.author, })            
        
        if len(available) == 0:
            return "No available books."
        else:
            return available
        
    def checked_out_books(self):
        unavailable = []
        for book in self.books:
            if book.is_checked_out:
                unavailable.append({"Title": book.title,"Author": book.author, })
        return unavailable