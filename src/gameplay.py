from src.grid import Grid
from src.conditions import Conditions
import os

def get_items():
    # Required items for the tic-tac-toe game
    p1 = "X"
    p2 = "O"
    empty = " "
    grid = Grid(3)
    board = grid.get_grid()
    conditions = Conditions(board, empty, p1, p2)
    return p1, p2, empty, grid, board, conditions

def check_input(input_text, board):
    # Checks if the given input is within range of the tic-tac-toe board.
    if input_text.isdigit():
        if int(input_text) > len(board) or int(input_text) == 0:
            print("Move is out of range of board, try again.")
            return "Invalid"
    else:
        print("Invalid move, try again.")
        return "Invalid"
    return "Valid"

def gameplay():
    # Gameplay loop
    p1, p2, empty, grid, board, conditions = get_items()
    condition = ""
    player = p1
    while condition == "":
        # Get next move
        while True:
            print(f"Next move for player {player}:")
            row = input("Row: ")
            validity = check_input(row, board)
            while validity == "Invalid":
                row = input("Row: ")
                validity = check_input(row, board)

            column = input("Column: ")
            validity = check_input(column, board)
            while validity == "Invalid":
                column = input("Column: ")
                validity = check_input(column, board)

            if board[int(row)-1][int(column)-1] == empty:
                board[int(row) - 1][int(column) - 1] = player
                break
            else:
                print("That tile is already claimed.")

        grid.print_board(board)
        condition = conditions.check_conditions()
        if player == p1:
            player = p2
        else:
            player = p1

def clear():
    # Refreshes the terminal screen after a player move
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# setup
P1, P2, Empty, the_grid, the_board, the_conditions = get_items()
the_grid.print_board(the_board)
gameplay()

# Post-game, asks if the user wants to play again, if yes, starts a new game.
while True:
    dummy = input("Play again? (Y/N): ")
    while dummy.upper() != "Y" and dummy.upper() != "N":
        dummy = input("Play again? (Y/N): ")
    if dummy.upper() == "Y":
        the_grid.print_board(the_board)
        gameplay()
    elif dummy.upper() == "N":
        exit(0)