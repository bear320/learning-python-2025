# 1.
def mySort(arr):
    n = len(arr)
    for i in range(n):
        # i is the number of elements already sorted
        # n - i - 1 is the number of elements to compare
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(mySort([17, 0, -3, 2, 1, 0.5]))  # returns [-3, 0, 0.5, 1, 2, 17]
