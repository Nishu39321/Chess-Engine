class Cell:
    
    def __init__(self, row, col, obj = None):
        self.row = row
        self.col = col
        self.obj = obj

rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
cols = [1, 2, 3, 4, 5, 6, 7, 8]        
row_map = {label: index for index, label in enumerate(rows)}
col_map = {label: index for index, label in enumerate(cols)}
board = [[Cell(rows[row], cols[col]) for col in range(8)] for row in range(8)]  

def get_cell(row_label, col_label):
    if row_label not in row_map or col_label not in col_map:
        return None  # Return None for invalid cells
    row_index = row_map[row_label]  
    col_index = col_map[col_label] 
    return board[row_index][col_index]  

class Pawn:

    def __init__(self,row, color):
        self.row = row
        self.color = color
        if self.color == "Black":
            self.col = 7
        else:
            self.col = 2
    
    def movement(self):
        ans = []

        if self.color == "Black":
            if self.col == 7:
                cnt = 0
                column = self.col-1
                while column >= 1 and cnt < 2 and get_cell(self.row, column) and get_cell(self.row, column).obj == None:
                    ans.append((self.row, column))
                    column -= 1
                    cnt += 1
            else:
                if self.col >= 2 and get_cell(self.row, self.col-1) and get_cell(self.row, self.col-1).obj == None:
                    ans.append((self.row, self.col-1))
                
        else:
            if self.col == 2:
                cnt = 0
                column = self.col+1
                while column <= 8 and cnt < 2 and get_cell(self.row, column) and get_cell(self.row, column).obj == None:
                    ans.append((self.row, column))
                    cnt += 1
                    column += 1
            else:
                if self.col <= 7 and get_cell(self.row, self.col+1) and get_cell(self.row, self.col+1).obj == None:
                    ans.append((self.row, self.col+1))
        return ans
    
    def attack(self):
        ans = []

        if self.color == "Black":
            if self.row >= 'B' and self.col >= 2:
                target = get_cell(chr(ord(self.row) - 1), self.col-1)
                if target and target.obj and target.obj.color != "Black":
                    ans.append((chr(ord(self.row) - 1), self.col-1))
            if self.row <= 'G' and self.col >= 2:
                target = get_cell(chr(ord(self.row) + 1), self.col-1)
                if target and target.obj and target.obj.color != "Black":
                    ans.append((chr(ord(self.row) + 1), self.col-1))

        else:
            if self.row >= 'B' and self.col <= 7:
                target = get_cell(chr(ord(self.row) - 1), self.col+1)
                if target and target.obj and target.obj.color == "Black":
                    ans.append((chr(ord(self.row) - 1), self.col+1))
            if self.row <= 'G' and self.col <= 7:
                target = get_cell(chr(ord(self.row) + 1), self.col+1)
                if target and target.obj and target.obj.color == "Black":
                    ans.append((chr(ord(self.row) + 1), self.col+1))

        return ans

