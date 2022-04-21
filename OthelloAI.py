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
                    
        possMoves = []
        for coord in existingPieces:
            validMove = False
            #up
            newCoord = coord
            while newCoord[1] < 7:
                newCoord[1] += 1
                temp = board[newCoord[0]][newCoord[1]]
                if temp != None and temp == not self.color:
                    validMove = True
                elif temp == self.color:
                    validMove = False
                    break
                else:
                    break

            if validMove:
                possMoves.append(newCoord)

        
                
                
                    
                
