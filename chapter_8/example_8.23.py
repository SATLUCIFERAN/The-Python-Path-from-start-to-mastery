
class Book:
    def __init__(self, title):
        self.title = title

    def __eq__(self, other):
        return self.title == other.title

b1 = Book("1984")
b2 = Book("1984")
print(b1 == b2) # True



