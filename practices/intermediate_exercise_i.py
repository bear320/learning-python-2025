# 1. Write a function called "mySort" that takes an list of integers as input, and returns the sorted version of the input list. You are not allowed to use the built-in sorted() function.
def mySort(arr):
    n = len(arr)
    for i in range(n):
        # i is the number of elements already sorted
        # n - i - 1 is the number of elements to compare
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# print(mySort([17, 0, -3, 2, 1, 0.5]))  # returns [-3, 0, 0.5, 1, 2, 17]


# 2. Write a function called "isPrime" that takes an integer as input, and returns a boolean value that indicates if the input number is prime.
def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


# print(isPrime(1))  # returns False
# print(isPrime(5))  # returns True
# print(isPrime(91))  # returns False
# print(isPrime(1000000))  # returns False


# 3. Write a function called "palindrome" that checks if the input string is a palindrome.
def palindrome(str):
    left = 0
    right = len(str) - 1
    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True


# print(palindrome("bearaeb"))  # True
# print(palindrome("Whatever revetahW"))  # True
# print(palindrome("Aloha, how are you today?"))  # False


# 4. Write a function called "pyramid" that takes an integer as input, and prints a pyramid in the following pattern:

# pyramid(1)
# *

# pyramid(2)
#  *
# ***

# pyramid(4)
#    *
#   ***
#  *****
# *******


def pyramid(n):
    for i in range(1, n + 1):
        print(f"{' ' * (n - i)}{'*' * (i * 2 - 1)}")


# pyramid(1)
# pyramid(2)
# pyramid(4)


# 5. Write a function called "inversePyramid" that draws pyramid upside down.
def inversePyramid(n):
    for i in range(n, 0, -1):
        print(f"{' ' * (n - i)}{'*' * (i * 2 - 1)}")


# inversePyramid(4)


# 6. Given a list of ints, return True if the list contains a 3 next to a 3.
def has_33(arr):
    for i in range(len(arr) - 1):
        if arr[i] == 3 and arr[i + 1] == 3:
            return True
    return False


print(has_33([1, 5, 7, 3, 3]))  # True
print(has_33([]))  # False
print(has_33([4, 3, 2, 1, 0]))  # False
