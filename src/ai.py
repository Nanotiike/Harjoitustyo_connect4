# Contains Ai class which will be the main focus of the project. The Ai class will use the minimax algorithm and alhpa-beta pruning algorithm.
import random

class Ai:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move_rng(self, board):
        # Makes a random move on the board.
        column = random.randint(0, 6)
        while not board.make_move(column, self.symbol):
            column = random.randint(0, 6)
