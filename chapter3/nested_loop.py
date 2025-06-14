counter = 0

for i in "1234":
    for j in "abcd":
        print(f"i={i}, j={j}")
        counter += 1

print(f"Total iterations: {counter}")
