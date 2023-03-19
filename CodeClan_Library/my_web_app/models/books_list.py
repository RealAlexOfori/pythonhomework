from models.book import *

book1 = Book( "Richest man in Babylon", "Clanson", "self help")
book2 = Book( "Holy Spirit", "Yongi Cho", "religious")
book3 = Book( "The Lean Startup", "Fred", "business")
book4 = Book( "Hit Makers","Dereck thompson","Self help")

books = [book1, book2, book3, book4]

def add_book(new_book):
    books.append(new_book)