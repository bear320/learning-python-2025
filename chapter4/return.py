def addition(a, b):
    return a + b


result_1 = addition(5, 3)
result_2 = addition(10, 20)
result_3 = addition(15, 25)

print(result_1 + result_2 + result_3)


# return in the loop
def loop(a, b):
    for i in range(a):
        for j in range(b):
            if i == 3 and j == 4:
                return
            print(f"i: {i}, j: {j}")


loop(5, 6)
