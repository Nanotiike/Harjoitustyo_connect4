# Test class for the AI class
import unittest
from ai import Ai
from board import Board

class TestAi(unittest.TestCase):
    def setUp(self):
        self.ai = Ai("AI", "Y", "R")
        self.board = Board()

    def test_choose_winning_move(self):
        """Test the choose_move method and the minimax algorithm of the Ai class when a winning move is available"""
        self.board.board = [["  " for _ in range(7)] for _ in range(6)]
        self.board.board[5] = ["R", "Y", "Y", "Y", "  ", "  ", "  "]
        self.assertEqual(self.ai.choose_move(self.board, 0), (10000, 4))

    def test_block_winning_move(self):
        """Test the choose_move method and the minimax algorithm of the Ai class when the opponent has a winning move"""
        self.board.board = [["  " for _ in range(7)] for _ in range(6)]
        self.board.board[5] = ["Y", "R", "R", "R", "  ", "  ", "  "]
        self.assertEqual(self.ai.choose_move(self.board, 0), (8, 4))

