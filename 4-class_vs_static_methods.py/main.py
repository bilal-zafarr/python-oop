"""
In Python, both class methods and static methods are ways to define methods that are bound to a class rather than an instance of the class.
However, they serve different purposes and have different behaviors.

* Class Method: *

Decorator: Defined using the @classmethod decorator.
First Parameter: Takes a reference to the class as its first parameter, conventionally named cls.
Accessing Class Variables: Can access and modify class-level variables.
Instance Access: Can be called on the class itself or an instance of the class.

Example:
"""
class MyClass:
    class_variable = 10

    @classmethod
    def class_method(cls, x):
        print(f'Class variable: {cls.class_variable}')
        print(f'Passed argument: {x}')

MyClass.class_method(5)

"""
* Static Method: *
Decorator: Defined using the @staticmethod decorator.
Parameters: Doesn't have a reference to the class or instance automatically, and doesn't need the first parameter to be cls or self.
Accessing Class Variables: Cannot access or modify class-level variables unless explicitly passed as arguments.
Instance Access: Can be called on the class itself or an instance of the class, but does not have access to instance-specific data.

Example:
"""
class MyClass:
    class_variable = 10

    @staticmethod
    def static_method(x):
        print(f'Passed argument: {x}')

MyClass.static_method(5)

"""
When to Use Each:
Class Method: Use when the method needs access to or modification of class-level variables. For example, when the method performs an action that affects the entire class.
Static Method: Use when the method is related to the class but doesn't need access to class or instance variables. For example, when the method performs a standalone action that doesn't depend on the state of the class or instance.
In summary, class methods are more closely tied to the class and can access and modify class-level variables, while static methods are more standalone and don't have access to class or instance-specific data by default.
"""

import csv


class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
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
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
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
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
Item.instantiate_from_csv()
print(Item.all)
