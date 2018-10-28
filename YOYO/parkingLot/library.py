
class Library:

    def __init__(self):
        self.bookcase = []

    def putting_book(self,book):
        if book is type(Book):
            self.bookcase.append(book)

    def searching_book(self,book):
        if book in self.bookcase:
            print("The book you search for is available")
        else:
            print("The book you search for is not available")

class Book:
    pass

class Holder:

    def __init__(self,book_list):
        self.book_list = []
        self.book_list.append(book)

Atlanta = Book()
bookcase = Library()
bookcase.putting_book(Atlanta)
bookcase.searching_book(Atlanta)

print(bookcase)
