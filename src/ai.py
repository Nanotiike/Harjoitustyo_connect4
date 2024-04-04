"""Contains Ai class which will be the main focus of the project. The Ai class will use the minimax algorithm and alhpa-beta pruning algorithm."""
import random

class Ai:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.not_symbol = "Y" if symbol == "R" else "R"
        self.evaluate = 0
        self.moves = [3,4,2,5,1,6,0]

    def make_move_rng(self, board):
        """Makes a random move on the board."""
        column = random.randint(0, 6)
        while not board.make_move(column, self.symbol):
            column = random.randint(0, 6)

    def make_move(self, board):
        """Makes a move on the board using the minimax algorithm."""
        self.minimax(board, 4, True)
        for column in self.moves:
            if board.make_move(column, self.symbol):
                return

    def minimax(self, board, depth, is_maximizing):
        """The minimax algorithm."""
        if depth == 0 or board.check_for_winner() is not None:
            self.evaluate = self.score(board)
            return self.evaluate
        if is_maximizing:
            self.evaluate = -100000
            for column in self.moves:
                if board.make_move(column, self.symbol):
                    self.evaluate = max(self.evaluate, self.minimax(board, depth - 1, False))
                    board.undo_move(column)
            return self.evaluate
        else:
            self.evaluate = 100000
            for column in self.moves:
                if board.make_move(column, self.not_symbol):
                    self.evaluate = min(self.evaluate, self.minimax(board, depth - 1, True))
                    board.undo_move(column)
            return self.evaluate

    def score(self, board):
        """How the board is evaluated for minimax."""
        if board.check_for_winner() == self.symbol:
            return 100
        elif board.check_for_winner() == self.not_symbol:
            return -100
        else:  
            return 0
