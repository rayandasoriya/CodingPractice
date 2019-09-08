class Library:
    def __init__(self,listOfBooks):
        self.availableBooks = listOfBooks
    
    def displayAvailableBooks(self):
        print(self.availableBooks)
    
    def lendBook(self,bookName):
        if bookName not in self.availableBooks:
            print("Book unavailable")
        else:
            self.availableBooks.remove(bookName)
    
    def returnBook(self, bookName):
        self.availableBooks.append(bookName)

class Student:
    def request_Book(self):
        self.book = input()
        return self.book
    
    def return_book(self):
        self.book = input()
        return self.book


library=Library(["The Last Battle","The Screwtape letters","The Great Divorce"])
library.displayAvailableBooks()
library.lendBook("The Great Divorce")
library.displayAvailableBooks()
library.returnBook("The Great Divorce")
library.displayAvailableBooks()
