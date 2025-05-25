import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        # Runs before every test
        self.customer = Customer("Alice")
        self.coffee = Coffee("Espresso")

    def test_order_creation(self):
        order = Order(customer=self.customer, coffee=self.coffee, price=5.0)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 5.0)

    def test_price_validation(self):
        # Invalid price (should raise errors)
        with self.assertRaises(ValueError):
            Order(customer=self.customer, coffee=self.coffee, price=0.9)  # Too low
        with self.assertRaises(ValueError):
            Order(customer=self.customer, coffee=self.coffee, price=10.1)  # Too high
        with self.assertRaises(ValueError):
            Order(customer=self.customer, coffee=self.coffee, price="five")  # Not a number

    def test_price_immutable(self):
        order = Order(customer=self.customer, coffee=self.coffee, price=5.0)
        with self.assertRaises(AttributeError):
            order.price = 6.0  # Should not allow changes

    def test_relationships(self):
        order = Order(customer=self.customer, coffee=self.coffee, price=5.0)
        self.assertIn(order, self.customer.orders())
        self.assertIn(order, self.coffee.orders())

if __name__ == "__main__":
    unittest.main()