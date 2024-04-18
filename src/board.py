"""Contains the board class, which is responsible for the game board, making moves and checking for victory."""
testing_board = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," ","R","R"," "],["Y"," "," ","Y","Y","R"," "]]
play_board = [[" "for _ in range(7)] for _ in range(6)]

class Board:
    def __init__(self):
        self.board = play_board

    def make_move(self, column, symbol):
        """Makes a move in the given column with the given symbol."""
        for i in range(5, -1, -1):
            if self.board[i][column] == " ":
                self.board[i][column] = symbol
                return i
        return False

    def check_for_winner(self, x, y):
        """Checks if there is a winner on the board."""
        symbol = self.board[y][x]
        counter = 1
        temp = -1
        while y+temp>=0 and self.board[y+temp][x] == symbol:
            counter += 1
            temp -= 1
        temp = 1
        while y+temp<=5 and self.board[y+temp][x] == symbol:
            counter += 1
            temp += 1
        if counter >= 4:
            return symbol
        counter = 1
        temp = -1
        while x+temp>=0 and self.board[y][x+temp] == symbol:
            counter += 1
            temp -= 1
        temp = 1
        while x+temp<=6 and self.board[y][x+temp] == symbol:
            counter += 1
            temp += 1
        if counter >= 4:
            return symbol
        counter = 1
        temp = -1
        while y+temp>=0 and x+temp>=0 and self.board[y+temp][x+temp] == symbol:
            counter += 1
            temp -= 1
        temp = 1
        while y+temp<=5 and x+temp<=6 and self.board[y+temp][x+temp] == symbol:
            counter += 1
            temp += 1
        if counter >= 4:
            return symbol
        counter = 1
        temp = -1
        while x+temp>=0 and y-temp<=5 and self.board[y-temp][x+temp] == symbol:
            counter += 1
            temp -= 1
        temp = 1
        while x+temp<=6 and y-temp>=0 and self.board[y-temp][x+temp] == symbol:
            counter += 1
            temp += 1
        if counter >= 4:
            return symbol
        return None


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
