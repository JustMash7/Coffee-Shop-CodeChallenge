import unittest
from coffee import Coffee

class TestCoffee(unittest.TestCase):
    def setUp(self):
        # Runs before every test
        self.coffee = Coffee("Espresso")

    def test_name_validation(self):
        # Valid name
        valid_coffee = Coffee("Latte")
        self.assertEqual(valid_coffee.name, "Latte")

        # Invalid names (should raise errors)
        with self.assertRaises(ValueError):
            Coffee("A")  # Too short
        with self.assertRaises(ValueError):
            Coffee(123)  # Not a string

    def test_orders(self):
        # Test that orders are tracked
        self.assertEqual(len(self.coffee.orders()), 0)

    def test_customers(self):
        # Test unique customers are tracked
        self.assertEqual(len(self.coffee.customers()), 0)

    def test_num_orders(self):
        self.assertEqual(self.coffee.num_orders(), 0)

    def test_average_price(self):
        self.assertEqual(self.coffee.average_price(), 0)

if __name__ == "__main__":
    unittest.main()