# Task_2 Library

class Author:                                                    # презентує автора
    
    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []                                         # власн книги автора

    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}', birthday='{self.birthday}')"

    def __str__(self):
        return f"{self.name} ({self.country}, born {self.birthday})"


class Book:                                                      # презентує книги авторів
   
    total_books = 0                                              # змінна для підрахунку книг

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        if not isinstance(author, Author):                        # екземпляри
            raise ValueError("author must be an instance of Author class")
        self.author = author
        Book.total_books += 1
        author.books.append(self)                                 # link на книгу з її автором

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author='{self.author.name}')"

    def __str__(self):
        return f"'{self.name}' by {self.author.name} ({self.year})"

class Library:                                                  # презентує бібліотеку з книгами та авторами    
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):   # "створює нову книгу та додає до бібл-ки
       
        new_book = Book(name, year, author)
        self.books.append(new_book)
        if author not in self.authors:
            self.authors.append(author)
        return new_book

    def group_by_author(self, author: Author):                  # повертає список книг написаних авторами 
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):                         # повертає список книг, опублікованих в якийсь рік
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library(name='{self.name}', books={len(self.books)}, authors={len(self.authors)})"

    def __str__(self):
        return f"Library '{self.name}' with {len(self.books)} books and {len(self.authors)} authors."

a1 = Author("J.K. Rowling", "UK", "31 July 1965")
a2 = Author("George R.R. Martin", "USA", "20 September 1948")

library = Library("BT Library")                                                       # створюємо бібліотеку

b1 = library.new_book("Harry Potter and the Philosopher's Stone", 1997, a1)             # додаємо книги
b2 = library.new_book("Harry Potter and the Chamber of Secrets", 1998, a1)
b3 = library.new_book("A Game of Thrones", 1996, a2)

print(library.group_by_author(a1))
print(library.group_by_year(1998))

print(library)                                                                          # загальна інформація
print(f"Total books created: {Book.total_books}")