# Test class for the AI class
import unittest
from ai import Ai
from board import Board

class TestAi(unittest.TestCase):
    def setUp(self):
        self.ai = Ai("AI", "Y", "R")
        self.board = Board()

    def test_choose_winning_move(self):
        """Test the choose_move method and the minimax algorithm of the Ai class when a winning move is available. Checking for horizontal win"""
        self.board.board = [["  " for _ in range(7)] for _ in range(6)]
        self.board.board[5] = ["R", "Y", "Y", "Y", "  ", "  ", "  "]
        self.assertEqual(self.ai.choose_move(self.board, 0), (10000, 4))
    
    def test_choose_winning_move2(self):
        """Test the choose_move method and the minimax algorithm of the Ai class when a winning move is available. Checking for vertical win"""
        self.board.board = [["  " for _ in range(7)] for _ in range(6)]
        self.board.board[3] = ["Y", "  ", "  ", "  ", "  ", "  ", "  "]
        self.board.board[4] = ["Y", "  ", "  ", "  ", "  ", "  ", "  "]
        self.board.board[5] = ["Y", "  ", "  ", "  ", "  ", "  ", "  "]
        self.assertEqual(self.ai.choose_move(self.board, 0), (10000, 0))

    def test_choose_winning_move3(self):
        """Test the choose_move method and the minimax algorithm of the Ai class when a winning move is available. Checking for diagonal win"""
        self.board.board[3] = ["  ", "  ", "Y", "R", "  ", "  ", "  "]
        self.board.board[4] = ["  ", "Y", "Y", "R", "  ", "  ", "  "]
        self.board.board[5] = ["Y", "Y", "R", "R", "  ", "  ", "  "]
        self.assertEqual(self.ai.choose_move(self.board, 0), (10000, 3))

    def test_block_winning_move(self):
        """Test the choose_move method and the minimax algorithm of the Ai class when the opponent has a winning move. Checking for horizontal win"""
        self.board.board = [["  " for _ in range(7)] for _ in range(6)]
        self.board.board[5] = ["Y", "R", "R", "R", "  ", "  ", "  "]
        self.assertEqual(self.ai.choose_move(self.board, 0), (8, 4))

    def test_block_winning_move2(self):
        """Test the choose_move method and the minimax algorithm of the Ai class when the opponent has a winning move. Checking for vertical win"""
        self.board.board = [["  " for _ in range(7)] for _ in range(6)]
        self.board.board[3] = ["R", "  ", "  ", "  ", "  ", "  ", "  "]
        self.board.board[4] = ["R", "  ", "  ", "  ", "  ", "  ", "  "]
        self.board.board[5] = ["R", "  ", "  ", "  ", "  ", "  ", "  "]
        self.assertEqual(self.ai.choose_move(self.board, 0), (6, 0))

    def test_block_winning_move3(self):
        """Test the choose_move method and the minimax algorithm of the Ai class when the opponent has a winning move. Checking for diagonal win"""
        self.board.board[3] = ["  ", "  ", "R", "Y", "  ", "  ", "  "]
        self.board.board[4] = ["  ", "R", "R", "Y", "  ", "  ", "  "]
        self.board.board[5] = ["R", "R", "Y", "R", "  ", "  ", "  "]
        self.assertEqual(self.ai.choose_move(self.board, 0), (9, 3))

    def test_result_unable_to_block(self):
        """Test the choose_move method and the minimax algorithm of the Ai class when the opponent has a winning move but the AI is unable to block it"""
        self.board.board = [["  " for _ in range(7)] for _ in range(6)]
        self.board.board[5] = [" ", "R", "R", "R", "  ", "  ", "  "]
        self.assertEqual(self.ai.choose_move(self.board, 0), (-10000, 4))

    def test_tie(self):
        """Test the choose_move method and the minimax algorithm of the Ai class when the game is a tie"""
        self.board.board = [["P" for _ in range(7)] for _ in range(6)]
        self.assertEqual(self.ai.choose_move(self.board, 42), (0, -1))