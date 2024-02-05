"""
Encapsulation is the bundling of data and the methods that operate on that data into a single unit, called a class.
It is a technique of restricting a user from directly modifying the data members or variables of a class in order to maintain the integrity of the data. 
Encapsulation is the practice of hiding information inside of a "black box" so that other developers working with the code don't have to worry about it.
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

While definitions are always changing, I like to think about abstraction and encapsulation in the following way.

-> Abstraction is a technique that helps us identify what information and behavior should be encapsulated, and what should be exposed.
-> Encapsulation is the technique for organizing the code to encapsulate what should be hidden, and make visible what is intended to be visible.

-> We do encapsulation to achieve abstraction.
-> Abstractions solves the problem at design level while Encapsulation solves it at implementation level

-> The process of using the double underscore is a form of encapsulation. The process of deciding which data deserves to be hidden behind the double underscore is abstraction.
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
Polymorphism is the ability of a variable, function, or object to take on multiple forms.

Same function having multiple forms, behaving differently under different conditions
i.e. len(str), len(list)

Example
"""


class Creature:
    def move(self):
        print("the creature moves")


class Dragon(Creature):
    def move(self):
        print("the dragon flies")


class Kraken(Creature):
    def move(self):
        print("the kraken swims")


for creature in [Creature(), Dragon(), Kraken()]:
    creature.move()
# prints:
# the creature moves
# the dragon flies
# the kraken swims

"""
In this example the child classes, Dragon and Kraken are overriding the behavior of their parent class's move() method.
When overriding methods, use the same function signature
"""

"""
Function Overloading vs Function Overriding

Function Overloading refers to defining multiple functions with the same name but with different parameter types or a different number of parameters.
"""


class OverloadExample:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z


# Usage
obj = OverloadExample()
result = obj.add(
    1, 2
)  # This will raise an error because there is no add method with two parameters.

# Note: While you can define functions with the same name, Python doesn't support traditional function overloading like some other languages do (e.g., C++ or Java). The last defined function with the same name will override the previous one.

"""
Function Overriding

Function overriding occurs when a derived class provides a specific implementation for a method that is already defined in its base class.
"""


class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


# Usage
dog = Dog()
dog.speak()  # Output: Dog barks
