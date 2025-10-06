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


# print(position("abcd"))  # returns -1
# print(position("AbcD"))  # returns ('A', 0)
# print(position("abCD"))  # returns ('C', 2)


# 4. Write a function called "findSmallCount" that takes one list of integers and one integer as input, and returns an integer indicating how many elements in the list is smaller than the input integer.
def findSmallCount(list, int):
    count = 0
    for i in list:
        if i < int:
            count += 1
    return count


# print(findSmallCount([1, 2, 3], 2))  # returns 1
# print(findSmallCount([1, 2, 3, 4, 5], 0))  # returns 0


# 5. Write a function called "findSmallerTotal" that takes one list of integers and one integer as input, and returns the sum of all elements in the list that are smaller than the input integer.
def findSmallerTotal(list, int):
    total = 0
    for i in list:
        if i < int:
            total += i
    return total


# print(findSmallerTotal([1, 2, 3], 3))  # returns 3
# print(findSmallerTotal([1, 2, 3], 1))  # returns 0
# print(findSmallerTotal([3, 2, 5, 8, 7], 999))  # returns 25
# print(findSmallerTotal([3, 2, 5, 8, 7], 0))  # returns 0


# 6. Write a function called "findAllSmall" that takes one list of integers and another integer as input, and returns an list of integers that contains all elements that are smaller than the input integer.
def findAllSmall(list, int):
    result = []
    for i in list:
        if i < int:
            result.append(i)
    return result


# print(findAllSmall([1, 2, 3], 10))  # returns [1, 2, 3]
# print(findAllSmall([1, 2, 3], 2))  # returns [1]
# print(findAllSmall([1, 3, 5, 4, 2], 4))  #  returns [1, 3, 2]


# 7. Write a function called "summ" that takes one list of numbers, and return the sum of all elements in the input list.
def summ(list):
    result = 0
    for i in list:
        result += i
    return result


print(summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # returns 55
print(summ([]))  # return 0
print(summ([-10, -20, -30]))  # return -60
