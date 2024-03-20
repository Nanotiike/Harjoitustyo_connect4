# Contains the board class, which is responsible for the game board, making moves and checking for victory.
class Board:
    def __init__(self):
        self.board = [[" "for _ in range(7)] for _ in range(6)]

    def make_move(self):
        pass

    def is_winner(self):
        pass

    def print_board(self):
        print("-----------------------------")
        for i in range(6):
            print("|", end=" ")
            for j in range(7):
                print(self.board[i][j], end=" ")
                print("|", end=" ")
            print("\n-----------------------------")
        print("- 1 - 2 - 3 - 4 - 5 - 6 - 7 -")