# 1. Write a function called "stars" which prints out layers of stars in the following pattern:

# stars(1)
# *

# stars(4)
# *
# **
# ***
# ****


def stars(n):
    for i in range(n):
        print("*" * (i + 1))


# stars(1)
# stars(4)

# 2. Write a function called "stars2" which prints out layers of stars in the following pattern:

# stars2(1)
# *

# stars2(4)
# *
# **
# ***
# ****
# ***
# **
# *


def stars2(n):
    for i in range(n):
        print("*" * (i + 1))
    for j in range(n - 1, 0, -1):
        print("*" * j)


# stars2(1)
# stars2(2)
# stars2(3)
# stars2(4)


# 3. Write a function called "table" which takes an input n, and prints out n x 1 to n x 9

# table(3);
# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 9 = 27


def table(n):
    for i in range(1, 10):
        print(f"{n} x {i} = {n*i}")


# table(3)

# 4. Write a function called "table9to9" that prints out the multiplication table:

# table9to9();
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# ...
# 1 x 9 = 9
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 9 x 9 = 81


def table9to9():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} x {j} = {i*j}")


table9to9()
