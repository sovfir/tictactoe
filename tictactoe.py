
class Tictactoe():
    def __init__(self):
        """class init"""
        self.x_score = 0
        self.zero_score = 0
        self.draw = False
        self.winner = None
        self.board = [[None]*3, [None]*3, [None]*3]
    # updating on winning status
    def ft_win(self):
        if self.draw:
            self.draw = False
            self.winner = None
            self.board = [[None]*3, [None]*3, [None]*3]    
        if self.winner == "x":
            self.x_score += 1
            self.draw = False
            self.winner = None
            self.board = [[None]*3, [None]*3, [None]*3]
        if self.winner =="0":
            self.zero_score += 1
            self.draw = False
            self.winner = None
            self.board = [[None]*3, [None]*3, [None]*3]
    
    def ft_status(self):
        # checking for winning rows
        for row in range(0, 3):
            if((self.board[row][0] == self.board[row][1] == self.board[row][2]) and (self.board[row][0] is not None)):
                self.winner = self.board[row][0]
                break
        # checking for winning columns
        for col in range(0, 3):
            if((self.board[0][col] == self.board[1][col] == self.board[2][col]) and (self.board[0][col] is not None)):
                self.winner = self.board[0][col]
                break
        # check for diagonal self.winners
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and (self.board[0][2] is not None):
            self.winner = self.board[0][2]
        # check for draw
        if(all([all(row) for row in self.board]) and self.winner is None):
            self.draw = True
        self.ft_win()
            
    

    