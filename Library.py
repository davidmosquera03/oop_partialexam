from typing import List

class Book:
    def __init__(self, name) -> None:
        self.name = name
        self.status = "available"
        """
        Class constructor of a Book
        name: name of the Book
        status: condition, can be avaible/borrowed/damaged/lost
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
        Class constructor of Library
        Books: list of books in Library
        """

    def add_list(self, lista: list)->None:
        """
        for each element in given list, add Book objects
        """
        for element in lista:
          B= Book(element)
          self.Books.append(B)      
        
    def reset(self, name : str):
        """
        sets a Book status back to available
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
        sets a Book status to lost
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
        sets a Book status to damaged
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
        remove damaged or lost books 
        """
        self.show() 
        self.Books = [Book for Book in self.Books if Book.name not in list ]
        # Updates books from Library removing those not in list

    def show(self) -> str:
        """
        Shows current status of Book list
        """
        print(self.Books)


class User:
    def __init__(self) -> None:
        self.user_books=[]
        """
        Class constructor of User
        user_books: list of books it has borrowed
        """

    def borrow_book(self, name: str ,library : Library)->None:
        """
        searches in library for book
        if it exists and is available, adds it to user list
        and changes status to borrowed
        else, shows it is not found
        """
        found = False
        borrowed = False
        for Book in library.Books:
            if Book.name==name and Book.status=="available":
                Book.status="borrowed"
                found = True
            elif Book.name==name and Book.status=="borrowed":
                borrowed = True
                print(name, "already borrowed")
        if(found and not borrowed):
            self.user_books.append(name)
        elif(not found and not borrowed):
            print(name," not found")
            
    def return_book(self,name: str, library : Library)->None:
        """
        If user has a given book, remove from user_books
        and return status on Library to available
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
        Shows books with available status from selected Library
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
    def is_book(self, name: str, library: Library) -> str:
        """
        Shows if one specific book is in Library
        """
        found = False
        for Book in library.Books:
            if Book.name==name and Book.status=="available":
                found = True
                print(Book.name," is ",Book.status)
        if(found):
            self.user_books.append(name)
        else:
            print(name," has not been found in Library")


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
        creates list of damaged and/or lost books
        and uses it to change books in Library
        """
        list=[]
        for Book in library.Books:
          
            if Book.status == "damaged" or Book.status =="lost":
                self.librarian_books.append(Book)
                list.append(Book.name)
        library.remove_list(list)   
        # print("list is ",list)        
    
    def show(self) -> str:
        """
        Shows the Books of the Librarian
        """
        print(self.librarian_books)
    
    def dispose(self) -> None:
        """
        erases librarian books  
        """
        self.librarian_books=[]

    def take_any(self, name: str, library: Library) ->None:
        """
        takes from Library specific available book
        """
        found = False
        for Book in library.Books:
            if Book.name==name and Book.status=="available":
                library.Books.remove(Book)
                self.librarian_books.append(Book.name)
                found = True
        if(not found):
            print("Unable to take ",name)
            

        
    