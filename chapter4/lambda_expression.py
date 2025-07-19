# lambda variable: operation

result_1 = (lambda x: x**2)(5)
print(result_1)  # 25

result_2 = (lambda x, y: (x + y, x - y))(3, 4)
print(result_2)  # (7, -1)

for item in map(lambda x: x**2, range(5)):
    print(item)  # 0, 1, 4, 9, 16

for item in filter(lambda x: x % 2 == 0, [0, 1, 2, 3, 4]):
    print(item)  # 0, 2, 4
