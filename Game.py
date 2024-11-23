from Player import HumanPlayer, RandomComputerPlayer 
class TicTacToe:

    def __init__(self):
        self.board =[' ' for _ in range (9)] #lista de repeticion de un tablero 3x3
        self.current_winner = None #mantener en cuenta quien va ganando

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+'| '.join(row)+ ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc te dice que numero corresponde a que casilla
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]for j in range (3)]
        for row in number_board:
            print (' |' + ' | '.join(row)+ ' |')

    ####def available_moves(self):
        ##moves = []
        ##for (i, x) in enumerate(self.board):
            #['x','x','o'] -->[(0,'x'),(1,'x'),(2,'o')]
           ### if  spot == ' ':
                ##moves.append(i)
        ####return moves      
    def available_moves(self):
        return [i for i, spot in enumerate(self.board)if spot == '']
 
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count('')
    
    def make_move(self, square, letter):
        #si es un movimiento valido, entonces asigna un cuadro a la letra 
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False

    def winner (self,square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        col_ind = square % 3
        column =[self.board[col_ind+i*3]for i in range(3)]
        if all([spot == letter for spot in row]):
            return True
        
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8] ]
            if all ([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6] ]
            if all ([spot == letter for spot in diagonal2]):
                return True
            
        return False

def play(game, x_player,o_player, print_game=True):
    if print.game:
        game.print_board_nums()


    letter - 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move (square,letter):
            if print_game:
                print(letter + f'makes a move to square{square}')
                game.print_board()
                print('')#linea en blanco

            if game.current_winner: 
                if print_game:
                    print(letter + 'Gana!')
                return letter
            letter = 'O' if letter == 'X' else 'X'

        if print_game:
            print('es un empate')

if __name__ == '_main_':
    x_player = HumanPlayer('x')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game = True)