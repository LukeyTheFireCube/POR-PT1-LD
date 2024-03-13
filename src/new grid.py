from grid import Grid
from conditions import Conditions

grid = Grid(3)
board = grid.get_grid()
print(board)
grid.print_board(board)

cond = Conditions(board, " ", "X", "O")
wc = cond.get_win_conditions(len(board[0]))
# Target winning conditions for a 3x3 grid:
# [0, 0], [0, 1], [0, 2]
# [1, 0], [1, 1], [1, 2]
# [2, 0], [2, 1], [2, 2]

# [0, 0], [1, 0], [2, 0]
# [0, 1], [1, 1], [2, 2]
# [0, 2], [1, 2], [2, 2]

# [0, 0], [1, 1], [2, 2]
# [0, 2], [1, 1], [2, 0]
print(wc)

board[0][0] = "X"
board[1][1] = "X"
board[2][2] = "X"
print(board)
cond.check_conditions()
