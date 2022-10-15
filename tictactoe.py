from player import RandomComputerPlayer
from player import HumanPlayer

class TictacToe:
    def __init__(self):
        self.board = [ ' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: # rows 0-2, 3-5, 6-8
            print("| " + " | ".join(row) + " |")
            
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")
            
    def available_moves(self):
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == " ":
        #         moves.append(i)
        #         
        # return moves
    
        return [i for i, spot in enumerate(self.board) if spot == " "] # adds to list the index of the board if  the value is empty
    
    def empty_squares(self):
        return " " in self.board
        
    def num_empty_squares(self):
        # return len(self.available_moves())
        return self.board.count(" ")
    
    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # row checking
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # col checking
        col_ind = square % 3
        col = [self.board[col_ind + i * 3] for i in range(3)] # [col_ind * 3 for _ in range(3)]
        if all([spot == letter for spot in col]):
            return True
        
        # diagonal checking
        if square % 2 == 0: # indeces are even
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            
            if all([spot == letter for spot in diagonal1]) or all([spot == letter for spot in diagonal2]):
                return True
            
        return False
    
    def previous_moves(self, letter):
        return [i for i, spot in enumerate(self.board) if spot == letter]
            
    
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    
    letter = "X"
    
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
            
        if square < 0:
            print(f"{letter} surrendered")
            winner = 'X' if letter == 'X' else 'O'
            print(f"{winner} wins!")
            return
        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square}')
                game.print_board()
                print("")
            if game.current_winner:
                if print_game:
                    print(f"{letter} wins!")
                return letter
            
            letter = 'O' if letter == 'X' else 'X'
            
    if print_game:
        print("It's a tie")
            
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    new_game = TictacToe()
    
    play(new_game, x_player, o_player)