# Test class for the Board class
import unittest
from board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
    
    def test_print_board(self):
        self.assertEqual(self.board.__str__(), "-----------------------------\n|   |   |   |   |   |   |   | \n-----------------------------\n|   |   |   |   |   |   |   | \n-----------------------------\n|   |   |   |   |   |   |   | \n-----------------------------\n|   |   |   |   |   |   |   | \n-----------------------------\n|   |   |   |   |   |   |   | \n-----------------------------\n|   |   |   |   |   |   |   | \n-----------------------------\n- 1 - 2 - 3 - 4 - 5 - 6 - 7 -")

    def test_make_move_success(self):
        self.assertTrue(self.board.make_move(0, "Y"))
        self.assertEqual(self.board.board[5][0], "Y")
    
    def test_make_move_failure(self):
        for i in range(6):
            self.board.make_move(0, "Y")
        self.assertFalse(self.board.make_move(0, "R"))
        self.assertEqual(self.board.board[0][0], "Y")

    def test_check_for_winner_horizontal(self):
        self.board.board = [[" ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " "],
                            ["Y", "Y", "Y", "Y", " ", " ", " "]]
        self.assertEqual(self.board.check_for_winner(), "Y")

    def test_check_for_winner_vertical(self):
        self.board.board = [[" ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " "],
                            ["Y", " ", " ", " ", " ", " ", " "],
                            ["Y", " ", " ", " ", " ", " ", " "],
                            ["Y", " ", " ", " ", " ", " ", " "],
                            ["Y", " ", " ", " ", " ", " ", " "]]
        self.assertEqual(self.board.check_for_winner(), "Y")

    def test_check_for_winner_diagonal_1(self):
        self.board.board = [[" ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", "Y", " ", " ", " "],
                            [" ", " ", "Y", " ", " ", " ", " "],
                            [" ", "Y", " ", " ", " ", " ", " "],
                            ["Y", " ", " ", " ", " ", " ", " "]]
        self.assertEqual(self.board.check_for_winner(), "Y")

    def test_check_for_winner_diagonal_2(self):
        self.board.board = [["Y", " ", " ", " ", " ", " ", " "],
                            [" ", "Y", " ", " ", " ", " ", " "],
                            [" ", " ", "Y", " ", " ", " ", " "],
                            [" ", " ", " ", "Y", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " "]]
        self.assertEqual(self.board.check_for_winner(), "Y")
    
    def test_check_for_winner_no_winner(self):
        self.board.board = [[" ", " ", " ", " ", " ", " ", " "],
                            [" ", "R", " ", " ", " ", " ", " "],
                            [" ", "Y", " ", " ", " ", " ", " "],
                            [" ", "Y", " ", " ", " ", " ", " "],
                            [" ", "R", " ", " ", " ", " ", " "],
                            ["Y", "Y", "R", "Y", " ", " ", " "]]
        self.assertEqual(self.board.check_for_winner(), None)