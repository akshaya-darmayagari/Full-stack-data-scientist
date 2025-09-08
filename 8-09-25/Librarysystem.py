class Library:
    def __init__(self,books):
        self.books=books
    def borrow(self,title):
        if title in self.books and self.books[title]>0:
            self.books[title]-=1
            return "You borrowed "+title
        else:
            return "Book not available"
    def return_book(self,title):
        self.books[title]+=1
        return "You returned "+title
    def show_books(self):
        return "Available books: "+str(self.books)
lib=Library({"Python 101": 3, "Data Science": 2})
print(lib.borrow("Python 101"))
print(lib.return_book("Data Science"))
print(lib.show_books())