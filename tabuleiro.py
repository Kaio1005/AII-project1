class Board:
    def __init__(self, _board, _print):
        self.board = _board
        self.print = _print
    
    def print_board (self):
        for i in range(self.board):
            for j in range(self.board[i]):
                print(self.board[i][j], end=' ')
            print()
    
    def move_up (self, i, j):
        if self.check_move_up(i, j):
            aux = [[],[],[]]
            for k in range(len(self.board)):
                for l in range(len(self.board[0])):
                    aux[k].append(self.board[k][l])
            aux_2 = aux[i-1][j]
            aux[i-1][j] = aux[i][j]
            aux[i][j] = aux_2
            new_board = Board(aux, self.print)
            return new_board
    
        else:
            return (-1)

    def move_down (self, i, j):
        if self.check_move_down(i,j):
            aux = [[],[],[]]
            for k in range(len(self.board)):
                for l in range(len(self.board[0])):
                    aux[k].append(self.board[k][l])
            aux_2 = aux[i+1][j]
            aux[i+1][j] = aux[i][j]
            aux[i][j] = aux_2
            new_board = Board(aux, self.print)
            return new_board

        else:
            return (-1)
    
    def move_left (self, i, j):
        if self.check_move_left(i, j):
            aux = [[],[],[]]
            for k in range(len(self.board)):
                for l in range(len(self.board[0])):
                    aux[k].append(self.board[k][l])
            aux_2 = aux[i][j-1]
            aux[i][j-1] = aux[i][j]
            aux[i][j] = aux_2
            new_board = Board(aux, self.print)
            return new_board
        
        else:
            return (-1)
    
    def move_right (self, i, j):
        if self.check_move_right(i, j):
            aux = [[],[],[]]
            for k in range(len(self.board)):
                for l in range(len(self.board[0])):
                    aux[k].append(self.board[k][l])
            aux_2 = aux[i][j+1]
            aux[i][j+1] = aux[i][j]
            aux[i][j] = aux_2
            new_board = Board(aux, self.print)
            return new_board
        
        else:
            return (-1)
    
    def check_move_up (self, i, j):
        if i > 0:
            return True
        
        else:
            return False
    
    def check_move_down (self, i, j):
        if i+1 < len(self.board):
            return True
        
        else:
            return False
    
    def check_move_left (self, i, j):
        if j > 0:
            return True
        
        else:
            return False
    
    def check_move_right (self, i, j):
        if j+1 < len(self.board[0]):
            return True
        
        else:
            return False
    
    def compare_boards (self, board_b):
        if (len(self.board) != len(board_b.board) or len(self.board[0]) != len(board_b.board[0])):
            return False
        
        else:
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if (self.board[i][j] != board_b.board[i][j]):
                        return False
                    else:
                        continue
            
            return True
    
    def find_zero (self):
        for i in range (len(self.board)):
            for j in range (len(self.board[i])):
                if (self.board[i][j] == 0):
                    return i,j