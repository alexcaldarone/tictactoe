import copy

class Board:
    """A class to represent a Tic-Tac-Toe game board.
    
    Attributes:
        self.board:  A list of lists to represent the game board

    """
    def __init__(self):
        """constructor"""
        self.board = [
            [None, None, None],
        [None, None, None],
        [None, None, None]
        ]
    
    def print_board(self):
        """Prints the board"""
        print(self.board)
    
    def __str__(self):
        """Conversion of the baord to string
        
        Returns
        -------------------
        string: str
            String implementation of the baord
        """
        return str(self.board)
    
    def __iter__(self):
        """Iterates over the board"""
        for row in self.board:
            for el in row:
                yield el
    
    def __getitem__(self, key):
        """Returns the item in the position indicated by $key.
        
        Parameters
        --------------------
        key: int/slice/tuple
            Position of the element to be returned

        
        Returns
        -------------------
        Element of the board in the position indicated by key (Any)
        """
        if isinstance(key, slice):
            start, stop, step = key.indices(9)
            return [self[i] for i in range(start, stop, step)]
        elif isinstance(key, int):
            row, col = divmod(key, 3)
            return self.board[row][col]
        elif isinstance(key, tuple):
            return self.board[key[0]][key[1]]
        else:
            raise TypeError('Indexes must be integers, slices or tuples')
    
    def __setitem__(self, key, elem):
        """Set an element of the board to that passed as argument
        
        Parameters
        --------------------
        key:    
            Position of the board to be modified
        elem:   
            Value to be set in position
        """
        if isinstance(key, int):
            row, col = divmod(key, 3)
            self.board[row][col] = elem
        elif isinstance(key, tuple):
            self.board[key[0]][key[1]] = elem

    
    def is_full(self):
        """Determines if the board is full or not.
        
        Returns
        -------------------
        Indication if the board is full or not (bool)
        """
        for i in range(9):
            if self[i] == None:
                return False
        return True
    
    def is_empty(self):
        """Determines if the board is empty or not
        
        Returns
        -------------------
        Indication if the board is empty or not (bool)
        """
        for i in range(9):
            if self[i] != None:
                return False
        return True
    
    def get_rows(self):
        """
        Returns a list of lists containing the rows of the board
        
        Returns
        -------------------
        rows: list
            A list of lists containing the rows of the board
        """
        return [ self[0:3], self[3:6], self[6:9] ]
    
    def get_columns(self):
        """
        Returns a list of lists containing the colums of the board
        
        Returns
        -------------------
        cols: list
            A list of lists containing the columns of the board
        """
        return [ self[0:9:3], self[1:9:3], self[2:9:3]]
    
    def get_diags(self):
        """
        Returns a list of lists containing the diagonals of the board
        
        Returns
        -------------------
        diags: list
            A list of lists containing the diagonals of the board
        """
        return [ [self[i] for i in (0, 4, 8)], [self[i] for i in (2, 4, 6)] ]
    
    def get_combos(self):
        """
        Returns a list of lists containing the combinations of the board 
        (all the rows, all the columns and all the diagonals)
        
        Returns
        -------------------
        combos: list
            A list of lists containing the combinations of the board
        """
        combos = []
        for row in self.get_rows(): combos.append(row)
        for column in self.get_columns(): combos.append(column)
        for diag in self.get_diags(): combos.append(diag)
        return combos
    
    def legal_moves(self):
        """
        Checks what are the legal moves that can be done on the board
        (A move is legal if the cell is empty)

        Returns
        -------------------
        moves: list
            List with the legal moves available
        """
        moves = []
        count = -1 #  by starting at minus -1 it is zero in the first cell i check
        for cell in self:
            count += 1
            if cell == None:
                moves.append(divmod(count, 3))
        return moves
    
    def is_valid_move(self, coords):
        """
        Determines if a move is valid
        (A move is valid if the cell where it is to be made is empty)

        Parameters
        -------------------
        coords: int or tuple
            Coordinates of the cell where we want to make move
        
        Returns
        -------------------
        Indication of whether the move is valid on not (bool)
        """
        return True if self[coords] == None else False
    
    def make_move(self, coords, player):
        """
        Makes a move. 
        (Making a move means chaning the value of one of the elements in the board to the value of the player)

        Parameters
        --------------------
        coords: int or tuple    
            Coordinates of cell where the player waint to make a move
        player: str   
            Player to make the move

        Returns
        -------------------
        new_board: Board
            A new board with the new move
        """
        if isinstance(coords, slice): # check that the player is not trying to make a move in more than one cell
            raise IndexError("Cannot make a move in more than one cell")
        if not self.is_valid_move(coords): # check if the move is a valid one
            raise Exception('Invalid move!')
        new_board = copy.deepcopy(self)
        new_board[coords] = player
        return new_board
    
    def get_winner(self):
        """ Determines if there is a winner in the board 
        (A player is a winner if it is the only one present in a combination)
        
        Returns
        -------------------
        winner: str or None
            The winner of the game
        """

        def __check_list_for_winner(lis):
            '''
            Checks if all the elements in the list are the same

            Parameters:
            -------------------
            lis: list
                The list to be checked
            
            Returns
            -------------------
            Indication if all the elements in the list are the same (bool)
            '''
            for i in range(1, len(lis)):
                if lis[i] != lis[i-1]:
                    return False
            return True
        

        if self.is_empty(): # if the board is empty then return None
            return None
        
        combos = self.get_combos()

        for combo in combos:
            if __check_list_for_winner(combo): # if thid point is reached a winner has been found
                return combo[0] # first element of the list will be winner
        
        return None # if this point has been reached then there is not winner

   
    def render(self):
        """Renders the playing board"""
        
        def __print_line(board, num):
            """
            Prints a single line of the playing board

            Parameters:
            -------------------
            board: Board
                The gaming board 
            num: int
                Number of the row to be printed
            """
            for i in range(3):
                if board.board[num][i] == None:
                    print(' ', end = ' ')
                else:
                    print(board.board[num][i], end = ' ')
        

        print('   0 1 2')
        print('  -------')
        print('0|', end = ' ')
        __print_line(self, 0)
        print('|')
        print('1|', end = ' ')
        __print_line(self, 1)
        print('|')
        print('2|', end = ' ')
        __print_line(self, 2)
        print('|')
        print('  -------')


