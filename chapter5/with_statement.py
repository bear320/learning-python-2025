with open("chapter5/my_file.txt", mode="r") as file:
    all_content = file.read()
    print(all_content)

with open("chapter5/my_file.txt", "a") as file:
    file.write("\nNew content added.")

with open("chapter5/my_file.txt", "w") as file:
    file.write("This will overwrite the entire file.")
