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

    def choose_move(self, board, moves_made):
        """Makes a move on the board using the minimax algorithm."""
        move = self.minimax(board, 5, True, -100000, 100000, 0, 0, moves_made)
        return move
            

    def minimax(self, board, depth, is_maximizing, alpha, beta, x, y, moves_made):
        """The minimax algorithm."""
        evaluate = 0
        best_move = 0
        winner = board.check_for_winner(x, y)
        if winner == self.symbol:
            return (10000, -1)
        elif winner == self.not_symbol:
            return (-10000, -1)
        if moves_made == 42:
            return (-1000, -1)
        if depth == 0:
            evaluate = self.score(depth, board, x, y)
            return (evaluate, -1)
        if is_maximizing:
            evaluate = -100000
            for column in self.moves:
                row = board.make_move(column, self.symbol)
                if row is not False:
                    moves_made += 1
                    temp = self.minimax(board, depth - 1, False, alpha, beta, column, row, moves_made)
                    board.undo_move(column)
                    moves_made -= 1
                    if evaluate < temp[0]:
                        evaluate = temp[0]
                        best_move = column
                    if temp[0] > beta:
                        break
                    alpha = max(alpha, temp[0])
            return (evaluate, best_move)
        else:
            evaluate = 100000
            for column in self.moves:
                row = board.make_move(column, self.not_symbol)
                if row is not False:
                    moves_made += 1
                    temp = self.minimax(board, depth - 1, True, alpha, beta, column, row, moves_made)
                    board.undo_move(column)
                    moves_made -= 1
                    if evaluate > temp[0]:
                        evaluate = temp[0]
                        best_move = column
                    if temp[0] < alpha:
                        break
                    beta = min(beta, temp[0])
            return (evaluate, best_move)

    def score(self, depth, board, x, y):
        """How the board is evaluated for minimax."""
        score = 0
        temp = -1
        while y+temp>=0:
            if board.board[y+temp][x] == self.symbol:
                score += 3
            elif board.board[y+temp][x] == " ":
                score += 1
            elif board.board[y+temp][x] == self.not_symbol:
                score -= 6
                break
            elif temp == -3:
                break
            temp -= 1
        temp = 1
        while y+temp<=5:
            if board.board[y+temp][x] == self.symbol:
                score += 3
            elif board.board[y+temp][x] == " ":
                score += 1
            elif board.board[y+temp][x] == self.not_symbol:
                score -= 6
                break
            elif temp == 3:
                break
            temp += 1
        temp = -1
        while x+temp>=0:
            if board.board[y][x+temp] == self.symbol:
                score += 3
            elif board.board[y][x+temp] == " ":
                score += 1
            elif board.board[y][x+temp] == self.not_symbol:
                score -= 6
                break
            elif temp == -3:
                break
            temp -= 1
        temp = 1
        while x+temp<=6:
            if board.board[y][x+temp] == self.symbol:
                score += 3
            elif board.board[y][x+temp] == " ":
                score += 1
            elif board.board[y][x+temp] == self.not_symbol:
                score -= 6
                break
            elif temp == 3:
                break
            temp += 1
        temp = -1
        while y+temp>=0 and x+temp>=0:
            if board.board[y+temp][x+temp] == self.symbol:
                score += 3
            elif board.board[y+temp][x+temp] == " ":
                score += 1
            elif board.board[y+temp][x+temp] == self.not_symbol:
                score -= 6
                break
            elif temp == -3:
                break
            temp -= 1
        temp = 1
        while y+temp<=5 and x+temp<=6:
            if board.board[y+temp][x+temp] == self.symbol:
                score += 3
            elif board.board[y+temp][x+temp] == " ":
                score += 1
            elif board.board[y+temp][x+temp] == self.not_symbol:
                score -= 6
                break
            elif temp == 3:
                break
            temp += 1
        temp = -1
        while x+temp>=0 and y-temp<=5:
            if board.board[y-temp][x+temp] == self.symbol:
                score += 3
            elif board.board[y-temp][x+temp] == " ":
                score += 1
            elif board.board[y-temp][x+temp] == self.not_symbol:
                score -= 6
                break
            elif temp == -3:
                break
            temp -= 1
        temp = 1
        while x+temp<=6 and y-temp>=0:
            if board.board[y-temp][x+temp] == self.symbol:
                score += 3
            elif board.board[y-temp][x+temp] == " ":
                score += 1
            elif board.board[y-temp][x+temp] == self.not_symbol:
                score -= 6
                break
            elif temp == 3:
                break
            temp += 1
        return score-depth

    def check_valid_moves():
        pass
