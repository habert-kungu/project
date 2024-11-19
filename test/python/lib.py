import os


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed.")

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"'{title}' by {author} added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"'{title}' removed from the library.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("\nBooks in the library:")
            for book in self.books:
                print(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def borrow_book(self, title):
        book = self.find_book(title)
        if book:
            book.borrow()
        else:
            print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        book = self.find_book(title)
        if book:
            book.return_book()
        else:
            print(f"Book titled '{title}' not found in the library.")

    def load_books(self):
        if os.path.exists("library_books.txt"):
            try:
                with open("library_books.txt", "r") as file:
                    for line in file:
                        title, author, is_borrowed = line.strip().split(",")
                        book = Book(title, author)
                        book.is_borrowed = is_borrowed == "True"
                        self.books.append(book)
                print("Books loaded from file.")
            except Exception as e:
                print(f"Error loading books from file: {e}")

    # def class update_books ():
    # print ("hello, world ")

    def save_books(self):
        try:
            with open("library_books.txt", "w") as file:
                for book in self.books:
                    file.write(f"{book.title},{book.author},{book.is_borrowed}\n")
            print("Books saved to file.")
        except Exception as e:
            print(f"Error saving books to file: {e}")

    def __del__(self):
        self.save_books()


def main():
    library = Library()
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            library.add_book(title, author)
        elif choice == "2":
            title = input("Enter book title to remove: ")
            library.remove_book(title)
        elif choice == "3":
            library.list_books()
        elif choice == "4":
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)
        elif choice == "5":
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == "6":
            print("Exiting library system. Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
