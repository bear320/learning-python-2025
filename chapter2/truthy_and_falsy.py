# empty list: []
if []:
    print("Empty list is truthy")
else:
    print("Empty list is falsy")

# empty tuple: ()
if ():
    print("Empty tuple is truthy")
else:
    print("Empty tuple is falsy")

# empty dictionary: {}
if {}:
    print("Empty dictionary is truthy")
else:
    print("Empty dictionary is falsy")

# empty set: set()
if set():
    print("Empty set is truthy")
else:
    print("Empty set is falsy")

# empty string: ""
if "":
    print("Empty string is truthy")
else:
    print("Empty string is falsy")

# empty range: range(0)
if range(0):
    print("Empty range is truthy")
else:
    print("Empty range is falsy")

# bool()
print(bool([]))  # False
print(bool(()))  # False
print(bool({}))  # False
print(bool(set()))  # False
print(bool(""))  # False
print(bool(range(0)))  # False
