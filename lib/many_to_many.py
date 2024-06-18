class Author:
    all = []

    def __init__(self, name) -> None:
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
            
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])

class Book:

    all = []

    def __init__(self, title) -> None:
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]



class Contract:

    all = []

    def __init__(self, author, book, date, royalties) -> None:
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else: 
            raise Exception('Author must be a valid instance of Author')
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if isinstance(value, Book):
            self._book = value
        else: 
            raise Exception('Book must be a valid instance of Book')
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if isinstance(value, str):
            self._date = value
        else:
            raise Exception('Date must be a valid date')
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if isinstance(value, int):
            self._royalties = value
        else:
            raise Exception('Royalties must be an integer')
        
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

        
# author = Author("Name")
# book1 = Book("Title 1")
# book2 = Book("Title 2")
# book3 = Book("Title 3")

# Contract(author, book1, "01/01/2001", 10)
# Contract(author, book2, "01/01/2001", 20)
# Contract(author, book3, "01/01/2001", 30)

# Author.total_royalties()

# breakpoint()