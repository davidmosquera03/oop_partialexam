from Library import Book,Library,User, Librarian

librero = Library() # Create a Library
print("Books in Library")
librero.show() # Show books (None until now)

marta = Librarian() # Create a Librarian

marta.add(["1984","Dune","We"])
print("Show Librarian Books")
marta.show()
print("Upload")
marta.upload(librero)
# Add 3 Books to librarian and uploads them to Library
print("Books in Library now")
librero.show() # Shows the books and their status

pedro = User() # Create a User
print("Books of User")
pedro.show() # Show books of User (None until now)

print("Borrow Trial 1 (Book not in Library) ")
pedro.borrow_book("Frankenstein", librero) # Try to borrow book not in library
pedro.show()
print("Showing available books")
pedro.avaiable_books(librero) # See available books in library

print("Borrowing Trial 2 (Book in library and available) ")
pedro.borrow_book("We",librero)
pedro.show()
print("Show available books in Library again")
librero.show()

print("Borrowing Trial 3(Book in library but borrowed) ")
lucas = User()
lucas.borrow_book("We",librero) # Another user tries to borrow same book

print("Updated Library")
lucas.avaiable_books(librero)

pedro.return_book("We",librero) # User Pedro will return one book and borrow the rests
pedro.borrow_book("Dune",librero)
pedro.borrow_book("1984",librero)
print("New status of available books after 2 being borrowed and 1 being returned")
pedro.avaiable_books(librero)

print("All book status")
librero.show()
print("Damage and lose books") # Pedro loses and damages each book
pedro.report_damaged("1984", librero)
pedro.report_lost("Dune",librero)

print("All book status in Library after damages")
librero.show()

print("Give damaged and/or books to librarian") # Librarian takes List
marta.take_books(librero)

print("Show Librarian Books") # Librarian has now these books
marta.show()
print("Show Library books") # These books have been removed from library
librero.show()

print("Search for specific book")
lucas.is_book("Dune",librero)

print("Librarian disposes of its books and uploads more")
marta.dispose()
marta.show()