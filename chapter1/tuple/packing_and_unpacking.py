# tuple packing
x = 10, 15
print(x)  # (10, 15)
print(type(x))  # <class 'tuple'>

# tuple unpacking
person = ("Alice", 25, "New York")
name, age, city = person
print(name)  # Alice
print(age)  # 25
print(city)  # New York

# tuple unpacking with asterisk
x = 10, 15, 20, 25
a, b, *c = x
print(a)  # 10
print(b)  # 15
print(c)  # [20, 25]

# tuple upacking and packing
m = 15
n = 20
m, n = n, m
print(m)  # 20
print(n)  # 15
