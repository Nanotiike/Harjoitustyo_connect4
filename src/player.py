# Contains the player class, which is used to represent a player in the game and handles player inputs.

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        move = input(f"{self.name} make your move (1-7): ")
        while not move.isdigit() or not 1 <= int(move) <= 7 or not board.make_move(int(move) - 1, self.symbol):
            if not move.isdigit():
                print("Invalid input, please enter a number")
            elif not 1 <= int(move) <= 7:
                print("Invalid input, please enter a number between 1 and 7")
            elif not board.make_move(int(move) - 1, self.symbol):
                print("Column is full, please choose another column")
            move = input(f"{self.name} make your move (1-7): ")
