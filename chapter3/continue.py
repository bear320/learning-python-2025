for i in "ABCDE":
    if i == "C":
        print("Continuing the loop at C")
        continue
    print(f"Current letter: {i}")
print("Loop has ended.")

for i in "123":
    print(f"Now the current i is {i}")
    continue
    print("This line will never be executed because of continue")