class Rook:
   
    def __init__(self, row, color):
        self.row = row
        self.color = color
        if self.color == "Black":
            self.col = 8
        else:
            self.col = 1
    
    def movement(self):
        ans = []
        column = self.col-1
        while column >= 1 and get_cell(self.row, column) and get_cell(self.row, column).obj == None:
            ans.append((self.row, column))
            column -= 1
        column = self.col+1
        while column <= 8 and get_cell(self.row, column) and get_cell(self.row, column).obj == None:
            ans.append((self.row, column))
            column += 1

        row = chr(ord(self.row) - 1)
        while 'A' <= row <= 'H' and get_cell(row, self.col) and get_cell(row, self.col).obj == None:
            ans.append((row, self.col))
            row = chr(ord(row) - 1)
        row = chr(ord(self.row) + 1)
        while 'A' <= row <= 'H' and get_cell(row, self.col) and get_cell(row, self.col).obj == None:
            ans.append((row, self.col))
            row = chr(ord(row) + 1)

        return ans

    def attack(self):
        ans = []
        column = self.col-1
        while column >= 1 and get_cell(self.row, column) and get_cell(self.row, column).obj == None:
            column -= 1
        if column >= 1 and get_cell(self.row, column) and get_cell(self.row, column).obj.color != self.color:
            ans.append((self.row, column))

        column = self.col+1
        while column <= 8 and get_cell(self.row, column) and get_cell(self.row, column).obj == None:
            column += 1
        if column <= 8 and get_cell(self.row, column) and get_cell(self.row, column).obj.color != self.color:
            ans.append((self.row, column))
        
        row = chr(ord(self.row) - 1)
        while 'A' <= row <= 'H' and get_cell(row, self.col) and get_cell(row, self.col).obj == None:
            row = chr(ord(row) - 1)
        if 'A' <= row <= 'H' and get_cell(row, self.col) and get_cell(row, self.col).obj.color != self.color:
            ans.append((row, self.col))

        row = chr(ord(self.row) + 1)
        while 'A' <= row <= 'H' and get_cell(row, self.col) and get_cell(row, self.col).obj == None:
            row = chr(ord(row) + 1)
        if 'A' <= row <= 'H' and get_cell(row, self.col) and get_cell(row, self.col).obj.color != self.color:
            ans.append((row, self.col))
        return ans
