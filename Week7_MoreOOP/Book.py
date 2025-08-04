class Book:

    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def change_number_of_copies(self, update_amount):
        self.copies += update_amount

    def __str__(self):
        return self.title + " by " + self.author + \
               " with " + str(self.copies) + " copies."


class Text_book(Book):

    def __init__(self,title, author, copies, subject, resources ):
        super().__init__(title, author, copies)
        self.subject = subject
        self.resources = resources

    def change_number_of_copies(self, update_amount):
        print("Textbook version")
        # self.copies += update_amount
        super().change_number_of_copies(update_amount)

    def __str__(self):
        return super().__str__() + f"in {self.subject} with resources {self.resources}"


def tester():
    book1 = Book("1984", "Orwell", 4)
    textbook1 = Text_book("Python for Beginners", "Dawson", 3, "computer science", "resource1")
    print(book1)
    print(textbook1)
    book1.change_number_of_copies(2)
    textbook1.change_number_of_copies(1)
    print(book1)
    print(textbook1)

tester()

if __name__ == "main":
    tester()

