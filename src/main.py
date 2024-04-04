"""Responsible for handling user and ai input and updating the game state."""
from board import Board
from player import Player
from ai import Ai

def main():
    """Main loop of the game."""

    board = Board()
    player1 = Player("Player", "Y")
    player2 = Ai("Ai", "R")
    while True:
        print(board)
        player1.make_move(board)
        if board.check_for_winner() == player1.symbol:
            print(board)
            print(f"{player1.name} wins!")
            break
        print(board)
        player2.make_move(board)
        print(player2.test)
        if board.check_for_winner() == player2.symbol:
            print(board)
            print(f"{player2.name} wins!")
            break


if __name__ == "__main__":
    main()
