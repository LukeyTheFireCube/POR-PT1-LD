import math
class Conditions:
    def __init__(self, board, empty=" ", p1="X", p2="O"):
        self.board = board
        self.empty = empty
        self.p1 = p1
        self.p2 = p2

    def check_conditions(self):
        # Check for win
        win_conditions = self.get_win_conditions()
        for wc in win_conditions:
            tick1 = 0
            tick2 = 0
            for i in range(len(wc)):
                if self.board[wc[i]] == self.p1:
                    tick1 += 1
                elif self.board[wc[i]] == self.p2:
                    tick2 += 1
            if tick1 == math.sqrt(len(self.board)):
                print("Player", self.p1, "wins!")
                exit(0)
            elif tick2 == math.sqrt(len(self.board)):
                print("Player", self.p2, "wins!")
                exit(0)
            elif self.empty not in self.board:
                print("It's a tie!")
                exit(0)

    def get_win_conditions(self):
        repeater = int(math.sqrt(len(self.board)))
        wc = []

        # Row win conditions
        count = 0
        for i in range(repeater):
            wc_part = []
            for j in range(repeater):
                wc_part.append(count)
                count += 1
            wc.append(wc_part)

        # Column win conditions
        count = 0
        column = 0
        for i in range(repeater):
            wc_part = []
            for j in range(repeater):
                wc_part.append(count)
                count += repeater
            wc.append(wc_part)
            column += 1
            count = column

        # Forward slash win condition
        count = 0
        wc_part = []
        for i in range(repeater):
            wc_part.append(count)
            count += repeater + 1
        wc.append(wc_part)

        # Backward slash win condition
        count = repeater - 1
        wc_part = []
        for i in range(repeater):
            wc_part.append(count)
            count += repeater - 1
        wc.append(wc_part)

        return wc