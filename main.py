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

def die(piece):
    return "Dead"

class Pawn:

    def __init__(self,row, colour):
        self.row = row
        self.colour = colour
        if self.colour == "Black":
            self.col = 7
        else:
            self.col = 2
    
    def movement(self):
        ans = []

        if self.colour == "Black":
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

        if self.colour == "Black":
            if self.row >= 'B' and self.col >= 2:
                target = get_cell(chr(ord(self.row) - 1), self.col-1)
                if target and target.obj and target.obj.colour != "Black":
                    ans.append((chr(ord(self.row) - 1), self.col-1))
            if self.row <= 'G' and self.col >= 2:
                target = get_cell(chr(ord(self.row) + 1), self.col-1)
                if target and target.obj and target.obj.colour != "Black":
                    ans.append((chr(ord(self.row) + 1), self.col-1))

        else:
            if self.row >= 'B' and self.col <= 7:
                target = get_cell(chr(ord(self.row) - 1), self.col+1)
                if target and target.obj and target.obj.colour == "Black":
                    ans.append((chr(ord(self.row) - 1), self.col+1))
            if self.row <= 'G' and self.col <= 7:
                target = get_cell(chr(ord(self.row) + 1), self.col+1)
                if target and target.obj and target.obj.colour == "Black":
                    ans.append((chr(ord(self.row) + 1), self.col+1))

        return ans

class Rook:
   
    def __init__(self, row, colour):
        self.row = row
        self.colour = colour
        if self.colour == "Black":
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
        if column >= 1 and get_cell(self.row, column) and get_cell(self.row, column).obj.colour != self.colour:
            ans.append((self.row, column))

        column = self.col+1
        while column <= 8 and get_cell(self.row, column) and get_cell(self.row, column).obj == None:
            column += 1
        if column <= 8 and get_cell(self.row, column) and get_cell(self.row, column).obj.colour != self.colour:
            ans.append((self.row, column))
        
        row = chr(ord(self.row) - 1)
        while 'A' <= row <= 'H' and get_cell(row, self.col) and get_cell(row, self.col).obj == None:
            row = chr(ord(row) - 1)
        if 'A' <= row <= 'H' and get_cell(row, self.col) and get_cell(row, self.col).obj.colour != self.colour:
            ans.append((row, self.col))

        row = chr(ord(self.row) + 1)
        while 'A' <= row <= 'H' and get_cell(row, self.col) and get_cell(row, self.col).obj == None:
            row = chr(ord(row) + 1)
        if 'A' <= row <= 'H' and get_cell(row, self.col) and get_cell(row, self.col).obj.colour != self.colour:
            ans.append((row, self.col))
        return ans
class Knight:

    def __init__(self, row, colour):
        self.row = row
        self.colour = colour
        if self.colour == "Black":
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
        if 'A' <= row1 <= 'H' and 1 <= self.col+1 <= 8 and get_cell(row1, self.col+1) and get_cell(row1, self.col+1).obj and get_cell(row1, self.col+1).obj.colour != self.colour:
            ans.append((row1, self.col+1))
        if 'A' <= row1 <= 'H' and 1 <= self.col-1 <= 8 and get_cell(row1, self.col-1) and get_cell(row1, self.col-1).obj and get_cell(row1, self.col-1).obj.colour != self.colour:
            ans.append((row1, self.col-1))
        if 'A' <= row2 <= 'H' and 1 <= self.col+1 <= 8 and get_cell(row2, self.col+1) and get_cell(row2, self.col+1).obj and get_cell(row2, self.col+1).obj.colour != self.colour:
            ans.append((row2, self.col+1))
        if 'A' <= row2 <= 'H' and 1 <= self.col-1 <= 8 and get_cell(row2, self.col-1) and get_cell(row2, self.col-1).obj and get_cell(row2, self.col-1).obj.colour != self.colour:
            ans.append((row2, self.col-1))
        if 'A' <= chr(ord(self.row) + 1) <= 'H' and 1 <= col1 <= 8 and get_cell(chr(ord(self.row) + 1), col1) and get_cell(chr(ord(self.row) + 1), col1).obj and get_cell(chr(ord(self.row) + 1), col1).obj.colour != self.colour:
            ans.append((chr(ord(self.row) + 1), col1))
        if 'A' <= chr(ord(self.row) - 1) <= 'H' and 1 <= col1 <= 8 and get_cell(chr(ord(self.row) - 1), col1) and get_cell(chr(ord(self.row) - 1), col1).obj and get_cell(chr(ord(self.row) - 1), col1).obj.colour != self.colour:
            ans.append((chr(ord(self.row) - 1), col1))
        if 'A' <= chr(ord(self.row) + 1) <= 'H' and 1 <= col2 <= 8 and get_cell(chr(ord(self.row) + 1), col2) and get_cell(chr(ord(self.row) + 1), col2).obj and get_cell(chr(ord(self.row) + 1), col2).obj.colour != self.colour:
            ans.append((chr(ord(self.row) + 1), col2))
        if 'A' <= chr(ord(self.row) - 1) <= 'H' and 1 <= col2 <= 8 and get_cell(chr(ord(self.row) - 1), col2) and get_cell(chr(ord(self.row) - 1), col2).obj and get_cell(chr(ord(self.row) - 1), col2).obj.colour != self.colour:
            ans.append((chr(ord(self.row) - 1), col2))

        return ans

def move(piece, row, col):
    if get_cell(row, col) and get_cell(row, col).obj != None:
        die(get_cell(row, col).obj)
    
    piece.row = row
    piece.col = col
    get_cell(row, col).obj = piece 

    
# Print logic
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


for j in range(8):
    for i in range(8):
        print(f"{i}   {j}   {board[i][j].obj}")
    

