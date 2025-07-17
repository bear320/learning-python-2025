def higher_order_function(fn):
    fn()


def example_function():
    print("This is an example function.")


higher_order_function(example_function)


numbers = [1, 2, -3, 4, 5]


# map()
def square(x):
    return x**2


for item in map(square, numbers):
    print(item)


# filter()
def is_positive(x):
    return x > 0


for item in filter(is_positive, numbers):
    print(item)
