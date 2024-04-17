"""Contains Ai class which will be the main focus of the project. The Ai class will use the minimax algorithm and alhpa-beta pruning algorithm."""
"""The minimax algorithm is an algorithm used for two-player games. 
The minimax algorithm is a recusrisve algorithm used to determine the best possible move when you don't know the opponents move. 
The algorithm assumes that the opponent will play the best possible move for them, thus the algorithm will try to minimize the maximum loss."""
"""The alpha-beta pruning algorithm is an optimization technique for the minimax algorithm. 
It reduces the number of nodes that are evaluated by the minimax algorithm in its search tree. 
The algorithm maintains two values, alpha and beta, which represent the minimum score that the maximizing player is assured of and the maximum score that the minimizing player is assured of respectively. 
Based on these two values the algorithm prunes the nodes that are not needed to be evaluated."""
import random

class Ai:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.not_symbol = "Y" if symbol == "R" else "R"
        self.moves = [3,4,2,5,1,6,0]

    def make_move_rng(self, board):
        """Makes a random move on the board."""
        column = random.randint(0, 6)
        while not board.make_move(column, self.symbol):
            column = random.randint(0, 6)
        return column

    def choose_move(self, board):
        """Makes a move on the board using the minimax algorithm."""
        move = self.minimax(board, 5, True, 0, 0)
        return move
            

    def minimax(self, board, depth, is_maximizing, x, y):
        """The minimax algorithm."""
        evaluate = 0
        best_move = 0
        winner = board.check_for_winner(x, y)
        if winner == self.symbol:
            return (10000, -1)
        elif winner == self.not_symbol:
            return (-10000, -1)
        # to-do: check if board is full, by calculating moves made (42 moves)
        if depth == 0:
            evaluate = self.score(depth, board)
            return (evaluate, -1)
        if is_maximizing:
            evaluate = -100000
            for column in self.moves:
                row = board.make_move(column, self.symbol)
                if row is not False:
                    temp = self.minimax(board, depth - 1, False, column, row)
                    board.undo_move(column)
                    if evaluate < temp[0]:
                        evaluate = temp[0]
                        best_move = column
            return (evaluate, best_move)
        else:
            evaluate = 100000
            for column in self.moves:
                row = board.make_move(column, self.not_symbol)
                if row is not False:
                    temp = self.minimax(board, depth - 1, True, column, row)
                    board.undo_move(column)
                    if evaluate > temp[0]:
                        evaluate = temp[0]
                        best_move = column
            return (evaluate, best_move)

    def score(self, depth, board):
        """How the board is evaluated for minimax."""
        return 0

    def check_valid_moves():
        pass
