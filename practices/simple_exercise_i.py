# 1. Write a function called "printMany" that prints out integers 1, 2, 3, ..., 100.
def printMany():
    for i in range(1, 101):
        print(i)


# printMany()


#  2. Write a function called "printEvery3" that prints out integers 1, 4, 7, 10, ..., 88.
def printEvery3():
    for i in range(1, 89, 3):
        print(i)


# printEvery3()


#  3. Write a function called "position" that returns a tuple of the first uppercase letter and its index location. If not found, returns -1.
def position(string):
    for i, char in enumerate(string):
        if char.isupper():
            return (char, i)
    return -1


print(position("abcd"))
print(position("AbcD"))
print(position("abCD"))
