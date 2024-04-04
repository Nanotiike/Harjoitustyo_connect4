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
        self.evaluate = 0
        self.moves = [3,4,2,5,1,6,0]

    def make_move_rng(self, board):
        """Makes a random move on the board."""
        column = random.randint(0, 6)
        while not board.make_move(column, self.symbol):
            column = random.randint(0, 6)
        return column

    def make_move(self, board):
        """Makes a move on the board using the minimax algorithm."""
        move_values = []
        moves = []
        move_made = False
        for column in self.moves:
            best_move = -100000
            if board.make_move(column, self.symbol):
                best_move = max(self.evaluate, self.minimax(board, 4, False))
                board.undo_move(column)
                move_values.append(best_move)
                moves.append(column)
                print(column, best_move,move_values,moves)
        for i in range(len(moves)):
            if move_values[i] == max(move_values):
                print("here")
                move_made = True
                board.make_move(moves[i], self.symbol)
                return((moves[i]+1,"minimax"))
        if not move_made:
            move = self.make_move_rng(board)
            return ((move+1,"rng"))
            

    def minimax(self, board, depth, is_maximizing):
        """The minimax algorithm."""
        if depth == 0 or board.check_for_winner() is not None:
            self.evaluate = self.score(depth, board)
            return self.evaluate
        if is_maximizing:
            self.evaluate = -100000
            for column in self.moves:
                if board.make_move(column, self.symbol):
                    # print(column,self.evaluate)
                    self.evaluate = max(self.evaluate, self.minimax(board, depth - 1, False))
                    board.undo_move(column)
            return self.evaluate
        else:
            self.evaluate = 100000
            for column in self.moves:
                if board.make_move(column, self.not_symbol):
                    # print(column,self.evaluate)
                    self.evaluate = min(self.evaluate, self.minimax(board, depth - 1, True))
                    board.undo_move(column)
            return self.evaluate

    def score(self, depth, board):
        """How the board is evaluated for minimax."""
        if board.check_for_winner() == self.symbol:
            return 100+depth
        elif board.check_for_winner() == self.not_symbol:
            return -100-depth
        else:  
            return 0
