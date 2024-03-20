import unittest
from src.grid import Grid
from src.conditions import Conditions

class Tests(unittest.TestCase):
    def test_winning_game(self):
        p1 = "X"
        p2 = "O"
        grid = Grid(3)
        board = grid.get_grid()
        conditions = Conditions(board, ' ', p1, p2)

        board[0][0] = p1
        board[1][0] = p1
        board[2][0] = p1
        board[2][2] = p1

        board[0][2] = p2
        board[1][1] = p2
        board[2][1] = p2

        condition = conditions.check_conditions()

        self.assertEqual(condition, "P1 Win")

if __name__ == "__main__":
    unittest.main()