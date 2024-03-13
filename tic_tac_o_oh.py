# A monolithic and poorly written tic-tac-toe for you to refactor.
# Generated by ChatGPT 4, refactored by Luke Downes.
# Game state
from src.grid import Grid
from src.conditions import Conditions
import os

def get_items():
    p1 = "X"
    p2 = "O"
    empty = " "
    grid = Grid(3)
    board = grid.get_grid()
    conditions = Conditions(board, empty, p1, p2)
    return p1, p2, empty, grid, board, conditions

def check_input(input, board):
    if input.isdigit():
        if int(input) > len(board):
            print("Move is out of range of board, try again.")
            return "Invalid"
    else:
        print("Invalid move, try again.")
        return "Invalid"
    return "Valid"

def gameplay():
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
                row = input("Column: ")
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
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear()

# setup
P1, P2, Empty, the_grid, the_board, the_conditions = get_items()
the_grid.print_board(the_board)
gameplay()

# Post-game
while True:
    dummy = input("Play again? (Y/N): ")
    while dummy.upper() != "Y" and dummy.upper() != "N":
        dummy = input("Play again? (Y/N): ")
    if dummy.upper() == "Y":
        the_grid.print_board(the_board)
        gameplay()
    elif dummy.upper() == "N":
        exit(0)


