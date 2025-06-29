x = [1, 2, 3]
y = ["a", "b", "c"]

for tuple in zip(x, y):
    print(f"Current tuple: {tuple}")

i = [1, 2]
j = ["a", "b", "c"]
k = ["one", "two", "three", "four"]

for tuple in zip(i, j, k):
    print(f"Current tuple: {tuple}")
