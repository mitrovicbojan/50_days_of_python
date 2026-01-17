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
        self.books = [books]
        
    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        return self.books
    
    def check_out_book(self, title):
        for i in self.books:
            if title in self.books and self.books[i].is_checked_out() == False:
                i.check_out()
    
    def return_book(self, title):
        pass