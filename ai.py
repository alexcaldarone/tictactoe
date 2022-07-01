from board import Board
import random

class AIPlayer:
    """ """
    def random_ai(self, board, player):
        """
        Random AI: makes a random move on the playing board

        Parameters
        -------------------
        board: Board
            Playing board where to make the random move
        player: str
            Player that is using the AI to make a random move

        Returns
        -------------------
        x: int
            X-axis coordinate of where the Ai wants to play
        y: int
            Y-axis coordinate of where the AI wants to play
        """
        x = random.randint(0, 2)
        y = random.randint(0, 2)

        while True:
            if board.is_valid_move((x,y)): # if the random move is valid return the coordiantes
                return x,y
            else: # otherwise choose new coordinates
                x = random.randint(0, 2)
                y = random.randint(0, 2)
    
    def find_winning_moves_ai(self, board, player):
        """
        Find winning moves AI: checks the board to see if there is 
        a winning move. If there is one, then it plays there, otherwise it 
        makes a random move by calling random_ai.

        Parameters
        -------------------
        board: Board
            Playing board where to make the random move
        player: str
            Player that is using the AI to make a random move

        Returns
        -------------------
        x: int
            X-axis coordinate of where the Ai wants to play
        y: int
            Y-axis coordinate of where the AI wants to play
        """
        rows = board.get_rows()
        for i in range(len(rows)):
            if self.__has_winning_move(rows[i], player): # see it there is a winning move in one of the rows
                y = self.__find_none(rows[i]) # if there is a winning move, find the spot
                return i,y
    
        cols = board.get_columns()
        for i in range(len(cols)):
            if self.__has_winning_move(cols[i], player): # see if there is a winning move in one of the columns
                x = self.__find_none(cols[i]) # if there is a winning move, find the spot
                return x,i
    
        diags = board.get_diags()
        if self.__has_winning_move(diags[0], player): # see if there is a winning move in the first diagonal
            x = self.__find_none(diags[0])  # if there is a winning move, find the spot
            return x,x
        elif self.__has_winning_move(diags[1], player): # see if there is a winning move in the second diagonal
            x = self.__find_none(diags[1])  # if there is a winning move, find the spot
            return x,2-x
        # if this point has been reached, there are no winning moves, so make a random one
        else:
            coords= self.random_ai(self, board, player)
            return coords
    
    def find_winning_moves_and_losing_moves_ai(self, board, player):
        """
        Find winning moves and losing moves AI: 
        Checks the board to see if there is a winning move for the plyer using the AI, if there is one play there.
        If there is no winning move for the player using the AI, check the board to see if there is a winning move for the opponent,
        if there is play there.
        If there are no winning move for neither of the players, make a random move.

        Parameters
        -------------------
        board: Board
            Playing board where to make the random move
        player: str
            Player that is using the AI to make a random move

        Returns
        -------------------
        x: int
            X-axis coordinate of where the Ai wants to play
        y: int
            Y-axis coordinate of where the AI wants to play
        """
        not_player = 'O' if player == 'X' else 'X' # select who the opponent is
        coord_player = self.find_winning_moves_ai(self, board, player) # the player uses winning find_winning_moves_ai
        coord_not_player = self.find_winning_moves_ai(self, board, not_player) # the opponent uses find_winning_moves_ai
    
        board_player = board.make_move(coord_player, player) # creae board with player's move
        board_not_player = board.make_move(coord_not_player, not_player) # create board with opponent's move

        if board_player.get_winner() == player: # if the player wins return the winning coordinates
            return coord_player
        elif board_not_player.get_winner() == not_player: # if the opponent wins return his winning coordinates
            return coord_not_player 
        else:
            return self.random_ai(self, board, player) # if nobody wins make a random move


    def __has_winning_move(list, player):
        """
        Check if a list has a winning move in it (A move is a winning move if in the list 
        2/3 elemnents are the player and the other one is an empty spot)

        Parameters
        -------------------
        list: list
            List to be checked
        player: str
            Player that is looking for a winning move
        
        Returns
        -------------------
        Indication of whether there is winning move for the player (bool)
        """
        pl_count = 0
        none_count = 0

        for i in range(len(list)):
            if list[i] == player:
                pl_count += 1
            elif list[i] == None:
                none_count += 1
    
        if pl_count == 2 and none_count == 1:
            return True
        else:
            return False

    def __find_none(list):
        """
        Finds the empty spot in a list

        Parameters
        -------------------
        list: list
            List to be checked
        
        Returns
        -------------------
        i: int
            Index of the empty spot
        """
        for i in range(len(list)):
            if list[i] == None:
                return i
    
    def __play_in_corners(board, player):
        """
        Returns a randomly selected corner to play in

        Parameters
        -------------------
        board: Board
            Playing board where we want to play in the corners
        player: str
            Player that wants to play in one of the corners
        
        Returns
        -------------------
        corner: tuple
            Coordinates of the selected corner to play in
        """
        corners = [(0,0), (0,2), (2,0), (2,2)]
        ind = random.randint(0,3)
        return corners[ind]



    def minimax_score(self, board, current_player, depth=0):
        """Determines the score of a board using the minimax algorithm
        
        Parameters
        -------------------
        board: Board
            Playing board to be evaluated
        current_palyer: str
            Player who wants to evaluate his score using the minimax algorithm
        depth: int
            Number used to keep track of the number of moves needed to bring the board to a terminal state
        
        Returns
        -------------------
        Score of the board (int)
        """
        # check if the board is in a terminal state
        if board.is_full() or board.get_winner() is not None:
            winner = board.get_winner()

            if winner == 'X':
                return 10 - depth # return the score adjust by the depth
            elif winner == 'O':
                return depth - 10 # return the score adjust by the depth
            else:
                return 0 # if there is a draw return 0
        
        # if not then apply the algorithm recursively
        legal_moves = board.legal_moves()

        scores = []
        for move in legal_moves: # call the algorithm to determine the score of the available moves
            new_board = board.make_move(move, current_player) 
            opponent = 'X' if current_player == 'O' else 'O'
            score = self.minimax_score(self, new_board, opponent, depth+1)
            scores.append(score)
        
        if current_player == 'X':# player that uses minimax is always X
            return max(scores)
        else:
            return min(scores)


    def minimax_ai(self, board, player):
        """
        Determines what is the best move for the player using the minimax algorithm

        Parameters
        -------------------
        board: Board
            Playing board
        player: str
            Player that is using the minimax algorithm to choos where to play
        
        Returns
        -------------------
        best_move: tuple
            Coordinates of the best move according to the minimax algorithm
        """
        if board.is_empty(): # if the board is empty the best thing to do is to play in one of the corners
            return self.__play_in_corners(board, player)
        
        scores = []
        legal_moves = board.legal_moves()

        for move in legal_moves:
            new_board = board.make_move(move, player) # move make_move method to Board
            opponent = 'X' if player == 'O' else 'O'
            score = self.minimax_score(self, new_board, opponent) # determine the score for each possible board
            scores.append(score)
        
        # depending on who the player is return the position with the highest score or the lowest
        best_ind = scores.index(max(scores)) if player == 'X' else scores.index(min(scores))
        best_move = legal_moves[best_ind]
        return best_move

if __name__ == '__main__':
    b = Board()
    b.board[0][0] = "X"
    b.board[0][1] = "X"
    b.board[1][1] = "O"
    b.board[2][1] = "O"
    ai = AIPlayer()
    print(ai.minimax_ai(b, 'X'))
    
    #find_winning_moves_and_losing_moves_ai(b, 'X')
    #win_coords = find_winning_moves_ai(b, 'X')
    #print('Coordinate vincenti per X:', win_coords)
    #win_coords_2 = find_winning_moves_ai(b, 'O')
    #print('Coordinate vincenti per O:', win_coords_2)