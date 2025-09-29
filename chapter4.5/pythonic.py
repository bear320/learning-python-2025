# example 1: swapping values
a = 10
b = 5

# traditional way
# temp = a
# a = b
# b = temp

# pythonic way
a, b = b, a

print(a, b)

x = 10
y = 20
z = 30

x, y, z = z, x, y

print(x, y, z)


# example 2: unpacking values


# get_user_info(id) returns a tuple (user_name, user_email)
def get_user_info(user_id):
    return ("Alice", "alice@example.com")


name, email = get_user_info(1)
print(f"Name: {name}, Email: {email}")

# example 3: chaining comparisons

i = 0

# traditional way
if i > 10 and i < 100:
    print("i is between 10 and 100")

# pythonic way
if 10 < i < 100:
    print("i is between 10 and 100")

# example 4: membership operator
cmd = input("Enter command: ").strip().lower()

# traditional way
if cmd == "cd" or cmd == "ls" or cmd == "rm":
    print(f"Executing {cmd} command")
else:
    print("Unknown command")

# pythonic way
if cmd in ("cd", "ls", "rm"):
    print(f"Executing {cmd} command")
else:
    print("Unknown command")
