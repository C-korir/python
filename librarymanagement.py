class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.borrowed = False

    def borrow_book(self):
        self.borrowed = True

    def return_book(self):
        self.borrowed = False

    def display_info(self):
        borrowed_status = "Not borrowed" if not self.borrowed else "Borrowed"
        print(f"Title: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publication_year}\nBorrowed Status: {borrowed_status}")


class LibraryMember(Book):
    def __init__(self, member_id, name):
        super().__init__("", "", 0)
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        book.borrow_book()
        self.borrowed_books.append(book)

    def return_book(self, book):
        book.return_book()
        self.borrowed_books.remove(book)

    def display_info(self):
        print(f"Member ID: {self.member_id}\nName: {self.name}\nBorrowed Books:")
        for book in self.borrowed_books:
            print(f"{book.title} by {book.author}")


if __name__ == "__main__":
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

    member = LibraryMember(1, "John Doe")

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