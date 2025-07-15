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