class Knight:

    def __init__(self, row, color):
        self.row = row
        self.color = color
        if self.color == "Black":
            self.col = 8
        else:
            self.col = 1
    
    def movement(self):
        ans = []
        row1 = chr(ord(self.row) - 2)
        row2 = chr(ord(self.row) + 2)
        col1 = self.col-2
        col2 = self.col+2
        
        # Check if the destination cell is valid and empty (None or out of bounds)
        if 'A' <= row1 <= 'H' and 1 <= self.col+1 <= 8 and get_cell(row1, self.col+1) and get_cell(row1, self.col+1).obj == None:
            ans.append((row1, self.col+1))
        if 'A' <= row1 <= 'H' and 1 <= self.col-1 <= 8 and get_cell(row1, self.col-1) and get_cell(row1, self.col-1).obj == None:
            ans.append((row1, self.col-1))
        if 'A' <= row2 <= 'H' and 1 <= self.col+1 <= 8 and get_cell(row2, self.col+1) and get_cell(row2, self.col+1).obj == None:
            ans.append((row2, self.col+1))
        if 'A' <= row2 <= 'H' and 1 <= self.col-1 <= 8 and get_cell(row2, self.col-1) and get_cell(row2, self.col-1).obj == None:
            ans.append((row2, self.col-1))
        if 'A' <= chr(ord(self.row) + 1) <= 'H' and 1 <= col1 <= 8 and get_cell(chr(ord(self.row) + 1), col1) and get_cell(chr(ord(self.row) + 1), col1).obj == None:
            ans.append((chr(ord(self.row) + 1), col1))
        if 'A' <= chr(ord(self.row) - 1) <= 'H' and 1 <= col1 <= 8 and get_cell(chr(ord(self.row) - 1), col1) and get_cell(chr(ord(self.row) - 1), col1).obj == None:
            ans.append((chr(ord(self.row) - 1), col1))
        if 'A' <= chr(ord(self.row) + 1) <= 'H' and 1 <= col2 <= 8 and get_cell(chr(ord(self.row) + 1), col2) and get_cell(chr(ord(self.row) + 1), col2).obj == None:
            ans.append((chr(ord(self.row) + 1), col2))
        if 'A' <= chr(ord(self.row) - 1) <= 'H' and 1 <= col2 <= 8 and get_cell(chr(ord(self.row) - 1), col2) and get_cell(chr(ord(self.row) - 1), col2).obj == None:
            ans.append((chr(ord(self.row) - 1), col2))

        return ans

    def attack(self):
        ans = []
        row1 = chr(ord(self.row) - 2)
        row2 = chr(ord(self.row) + 2)
        col1 = self.col-2
        col2 = self.col+2
        
        # Check if the target cell contains an opposing piece
        if 'A' <= row1 <= 'H' and 1 <= self.col+1 <= 8 and get_cell(row1, self.col+1) and get_cell(row1, self.col+1).obj and get_cell(row1, self.col+1).obj.color != self.color:
            ans.append((row1, self.col+1))
        if 'A' <= row1 <= 'H' and 1 <= self.col-1 <= 8 and get_cell(row1, self.col-1) and get_cell(row1, self.col-1).obj and get_cell(row1, self.col-1).obj.color != self.color:
            ans.append((row1, self.col-1))
        if 'A' <= row2 <= 'H' and 1 <= self.col+1 <= 8 and get_cell(row2, self.col+1) and get_cell(row2, self.col+1).obj and get_cell(row2, self.col+1).obj.color != self.color:
            ans.append((row2, self.col+1))
        if 'A' <= row2 <= 'H' and 1 <= self.col-1 <= 8 and get_cell(row2, self.col-1) and get_cell(row2, self.col-1).obj and get_cell(row2, self.col-1).obj.color != self.color:
            ans.append((row2, self.col-1))
        if 'A' <= chr(ord(self.row) + 1) <= 'H' and 1 <= col1 <= 8 and get_cell(chr(ord(self.row) + 1), col1) and get_cell(chr(ord(self.row) + 1), col1).obj and get_cell(chr(ord(self.row) + 1), col1).obj.color != self.color:
            ans.append((chr(ord(self.row) + 1), col1))
        if 'A' <= chr(ord(self.row) - 1) <= 'H' and 1 <= col1 <= 8 and get_cell(chr(ord(self.row) - 1), col1) and get_cell(chr(ord(self.row) - 1), col1).obj and get_cell(chr(ord(self.row) - 1), col1).obj.color != self.color:
            ans.append((chr(ord(self.row) - 1), col1))
        if 'A' <= chr(ord(self.row) + 1) <= 'H' and 1 <= col2 <= 8 and get_cell(chr(ord(self.row) + 1), col2) and get_cell(chr(ord(self.row) + 1), col2).obj and get_cell(chr(ord(self.row) + 1), col2).obj.color != self.color:
            ans.append((chr(ord(self.row) + 1), col2))
        if 'A' <= chr(ord(self.row) - 1) <= 'H' and 1 <= col2 <= 8 and get_cell(chr(ord(self.row) - 1), col2) and get_cell(chr(ord(self.row) - 1), col2).obj and get_cell(chr(ord(self.row) - 1), col2).obj.color != self.color:
            ans.append((chr(ord(self.row) - 1), col2))

        return ans

def die(piece):
    get_cell(piece.row, piece.col).obj = None

def move(piece, row, col):
    if get_cell(row, col) and get_cell(row, col).obj != None:
        die(get_cell(row, col).obj)
    get_cell(piece.row, piece.col).obj = None
    piece.row = row
    piece.col = col
    get_cell(row, col).obj = piece 

class King():

    def __init__(self, row, col,color):
        self.row = row
        self.col = col
        self.color = color

    def movement(self):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]
        return valid_moves(directions, self.row, self.col, self.color, 'm', one_step = True)
    
    def attack(self):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]
        return valid_moves(directions, self.row, self.col, self.color, 'a', one_step = True)

    def check_mate(self, board_occupancy, chess_piece):
        # Check if the king is in check
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]
        valid_moves_list = self.show_valid_moves(board_occupancy, chess_piece)
        
        is_in_check = False
        attacking_piece = None
        
        for direction in directions:
            [d_row, d_col] = direction
            r, c = self.position
            while 0 <= r + d_row < 8 and 0 <= c + d_col < 8:
                r += d_row
                c += d_col
                if board_occupancy[r][c] == 0:  # Empty square
                    continue
                elif chess_piece[r][c] and chess_piece[r][c].color != self.color:  # Opponent piece
                    is_in_check = True
                    attacking_piece = chess_piece[r][c]
                    break
                else:
                    break
        
        if is_in_check:
            # Check if no valid moves to escape check
            if not valid_moves_list:
                print("Checkmate Occurred!")
            else:
                print("King is in Check, but there are valid moves to escape.")
        else:
            print("King is not in Check.")
        
        # Stalemate check: no valid moves, King is not in check
        if not valid_moves_list and not is_in_check:
            print("Stalemate Occurred!")

