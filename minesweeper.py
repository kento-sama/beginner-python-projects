import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        
        self.board = self.make_new_board()
        self.assign_values_to_board()
        
        self.dug = set()
       
    # generate new board
    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)] # creates a 2x2 array of None
        
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size # 0, 10, 20, 30, 40, 50s are row
            col = loc % self.dim_size # 0 - +9 col
            
            if board[row][col] == '*': # skil if location already has a bomb
                continue
            
            board[row][col] = '*'
            bombs_planted += 1
            
        return board
    
    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)
                
    def get_num_neighboring_bombs(self, row, col):
        # neighbor's location
        # top left = row-1, col-1
        # top middle = row-1, col
        # top right = row-1, col+1
        # left = row, col-1
        # right = row, col+1
        # bottom left = row+1, col-1
        # bottom middle = row+1, col
        # bottom right = row+1, col+1
        num_neignboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size - 1, row+1) + 1): # [row - 1: (row+1) + 1) range in row surrounding the bomb. *Max() to not use below 0 and min() dim_size to not use values above dim_size
            for c in range(max(0, col-1), min(self.dim_size - 1, col+1) + 1): # [col - 1: (col+1) + 1) range in cols surrounding the bomb
                if r == row and c == col: # this is the bomb
                    continue
                if self.board[r][c] == "*":
                    num_neignboring_bombs += 1
                    
        return num_neignboring_bombs
                
        
    def dig(self, row, col):
        self.dug.add((row, col))
        
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        for r in range(max(0, row-1), min(self.dim_size - 1, row+1) + 1):
            for c in range(max(0, col-1), min(self.dim_size - 1, col+1) + 1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
                
        return True

    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
                    
        board = ' '
        
        col_num = 0
        for col in range(self.dim_size + 1):
            if col == 0:
                board += "  "
            else:
                board += f"  {str(col_num)} "
                col_num += 1
        board += "\n"
        
        for _ in range(self.dim_size + 1):
            board += f"----"
        board += "\n"
        
        row_num = 0
        for row in visible_board:
            board += f" {str(row_num)} | "
            board += " | ".join([str(elem) for elem in row]) + "\n"
            row_num += 1
            
        for _ in range(self.dim_size + 1):
            board += f"----"
        board += "\n"
            
        return board
                    
        
    
    
def play(dim_size=10, num_bombs=10):
    board = Board(dim_size, num_bombs)
    
    safe = True
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*',input("Where would you like to dig? Input as row, col: ")) #split on comma, whitespace and more whitespaces
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
            print("Invalid location")
            continue
        
        safe = board.dig(row, col) # True if not bombs dug
        if not safe:
            break
    
    if safe:
        print("You won!")
    else:
        print("Game Over")
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)
        
if __name__ == '__main__':
    play()