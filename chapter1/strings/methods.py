myString = "Hello"

# length
print(len(myString))  # 5

# typecasting
print(int("5"))  # 5
print(float("5.5"))  # 5.5
print(str(5))  # '5'

# upper and lower
print(myString.upper())  # HELLO
print(myString.lower())  # hello

# isupper and islower
print(myString.isupper())  # False
print(myString.islower())  # False

# method chaining
print(myString.upper().isupper())  # True
print(myString.lower().islower())  # True

# index
print(myString.index("e"))  # 1
print(myString.index("l"))  # 2
print(myString.index("lo"))  # 3
# print(myString.index("z"))  # ValueError: substring not found
