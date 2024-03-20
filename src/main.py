# Contains the main loop of the game. Responsible for handling user and ai input and updating the game state.
from board import Board
from player import Player
from ai import Ai

def main():
    board = Board()
    player1 = Player("Player 1", "Y")
    player2 = Player("Player 2", "R")
    while True:
        print(board)
        player1.make_move(board)
        print(board)
        player2.make_move(board)


if __name__ == "__main__":
    main()