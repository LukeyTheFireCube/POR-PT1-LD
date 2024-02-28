class Grid:
    def __init__(self, grid_size):
        self.grid_size = grid_size

    def get_grid(self):
        a_row = [" "] * self.grid_size
        the_grid = a_row * self.grid_size
        return the_grid
    def print_board(self, board):
        for i in board:
            row = ""
            for j in i:
                row += j + " | "
            print(row)
            print("---------")
        print()