class Queen():

    def __init__(self, row, col,color):
        self.row = row
        self.col = col
        self.color = color

    def movement(self):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]
        return valid_moves(directions, self.row, self.col, self.color, 'm')

    def attack(self):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]
        return valid_moves(directions, self.row, self.col, self.color, 'a')


class Bishop():

    def __init__(self, row, col,color):
        self.row = row
        self.col = col
        self.color = color

    def movement(self):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        return valid_moves(directions, self.row, self.col, self.color, 'm')

    def attack(self):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        return valid_moves(directions, self.row, self.col, self.color, 'a')


def valid_moves(directions, row, col, color, op, one_step=False):
    valid_moves_list = []
    attack_moves_list = []

    # Convert row from letter to index for arithmetic operations
    r_index = row_map[row]
    c_index = col - 1  # Adjust column to 0-based index
    
    for direction in directions:
        d_row, d_col = direction
        r, c = r_index, c_index

        # For pieces like Queen and Rook that move until blocked (in all directions)
        if not one_step:
            while 0 <= r + d_row < 8 and 0 <= c + d_col < 8:
                r += d_row
                c += d_col
                if board[r][c].obj is None:  # Empty square
                    valid_moves_list.append((rows[r], c + 1))  # Convert back to letter and 1-based column
                elif board[r][c].obj and board[r][c].obj.color != color:  # Opponent piece
                    attack_moves_list.append((rows[r], c + 1))
                    break  # Can capture but can't move further
                else:  # Same color piece
                    break
        else:
            # For King (or any piece with one-step movement), check one square in each direction
            r, c = r + d_row, c + d_col
            if 0 <= r < 8 and 0 <= c < 8:
                if board[r][c].obj is None:  # Empty square
                    valid_moves_list.append((rows[r], c + 1))
                elif board[r][c].obj and board[r][c].obj.color != color:  # Opponent piece
                    attack_moves_list.append((rows[r], c + 1))

    # Return valid moves or attack moves based on the operation type (movement or attack)
    if op == 'm':
        return valid_moves_list
    else:
        return attack_moves_list

for i in range(8):
    c = chr(ord('A') + i) 
    get_cell(c, 2).obj = Pawn(c, "White")
    get_cell(c, 7).obj = Pawn(c, "Black")

get_cell('A',1).obj = Rook('A',"White")
get_cell('H',1).obj = Rook('H',"White")
get_cell('A',8).obj = Rook('A',"Black")
get_cell('H',8).obj = Rook('H',"Black")

get_cell('B',1).obj = Knight('B',"White")
get_cell('G',1).obj = Knight('G',"White")
get_cell('B',8).obj = Knight('B',"Black")
get_cell('G',8).obj = Knight('G',"Black")

get_cell('C',1).obj = Bishop('C',1,"White")
get_cell('F',1).obj = Bishop('F',1,"White")
get_cell('C',8).obj = Bishop('C',8,"Black")
get_cell('F',8).obj = Bishop('F',8,"Black")

get_cell('D',1).obj = Queen('D',1,"White")
get_cell('D',8).obj = Queen('D',8,"Black")

get_cell('E',1).obj = King('E',1,"White")
get_cell('E',8).obj = King('E',8,"Black")

for j in range(8):
    for i in range(8):
        print(f"{i}   {j}   {board[i][j].obj}")
    
