"""Test class for the Board class"""
import unittest
from board import Board

class TestBoard(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.board = Board()
        self.board.board = [["  "for _ in range(7)] for _ in range(6)]
    
    def test_print_board(self):
        """Test the __str__ method of the Board class"""
        board_string = "\
------------------------------------\n\
|    |    |    |    |    |    |    | \
\n------------------------------------\n\
|    |    |    |    |    |    |    | \
\n------------------------------------\n\
|    |    |    |    |    |    |    | \
\n------------------------------------\n\
|    |    |    |    |    |    |    | \
\n------------------------------------\n\
|    |    |    |    |    |    |    | \
\n------------------------------------\n\
|    |    |    |    |    |    |    | \
\n------------------------------------\n\
-  1 -  2 -  3 -  4 -  5 -  6 -  7 -"
        self.assertEqual(str(self.board), board_string)
                         
    def test_make_move_success(self):
        """Test the make_move method of the Board class is successful"""
        self.assertEqual(self.board.make_move(0, "Y"), 5)
        self.assertEqual(self.board.board[5][0], "Y")
    
    def test_make_move_failure(self):
        """Test the make_move method of the Board class when it fails"""
        for i in range(6):
            self.board.make_move(0, "Y")
        self.assertFalse(self.board.make_move(0, "R"))
        self.assertEqual(self.board.board[0][0], "Y")

    def test_check_for_winner_horizontal(self):
        """Test the check_for_winner method of the Board class for a horizontal win"""
        self.board.board = [[" ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " "],
                            ["Y", "Y", "Y", "Y", " ", " ", " "]]
        self.assertEqual(self.board.check_for_winner(0,5), "Y")

    def test_check_for_winner_vertical(self):
        """Test the check_for_winner method of the Board class for a vertical win"""
        self.board.board = [[" ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " "],
                            ["Y", " ", " ", " ", " ", " ", " "],
                            ["Y", " ", " ", " ", " ", " ", " "],
                            ["Y", " ", " ", " ", " ", " ", " "],
                            ["Y", " ", " ", " ", " ", " ", " "]]
        self.assertEqual(self.board.check_for_winner(0,5), "Y")

    def test_check_for_winner_diagonal_1(self):
        """Test the check_for_winner method of the Board class for a diagonal win from bottom left to top right"""
        self.board.board = [[" ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", "Y", " ", " ", " "],
                            [" ", " ", "Y", " ", " ", " ", " "],
                            [" ", "Y", " ", " ", " ", " ", " "],
                            ["Y", " ", " ", " ", " ", " ", " "]]
        self.assertEqual(self.board.check_for_winner(0,5), "Y")

    def test_check_for_winner_diagonal_2(self):
        """Test the check_for_winner method of the Board class for a diagonal win from top left to bottom right"""
        self.board.board = [["Y", " ", " ", " ", " ", " ", " "],
                            [" ", "Y", " ", " ", " ", " ", " "],
                            [" ", " ", "Y", " ", " ", " ", " "],
                            [" ", " ", " ", "Y", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " "]]
        self.assertEqual(self.board.check_for_winner(0,0), "Y")
    
    def test_check_for_winner_no_winner(self):
        """Test the check_for_winner method of the Board class when there is no winner"""
        self.board.board = [[" ", " ", " ", " ", " ", " ", " "],
                            [" ", "R", " ", " ", " ", " ", " "],
                            [" ", "Y", " ", " ", " ", " ", " "],
                            [" ", "Y", " ", " ", " ", " ", " "],
                            [" ", "R", " ", " ", " ", " ", " "],
                            ["Y", "Y", "R", "Y", " ", " ", " "]]
        self.assertEqual(self.board.check_for_winner(1,5), None)

    def test_undo_move(self):
        self.board.make_move(0, "Y")
        self.board.undo_move(0)
        self.assertEqual(self.board.board[5][0], "  ")

    def test_undo_move_nothing(self):
        self.board.undo_move(0)
        self.assertEqual(self.board.board[5][0], "  ")
