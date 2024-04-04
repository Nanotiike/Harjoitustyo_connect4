"""Responsible for handling user and ai input and updating the game state."""
from board import Board
from player import Player
from ai import Ai

def main():
    """Main loop of the game."""

    moves = []
    board = Board()
    player1 = Ai("Ai1", "Y")
    player2 = Ai("Ai2", "R")
    while True:
        print(board)
        move1 = player1.make_move(board)
        moves.append([move1,"Y"])
        if board.check_for_winner() == player1.symbol:
            print(board)
            print(f"{player1.name} wins!")
            break
        print(board)
        move2 = player2.make_move(board)
        moves.append([move2,"R"])
        if board.check_for_winner() == player2.symbol:
            print(board)
            print(f"{player2.name} wins!")
            break
    print(moves)


if __name__ == "__main__":
    main()
