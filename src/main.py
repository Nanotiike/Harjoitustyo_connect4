"""Responsible for handling user and ai input and updating the game state."""
from board import Board
from player import Player
from ai import Ai

def main():
    """Main loop of the game."""

    moves = []
    board = Board()
    player1 = Player("Ai1", "Y")
    player2 = Ai("Ai2", "R")
    while True:
        print(board)
        move1 = player1.choose_move(board)
        """move1 = player1.choose_move(board)
        board.make_move(move1, player1.symbol)"""
        moves.append([move1,"Y"])
        if board.check_for_winner(move1[0],move1[1]) == player1.symbol:
            print(board)
            print(f"{player1.name} wins!")
            break
        print(board)
        move2 = player2.choose_move(board)
        move3 = board.make_move(move2[1], player2.symbol)
        moves.append([move2,"R"])
        if board.check_for_winner(move2[1],move3) == player2.symbol:
            print(board)
            print(f"{player2.name} wins!")
            break
    print(moves)


if __name__ == "__main__":
    main()
