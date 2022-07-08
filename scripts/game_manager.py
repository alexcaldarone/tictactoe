from scripts.ai import AIPlayer
from scripts.board import Board
import json


class GameManager:
    """
    A class to manage the execution of the Tic-Tac-Toe game

    Attributes:
        self.stats: dict
            A dictionary containing the gamess won by each player
    """
    stats = {"X":0, "O":0, "Draw":0, "Total":0} # dictionary containing games won by each player

    def __init__(self):
        """Contstuctor"""
        pass

    def play_game(self):
        """
        Plays a game of Tic-Tac-Toe
        """
        b = Board() # create the playing board
        ai_function = self.select_ai() # allow the human player to select the AI it wants to play against
        ai_name = getattr(AIPlayer, ai_function) # retrieve the correspoding method from the AIPlayer class
        last_player = None # set last player to None
        winner = None # set winner to None

        while winner is None and (not b.is_full()): # keep playing as long as there is not a winner or the board is not full
            if last_player == None or last_player == 'O': # The AI always plays first 
                ai_move = ai_name(AIPlayer, b, 'X') # the AI chooses where it wants to play
                new = b.make_move(ai_move, 'X') # a move is made in the chosen position
                new.render() # render the new board
                winner = new.get_winner() # determine if there is a winner
                b = new # set the playing board to the new board
                last_player = 'X' # set the last player to the AI
            else:
                human_move = self.get_human_move() # get the move the human wants to make
                new = b.make_move(human_move, 'O') # make the move
                winner = new.get_winner() # determine if there is a winner
                new.render() # render the new board
                b = new # set the playing board to the new board
                last_player = 'O' # set the last player to the human
        
        if winner == None: # if there is no winner
            print("The game ended in a draw")
            self.stats["Draw"] += 1
        else: # if there is a winner print who it is
            print("The winner is the AI.") if winner == "X" else print("The winner is the human")
            self.stats[winner] += 1
        self.stats["Total"] += 1
        

    def print_stats(self):
        """
        Prints the leaderboard 
        """

        if self.stats["Total"] == 0: # if this point is reached then no games have been played
            print('No games have been played yet: No statistics available!')
        else: # otherwise print the leaderboard
            print('Leaderboard:')
            print(f" - AI (X): {self.stats['X']} games won ({self.stats['X'] / self.stats['Total'] * 100}%)")
            print(f" - Human (O): {self.stats['O']} games won ({self.stats['O'] / self.stats['Total'] * 100}%)")
            print(f" - Draws: {self.stats['Draw']} games ({self.stats['Draw'] / self.stats['Total'] * 100}%)")
    
    def download_stats(self):
        """
        Download the dictionary containing the game statistics as a json file
        """
        if self.stats["Total"] == 0: # it there are no statistics to print
            print('No games have been played yet: No statistics available!')
        else:
            out_file = open("game_stats.json", "w")
            json.dump(self.stats, out_file)
            out_file.close()
            print('Your file has been created.')
    
    def upload_game_history(self):
        """
        Upload exsting game statistics from a json file
        """
        print("Enter the file name: ", end='')
        inp = input()
        in_file = open(inp)
        self.stats = json.load(in_file) # load the file as the current statistics
        in_file.close()
        print('Game history successfully loaded.')

    def select_ai(self):
        """
        Allow the user to choose an AI to play against

        Returns
        -------------------
        inp: str
            Name of the AI the human wants to play against
        """
        available = {"random_ai", "find_winning_moves_ai", "find_winning_moves_and_losing_moves_ai", "minimax_ai"}
        print("Choose an AI to play against.")
        print("""
        AIs available:
        1 - random_ai
        2 - find_winning_moves_ai
        3 - find_winning_moves_and_losing_moves_ai
        4 - minimax_ai
        """)
        
        while True:
            inp = input("> ")
            if inp in available: return inp
            else: print('Invalid input, please try again.')


    def get_human_move(self):
        """
        Get the move of the human player in input

        Returns
        -------------------
        x: int
            X-axis coordinate of where the human player wants to play
        y: int
            Y-axis coordinate of where the human player wants to play
        """
        print('Enter the coordinates of where you want to place your next move.')
        x = int(input('Enter X-axis coordinate: '))
        y = int(input('Enter Y-axis coordinate: '))
        return x, y
    

if __name__ == '__main__':
    g = GameManager()
    g.play_game()