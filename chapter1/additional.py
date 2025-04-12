# Python supports complex numbers with a real and imaginary part.
# The imaginary part is denoted with a j.
x = 3 + 4j
y = 2 + 5j
print(x)  # (3+4j)
print(y)  # (2+5j)
print(x + y)  # (5+9j)
print(x - y)  # (1-1j)


# None
def hello():  # hello is a function stored in RAM
    print("Hello, World!")


print(hello)  # <function hello at 0x7f8c1c3e2d30>
print(hello())  # Hello, World! # None

# floating-point binary problem
print(0.1 + 0.2 - 0.3)  # 5.551115123125783e-17

# join()
my_list_1 = ["Hello", "World"]
print(" ".join(my_list_1))  # Hello World

my_list_2 = ["a", "b", "c"]
print(", ".join(my_list_2))  # a, b, c
