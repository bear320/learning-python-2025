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

# difference()
s1 = {1, 2, 3}
s2 = {3, 4, 5}

diff = s1.difference(s2)
print(diff)  # Output: {1, 2}

diff = s2.difference(s1)
print(diff)  # Output: {4, 5}

# intersection()
s1 = {1, 2, 3}
s2 = {3, 4, 5}

inter = s1.intersection(s2)
print(inter)  # Output: {3}

inter = s2.intersection(s1)
print(inter)  # Output: {3}

# union()
s1 = {1, 2, 3}
s2 = {3, 4, 5}

union = s1.union(s2)
print(union)  # Output: {1, 2, 3, 4, 5}

union = s2.union(s1)
print(union)  # Output: {1, 2, 3, 4, 5}

# isdisjoint()
s1 = {1, 2, 3}
s2 = {4, 5, 6}

is_disjoint = s1.isdisjoint(s2)
print(is_disjoint)  # Output: True

# issubset()
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}

is_subset = s1.issubset(s2)
print(is_subset)  # Output: True

is_subset = s2.issubset(s1)
print(is_subset)  # Output: False

# issuperset()
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}

is_superset = s1.issuperset(s2)
print(is_superset)  # Output: False

is_superset = s2.issuperset(s1)
print(is_superset)  # Output: True
