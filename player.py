import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter
        
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        # square = random.choice(game.available_moves()) # randomly choose from the available moves
        winning_squares = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        previous_moves = game.previous_moves(self.letter)
        #square = random.choice([i for l in winning_sqaures for i in l if i in game.available_moves()])
        #square = random.choice([i for l in winning_sqaures if all([i in game.available_moves() for i in l]) for i in l])
        winning_moves = []
        available_moves = list(set(game.available_moves() + previous_moves))
        for l in winning_squares:
            if all([i in available_moves for i in l]):
                winning_moves += l
        winning_moves = list(set(winning_moves) - set(previous_moves))
        if len(winning_moves) > 0:
            square = random.choice(winning_moves)
        elif len(winning_moves) == 0 and len(game.available_moves() > 0):
            square = random.choice(game.available_moves())
        return square
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = int(input(f"{self.letter}'s turn. Input move (0-8): "))
            
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
                #if val in game.available_moves():
                #    valid_square = True
            except ValueError:
                valid_square = False
                print("Invalid square. Try again.")
                
        return val