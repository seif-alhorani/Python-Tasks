class Book:
    def __init__(self,book_id,title,author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True
    def mark_as_borrowed(self):
        self.is_available=False
    def mark_as_returned(self):
        self.is_available = True
    def __str__(self):
        status=""
        if self.is_available:
            status = "Available"
        else:
            status = "Borrowed"
        return f"[{self.book_id}] {self.title} by {self.author} - Status: {status}" 
class User:
    def __init__(self,user_id,name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []
    def borrow_book(self,book):
        if book.is_available:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} successfully borrowed '{book.title}'.")
        else:
            print(f"Sorry '{book.title}' is currently unavailable")
    def return_book(self,book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} does not have this book.")
    def __str__(self):
        if len(self.borrowed_books) == 0:
            books_held = "No books"
        else:
            books_held = ""
            for i in range(len(self.borrowed_books)):
                book = self.borrowed_books[i]
                books_held += book.title
                if i < len(self.borrowed_books) - 1:
                    books_held += ", "
        return f"User: {self.name} (ID: {self.user_id}) | Borrowed: {books_held}"

class Library:
    def __init__(self):
        self.books = []
        self.users = []
    def add_book(self , book):
        self.books.append(book)
    def register_user(self, user):
        self.users.append(user)
    def display_all_books(self):
        print("\n--- Library Catalog ---")
        for book in self.books:
            print(book)
    def display_all_users(self):
        print("\n--- Registered Users ---")
        for user in self.users:
            print(user)


my_library = Library()
b1 = Book(101,"Book1","Author1")
b2 = Book(102,"Book2","Author2")
my_library.add_book(b1)
my_library.add_book(b2)
u1 = User(1, "Alice")
my_library.register_user(u1)
my_library.display_all_books()
u1.borrow_book(b1) 
my_library.display_all_books() 
u1.return_book(b1) 
my_library.display_all_books() 
