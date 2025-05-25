class Coffee:
    def __init__(self, name):
        # First check if name is a string
        if not isinstance(name, str):
            raise ValueError("Coffee name must be a string")
        # Then check length
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters")
        self._name = name
        self._orders = []
    # Getter for name (immutable)
    @property
    def name(self):
        return self._name

    # Returns all orders for this coffee
    def orders(self):
        return self._orders

    # Returns unique customers who ordered this coffee
    def customers(self):
        return list(set(order.customer for order in self._orders))

    # Total number of orders for this coffee
    def num_orders(self):
        return len(self._orders)

    # Average price of this coffee across all orders
    def average_price(self):
        if not self._orders:
            return 0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)