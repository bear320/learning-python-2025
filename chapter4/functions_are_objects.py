def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


addition = subtraction
print(addition(5, 3))  # This will now call subtraction, output will be 2


str = "Hello, World!"
z = 25
# print("Hello" + str(z))  # TypeError: 'str' object is not callable
