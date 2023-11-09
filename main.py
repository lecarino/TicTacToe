from tictactoe import Tictactoe
tictactoe = Tictactoe()
is_finished = False
game_over = False
print('''

 ______   __     ______        ______   ______     ______        ______   ______     ______    
/\__  _\ /\ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\   
\/_/\ \/ \ \ \  \ \ \____     \/_/\ \/ \ \  __ \  \ \ \____     \/_/\ \/ \ \ \/\ \  \ \  __\   
   \ \_\  \ \_\  \ \_____\       \ \_\  \ \_\ \_\  \ \_____\       \ \_\  \ \_____\  \ \_____\ 
    \/_/   \/_/   \/_____/        \/_/   \/_/\/_/   \/_____/        \/_/   \/_____/   \/_____/ 
                                                                                                
by Larrenz Carino
''')
while not is_finished:
    print('Menu:\n'
          '1. Start a new game.\n'
          '2. Exit.\n')
    
    choice = input('Please input your desired choice: ')

    if choice == '1':
        print("\nStarting a new game... ") 
        tictactoe.generate_players()
        tictactoe.game()

    elif choice == '2':
        print("\nThank You For Playing!")
        is_finished = True
    
