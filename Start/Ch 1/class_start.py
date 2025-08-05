# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ( "HARDCOVER", "PAPERBACK", "EBOOK" )

    # TODO: double-underscore properties are hidden from other classes
    __book_list = None

    # TODO: create a class method
    @classmethod
    def getBookTypes(self):
        return self.BOOK_TYPES

    # TODO: create a static method
    def getBookList():
        if Book.__book_list == None:
            Book.__book_list = []
        
        return Book.__book_list

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, book_type):
        self.title = title
        if book_type not in self.BOOK_TYPES:
            raise ValueError(f"{book_type} is not a valid book type")
        else:
            self.book_type = book_type


# TODO: access the class attribute
print("book type of class", Book.getBookTypes())

# TODO: Create some book instances
b1 = Book("New Book 1", "HARDCOVER")
b2 = Book("New Book 2", "PAPERBACK")


# TODO: Use the static method to access a singleton object
book_list = Book.getBookList()
book_list.append(b1)
book_list.append(b2)
print(book_list)
