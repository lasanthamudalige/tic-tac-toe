import random
import sys


def main():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    print_map(board)

    while " " in board:
        # get user input
        position = get_move()
        # move move 'x' to the position in the map
        move(board, position, "x")
        # computer's move
        computer_move(board)
        print_map(board)
        get_winner(board)

    print("Nobody won. Game is a draw")
    sys.exit()


def print_map(board):
    col = 0
    row = 0
    # after printing 3 " " s. move to the next line.
    for i in board:
        if col == 2:
            print(f"{i}", end="\n")
            if row != 2:
                print("_________")
            print()
            col = 0
            row += 1
        else:
            print(f"{i} | ", end="")
            col += 1


def get_move():
    # if move is between 1 - 9. then return the move
    while True:
        try:
            move = int(input("Move: "))

            if move >= 1 and move <= 9:
                return move

        except ValueError:
            print("Invalid input")


def move(board, position, symbol):
    # if position is empty. then add it to the map
    if board[position - 1] == " ":
        board[position - 1] = symbol
    else:
        print("Position is already filled!")


def computer_move(board):
    position = random.randint(0, 8)

    # is there are empty slots in the map. then add 'o' to the map
    if " " in board:
        if board[position] == " ":
            board[position] = "o"
        else:
            computer_move(board)


def get_winner(board):
    # player's winning opportunity
    if board[0] == "x" and board[1] == "x" and board[2] == "x":
        print("You won!")
        sys.exit()
    elif board[3] == "x" and board[4] == "x" and board[5] == "x":
        print("You won!")
        sys.exit()
    elif board[6] == "x" and board[7] == "x" and board[8] == "x":
        print("You won!")
        sys.exit()
    elif board[0] == "x" and board[3] == "x" and board[6] == "x":
        print("You won!")
        sys.exit()
    elif board[1] == "x" and board[4] == "x" and board[7] == "x":
        print("You won!")
        sys.exit()
    elif board[2] == "x" and board[5] == "x" and board[8] == "x":
        print("You won!")
        sys.exit()
    elif board[0] == "x" and board[4] == "x" and board[8] == "x":
        print("You won!")
        sys.exit()
    elif board[2] == "x" and board[4] == "x" and board[6] == "x":
        print("You won!")
        sys.exit()
    # computer's winning opportunity
    elif board[0] == "o" and board[1] == "o" and board[2] == "o":
        print("computer won! try again")
        sys.exit()
    elif board[3] == "o" and board[4] == "o" and board[5] == "o":
        print("computer won! try again")
        sys.exit()
    elif board[6] == "o" and board[7] == "o" and board[8] == "o":
        print("computer won! try again")
        sys.exit()
    elif board[0] == "o" and board[3] == "o" and board[6] == "o":
        print("computer won! try again")
        sys.exit()
    elif board[1] == "o" and board[4] == "o" and board[7] == "o":
        print("computer won! try again")
        sys.exit()
    elif board[2] == "o" and board[5] == "o" and board[8] == "o":
        print("computer won! try again")
        sys.exit()
    elif board[0] == "o" and board[4] == "o" and board[8] == "o":
        print("computer won! try again")
        sys.exit()
    elif board[2] == "o" and board[4] == "o" and board[6] == "o":
        print("computer won! try again")
        sys.exit()


main()
