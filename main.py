import random
import sys


def main():
    board = [["_", "_", "_"],
             ["_", "_", "_"],
             ["_", "_", "_"]]

    user = "O"
    computer = "X"

    on = True

    # Display board for the first time
    display_board(board)
    # This is to print a space after the board
    print()

    while on:
        # Get position from the user
        position = get_move()
        # Move to that position of if it is empty
        move(board, position, player=user)
        # Check if user got 3 squares in row
        won = get_winner(board, player=user)
        # Show the board after the move
        display_board(board)
        print()
        # If user got 3 squares in row, exit the game by showing 'user won!'
        if won == 1:
            print("You won! :)")
            on = False
            sys.exit(0)

        # Ask the computer to move
        computer_move(board)
        display_board(board)
        print()
        won = get_winner(board, player=computer)
        if won == 1:
            print("Computer won! :(")
            on = False
            sys.exit(0)


# Print the whole board
def display_board(board):
    print("| " + board[0][0] + " | " + board[0]
          [1] + " | " + board[0][2] + " | ")
    print("| " + board[1][0] + " | " + board[1]
          [1] + " | " + board[1][2] + " |")
    print("| " + board[2][0] + " | " + board[2]
          [1] + " | " + board[2][2] + " |")


# If move is between 1 - 9. then return the move
def get_move():
    try:
        move = int(input("Move (1-9): "))

        if move >= 1 and move <= 9:
            return move

    except ValueError:
        return get_move()


# If position is empty. then add it to the map
# Else return 1
def move(board, position, player):
    if position == 1:
        if board[0][0] == "_":
            board[0][0] = player
        else:
            return 1
    elif position == 2:
        if board[0][1] == "_":
            board[0][1] = player
        else:
            return 1
    elif position == 3:
        if board[0][2] == "_":
            board[0][2] = player
        else:
            return 1
    elif position == 4:
        if board[1][0] == "_":
            board[1][0] = player
        else:
            return 1
    elif position == 5:
        if board[1][1] == "_":
            board[1][1] = player
        else:
            return 1
    elif position == 6:
        if board[1][2] == "_":
            board[1][2] = player
        else:
            return 1
    elif position == 7:
        if board[2][0] == "_":
            board[2][0] = player
        else:
            return 1
    elif position == 8:
        if board[2][1] == "_":
            board[2][1] = player
        else:
            return 1
    elif position == 9:
        if board[2][2] == "_":
            board[2][2] = player
        else:
            return 1


# Generate a position and move to that
def computer_move(board):
    position = random.randint(1, 9)

    movement = move(board, position, "X")
    if movement == 1:
        computer_move(board)


# If user or computer got 3 squares in row. that one is going to win
def get_winner(board, player):
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return 1
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return 1
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return 1
    elif board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return 1
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return 1
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return 1
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return 1
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return 1


main()
