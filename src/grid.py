class Grid:
    def __init__(self, grid_size):
        self.grid_size = grid_size

    def get_grid(self):
        # Grid setup
        the_grid = [[' '] * self.grid_size for _ in range(self.grid_size)]
        return the_grid

    @staticmethod
    def print_board(board):
        # Draws the grid. Nothing else to say, really.
        row = ""
        row_split = ""
        count = 0
        count2 = 0
        for i in board:
            count += 1
            for j in i:
                count2 += 1
                if count2 == len(i):
                    row += j
                    print(row)
                    row = ""
                    row_split += "-"
                    count2 = 0
                else:
                    row += j + " | "
                    row_split += "----"
            if count != len(board):
                print(row_split)
                row_split = ""
        print()