greeting = "Hello"
myName = "Oliver"

# Concatenation
print(greeting + ", " + myName + "!")

# Interpolation
print(f"{greeting}, {myName}!")

# Format method
print("{}, {}!".format(greeting, myName))
print("{0}, {1}!".format(greeting, myName))
print("{greeting}, {name}!".format(greeting=greeting, name=myName))

# Concatenation with numbers
print("2 + 3 = " + str(2 + 3))
print("2 + 3 = {}".format(2 + 3))
print("2 + 3 = {0}".format(2 + 3))
print("2 + 3 = {result}".format(result=2 + 3))

myString = "Hello"
myNumber = 3

# print(myString + myNumber)  # TypeError: can only concatenate str (not "int") to str
print(myString + str(myNumber))
