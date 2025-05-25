class Customer:
    def __init__(self, name):
        # Uses the setter for validation
        self.name = name  
        # Stores all orders for this customer
        self._orders = []

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name (validates input)
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Name must be 1-15 characters")
        self._name = value

    # Returns all orders for this customer
    def orders(self):
        return self._orders

    # Returns unique coffees this customer has ordered
    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    # Creates a new order for this customer
    def create_order(self, coffee, price):
        # Import Order here to avoid circular dependency
        from order import Order  
        return Order(customer=self, coffee=coffee, price=price)

    # Bonus: Finds the customer who spent the most on a specific coffee
    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders():
            return None
        spending = {}
        for order in coffee.orders():
            customer = order.customer
            spending[customer] = spending.get(customer, 0) + order.price
        return max(spending.items(), key=lambda x: x[1])[0]