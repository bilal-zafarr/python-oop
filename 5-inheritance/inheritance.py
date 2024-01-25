"""
* Key Concept *
-> Inheritance allows you to create new classes (called child classes or subclasses) that \
      inherit attributes and methods from existing classes \
        (called parent classes or base classes).
-> It promotes code reusability, code organization, and modeling of real-world relationships.

* Key Terms *
-> Parent class (base class): The class being inherited from.
-> Child class (subclass): The class that inherits from the parent class.
-> Inheritance hierarchy: The structure of classes created through inheritance relationships.

* Features *
-> Inheriting attributes and methods: Child classes automatically gain access to \
    the parent class's attributes and methods.
-> Overriding methods: Child classes can redefine inherited methods to provide \
    their own specific behavior.
-> Adding new attributes and methods: Child classes can introduce new attributes \
      and methods to extend functionality.
-> Using the super() function: The super() function allows child classes to access \
      inherited methods and attributes from their parent classes, \
          enabling cooperation between the two.
"""

import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return (
            f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
        )


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)

        # Run validations to the received arguments
        assert (
            broken_phones >= 0
        ), f"Broken Phones {broken_phones} is not greater or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones


phone1 = Phone("jscPhonev10", 500, 5, 1)

print(Item.all)
