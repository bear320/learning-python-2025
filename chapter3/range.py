print(range(5))  # range(0, 5)

# range() returns an iterable object
# range(stop)
for i in range(5):
    print(f"Current number: {i}")

# range(start, stop)
for j in range(10, 15):
    print(f"Current number: {j}")

# range(start, stop, step)
for k in range(0, 20, 5):
    print(f"Current number: {k}")

for l in range(20, 0, -5):
    print(f"Current number: {l}")

# typecasting range to list
my_list = list(range(0, 15, 2))
print(my_list)  # [0, 2, 4, 6, 8, 10, 12, 14]
