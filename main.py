import random
import sys


def main():
    map = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    print_map(map)

    while " " in map:
        # get user input
        position = get_move()
        # move move 'x' to the position in the map
        move(map, position, "x")
        # computer's move
        computer_move(map)
        print_map(map)
        get_winner(map)

    print("Nobody won. Game is a draw")
    sys.exit()


def print_map(map):
    col = 0
    row = 0
    # after printing 3 " " s. move to the next line.
    for i in map:
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


def move(map, position, symbol):
    # if position is empty. then add it to the map
    if map[position - 1] == " ":
        map[position - 1] = symbol
    else:
        print("Position is already filled!")


def computer_move(map):
    position = random.randint(0, 8)

    # is there are empty slots in the map. then add 'o' to the map
    if " " in map:
        if map[position] == " ":
            map[position] = "o"
        else:
            computer_move(map)


def get_winner(map):
    # player's winning opportunity
    if map[0] == "x" and map[1] == "x" and map[2] == "x":
        print("You won!")
        sys.exit()
    elif map[3] == "x" and map[4] == "x" and map[5] == "x":
        print("You won!")
        sys.exit()
    elif map[6] == "x" and map[7] == "x" and map[8] == "x":
        print("You won!")
        sys.exit()
    elif map[0] == "x" and map[3] == "x" and map[6] == "x":
        print("You won!")
        sys.exit()
    elif map[1] == "x" and map[4] == "x" and map[7] == "x":
        print("You won!")
        sys.exit()
    elif map[2] == "x" and map[5] == "x" and map[8] == "x":
        print("You won!")
        sys.exit()
    elif map[0] == "x" and map[4] == "x" and map[8] == "x":
        print("You won!")
        sys.exit()
    elif map[2] == "x" and map[4] == "x" and map[6] == "x":
        print("You won!")
        sys.exit()
    # computer's winning opportunity
    elif map[0] == "o" and map[1] == "o" and map[2] == "o":
        print("computer won! try again")
        sys.exit()
    elif map[3] == "o" and map[4] == "o" and map[5] == "o":
        print("computer won! try again")
        sys.exit()
    elif map[6] == "o" and map[7] == "o" and map[8] == "o":
        print("computer won! try again")
        sys.exit()
    elif map[0] == "o" and map[3] == "o" and map[6] == "o":
        print("computer won! try again")
        sys.exit()
    elif map[1] == "o" and map[4] == "o" and map[7] == "o":
        print("computer won! try again")
        sys.exit()
    elif map[2] == "o" and map[5] == "o" and map[8] == "o":
        print("computer won! try again")
        sys.exit()
    elif map[0] == "o" and map[4] == "o" and map[8] == "o":
        print("computer won! try again")
        sys.exit()
    elif map[2] == "o" and map[4] == "o" and map[6] == "o":
        print("computer won! try again")
        sys.exit()


main()
