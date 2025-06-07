
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int

book1 = Book("1984", "George Orwell", 328)
print(book1)  

# Book(title='1984', author='George Orwell', pages=328)

