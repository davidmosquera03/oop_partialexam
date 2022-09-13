from Library import Book,Library,User, Librarian

librero = Library() # Create a Library
print("Books in Library")
librero.show() # Show books (None until now)

marta = Librarian() # Create a Librarian

marta.add(["1984","Dune","We"])
print("Show Librarian Books")
marta.show()
marta.upload(librero)
# Add 3 Books to librarian and uploads them to Library
print("Books in Library now")
librero.show() # Shows the books and their status

pedro = User() # Create a User
print("Books of User")
pedro.show() # Show books of User (None until now)

print("Borrow Trial 1 (Book not in Library)")
pedro.borrow_book("Frankenstein", librero) # Try to borrow book not in bookshelf
pedro.show()
print("Showing available books")
pedro.avaiable_books(librero) # See available books in library

print("Borrowing Trial 2")
pedro.borrow_book("We",librero)
pedro.show()
print("Show updated Library")
librero.show()

print("Borrowing Trial 3")
lucas = User()
lucas.borrow_book("We",librero) # Another user tries to borrow same book

print("Updated Library")
lucas.avaiable_books(librero)

print("Returning Book")
pedro.return_book("We",librero) # User Pedro will return one book and borrow the rests
pedro.borrow_book("Dune",librero)
pedro.borrow_book("1984",librero)
print("New available books")
pedro.avaiable_books(librero)

print("All book status")
librero.show()
print("Damage and lose books") # Pedro loses and damages each book
pedro.report_damaged("1984", librero)
pedro.report_lost("Dune",librero)

print("All book status in Library")
librero.show()

print("Give damaged and/or books to librarian") # Librarian takes List
marta.take_books(librero)

print("Show Librarian Books")
marta.show()
print("Show Library books")
librero.show()

lucas.is_book("Dune",librero)