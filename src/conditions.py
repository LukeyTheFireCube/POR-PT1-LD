class Conditions:
    def __init__(self, board, empty=" ", p1="X", p2="O"):
        self.board = board
        self.empty = empty
        self.p1 = p1
        self.p2 = p2

    def check_conditions(self):
        condition = ""
        # Check for win
        win_conditions = self.get_win_conditions(len(self.board[0]))
        for wc in win_conditions:
            symbols = [self.board[i[0]][i[1]] for i in wc]
            if all(symbol == 'X' for symbol in symbols):
                print("Player", self.p1, "wins!")
                condition = "P1 Win"
            elif all(symbol == 'O' for symbol in symbols):
                print("Player", self.p2, "wins!")
                condition = "P2 Win"

        space = 0
        for row in self.board:
            if self.empty not in row:
                space += 1
            if space == len(self.board):
                print("It's a tie!")
                condition = "Tie"

        return condition

    @staticmethod
    def get_win_conditions(grid_size):
        wc = []

        # Row win conditions
        for i in range(grid_size):
            wc.append([(i, j) for j in range(grid_size)])

        # Column win conditions
        for j in range(grid_size):
            wc.append([(i, j) for i in range(grid_size)])

        # Backward slash win condition
        wc.append([(i, i) for i in range(grid_size)])

        # Forward slash win condition
        wc.append([(i, grid_size - 1 - i) for i in range(grid_size)])

        return wc