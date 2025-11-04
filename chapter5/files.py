file = open("chapter5/my_file.txt", "r")

print(file.read(5))
print(file.read(3))

file.seek(0)

print(file.read())  # returns a string
print(type(file.read()))  # <class 'str'>

file.seek(0)

print(file.readlines())  # returns a list of strings

# for line in file.readlines():
#     print(line)

file.seek(0)

print(file.readline())  # returns the first line
print(file.readline())  # returns the second line

file.close()
