x = ([1, 2, 3], "Oliver")  # Could be used as a dictionary key? Nope!

# x[0] = "hello"
# print(x)  # 'tuple' object does not support item assignment

x[0][1] = 100
print(x)  # ([1, 100, 3], 'Oliver')

# If an element in a tuple is mutable, we can directly select and modify it.

# However, if we want to use a tuple as a dictionary key, all its elements must be immutable.

# Example of using a tuple as a dictionary key
# 15 # Yes, because numbers are immutable
# 'Oliver' # Yes, because integers are immutable
# ('hello', [1, 2, 3]) # No, because the list is mutable
# ['filename', (10, 20)] # No, because the list is mutable
# 'filename' # Yes, because strings are immutable
# ('filename', 100, 'extension') # Yes, because all elements in the tuple are immutable
