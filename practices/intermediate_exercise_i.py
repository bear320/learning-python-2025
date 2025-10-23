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


print(palindrome("bearaeb"))  # True
print(palindrome("Whatever revetahW"))  # True
print(palindrome("Aloha, how are you today?"))  # False
