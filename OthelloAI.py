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

    def opponentPossMoves(self, board):
        '''carbon copy of possMoves, just for the opponent to the AI'''
        possMoves = []
        existingPieces = []
        arr = board.getBoard()
        
        for x in range(8):
            for y in range(8):
                if arr[x][y] == (not self.color):
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
                    if temp != None and temp == self.color:
                        validMove = True
                    elif temp == (not self.color):
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

        #above is the ai color
        #below is the opponent's response

        for item in moveList:
            tempList = self.opponentPossMoves(item.getBoard())
            oppMoveList = []
            for coord in tempList:
                newMove = Move(item.getMoveDepth() + 1, None, coord, Board(item.getBoard()), None)
                self.tryOpp(newMove)
                oppMoveList.append(newMove)

            item.setNext(oppMoveList)
            

        

        return moveList
            
    def trySelf(self, move):
        move.getBoard().placePiece(move.getCoord(), self.color)
        score = self.calcWeighted(move.getBoard())
        move.updateScore(score)
        
    def tryOpp(self, move):
        '''carbon copy of trySelf, just with swapped colors'''
        move.getBoard().placePiece(move.getCoord(), (not self.color))
        score = self.calcWeighted(move.getBoard())
        move.updateScore(score)

    def simTurn(self, board):
        output = self.simulate(board, self.possMoves(board))
        optimalMoves = []
        bestScore = -1 * 1000
        for move in output:
            lowScore = 1000
            for move2 in move.getNext():
                #for each two-move deep simulation, the lowest possible score is found
                #finds lowest score within each branch
                score = move2.getScore()
                if score < lowScore:
                    lowScore = score

            if lowScore > bestScore:
                #if the lowest score within each branch yields a higher score
                optimalMoves = []
                optimalMoves.append(move)#the entire move is appended to optimalMoves
                bestScore = score

                
                
            if lowScore == bestScore:
                optimalMoves.append(move)

        
        #optimalMoves is a list of all 'good' moves at (as of right now) one turn and one return turn of simulation

        

        return optimalMoves[len(optimalMoves)//2].getCoord() #picks a single move from the list of optimalMoves
        

    def calcWeighted(self, boardObj):
        #checks each of the 64 spaces in the board object and tallies the number of each piece
        #sides and corners are worth more
        #for use in AI
        white = 0
        black = 0
        board = boardObj.getBoard()
        for x in range(8):
            for y in range(8):
                if board[x][y] == True:
                    if (x == 0 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 0) or (x == 7 and y == 7):
                        white += 5
                    elif x == 0 or y == 0:
                        white += 2
                    else:
                        white += 1
                if board[x][y] == False:
                    if (x == 0 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 0) or (x == 7 and y == 7):
                        black += 5
                    elif x == 0 or y == 0:
                        black += 2
                    else:
                        black += 1
        return white, black
    
    
                            

class Move:

    def __init__(self, moveDepth, score, moveCoordinate, currentBoard, nextMoves):

        self.moveDepth = moveDepth
        self.score = score
        self.moveCoordinate = moveCoordinate
        self.currentBoard = currentBoard
        self.nextMoves = nextMoves

    def updateScore(self, newScore):

        self.score = newScore

    def getScore(self):

        
        return self.score[1] - self.score[0]

        #score is stored as (white, black), getScore returns the difference
        #in turns controlled. higher the number, the more "winning" the move

    def getMoveDepth(self):

        return self.moveDepth

    def getCoord(self):

        return self.moveCoordinate

    def getBoard(self):

        return self.currentBoard

    def setNext(self, nextMoves):

        self.nextMoves = nextMoves

    def getNext(self):

        return self.nextMoves

    def printInfo(self):
        #for debugging purposes
        print("Move Info: ", self.moveDepth, self.score, self.moveCoordinate, 'CurrentBoardBelow')
        #print(self.currentBoard.rowPrint())
        print()
        if self.nextMoves != None:
            
            for item in self.nextMoves:

                item.printInfo()


"""test = Board()
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

ai = OthelloAI(False)

moveList = ai.simTurn(test)

test.rowPrint()
print()

print(moveList)"""
            

    
    
        
                
                
                    
                
