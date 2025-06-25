counter = 0
for letter in "How are you?":
    if counter < 5:
        print(letter)
    counter += 1

# enumerate
for i, letter in enumerate("How are you?"):
    if i < 5:
        print(i, letter)
