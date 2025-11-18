class Animal:
    # docstring
    """A class representing an animal with a name, species, and age."""

    # attributes
    farm = "Chiikawa World"

    # constructor
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    # method
    def move(self):
        print(f"{self.name} the {self.species} is moving.")

    def sleep(self, hours):
        print(f"{self.name} is going to sleep for {hours} hours.")

    def greet(self):
        print(f"Hello, I am {self.name} and belong to {self.__class__.farm}.")

    # static method
    @staticmethod
    def introduce():
        print("Welcome to the Animal Farm!")


Usagi = Animal("Usagi", "Rabbit", 3)
# print(type(Usagi))  # Output: <class '__main__.Animal'>
# print(Usagi.name)  # Output: Usagi
# print(Usagi.species)  # Output: Rabbit
# print(Usagi.age)  # Output: 3
# print(
#     Usagi.__doc__
# )  # Output: A class representing an animal with a name, species, and age.
# Usagi.move()  # Output: Usagi the Rabbit is moving.


Momonga = Animal("Momonga", "Flying Squirrel", 2)
# print(type(Momonga))  # Output: <class '__main__.Animal'>
# print(Momonga.name)  # Output: Momonga
# print(Momonga.species)  # Output: Flying Squirrel
# print(Momonga.age)  # Output: 2
# Momonga.sleep(5)  # Output: Momonga is going to sleep for 5 hours.

# print(Usagi.age > Momonga.age)  # Output: True

# print(Animal.farm)  # Output: Chiikawa World
# print(Usagi.farm)  # Output: Chiikawa World

# Usagi.greet()  # Output: Hello, I am Usagi and belong to Chiikawa World.

Animal.introduce()  # Output: Welcome to the Animal Farm!
Usagi.__class__.introduce()  # Output: Welcome to the Animal Farm!


class Circle:
    """A class representing a circle with a given radius."""

    pi = 3.14159
    all_circles = []

    def __init__(self, radius):
        self.radius = radius
        self.__class__.all_circles.append(self)

    def area(self):
        return self.__class__.pi * (self.radius**2)

    @staticmethod
    def total_area():
        total = 0
        for circle in Circle.all_circles:
            total += circle.area()
        return total

    @classmethod
    def total_area_cls(cls):
        total = 0
        for circle in cls.all_circles:
            total += circle.area()
        return total


c1 = Circle(3)
c2 = Circle(4)
print(c1.__class__.total_area())
print(c1.__class__.total_area_cls())
