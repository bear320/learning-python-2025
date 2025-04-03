my_tuple = (10, "hello", True, 3.14)

# indexing
print(my_tuple[0])  # Output: 10
print(my_tuple[1:2])  # Output: ('hello',)
print(my_tuple[1:])  # Output: ('hello', True, 3.14)
print(my_tuple[:2])  # Output: (10, 'hello')
print(my_tuple[-1])  # Output: 3.14
print(my_tuple[-2:])  # Output: (True, 3.14)
print(my_tuple[-2:-1])  # Output: (True,)
print(my_tuple[-2:1])  # Output: ()

# len()
print(len(my_tuple))  # Output: 4

# count()
print(my_tuple.count(10))  # Output: 1
print(my_tuple.count("10"))  # Output: 0

# index()
print(my_tuple.index(10))  # Output: 0
print(my_tuple.index("hello"))  # Output: 1

# error
my_tuple.append(5)  # AttributeError: 'tuple' object has no attribute 'append'
my_tuple[0] = 20  # TypeError: 'tuple' object does not support item assignment
