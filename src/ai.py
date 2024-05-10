import time

"""Contains Ai class which will be the main focus of the project. 
The Ai class will use the minimax algorithm and alhpa-beta pruning algorithm."""
"""The minimax algorithm is an algorithm used for two-player games. 
The minimax algorithm is a recusrisve algorithm used to determine the best possible move when you don't know the opponents move. 
The algorithm assumes that the opponent will play the best possible move for them, thus the algorithm will try to minimize the maximum loss."""
"""The alpha-beta pruning algorithm is an optimization technique for the minimax algorithm. 
It reduces the number of nodes that are evaluated by the minimax algorithm in its search tree. 
The algorithm maintains two values, alpha and beta, 
which represent the minimum score that the maximizing player is assured of and the maximum score that the minimizing player is assured of respectively. 
Based on these two values the algorithm prunes the nodes that are not needed to be evaluated."""
"""The iterative deepening algorithm is an addition to minimax that starts the algorithm at a defined depth and increases the depth until a time limit is reached."""
"""The hash table is used to store the best moves for a given board state. 
If the minimax algorithm reaches a board state that has already been evaluated, 
it uses the hash table to get the best move for that state and uses it as a starting point."""

class Ai:
    def __init__(self, name, symbol, not_symbol):
        self.name = name
        self.symbol = symbol
        self.not_symbol = not_symbol

    def choose_move(self, board, moves_made):
        """Makes a move on the board using the minimax algorithm."""
        move = self.iterative_deepening(3, board, moves_made, 1.5)
        return move

    def minimax(self, board, depth, is_maximizing, alpha, beta, x, y, moves_made, hash_table):
        """The minimax algorithm, with alpha-beta pruning and a hash table to store the best moves."""
        moves = [3,4,2,5,1,6,0]
        winner = board.check_for_winner(x, y)
        if winner == self.symbol:
            return (10000, -1)
        if winner == self.not_symbol:
            return (-10000, -1)
        if moves_made == 42:
            return (0, -1)
        if depth == 0:
            evaluate = self.score(depth, board, x, y)
            return (evaluate, -1)
        if is_maximizing:
            evaluate = -100000
            hash_key = hash(str(board.board))
            best_move = hash_table.get(hash_key)
            if best_move is not None:
                moves.remove(best_move)
                moves.insert(0, best_move)
            for column in moves:
                row = board.make_move(column, self.symbol)
                if row is not False:
                    moves_made += 1
                    temp = self.minimax(board, depth - 1, False, alpha, beta, column, row, moves_made, hash_table)
                    board.undo_move(column)
                    moves_made -= 1
                    if evaluate < temp[0]:
                        evaluate = temp[0]
                        best_move = column
                    if temp[0] > beta:
                        break
                    alpha = max(alpha, temp[0])
            hash_table[hash_key] = best_move
            return (evaluate, best_move)
        else:
            evaluate = 100000
            hash_key = hash(str(board.board))
            best_move = hash_table.get(hash_key)
            if best_move is not None:
                moves.remove(best_move)
                moves.insert(0, best_move)
            for column in moves:
                row = board.make_move(column, self.not_symbol)
                if row is not False:
                    moves_made += 1
                    temp = self.minimax(board, depth - 1, True, alpha, beta, column, row, moves_made, hash_table)
                    board.undo_move(column)
                    moves_made -= 1
                    if evaluate > temp[0]:
                        evaluate = temp[0]
                        best_move = column
                    if temp[0] < alpha:
                        break
                    beta = min(beta, temp[0])
            hash_table[hash_key] = best_move
            return (evaluate, best_move)

    def score(self, depth, board, x, y):
        """How the board is evaluated for minimax. 
        The function scores the position based on the number of own pieces, 
        empty spaces, and opponent pieces close to the specified position."""
        score = 0
        temp = -1
        while y+temp>=0:
            if board.board[y+temp][x] == self.symbol:
                score += 3
            elif board.board[y+temp][x] == "  ":
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
            elif board.board[y+temp][x] == "  ":
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
            elif board.board[y][x+temp] == "  ":
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
            elif board.board[y][x+temp] == "  ":
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
            elif board.board[y+temp][x+temp] == "  ":
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
            elif board.board[y+temp][x+temp] == "  ":
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
            elif board.board[y-temp][x+temp] == "  ":
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
            elif board.board[y-temp][x+temp] == "  ":
                score += 1
            elif board.board[y-temp][x+temp] == self.not_symbol:
                score -= 6
                break
            elif temp == 3:
                break
            temp += 1
        return score-depth

    def iterative_deepening(self, depth, board, moves_made, timelimit):
        """Iterative deepening algorithm. Starts at a defined depth and increases the depth until the time limit is reached."""
        current_time = time.time()
        max_time = current_time + timelimit
        hash_table = {}
        while True:
            value = self.minimax(board, depth, True, -100000, 100000, 0, 0, moves_made, hash_table)
            if value[0] == 10000 or value[0] == -10000:
                break
            if time.time() >= max_time:
                break
            depth += 1
        return value