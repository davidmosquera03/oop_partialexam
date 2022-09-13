from typing import List

class Book:
    def __init__(self, name) -> None:
        self.name = name
        self.status = "available"
        """
        Class constructor of Book
        name: name of the Book
        status: condition, avaible/borrowed/damaged
        """
        
    def __repr__(self) -> str:
        """
        Shows atrributes of a book
        """
        return (f"'{self.name}' status: {self.status}")

       
class Library:
    def __init__(self) -> None:
        self.Books =[]
        """
        Class constructor of Bookshelf or Library
        Books: list of books in Bookshelf
        """

    def add_list(self, lista: list)->None:
        """
        for each element in list, add Book objects
        """
        for element in lista:
          B= Book(element)
          self.Books.append(B)      
        
    def reset(self, name : str):
        """
        sets a book status back to available
        """
        found = False
        for Book in self.Books:
            if Book.name==name:
                Book.status ="available"
                found = True
        if not found:
            print(name," is not from this Bookshelf")
        
    def lose(self, name : str) -> None:
        """
        sets a book status to lost
        """
        found = False
        for Book in self.Books:
            if Book.name==name:
                Book.status ="lost"
                found = True
        if not found:
            print(name," is not from this Bookshelf")

    def damage(self, name : str) -> None:
        """
        sets a book status to damaged
        """
        found = False
        for Book in self.Books:
            if Book.name==name:
                Book.status ="damaged"
                found = True
        if not found:
            print(name," is not from this Bookshelf")
    
    def remove_list(self, list: List) -> None:
        """
        give damaged or lost books to librarian
        """
        print("libros ahora")
        self.show()
        self.Books = [Book for Book in self.Books if Book.name not in list ]

    def show(self) -> str:
        print(self.Books)


class User:
    def __init__(self) -> None:
        self.user_books=[]

    def borrow_book(self, name: str ,library : Library)->None:
        """
        searches in bookshelf for book
        if it exists and is available, adds it to user list
        and changes status to borrowed
        else, shows it is not found
        """
        found = False
        for Book in library.Books:
            if Book.name==name and Book.status=="available":
                Book.status="borrowed"
                found = True
        if(found):
            self.user_books.append(name)
        else:
            print(name," not found")
            
    def return_book(self,name: str, library : Library)->None:
        """
        If user has a given book, remove from user_books
        and return status on bookshelf to available
        """
        if name in self.user_books:
            self.user_books.remove(name)
            library.reset(name)
        else:
            print("You do not have this book")

    def show(self) -> str:
        """
        Shows the Books of the User
        """
        print(self.user_books)
    
    def avaiable_books(self, library : Library) -> List:
        """
        Shows books with available status from selected Bookshelf
        """
        for x in library.Books:
            if x.status=="available":
                print(x)
    def report_lost(self, name: str, library : Library) -> None:
        """
        changes book status from borrowed to lost
        """
        if name in self.user_books:
            self.user_books.remove(name)
            library.lose(name)
        else:
            print("You do not have this book")

    def report_damaged(self, name: str, library : Library) -> None:
        """
        changes book status from borrowed to lost
        """
        if name in self.user_books:
            self.user_books.remove(name)
            library.damage(name)
        else:
            print("You do not have this book")

class Librarian:
    def __init__(self) -> None:
        self.librarian_books=[]
        """
        Class Constructor of books
        librarian_books: list of books to upload 
        """

    def add(self, booklist: list)->None:
        """
        Adds books to librarian_books
        """
        self.librarian_books=booklist

    def upload(self,library : Library)->None:
        """"
        appends books on list to selected Bookshelf
        """
        library.add_list(self.librarian_books)
        self.librarian_books=[]

    def take_books(self, library : Library) -> None:
        """
        receive list damaged and/or lost books
        """
        list=[]
        for Book in library.Books:
          
            if Book.status == "damaged" or Book.status =="lost":
                self.librarian_books.append(Book)
                list.append(Book.name)
        library.remove_list(list)   
        print("list is ",list)        
    
    def show(self) -> str:
        """
        Shows the Books of the Librarian
        """
        print(self.librarian_books)
        
        
    