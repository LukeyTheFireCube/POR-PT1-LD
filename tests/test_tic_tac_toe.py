import unittest
from src.grid import Grid

class Tests(unittest.TestCase):
    def test_winning_game(self):
        p1 = "X"
        p2 = "O"
        grid = Grid(3)
        board = grid.get_grid()

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