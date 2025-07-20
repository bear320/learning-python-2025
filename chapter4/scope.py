name = "John"


def greet_1():
    name = "Alice"

    def hello_1():
        print(f"Hello, {name}!")

    hello_1()


greet_1()  # Hello, Alice!


def greet_2():
    hello_2()


def hello_2():
    print(f"Hello, {name}!")


greet_2()  # Hello, John!
