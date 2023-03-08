import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Bruce", 150.00)

    def test_customer_has_name(self):
            self.assertEqual("Bruce", self.customer.name)

    def test_customer_has_wallet(self):
         self.assertEqual(150.00, self.customer.wallet)

    def test_reduce_cash(self):
          self.customer.reduce_cash(5)
          expected = 145.00
          actual = self.customer.wallet
          self.assertEqual(expected,actual)
