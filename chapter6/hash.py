a = "hello"
b = 100
c = 1.0
d = True
e = None
f = (1, 2, 3)
g = [1, 2, 3]
h = {"name": "Alice", "age": 30}

print(hash(a))  # Output: 8853298935319858761
print(hash(b))  # Output: 100
print(hash(c))  # Output: 1
print(hash(d))  # Output: 1
print(hash(e))  # Output: 4238894112
print(hash(f))  # Output: 529344067295497451
# print("Hash of g:", hash(g))  # TypeError: unhashable type: 'list'
# print("Hash of h:", hash(h))  # TypeError: unhashable type: 'dict'


class Robot:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    # define a private method __key()
    def __key(self):
        return (self.name, self.age, self.address)

    # implement __hash__() function
    def __hash__(self):
        return hash(self.__key())

    # implement __eq__() function
    def __eq__(self, other):
        if isinstance(other, Robot):
            return self.__key() == other.__key()
        return NotImplemented


robot1 = Robot("R2-D2", 5, "Naboo")
robot2 = Robot("C-3PO", 10, "Tatooine")
robot3 = Robot("R2-D2", 5, "Naboo")

dictionary = {robot1: "Astromech Droid"}
print(dictionary[robot1])  # Output: Astromech Droid

print(robot1 == robot2)  # Output: False
print(robot1 == robot3)  # Original Output: False --> Self-defined __eq_() makes it True
