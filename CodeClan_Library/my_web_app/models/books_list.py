from models.book import *

book1 = Book( "Richest man in Babylon", "Clanson", "self help")
book2 = Book( "Holy Spirit", "Yongi Cho", "religious")
book3 = Book( "The Lean Startup", "Fred", "business")
book4 = Book( "Hit Makers","Dereck thompson","Self help")

books = [book1, book2, book3, book4]

def add_book(newBook):
    books.append(newBook)

def remove_book(book_to_be_removed):
    books.remove(book_to_be_removed[0])