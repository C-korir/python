class LibraryMember:
    def __init__(self, name, library_card_number):
        self.name = name
        self.library_card_number = library_card_number
        self.borrowed_books = []

    def borrow_book(self, book):
        book.borrow_book()
        self.borrowed_books.append(book)

    def return_book(self, book):
        book.return_book()
        self.borrowed_books.remove(book)

    def display_info(self):
        print(f"Name: {self.name}\nLibrary Card Number: {self.library_card_number}\nNumber of Borrowed Books: {len(self.borrowed_books)}")


if __name__ == "__main__":
    member = LibraryMember("John Doe", 123456)

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

    print("\nBefore borrowing books:")
    member.display_info()

    member.borrow_book(book1)
    member.borrow_book(book2)

    print("\nAfter borrowing books:")
    member.display_info()

    print("\nReturning books:")
    member.return_book(book1)

    print("\nAfter returning a book:")
    member.display_info()