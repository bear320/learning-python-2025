# global variables
name = "Alice"
age = 25


def print_info():
    # accessing global variables
    print("Name:", name)
    print("Age:", age)


print_info()


# local variables
def greet():
    greeting = "Hello, " + name  # local variable
    print(greeting)


greet()


# print(greeting)  # This will raise an error because 'greeting' is not defined outside the function
