class Board:

    def __init__(self, copy = None):
        '''when copying the board, input the another Board object as the copy parameter'''

        if copy != None:
            self.board = copy.copyBoard()

        else:
            self.board = [
                    [], [], [], [], [], [], [], []
                    ]
            for index in self.board:
                for i in range(8):
                    index.append(None)
                
    def __sub__(self, other):
        difference = []
        for x in range(8):
            for y in range(8):
                if self.board[x][y] != other.board[x][y]:
                    difference.append((x, y))
                    
        return difference

    def reset(self):

        for x in range(8):
            for y in range(8):
                self.board[x][y] = None

    def getValue(self, x, y):
        return self.board[x][y]

    def setValue(self, x, y, color):
        '''the color parameter should be a boolean'''
        
        self.board[x][y] = color

    def toggle(self, x, y):
        '''swaps the board. only to be used if the square has already been set'''
        if self.board[x][y] == None:
            return
        
        self.board[x][y] = not self.board[x][y]

    def arr(self):
        '''returns the entire board'''

        return self.board

    def copyBoard(self):
        #didn't want to import numpy or deepcopy
        newBoard = []
        for i in range(8):
            newBoard.append(self.board[i].copy())
    
        return newBoard


        
