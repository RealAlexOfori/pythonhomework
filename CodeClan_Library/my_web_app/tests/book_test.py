import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    
    def setUp(self):
        self.book = Book("Holy spirit", "Yongi Cho", "religious")
        
    
    def test_book_has_name(self):
        self.assertEqual("Holy spirit", self.book.name)
                        
                        
    def test_book_has_author(self):
        self.assertEqual("Yongi Cho", self.book.author)  


    def test_book_has_genre(self):
        self.assertEqual("religious", self.book.genre) 