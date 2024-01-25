"""
Class Attribure vs Instance Attribute in Python

* Class Attributes

Defined directly within the class body, outside of any methods.
Shared by all instances (objects) of the class.
Accessed using both the class name and instance name.
Changes to a class attribute affect all instances.

* Instance Attributes

Defined within the __init__() method (constructor) of a class.
Unique to each individual instance (object) of the class.
Accessed using the instance name.
Changes to an instance attribute only affect that specific instance.

* Best Practices:

Use class attributes for data that is common to all instances of a class.
Use instance attributes for data that is specific to individual instances.
Be mindful of the implications of modifying class attributes, as changes will affect all instances.
Consider using properties to control access to attributes for encapsulation and data integrity.
"""


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount (Pay rate here is class attribute)
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name  # Instance attribute
        self.price = price
        self.quantity = quantity

        # Actions to execute
        # Whenever a new instance is created the below line will add that instance to the class attribute `all`
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # object representation
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

# Prints all the objects associated with Item class
print(Item.all)

# Prints all the attributes belonging to this object
print(Item.__dict__)
