# Contains the main loop of the game. Responsible for handling user and ai input and updating the game state.
from board import Board
from player import Player
from ai import AI

def main():
    board = Board()
    board.print_board()

if __name__ == "__main__":
    main()