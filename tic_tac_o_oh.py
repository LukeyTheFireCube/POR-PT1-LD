'''A monolithic and poorly written tic-tac-toe for you to refactor.'''
# Generated by ChatGPT 4, refactored by Luke Downes
# Game state
from src.grid import Grid
from src.conditions import Conditions
import os
p1 = "X"
p2 = "O"
empty = " "
grid = Grid(3)
board = grid.get_grid()
conditions = Conditions(board, empty, p1, p2)

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear()

# Game loop
while True:
    # Get next move
    while True:
        player = p1 if board.count(empty) % 2 == 1 else p2
        grid.print_board(board)
        move = input(f"Next move for player {player} (1-{len(board)}): ")
        if move.isdigit():
            move = int(move)
            move -= 1
            if 0 <= move <= (len(board)-1) and board[move] == empty:
                board[int(move)] = player
                break
            else:
                clear()
                print("Move is out of range of board, try again.")
        else:
            clear()
            print("Invalid move, try again.")
    conditions.check_conditions()
