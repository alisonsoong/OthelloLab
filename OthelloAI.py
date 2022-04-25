#blub

class OthelloAI:

    def __init__(self, color):
        '''color should be a boolean: True is White, False is black'''
        
        self.color = color

    def possMoves(self, board):
    '''board parameter should be passed as a Board object'''
        existingPieces = []
        
        for x in range(8):
            for y in range(8):
                if board[x][y] == self.color:
                    existingPieces.append([x,y])

        #checking 8 directions
                    
        directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
        for coord in existingPieces:
            #for each piece, the board spaces in the 8 directions are checked iteratively
            #if the move is legal, then it is added to possMoves
            for direction in directions:
                newCoord = [coord[0], coord[1]]
                validMove = False
                while 0 < newCoord[0] < 7 and 0 < newCoord[1] < 7:
                    newCoord[1] += direction[1]
                    newCoord[0] += direction[0]
                    temp = board[newCoord[0]][newCoord[1]]
                    if temp != None and temp == (not self.color):
                        validMove = True
                    elif temp == self.color:
                        validMove = False
                        break
                    else:
                        break

                if validMove:
                    possMoves.append((newCoord[0], newCoord[1]))
                    
        return possMoves

        
                
                
                    
                
