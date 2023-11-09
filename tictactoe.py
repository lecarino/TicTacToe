class Tictactoe():
    def __init__(self):
        self.player1 = ''
        self.player2 = ''
        self.initialize_board()
        
    def initialize_board(self):
        self.display = [
            ['1', ' ', '|', ' ', '|', ' '],
            [' ', '-', '+', '-', '+', '-'],
            ['2', ' ', '|', ' ', '|', ' '],
            [' ', '-', '+', '-', '+', '-'],
            ['3', ' ', '|', ' ', '|', ' '],
            [' ', 'A', ' ', 'B', ' ', 'C'],
        ]
        
    def generate_gameboard(self):
       for i in range(6):
        for j in range(6):
            print(self.display[i][j], end='')
        print()

    def generate_players(self):
       self.player1=input('Player 1, please type in what symbol you would like to use for the game: ex: "x", "o" \n')   
       self.player2=input('Player 2, please type in what symbol you would like to use for the game: ex: "x", "o" \n')

    def win_check(self, player_turn):
        # Check row win conditions
        for i in range(0,6,2):
            if self.display[i][1] == player_turn and self.display[i][3] == player_turn and self.display[i][5] == player_turn:
                return True

        # Check column win conditions
        for i in range(1,6,2):
            if self.display[0][i] == player_turn and self.display[2][i] == player_turn and self.display[4][i] == player_turn:
                return True

        # Check diagonal win conditions
        if (self.display[0][1] == player_turn and self.display[2][3] == player_turn and self.display[4][5] == player_turn) or (self.display[0][5] == player_turn and self.display[2][3] == player_turn and self.display[4][1] == player_turn):
            return True

    def game(self):
        self.initialize_board()
        player_turn = self.player1
        winner = None

        while True:
            self.generate_gameboard()
            move = input(f'Player {player_turn}, choose a row (1-3) and column (A-C), e.g., "1A" (or "Q" to quit): ').upper()

            if move == 'Q':
                print('You quit the game!')
                break
            if len(move) == 2 and move[0] in '123' and move[1] in 'ABC' and self.display[(int(move[0]) - 1)*2][(ord(move[1]) - ord('A'))*2 + 1] == ' ':
                row = (int(move[0]) - 1)*2
                col = (ord(move[1]) - ord('A'))*2 + 1
                self.display[row][col] = player_turn

                if self.win_check(player_turn):
                    winner = player_turn
                    break
            
                player_turn = self.player2 if player_turn == self.player1 else self.player1
            else:
                print("Invalid move. Please try again. ")

        self.generate_gameboard()

        if winner:
            print(f'\nPlayer {winner} wins! Congratulations!\n')
        else:
            print("\nIt's a tie! Thanks for playing.\n")
            
