"""Example of a class and object instantiation."""

# Class name convention start with upper-case letter
# class is a reserved word in Python


class Pizza:
    """Models the idea of a Pizza."""
 
    # Attribute Definitions
    size: str
    toppings: int 
    extra_cheese: bool = False 
    
    def __init__(self, size: str, toppings: int, extra_cheese: bool):
        """Constructor definition for initialization of attributes."""
        self.size = size
        self.toppings = toppings 
    
    def price(self, tax: float) -> float:
        """Calculate the price of a pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0

        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0

        return total 


a_pizza: Pizza = Pizza("large", 3)
print(Pizza)
print(a_pizza)
# When we print a_pizza its an object. 
print(a_pizza.size)
print(f"Price ${a_pizza.price(1.05)}")

another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_cheese() = True
print(a_pizza.size)
print(f"Price: {another_pizza.price(1.05)}")