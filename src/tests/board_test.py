# Test class for the Board class
import unittest
from board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
    
    def test_print_board(self):
        self.assertEqual(self.board.__str__(), "-----------------------------\n|   |   |   |   |   |   |   | \n-----------------------------\n|   |   |   |   |   |   |   | \n-----------------------------\n|   |   |   |   |   |   |   | \n-----------------------------\n|   |   |   |   |   |   |   | \n-----------------------------\n|   |   |   |   |   |   |   | \n-----------------------------\n|   |   |   |   |   |   |   | \n-----------------------------\n- 1 - 2 - 3 - 4 - 5 - 6 - 7 -")
