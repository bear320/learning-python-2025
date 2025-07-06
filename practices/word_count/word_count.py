from sys import argv  # argv is a list of command line arguments

if len(argv) < 2:
    print("Please provide a file name as an argument.")
else:
    file = open(argv[1])
    text = file.read()

    # line count
    lines = len(text.splitlines())

    # word and character count
    words = 0
    characters = 0
    for line in text.splitlines():
        words += len(line.split(" "))
        characters += len(line)

    print(f"Number of lines: {lines}")
    print(f"Number of words: {words}")
    print(f"Number of characters: {characters}")
