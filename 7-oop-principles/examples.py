"""
Encapsulation is the bundling of data and the methods that operate on that data into a single unit, called a class.
It is a technique of restricting a user from directly modifying the data members or variables of a class in order to maintain the integrity of the data. 
How do we do that? We restrict the access of the variables by switching the access-modifier to private and exposing public methods that we can use to access the data.

Real-world analogy: Think of a smartphone as a class. The internal components (processor, battery, etc.) are encapsulated within the phone's body. 
Users interact with the phone through its interface (touchscreen, buttons), and they don't need to know the internal details to use the phone effectively.
Example
"""


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__fuel = 100  # private variable

    @property
    def fuel(self):
        return self.__fuel

    def drive(self, distance):
        # Perform some checks and calculations
        self.__fuel -= distance * 0.1

    def get_fuel_level(self):
        return self.__fuel


my_car = Car("Toyota", "Camry")
my_car.drive(50)
print(f"Fuel level: {my_car.get_fuel_level()}%")

"""
Abstraction involves hiding the complex reality while exposing only the necessary parts. 
It allows you to focus on what an object does rather than how it achieves it.
This helps in reducing the operational complexity at the user-end.

Real-world analogy: Consider driving a car. 
As a driver, you interact with the car through the steering wheel, pedals, and dashboard, 
but you don't need to understand the internal combustion engine's complexities to operate the vehicle. 
The car abstracts away the complexities, providing a simplified interface for the driver.

Example
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side**2


# Cannot instantiate an abstract class
# my_shape = Shape()

my_circle = Circle(5)
my_square = Square(4)

print(my_circle.calculate_area())  # Output: 78.5
print(my_square.calculate_area())  # Output: 16

"""
Difference in Encapsulation and Abstraction



"""

"""
Inheritance allows a class (subclass/derived class) to inherit the properties and methods of another class (superclass/base class). 
It promotes code reuse and establishes a relationship between classes.


Real-world analogy: Consider the concept of vehicles. A superclass could be "Vehicle," and subclasses could be "Car," "Motorcycle," and "Bicycle." 
Each subclass inherits common properties and behaviors from the "Vehicle" class. For instance, they might all have a common method like "move."

Example
"""


class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


my_dog = Dog()
my_cat = Cat()

print(my_dog.speak())  # Output: Woof!
print(my_cat.speak())  # Output: Meow!

"""
Polymorphism allows objects of different classes to be treated as objects of a common base class. 
It enables a single interface to represent different types of objects.

Example
"""


class Circle:
    def calculate_area(self, radius):
        return 3.14 * radius**2


class Square:
    def calculate_area(self, side):
        return side**2


def print_area(shape, size):
    print(f"Area: {shape.calculate_area(size)}")


circle = Circle()
square = Square()

print_area(circle, 5)  # Output: Area: 78.5
print_area(square, 4)  # Output: Area: 16
