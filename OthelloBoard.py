class Board:

    def __init__(self, copy = None):
        '''when copying the board, input the desired Board object as the copy parameter'''
        
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

        self.board[3][3] = True
        self.board[4][4] = True
        self.board[3][4] = False
        self.board[4][3] = False

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

    def simMoves(self, color):
        '''returns a list of possible moves based on the color parameter.
        Colors passed as booleans, white is True, black is False.'''
        
        possMoves = []

        existingPieces = []
        
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == color:
                    existingPieces.append([x,y])

        # print(existingPieces)

        #checking 8 directions
        directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
        for coord in existingPieces:
            #for each piece, the board spaces in the 8 directions are checked iteratively
            #if the move is legal, then it is added to possMoves
            
            for direction in directions:
                newCoord = [coord[0], coord[1]]
                validMove = False
                while 0 <= newCoord[0] + direction[0] <= 7 and 0 <= newCoord[1] + direction[1] <= 7:
                    newCoord[1] += direction[1]
                    newCoord[0] += direction[0]
                    temp = self.board[newCoord[0]][newCoord[1]]
                    if temp != None and temp == (not color):
                        validMove = True
                    elif temp == color:
                        validMove = False
                        break
                    else:
                        break

                if validMove and self.board[newCoord[0]][newCoord[1]] == None:
                    possMoves.append((newCoord[0], newCoord[1]))
        return possMoves

    def calcScore(self):
        '''returns white score then black score'''
        #checks each of the 64 spaces in the board object and tallies the number of each piece
        white = 0
        black = 0
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == True:
                    white += 1
                if self.board[x][y] == False:
                    black += 1
        return white, black

    def placePiece(self, coord, color):
        '''uses methods from Othello Piece class to place a piece and update the board.
        coord should be a tuple pair'''

        self.board[coord[0]][coord[1]] = color
        # print("COORD PLACED: ", coord)
        directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
        for direction in directions:
            newCoord = [coord[0], coord[1]]
            swap = False
            seenStuff = False

            while 0 <= newCoord[0] + direction[0] <= 7 and 0 <= newCoord[1] + direction[1] <= 7:
                newCoord[1] += direction[1]
                newCoord[0] += direction[0]
                temp = self.board[newCoord[0]][newCoord[1]]
                if temp != None and temp == (not color):
                    swap = True
                    seenStuff = True
                    if not (0 <= newCoord[0] + direction[0] <= 7 and 0 <= newCoord[1] + direction[1] <= 7):
                        # if the next step is out of the board
                        swap = False
                        break
                elif temp == None:
                    swap = False
                    break
                elif temp == color:
                    # at end of flip
                    if seenStuff: swap = True
                    else: swap = False
                    break
                else:
                    break

            # print("direction: ", direction, " swap? ", swap)
            if swap:
                newCoord2 = [coord[0], coord[1]]
                while 0 <= newCoord2[0] + direction[0] <= 7 and 0 <= newCoord2[1] + direction[1] <= 7:
                    newCoord2[0] += direction[0]
                    newCoord2[1] += direction[1]

                    temp = self.board[newCoord2[0]][newCoord2[1]]
                    
                    if temp == (not color):
                        # print(newCoord)
                        self.board[newCoord2[0]][newCoord2[1]] = color
                    else:
                        break
                    
    def getBoard(self):
        return self.board

    def rowPrint(self):
        temp = []
        for y in range(7,-1,-1):
            temp2 = []
            for x in range(8):
                temp2.append(self.board[x][y])
            temp.append(temp2)

        for item in temp:
            print(item)
            
    def printBoard(self):
        for y in range(8):
            for x in range(8):
                print(self.board[x][7-y], end=" ")
            print()
                             
def test():
    test = Board()
    test.setValue(3,3, False)
    test.setValue(3,4, True)
    test.setValue(4,3, True)
    test.setValue(4,4, False)

    '''test.setValue(2,6, True)
    test.setValue(2,5, True)
    test.setValue(2,4, True)
    test.setValue(4,4, True)

    test.setValue(3,2, False)
    test.setValue(3,3, False)
    test.setValue(3,4, False)
    test.setValue(4,3, False)'''

    

    possMoves = test.simMoves(False)
    print(possMoves)

    w, b = test.calcScore()
    print(w, b)

    a = input()

    test.placePiece((2,4), False)

    w, b = test.calcScore()
    print(w, b)
    print(test.board)



        
