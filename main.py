from scripts.game_manager import GameManager

def show_menu():
    print('''\nSelect something to do:
    
    1 - Play a game of Tic Tac Toe
    2 - Get statistics
    3 - Download statistics
    4 - Load game history
    0 - Exit''')

if __name__ == '__main__':
    game = GameManager()
    choice = -1

    while choice != 0:
        show_menu()
        inp = int(input("> "))
        if inp == 1: game.play_game()
        elif inp == 2: game.print_stats()
        elif inp == 3: game.download_stats()
        elif inp == 4: game.upload_game_history()
        elif inp == 0: break
        else:
            print('Invalid input! Try something else')
    
    print('Thank you for playing!')