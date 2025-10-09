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


stars2(1)
stars2(2)
stars2(3)
stars2(4)
