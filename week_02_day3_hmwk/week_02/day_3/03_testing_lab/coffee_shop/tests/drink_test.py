import unittest
from src.drink import Drink 



class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("tea", 2.99)

    def test_drink_has_name(self):
            self.assertEqual("tea", self.drink.name)

    def test_drink_has_price(self):
            self.assertEqual(2.99, self.drink.price)