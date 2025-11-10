COUNTER = 0
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
board = [row1, row2, row3]


def print_board():
    for row in board:
        print(" | ".join(row))
        if row is not board[-1]:
            print("-" * 9)


def user_choice():
    global COUNTER
    if COUNTER % 2 == 0:
        square = input("Player O, choose a position from 1-9: ")
    else:
        square = input("Player X, choose a position from 1-9: ")

    while not square.isdigit() or int(square) not in range(1, 10):
        square = input("Invalid input. Choose a position from 1-9: ")

    return int(square)


def place_marker(square):
    global COUNTER
    row = (square - 1) // 3
    col = (square - 1) % 3
    marker = "O" if COUNTER % 2 == 0 else "X"

    if board[row][col] == " ":
        board[row][col] = marker
        COUNTER += 1
        print_board()
    else:
        print("Position already taken. Try again.")
        new_square = user_choice()
        place_marker(new_square)


def check_winner():
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


def main():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while COUNTER < 9:
        square = user_choice()
        place_marker(square)

        if check_winner():
            print("Congratulations! Player", "O" if COUNTER % 2 == 1 else "X", "wins!")
            return

    print("Game over! It's a draw.")


if __name__ == "__main__":
    main()
