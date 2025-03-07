friend1 = "Oliver"
friend2 = "Wilson"
friend3 = "Alice"
print(f"{friend1}, {friend2} and {friend3} are my friends.")

friends = ["Oliver", "Wilson", "Alice"]
print(f"{friends[0]}, {friends[1]} and {friends[2]} are my friends.")

# Nested lists (lists within lists) can be used to represent a matrix.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][0])  # 1
print(matrix[1][1])  # 5

# length of a list
print(len(friends))  # 3

# indexing and slicing
print(friends[0])  # Oliver
print(friends[1])  # Wilson
print(friends[-1])  # Alice
print(friends[0:2])  # ['Oliver', 'Wilson']

# count and index
print(friends.count("Oliver"))  # 1
print(friends.index("Oliver"))  # 0

# concatenation
more_friends = ["Bob", "Charlie"]
all_friends = friends + more_friends
print(all_friends)  # ['Oliver', 'Wilson', 'Alice', 'Bob', 'Charlie']

# repetition
print(friends * 2)  # ['Oliver', 'Wilson', 'Alice', 'Oliver', 'Wilson', 'Alice']

# mutability
friends[0] = "Olivia"
print(friends)  # ['Olivia', 'Wilson', 'Alice']
