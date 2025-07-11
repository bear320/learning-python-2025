# parameters are local variables in the function
x = 5


def change(val):
    # val = x (copy by value) => val = 5
    val = 10


change(x)
print(x)  # x remains unchanged, prints 5

y = [1, 2, 3]


def change_list(lst):
    # lst = y (copy by reference) => lst points to the same list as y
    lst[0] = 10


change_list(y)
print(y)  # y is changed, prints [10, 2, 3]


# How can we change any copy by value global variable?
a = 10


def change_global(val):
    global a  # declare a as global to modify it
    a = 25


change_global(a)
print(a)  # a is changed, prints 25
