from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        self._customer = None
        self._coffee = None
        self._price = None
        
        # Uses setters for validation
        self.customer = customer  
        self.coffee = coffee
        self.price = price
        
        # Add this order to the customer and coffee's lists
        customer._orders.append(self)
        coffee._orders.append(self)

    # Getter for customer
    @property
    def customer(self):
        return self._customer

    # Setter for customer (validates type)
    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise ValueError("Customer must be a Customer instance")
        self._customer = value

    # Getter for coffee
    @property
    def coffee(self):
        return self._coffee

    # Setter for coffee (validates type)
    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be a Coffee instance")
        self._coffee = value

    # Getter for price
    @property
    def price(self):
        return self._price

    # Setter for price (immutable after initial set)
    @price.setter
    def price(self, value):
        if hasattr(self, '_price') and self._price is not None:
            raise AttributeError("Price is immutable")
        if not isinstance(value, (int, float)) or value < 1.0 or value > 10.0:
            raise ValueError("Price must be a number between 1.0 and 10.0")
        self._price = float(value)