if __name__ == "__main__":
    board = Board()
    for num in range(0,9):
        row, col = divmod(num, 3)
        board.board[row][col] = num
    
    print('-> Testing __getitem__')
    try: 
        print(board[(1,1)], end= ' ')
        print('Test passed')
    except:
        print('    Test failed')
    
    print('-> Testing __iter__')
    try:
        for i in board:
            print(i)
        print('Test passed')
    except:
        print('    Test failed')
    
    print('-> Testing get_rows')
    try:
        rows = board.get_rows()
        print(rows)
        print('Test passed')
    except:
        print('   Test failed')

    print('-> Testing get_columns')
    try:
        cols = board.get_columns()
        print(cols)
        print('Test passed')
    except:
        print('   Test failed')
    
    print('-> Testing get_diags')
    try:
        diags = board.get_diags()
        print(diags)
        print('Test passed')
    except:
        print('   Test failed')
    
    print('-> Testing get_combos')
    try:
        comb = board.get_combos()
        print(comb)
        print('Test passed')
    except:
        print('   Test failed')
    
    print('-> testing is_full')
    try:
        print(board.is_full(), end=' ')
        print('test passed')
    except:
        print('test failed')
    
    print('-> testing is_empty')
    try:
        print(board.is_empty(), end=' ')
        print('test passed')
    except:
        print('test failed')
    
    print('-> Testing render')
    board.render()