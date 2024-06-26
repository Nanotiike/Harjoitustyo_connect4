"""Test class for the Player class"""
import unittest
from player import Player
from board import Board
from tests.test_base import set_keyboard_input, get_display_output

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Test Player", "Y")
        self.board = Board()

    def test_choose_move_quit(self):
        """Test the make_move method of the Player class when the player quits"""
        set_keyboard_input(["q"])
        with self.assertRaises(SystemExit):
            self.player.choose_move(self.board)
        output = get_display_output()
        self.assertEqual(output, ["Test Player make your move (1-7), or quit (q): "])

    def test_choose_move(self):
        """Test the make_move method of the Player class when the player inputs wrong values"""
        set_keyboard_input(["e", "10", "1"])
        self.player.choose_move(self.board)
        output = get_display_output()
        self.assertEqual(output, ["Test Player make your move (1-7), or quit (q): ", "Invalid input, please enter a number", "Test Player make your move (1-7), or quit (q): ", "Invalid input, please enter a number between 1 and 7", "Test Player make your move (1-7), or quit (q): "])
        self.assertEqual(self.board.board[5][0], "Y")

    def test_choose_move_full_column(self):
        """Test the make_move method of the Player class when the player inputs into a full column"""
        for i in range(6):
            self.board.make_move(0, "Y")
        set_keyboard_input(["1", "2"])
        self.player.choose_move(self.board)
        output = get_display_output()
        self.assertEqual(output, ["Test Player make your move (1-7), or quit (q): ", "Column is full, please choose another column", "Test Player make your move (1-7), or quit (q): "])

