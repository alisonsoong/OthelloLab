# Alison

# todo: 
# - random generation of memes after pick color 
# 

# from ctypes.wintypes import RGB
# from this import d
# from turtle import color
from OthelloBoard import Board
from graphics import *
from Button import Button
from OthelloPiece import Piece
import time

class OthelloGUI:
    def __init__(self):
        self.curBoard = Board()
        self.curBoard.reset()
        self.prevBoard = Board()
        self.win = GraphWin("Othello", 800, 600, autoflush = False)
        self.win.setBackground("white")
        self.win.setCoords(-15,-17,150+2,150*3/4)

        self.pieces = []
        for yy in range(8):
            row = []
            y = 8-yy
            for x in range(8):
                row.append(Piece(x,y,False))
            self.pieces.append(row)

        # Set up gui
        self.setUpButtons()
        self.setUpScoreboard()
        self.setUpBoard()
        self.setUpPrompt()

        # title
        title = Text(Point(115, 90), "Othello") 
        title.setSize(36)
        title.draw(self.win)

        # choose to be white or black
        self.startPrompt = Text(Point(115, 58), "Choose what color you want\nto play as:") 
        self.startPrompt.setSize(13)
        self.whiteButton = Button(Point(101,48), 22, 8, "White")
        self.whiteButton.setOutlineFillText(color_rgb(255,255,255), color_rgb(98, 150, 100), color_rgb(255,255,255))
        self.blackButton = Button(Point(129,48), 22, 8, "Black")
        self.blackButton.setOutlineFillText(color_rgb(255,255,255), color_rgb(98, 150, 100), color_rgb(255,255,255))

        self.gameStart_ = True
        self.prevGameStart_ = False # state
        self.currentlyGettingColor_ = False # lol my variable names don't flame me

        self.userColor_ = True # color that user chooses at the start of the game
        self.curPlayerColor_ = False # start with white
        self.isDone_ = False
        self.turnSkip_ = False

        self.posMoves = []

        self.win.update()

    def setUpPrompt(self):
        # prompt box
        promptBox = Rectangle(Point(-5, -5), Point(140, 10))
        promptBox.setOutline(color_rgb(255,255,255))
        promptBox.setFill(color_rgb(60,60,60))
        promptBox.draw(self.win)

        # prompt text
        self.prompt = Text(Point(135/2, 5/2), "PROMPT")
        self.prompt.setTextColor(color_rgb(255,255,255))
        self.prompt.draw(self.win)

    def setPrompt(self, text):
        # wrap prompt
        self.prompt.setText(self.wrapPrompt(text))
        self.win.update()

    def wrapPrompt(self, text):
        adjusted = ""
        index = 0
        for i in range(1,len(text)//130+1):
            adjusted += text[index:130*i]
            if (text[i*130] == " " or text[i*130-1] == " "): adjusted += "\n"
            else: adjusted += "-\n"
            index = i*130
        adjusted += text[index:]
        return adjusted

    def setUpButtons(self):
        self.quitButton = Button(Point(115,30), 50, 8, "Quit")
        self.quitButton.activate()
        self.quitButton.setOutlineFillText(color_rgb(255,255,255), color_rgb(60,60,60), color_rgb(255,255,255))
        self.quitButton.draw(self.win)
        self.replayButton = Button(Point(115,19), 50, 8, "Reset")
        self.replayButton.activate()
        self.replayButton.setOutlineFillText(color_rgb(255,255,255), color_rgb(60,60,60), color_rgb(255,255,255))
        self.replayButton.draw(self.win)

    def setUpScoreboard(self):
        self.scoreLabel = Text(Point(115, 75), "Score") 
        self.scoreLabel.setSize(25)
        self.scoreLabel.draw(self.win)
        Text(Point(101, 70), "White").draw(self.win)
        Text(Point(129, 70), "Black").draw(self.win)
        self.whiteScoreLabel = Text(Point(101, 75), "2") 
        self.whiteScoreLabel.setSize(20)
        self.whiteScoreLabel.draw(self.win)
        self.blackScoreLabel = Text(Point(129, 75), "2")
        self.blackScoreLabel.setSize(20) 
        self.blackScoreLabel.draw(self.win)

        self.whiteScore = 2
        self.blackScore = 2

    def setUpBoard(self):
        # draw grid
        for y in range(8):
            for x in range(8):
                rec = Rectangle(Point(x*10-5,y*10+10+5), Point(x*10+10-5,y*10+10+10+5))
                rec.setFill(color_rgb(98, 150, 100))
                rec.setOutline(color_rgb(255, 255, 255))
                rec.draw(self.win)

        # draw the text
        for i in range(8):
            Text(Point(10*i, 97.5), chr(i+ord('a'))).draw(self.win)
        for i in range(8):
            Text(Point(77.5, 10*i+20), i+1).draw(self.win)
        
        # draw the pieces
        self.updateBoard()

    def updateBoard(self):
        # print("updated board")
        diff = self.curBoard-self.prevBoard
        # print(diff)
        for change in diff:
            x,y = change[0], change[1]
            newPiece = self.pieces[x][y]
            newVal = self.curBoard.getValue(x,y)
            if newVal == None:
                newPiece.undraw()
            elif newVal == True:
                newPiece.toggleToColor(True)
                if (self.prevBoard.getValue(x,y) == None): newPiece.draw(self.win)
            elif newVal == False:
                newPiece.toggleToColor(False)
                if (self.prevBoard.getValue(x,y) == None): newPiece.draw(self.win)
        
        self.whiteScore = 0
        self.blackScore = 0
        for x in range(8):
            for y in range(8):
                if self.curBoard.getValue(x,y) == True: self.whiteScore += 1
                elif self.curBoard.getValue(x,y) == False: self.blackScore += 1

        self.updateScore()
        self.win.update()

    def gameStartLogic(self):
        if self.gameStart_:
            if not self.prevGameStart_: 
                self.configForStart()
                self.prevGameStart_ = True
                self.pt = Point(-100,-100)
            else:
                self.pt = self.win.getMouse()
            self.getUserColor(self.pt)
        else:
            if not self.turnSkip_:
                self.pt = self.win.getMouse()
            else:
                time.sleep(1.5)
        
        self.win.update()



    def update(self):

        self.gameStartLogic()

        if self.quitButton.clicked(self.pt):
            self.isDone_ = True
            print("Thank you for playing Othello!")
            self.win.close()
            return

        if self.replayButton.clicked(self.pt):
            self.gameStart_ = True
            self.prevGameStart_ = False
            self.curPlayerColor_ = False
            self.turnSkip_  = False
            self.resetBoard()
            self.removeConfigForStart()
            self.setPrompt(self.msg)
            self.updateBoard()
            return
        
        self.setPrompt(self.msg)
        if self.gameStart_: return
        # otherwise, if done with getting user color at start...

        curX = self.pt.getX() + 5
        curY = self.pt.getY() - 15
        curPos = (int(curX/10), int(curY/10)) # current tile clicked
        curX, curY = curPos[0], curPos[1]
        # print(curPos)
        
        self.prevBoard = Board(self.curBoard) # make a copy of the previous board

        # print(self.userColor_, self.curPlayerColor_)
        self.getUserMoves()

        if self.userColor_ and not self.curPlayerColor_ or self.turnSkip_: # if user color is white, let AI move if cur player is black
            print("first move lol")
            self.makeAIMove()
            self.getUserMoves()
            if self.turnSkip_: 
                self.curPlayerColor_ = not self.curPlayerColor_
                print("SKIP MOVE=-=-=-=-===-=-=-=-=-")
        elif self.makeMove(curPos): # and self.curPlayerColor_ == self.userColor_:
            # print("Made move!")
            if self.curPlayerColor_ == True: self.msg = "White made a move!"
            else: self.msg = "Black made a move!"

            # switch color
            self.curPlayerColor_ = not self.curPlayerColor_
            self.msg += " It is now "
            if self.curPlayerColor_ == True: self.msg += "White's turn to play."
            else: self.msg += "Black's turn to play."

            # let AI move
            self.makeAIMove()
            self.getUserMoves()
            if self.turnSkip_: 
                self.curPlayerColor_ = not self.curPlayerColor_
                print("SKIP MOVE=-=-=-=-===-=-=-=-=-")
        else:
            self.msg = "It is now "
            if self.curPlayerColor_ == True: self.msg += "White's turn to play. "
            else: self.msg += "Black's turn to play. "
            self.msg += "Please press a square with a valid move."
        
        # testing updating board
        # if curPos[0] == 15 and curPos[1] == 9: 
        #     print("GENERATE NEW BOARD")
        #     self.curBoard = self.generateTestBoard()

        # print("AFTER")
        # for y in range(8):
        #     for x in range(8):
        #         print(self.curBoard.getValue(x,y), end=" ")
        #     print()

        self.setPrompt(self.msg)
        self.updateBoard()

    def getUserMoves(self):
        if self.posMoves == []:
            # create new list of possible moves for user
            # self.posMoves = self.curBoard.posMoves() # TODO implement this
            if self.posMoves == []:
                # if it's STILL empty, then move onto the AI
                print("MOVE ON")
                self.turnSkip_ = True
            print("moves generated")
    
    def makeAIMove(self):
        if self.turnSkip_:
            if self.userColor_: self.msg = "White's turn was skipped because no valid moves left! It is Black's "
            else: self.msg = "Black's turn was skipped because no valid moves left! It is White's "
            self.turnSkip_ = False
        else:
            if self.userColor_: self.msg = "It is Black's "
            else: self.msg = "It is White's "
        self.msg += "turn to play! The AI is making a move."
        self.setPrompt(self.msg)
        print("SIMULATE AI, MAKE AI MOVE FIRST")
        time.sleep(1.5)
        self.posMoves = [] # reset
        print("AI DONE")

        # switch color
        self.curPlayerColor_ = not self.curPlayerColor_
        self.msg = " It is now "
        if self.curPlayerColor_ == True: self.msg += "White's turn to play."
        else: self.msg += "Black's turn to play."

            
    def makeMove(self, pos):
        if abs(pos[0]) > 7 or abs(pos[1]) > 7: return False
        return True

    def generateTestBoard(self):
        board = Board()
        
        board.setValue(2,4,True)
        board.setValue(5,1,False)
        
        return board

    def isDone(self):
        return self.isDone_

    def updateScore(self):
        self.whiteScoreLabel.setText(str(self.whiteScore))
        self.blackScoreLabel.setText(str(self.blackScore))

    def resetBoard(self):

        for i in range(8):
            for j in range(8):
                self.pieces[i][j].undraw()
        self.prevBoard = Board() # empty
        self.curBoard.reset()

        self.whiteScore = 2
        self.blackScore = 2
        self.updateScore()

    def configForStart(self):
        curPlayerColor_ = True

        self.msg = "Please choose what color you want to play as. Black moves first!"

        self.startPrompt.draw(self.win)
        self.whiteButton.draw(self.win)
        self.blackButton.draw(self.win)
        self.whiteButton.activate()
        self.blackButton.activate()
        self.win.update()
    
    def removeConfigForStart(self):
        self.startPrompt.undraw()
        self.whiteButton.undraw()
        self.blackButton.undraw()

    def getUserColor(self, pt):
        if self.whiteButton.clicked(pt):
            self.prevGameStart_ = False
            self.gameStart_ = False
            self.userColor_ = True
            self.removeConfigForStart()
            return
        elif self.blackButton.clicked(pt):
            self.prevGameStart_ = False
            self.gameStart_ = False
            self.userColor_ = False
            self.removeConfigForStart()
            return
        
        
        




if __name__ == '__main__': 
    test = OthelloGUI()
    while not test.isDone():
        test.update()