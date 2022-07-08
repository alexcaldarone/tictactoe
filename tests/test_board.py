from scripts.board import Board
import unittest

class TestBoard(unittest.TestCase):
    
    def test_isfull(self):
        b = Board()
        for i in range(9):
            b[i] = i
        
        self.assertTrue(b.is_full())
    
    def test_isempty(self):
        b = Board()
        self.assertTrue(b.is_empty())

    def test_getitem(self):
        b = Board()
        self.assertEqual(b[1], b.board[0][1]) # testing integer index
        self.assertEqual(b[(0,1)], b.board[0][1]) # testing tuple index
        self.assertEqual(b[0:2:], [b.board[0][0], b.board[0][1]]) # testing slice index
    
    def test_setitem(self):
        b = Board()
        b[1] = 1
        self.assertEqual(b[1], 1)
        b[(0,2)] = 2
        self.assertEqual(b[(0,2)], 2)
    
    def test_getrows(self):
        b = Board()
        for i in range(9):
            b[i] = i
        
        row1 = b.board[0]
        row2 = b.board[1]
        row3 = b.board[2]
        rows = [row1, row2, row3] # list of lists containing all the rows

        self.assertEqual(rows, b.get_rows())
    
    def test_getcols(self):
        b = Board()
        for i in range(9):
            b[i] = i
        
        col1 = []
        col2 = []
        col3 = []
        for i in range(3):
            col1.append(b.board[i][0])
        for j in range(3):
            col2.append(b.board[j][1])
        for z in range(3):
            col3.append(b.board[z][2])
        cols = [col1, col2, col3] # list of lists containing all the columns

        self.assertEqual(cols, b.get_columns())
    
    def test_getdiags(self):
        b = Board()
        for i in range(9):
            b[i] = i
        
        diag1 = [b[0], b[4], b[8]]
        diag2 = [b[2], b[4], b[6]]
        diags = [diag1, diag2] # list of lists containing all the diagoals

        self.assertEqual(diags, b.get_diags())
    
    def test_getcombos(self):
        b = Board()
        for i in range(9):
            b[i] = i
        
        combos = [
            b[0:3:], # row 1
            b[3:6:], # row 2
            b[6:9:], # row 3
            [b[0], b[3], b[6]], # col 1
            [b[1], b[4], b[7]], # col 2
            [b[2], b[5], b[8]], # col 3
            [b[0], b[4], b[8]], # diag 1
            [b[2], b[4], b[6]], # diag 2
        ]

        self.assertEqual(combos, b.get_combos())
    
    def test_isvalidmove(self):
        b = Board()
        b[1] = "X"

        self.assertTrue(b.is_valid_move(0))
        self.assertFalse(b.is_valid_move(1))
    
    def test_legalmoves(self):
        b = Board()
        for _ in range(6):
            b[_] = _
        
        empty = [(2,0), (2,1), (2,2)] # list containing the coordinates of the last row

        self.assertEqual(b.legal_moves(), empty)
    
    def test_makemove(self):
        pass
    
    def test_getwinner(self):
        b = Board()
        self.assertEqual(None, b.get_winner())

        for _ in range(3):
            b[_] = "X"
        self.assertEqual("X", b.get_winner())


if __name__ == "__main__":
    unittest.main()