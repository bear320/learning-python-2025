str = "Python"
i = 4

# indexing
print(str[0])  # P
print(str[1])  # y
print(str[i])  # o

# negative indexing
print(str[-1])  # n
print(str[-2])  # o

# IndexError
# print(str[6])  # IndexError: string index out of range
# print(str[-7])  # IndexError: string index out of range

# slicing
print(str[0:2])  # Py
print(str[2:5])  # tho
print(str[:3])  # Pyt

# step
print(str[0:5:2])  # Pto
print("abcdefgh"[::2])  # aceg
print("abcdefgh"[1::2])  # bdfh
print("abcdefgh"[::-1])  # hgfedcba
