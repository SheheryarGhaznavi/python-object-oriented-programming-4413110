# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author = None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addChapter(self, chapter):
        self.chapters.append(chapter)

    def getPagesCount(self):
        count = 0
        for chapter in self.chapters:
            count += chapter.pages
        return count


class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"Fname {self.fname} Lname {self.lname}"


class Chapter:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages


# author = Author("Leo", "Tolstoy")
# b1 = Book("War and Peace", 39.0, author)

# chapter1 = Chapter("Chapter 1", 125)
# chapter2 = Chapter("Chapter 2", 97)
# chapter3 = Chapter("Chapter 3", 143)

# b1.addChapter(chapter1)
# b1.addChapter(chapter2)
# b1.addChapter(chapter3)

b1 = Book("War and Peace", 39.0, Author("Leo", "Tolstoy"))

b1.addChapter( Chapter("Chapter 1", 125) )
b1.addChapter( Chapter("Chapter 2", 97) )
b1.addChapter( Chapter("Chapter 3", 143) )

print(b1.title)
print(b1.author)
print(b1.getPagesCount())
