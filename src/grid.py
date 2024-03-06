import math
import os
class Grid:
    def __init__(self, grid_size):
        self.grid_size = grid_size

    def get_grid(self):
        the_grid = [" "] * self.grid_size * self.grid_size
        return the_grid

    @staticmethod
    def print_board(board):
        row = ""
        row_split = ""
        count = 0
        count2 = 0
        for i in board:
            count += 1
            count2 += 1
            if count == math.sqrt(len(board)):
                row += i
                print(row)
                row = ""
                row_split += "-"
                count = 0
                if not count2 == len(board):
                    print(row_split)
                    row_split = ""
            else:
                row += i + " | "
                row_split += "----"
        print()