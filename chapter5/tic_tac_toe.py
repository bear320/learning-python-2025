row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
board = [row1, row2, row3]


def print_board():
    for row in board:
        print("|".join(row))
        if row is not board[-1]:
            print("-" * 5)


def user_choice():
    square = input("Choose a position from 1-9: ")

    while not square.isdigit() or int(square) not in range(1, 10):
        square = input("Invalid input. Choose a position from 1-9: ")

    return int(square)


# print_board()
user_choice()
