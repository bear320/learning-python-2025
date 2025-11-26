class Robot:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __key(self):
        return (self.name, self.age, self.address)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Robot):
            return self.__key() == other.__key()
        return NotImplemented

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return f"{self.name} is now {self.age} years old and lives in {self.address}."

    def __repr__(self):
        return f"Robot(name={self.name}, age={self.age}, address={self.address})"

    def __add__(self, other):
        if isinstance(other, Robot):
            return self.age + other.age
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Robot):
            return self.age > other.age
        return NotImplemented


robot1 = Robot("R2-D2", 5, "Naboo")
robot2 = Robot("C-3PO", 10, "Tatooine")

print(len(robot1))  # Output: 5
print(str(robot1))  # Output: R2-D2 is now 5 years old and lives in Naboo.
print(repr(robot1))  # Output: Robot(name=R2-D2, age=5, address=Naboo)
print(robot1 + robot2)  # Output: 15
print(robot1 > robot2)  # Output: False
