"""Contains the player class. Used to represent a player in the game and handles player inputs."""
import sys

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def choose_move(self, board):
        """Asks the player for input and updates the board according to it."""
        move = input(f"{self.name} make your move (1-7), or quit (q): ")
        if move == "q":
            sys.exit()
        if move.isdigit() and 1 <= int(move) <= 7:
            temp = board.make_move(int(move) - 1, self.symbol)
        while not move.isdigit() or not 1 <= int(move) <= 7 or temp is False:
            if not move.isdigit():
                print("Invalid input, please enter a number")
            elif not 1 <= int(move) <= 7:
                print("Invalid input, please enter a number between 1 and 7")
            elif temp is False:
                print("Column is full, please choose another column")
            move = input(f"{self.name} make your move (1-7), or quit (q): ")
            if move == "q":
                sys.exit()
            if move.isdigit() and 1 <= int(move) <= 7:
                temp = board.make_move(int(move) - 1, self.symbol)
        return (temp, int(move)-1)
