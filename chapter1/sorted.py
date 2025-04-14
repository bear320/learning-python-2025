x = [4, 2, 3, 1]

y = sorted(x)
print(y)  # [1, 2, 3, 4]

z = sorted(x, reverse=True)  # keyword arguments
print(z)  # [4, 3, 2, 1]

# tuple
a = (4, 2, 3, 1)
b = sorted(x)
print(a)  # (4, 2, 3, 1)
print(b)  # [1, 2, 3, 4]

# dictionary keys
i = {"b": 4, "d": 2, "c": 3, "a": 1}
j = sorted(i)
print(i)  # {'b': 4, 'd': 2, 'c': 3, 'a': 1}
print(j)  # ['a', 'b', 'c', 'd']

# set
m = {4, 2, 3, 1}
n = sorted(m)
print(m)  # {1, 2, 3, 4}
print(n)  # [1, 2, 3, 4]

# string
k = "How are you?"
l = sorted(k)
print(k)  # How are you?
print(l)  # [' ', 'H', 'a', 'e', 'o', 'o', 'r', 'u', 'w', '?']
