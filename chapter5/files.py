file = open("chapter5/my_file.txt", "r")

print(file.read(5))
print(file.read(3))
file.seek(0)
print(file.read())

print(type(file.read()))  # <class 'str'>

file.close()
