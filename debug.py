from customer import Customer
from coffee import Coffee
from order import Order

def test_coffee_shop():
    # Create test objects
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    coffee = Coffee("Espresso")
    
    # Create orders
    order1 = customer1.create_order(coffee, 5.0)
    order2 = customer2.create_order(coffee, 6.5)
    
    # Test relationships
    print("Testing relationships:")
    print(len(coffee.orders()) == 2)  # True
    print(len(customer1.orders()) == 1)  # True
    print(customer1.coffees()[0].name == "Espresso")  # True
    
    # Test aggregates
    print("\nTesting aggregates:")
    print(coffee.average_price() == 5.75)  # True
    
    # Test bonus method
    print("\nTesting bonus method:")
    print(Customer.most_aficionado(coffee).name == "Bob")  # True

if __name__ == "__main__":
    test_coffee_shop()