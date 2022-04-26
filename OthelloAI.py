#blub
from OthelloGUI import *
class OthelloAI:

    def __init__(self, color):
        '''color should be a boolean: True is White, False is black'''
        
        self.color = color

    def possMoves(self, board):
        '''board parameter should be passed as a Board object'''
        possMoves = []
        existingPieces = []
        arr = board.getBoard()
        
        for x in range(8):
            for y in range(8):
                if arr[x][y] == self.color:
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
                    temp = arr[newCoord[0]][newCoord[1]]
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

    '''def trySelfMove(self, MoveObj):
        MoveObj.getBoard.placePiece(MoveObj.getCoord(), self.color)
        score = MoveObj.getBoard.calcScore()
        MoveObj.updateScore(score)
        
        
        

    def tryOpponentMove(self, board, newMove):
        #the opponent is dumb, and will always pick the highest scoring move

    def simulate(self, board, possMoves):

        #moveList stores five item lists that are [moveDepth, score, moveCoordinate, currentBoard, nextMoves[]]
        #another moveList object is appended to the end of the move
        moveList = []
        for coord in possMoves:
            moveList.append(Move(1, None, coord, Board(board)), None)

        for item in moveList:
            self.trySelfMove(item)
            
            if item.getMoveDepth() = 1:
                return moveList

            else:
                moveList[4] = self.possMoves(item[3])
                self.simulate(moveList[4])
                
                
            


        #the strength/value of each move is tracked by your score - opponent score
        #do i need to use moveDepth as an index for an expanding moveList to prevent aliasing?'''

    def simulate(self, board, possMoves):
        moveList = []
        for coord in possMoves:
            moveList.append(Move(1, None, coord, Board(board), None))

        for item in moveList:
            self.trySelf(item)

        return moveList
            
    def trySelf(self, move):
        move.getBoard().placePiece(move.getCoord(), self.color)
        score = move.getBoard().calcScore()
        if self.color == True:
            move.updateScore(score[0])

        else:
            move.updateScore(score[1])

    def simTurn(self, board):
        output = self.simulate(board, self.possMoves(board))

        return output
        


    
    
                            

class Move:

    def __init__(self, moveDepth, score, moveCoordinate, currentBoard, nextMoves):

        self.moveDepth = moveDepth
        self.score = score
        self.moveCoordinate = moveCoordinate
        self.currentBoard = currentBoard
        self.nextMoves = nextMoves

    def updateScore(self, newScore):

        self.score = newScore

    def getMoveDepth(self):

        return self.moveDepth

    def getCoord(self):

        return self.moveCoordinate

    def getBoard(self):

        return self.currentBoard

    def printInfo(self):
        #for debugging purposes
        print("Move Info: ", self.moveDepth, self.score, self.moveCoordinate, 'CurrentBoardBelow', self.nextMoves)
        print(self.currentBoard.rowPrint())


test = Board()
'''test.setValue(3,3, False)
test.setValue(3,4, True)
test.setValue(4,3, True)
test.setValue(4,4, False)'''

test.setValue(2,6, True)
test.setValue(2,5, True)
test.setValue(2,4, True)
test.setValue(4,4, True)

test.setValue(3,2, False)
test.setValue(3,3, False)
test.setValue(3,4, False)
test.setValue(4,3, False)

ai = OthelloAI(False)

temp = ai.simTurn(test)


for item in temp:
    
    item.printInfo()
    print()
            

    
    
        
                
                
                    
                
