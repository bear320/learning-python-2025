class Animal:
    # docstring
    """A class representing an animal with a name, species, and age."""

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


Usagi = Animal("Usagi", "Rabbit", 3)
print(type(Usagi))  # Output: <class '__main__.Animal'>
print(Usagi.name)  # Output: Usagi
print(Usagi.species)  # Output: Rabbit
print(Usagi.age)  # Output: 3
print(
    Usagi.__doc__
)  # Output: A class representing an animal with a name, species, and age.
Usagi.move()  # Output: Usagi the Rabbit is moving.


Momonga = Animal("Momonga", "Flying Squirrel", 2)
print(type(Momonga))  # Output: <class '__main__.Animal'>
print(Momonga.name)  # Output: Momonga
print(Momonga.species)  # Output: Flying Squirrel
print(Momonga.age)  # Output: 2
Momonga.sleep(5)  # Output: Momonga is going to sleep for 5 hours.

print(Usagi.age > Momonga.age)  # Output: True
