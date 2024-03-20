# Contains the board class, which is responsible for the game board, making moves and checking for victory.
class Board:
    def __init__(self):
        self.board = [[" "for _ in range(7)] for _ in range(6)]

    def make_move(self, column, symbol):
        while True:
            for i in range(5, -1, -1):
                if self.board[i][column] == " ":
                    self.board[i][column] = symbol
                    return True
            return False

    def check_for_winner(self):
        pass

    def __str__(self):
        board_string = ""
        board_string += "-----------------------------\n"
        for i in range(6):
            board_string += "| "
            for j in range(7):
                board_string += self.board[i][j] + " | "
            board_string += "\n-----------------------------\n"
        board_string += "- 1 - 2 - 3 - 4 - 5 - 6 - 7 -"
        return board_string