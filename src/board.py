"""Contains the board class, which is responsible for the game board, making moves and checking for victory."""
testing_board = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," ","R","R"," "],["Y"," "," ","Y","Y","R"," "]]
play_board = [[" "for _ in range(7)] for _ in range(6)]

class Board:
    def __init__(self):
        self.board = testing_board

    def make_move(self, column, symbol):
        """Makes a move in the given column with the given symbol."""
        while True:
            for i in range(5, -1, -1):
                if self.board[i][column] == " ":
                    self.board[i][column] = symbol
                    return True
            return False

    def check_for_winner(self):
        """Checks if there is a winner on the board."""
        winner = None
        for i in range(5, -1, -1):
            for j in range(7):
                if self.board[i][j] != " ":
                    if i - 3 >= 0 and self.board[i][j] == self.board[i - 1][j] == self.board[i - 2][j] == self.board[i - 3][j]:
                        winner = self.board[i][j]
                    if j + 3 < 7 and self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] == self.board[i][j + 3]:
                        winner = self.board[i][j]
                    if i + 3 < 6 and j + 3 < 7 and self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3]:
                        winner = self.board[i][j]
                    if i - 3 >= 0 and j + 3 < 7 and self.board[i][j] == self.board[i - 1][j + 1] == self.board[i - 2][j + 2] == self.board[i - 3][j + 3]:
                        winner = self.board[i][j]
                if winner is not None:
                    break
            if winner is not None:
                break
        return winner
    
    def undo_move(self, column):
        """Undoes a move in the given column."""
        for i in range(6):
            if self.board[i][column] != " ":
                self.board[i][column] = " "
                break

    def __str__(self):
        """Returns the board as a string."""
        board_string = ""
        board_string += "-----------------------------\n"
        for i in range(6):
            board_string += "| "
            for j in range(7):
                board_string += self.board[i][j] + " | "
            board_string += "\n-----------------------------\n"
        board_string += "- 1 - 2 - 3 - 4 - 5 - 6 - 7 -"
        return board_string
