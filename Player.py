import math 
import random


class Player:
    def _init_(self,letter):
        #la letra es X u O
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def _init_(self, letter):
        super()._init_(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def _init_(self, letter):
        super()._init_(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. imput move (0-9):')
            #tenemos que verificar que este es un valor correcto
            #si el spot no esta disponible en el tablero, decimos que es invalido
            try:
                val= int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print('invalid square, Try again.')

        return val