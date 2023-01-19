class Book1:
    def __init__(self, pages):
        self.pages = pages
    
    def __add__(self, book):
        return self.pages + book.pages
    
    def __gt__(self, book):
        return self.pages > book.pages

class Book2:
    def __init__(self, pages):
        self.pages = pages
    
    def __gt__(self, book):
        return self.pages < book.pages

b1 = Book1(20)
b2 = Book2(40)
print(b1 + b2)
print(b1 > b2)
print(b2 > b1)
