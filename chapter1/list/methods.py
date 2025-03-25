# insert()
friends = ["Oliver", "Wilson", "Alice"]
friends.insert(1, "Bob")
print(friends)  # ['Oliver', 'Bob', 'Wilson', 'Alice']

# remove()
friends = ["Oliver", "Wilson", "Alice"]
friends.remove("Wilson")
print(friends)  # ['Oliver', 'Alice']

# friends.remove("Sally")  # ValueError: list.remove(x): x not in list

# clear()
friends.clear()
print(friends)  # []

# sort()
friends = ["Oliver", "Wilson", "Alice"]
friends.sort()
print(friends)  # ['Alice', 'Oliver', 'Wilson']

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, -5]
numbers.sort()
print(numbers)  # [-5, 1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

# reverse()
friends = ["Oliver", "Wilson", "Alice"]
friends.reverse()
print(friends)  # ['Alice', 'Wilson', 'Oliver']

other_friends = ["Bob", "Charlie", "David"]
other_friends = other_friends[::-1]
print(other_friends)  # ['David', 'Charlie', 'Bob']
