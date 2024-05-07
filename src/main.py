"""Responsible for handling user and ai input and updating the game state."""
from board import Board
from player import Player
from ai import Ai

def main():
    """Main loop of the game."""

    moves_made = 0
    board = Board()
    try:
        player1 = Player("Player Y", "\U0001F7E1")
    except:
        player1 = Player("Player Y", "YY")
    #player2 = Player("Player R", "\U0001F534")
    #player1 = Ai("AI Y", "\U0001F7E1", "\U0001F534")
    try:
        player2 = Ai("AI R", "\U0001F534", "\U0001F7E1")
    except:
        player2 = Ai("AI R", "RR", "YY")
    while True:
        print(board)
        if player1.name == "Player Y":
            move1 = player1.choose_move(board)
            move12 = move1[0]
        if player1.name == "AI Y":
            move1 = player1.choose_move(board, moves_made)
            move12 = board.make_move(move1[1], player1.symbol)
        moves_made += 1
        if board.check_for_winner(move1[1],move12) == player1.symbol:
            print(board)
            print(f"{player1.name} wins!")
            break
        if moves_made == 42:
            print(board)
            print("It's a tie!")
            break
        print(board)
        if player2.name == "Player R":
            move2 = player2.choose_move(board)
            move22 = move2[1]
        if player2.name == "AI R":
            move2 = player2.choose_move(board, moves_made)
            move22 = board.make_move(move2[1], player2.symbol)
        moves_made += 1
        if board.check_for_winner(move2[1],move22) == player2.symbol:
            print(board)
            print(f"{player2.name} wins!")
            break
        if moves_made == 42:
            print(board)
            print("It's a tie!")
            break


if __name__ == "__main__":
    main()
