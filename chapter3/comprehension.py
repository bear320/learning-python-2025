x = [1, 2, 3, 4, 5]

# original method
squared_x = []

for i in x:
    squared_x.append(i**2)

print(squared_x)  # [1, 4, 9, 16, 25]

# list comprehension
squared_x = [i**2 for i in x if i > 2]

print(squared_x)  # [9, 16, 25]

# dictionary comprehension
squared_x = {i: i**2 for i in x if i > 2}

print(squared_x)  # {3: 9, 4: 16, 5: 25}

# set comprehension
squared_x = {i**2 for i in x if i > 2}

print(squared_x)  # {16, 9, 25}

# generator comprehension
squared_x = (i**2 for i in x if i > 2)

print(squared_x)

for i in squared_x:
    print(i)  # 9, 16, 25
