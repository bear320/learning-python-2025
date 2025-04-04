s = set()

# add()
s.add(1)
print(s)  # Output: {1}

s.add(2)
print(s)  # Output: {1, 2}

s.add(2)
print(s)  # Output: {1, 2} (no duplicate)

s.add(3)
print(s)  # Output: {1, 2, 3}

# discard()
s.discard(1)
print(s)  # Output: {2, 3}

s.discard(4)  # No error, even though 4 is not in the set
print(s)  # Output: {2, 3}

# clear()
s.clear()
print(s)  # Output: set() (empty set)
