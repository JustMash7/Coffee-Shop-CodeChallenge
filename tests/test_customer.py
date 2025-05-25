import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):
    def setUp(self):
        # Runs before every test
        self.customer = Customer("Alice")
        self.coffee = Coffee("Espresso")

    def test_name_validation(self):
        # Valid name
        valid_customer = Customer("Bob")
        self.assertEqual(valid_customer.name, "Bob")

        # Invalid names (should raise errors)
        with self.assertRaises(ValueError):
            Customer("")  # Too short
        with self.assertRaises(ValueError):
            Customer("A" * 16)  # Too long
        with self.assertRaises(ValueError):
            Customer(123)  # Not a string

    def test_create_order(self):
        order = self.customer.create_order(self.coffee, 5.0)
        self.assertIn(order, self.customer.orders())
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 5.0)

    def test_coffees_list(self):
        # Create orders for different coffees
        latte = Coffee("Latte")
        self.customer.create_order(self.coffee, 5.0)
        self.customer.create_order(latte, 4.5)
        self.assertEqual(len(self.customer.coffees()), 2)

    def test_most_aficionado(self):
        # Create two customers
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")

        # Create a coffee
        coffee = Coffee("Espresso")

        # Create orders
        customer1.create_order(coffee, 5.0)
        customer2.create_order(coffee, 6.5)

        # Test who spent the most
        self.assertEqual(Customer.most_aficionado(coffee).name, "Bob")

if __name__ == "__main__":
    unittest.main()