import unittest

from src.conditions import Conditions
from src.grid import Grid



class Tests(unittest.TestCase):
    def test_winning_game(self):
        p1 = "X"
        p2 = "O"
        empty = " "
        grid = Grid(3)
        board = grid.get_grid()
        conditions = Conditions(board, empty, p1, p2)
        wc = conditions.get_win_conditions()

        board[0] = p1
        board[2] = p1
        board[5] = p1
        board[8] = p1

        board[1] = p2
        board[4] = p2
        board[6] = p2

        self.assertEqual([board[2], board[5], board[8]], ["X", "X", "X"])

if __name__ == "__main__":
    unittest.main()