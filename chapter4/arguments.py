def exponent(a, b):
    return a**b


# positional arguments
print(exponent(2, 3))  # 8

# keyword arguments
print(exponent(b=2, a=3))  # 9


# default arguments
def sum(n1=0, n2=0):
    return n1 + n2


# SyntaxError: parameter without a default follows parameter with a default
# def sum2(n1=10, n2):
#     return n1 + n2

print(sum())  # 0
print(sum(12))  # 12
print(sum(12, 8))  # 20

print(sum(n2=5))  # 5
print(sum(n2=10, n1=5))  # 15


# arbitrary arguments
def sum_all(*args):
    total = 0
    for n in range(len(args)):
        total += args[n]
        print(f"Adding {args[n]} to total, current total: {total}")
    return total


print(sum_all(1, 2, 3))  # 6
print(sum_all(2, -3, 4, 5))  # 8


def introduce(**kwargs):
    print(
        "{} is now {} years old and lives in {}.".format(
            kwargs["name"], kwargs["age"], kwargs["city"]
        )
    )
    # for key, value in kwargs.items():
    #     print(f"{key}: {value}")


introduce(name="Alice", age=30, city="New York")


def my_func(*args, **kwargs):
    print("{} would like to eat {} {}.".format(kwargs["name"], args[0], kwargs["food"]))


my_func(5, 10, 15, name="John", food="eggs")
