myString = "Hello"

# length
print(len(myString))  # 5

# typecasting
print(int("5"))  # 5
print(float("5.5"))  # 5.5
print(str(5))  # '5'

# upper and lower
print(myString.upper())  # HELLO
print(myString.lower())  # hello

# isupper and islower
print(myString.isupper())  # False
print(myString.islower())  # False

# method chaining
print(myString.upper().isupper())  # True
print(myString.lower().islower())  # True

# index
print(myString.index("e"))  # 1
print(myString.index("l"))  # 2
print(myString.index("lo"))  # 3
# print(myString.index("z"))  # ValueError: substring not found

# replace
print(myString.replace("H", "B"))  # Bello

# split
sentence = "Today is a good day."
print(sentence.split())  # ['Today', 'is', 'a', 'good', 'day.']

# list >>> typecasting
print(list(myString))  # ['H', 'e', 'l', 'l', 'o']
print(
    list(sentence)
)  # ['T', 'o', 'd', 'a', 'y', ' ', 'i', 's', ' ', 'a', ' ', 'g', 'o', 'o', 'd', ' ', 'd', 'a', 'y', '.']

# format
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
# My name is Alice and I am 25 years old.
print("My name is {2} and I am {1} years old.".format("Oliver", 27, "Olie"))
# My name is Olie and I am 27 years old.
print("My name is {name} and I am {age} years old.".format(name="Bob", age=30))
# My name is Bob and I am 30 years old.
print("I have a string {}".format(["hello", "world"]))
# I have a string ['hello', 'world']

# fstring
print(f"My name is {name} and I am {age} years old.")
# My name is Alice and I am 25 years old.

# count
print(myString.count("l"))  # 2
print(sentence.count("good"))  # 1
print("Good day is a good day.".lower().count("good"))  # 2

# find
print(myString.find("l"))  # 2
print(myString.find("z"))  # -1

# startswith and endswith
print(myString.startswith("H"))  # True
print(myString.startswith("He"))  # True
print(myString.endswith("z"))  # False
