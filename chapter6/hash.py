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
