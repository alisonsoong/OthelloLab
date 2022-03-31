# Alison

from ctypes.wintypes import RGB
from turtle import color
from OthelloBoard import Board
from graphics import *
from Button import Button
from OthelloPiece import Piece

class OthelloGUI:
    def __init__(self):
        curBoard = Board()
        prevBoard = Board()
        self.win = GraphWin("Othello", 800, 600, autoflush = False)
        self.win.setBackground("white")
        self.win.setCoords(-15,-17,150+2,150*3/4)

        self.pieces = []
        for yy in range(8):
            row = []
            y = 8-yy
            for x in range(8):
                row.append(Piece(x,y,True))
            self.pieces.append(row)

        # Set up gui
        self.SetUpButtons()
        self.SetUpScoreboard()
        self.SetUpBoard()

        # title
        title = Text(Point(115, 90), "Othello") 
        title.setSize(36)
        title.draw(self.win)

        # choose to be white or black
        self.startPrompt = Text(Point(115, 35), "Choose what color you want\nto play as (black moves first!)") 
        self.startPrompt.setSize(13)
        self.whiteButton = Button(Point(101,25), 22, 8, "White")
        self.blackButton = Button(Point(129,25), 22, 8, "Black")

        self.gameStart = True
        self.prevGameStart = False # state
        self.currentlyGettingColor = False # lol my variable names don't flame me

        self.userColor = True # color that user chooses at thte start of the game
        self.isDone = False

        self.curPlayer = False

        self.win.update()

    def SetUpButtons(self):
        self.quitButton = Button(Point(115,7), 50, 8, "Quit")
        self.quitButton.activate()
        self.quitButton.draw(self.win)
        self.replayButton = Button(Point(115,-5), 50, 8, "Reset")
        self.replayButton.activate()
        self.replayButton.draw(self.win)

    def SetUpScoreboard(self):
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

    def SetUpBoard(self):
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

        self.pieces[3][3].toggleToColor(True)
        self.pieces[3][4].toggleToColor(False)
        self.pieces[4][4].toggleToColor(True)
        self.pieces[4][3].toggleToColor(False)
        for i in range(3,5):
            for j in range(3,5):
                self.pieces[i][j].draw(self.win)

    def Update(self):

        if self.gameStart:
            if not self.prevGameStart: 
                self.ConfigForStart()
                self.prevGameStart = True
                pt = Point(-100,-100)
            else:
                pt = self.win.getMouse()
            self.GetUserColor(pt)
        else:
            pt = self.win.getMouse()

        if self.quitButton.clicked(pt):
            self.isDone = True
            print("Thank you for playing Othello!")
            self.win.close()
            return

        if self.replayButton.clicked(pt):
            self.gameStart = True
            self.prevGameStart = False
            self.ResetBoard()
            self.RemoveConfigForStart()
            return
        
        curX = pt.getX() + 5
        curY = pt.getY() - 15
        curPos = (int(curX/10), int(curY/10)) # current tile clicked

        if self.gameStart: return
        # otherwise, if done with getting user color at start...

        print("AH DONE")
        if self.curPlayer == self.userColor and self.WithinBoard(curPos):
            print("You move")
            self.curPlayer = not self.userColor

        if (self.curPlayer != self.userColor):
            print("AI moves")
            self.curPlayer = self.userColor

    def WithinBoard(self, pos):
        return 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7

    def IsDone(self):
        return self.isDone

    def UpdateScore(self):
        self.whiteScoreLabel.setText(str(self.whiteScore))
        self.blackScoreLabel.setText(str(self.blackScore))

    def ResetBoard(self):
        for i in range(8):
            for j in range(8):
                self.pieces[i][j].undraw()

        self.pieces[3][3].toggleToColor(True)
        self.pieces[3][4].toggleToColor(False)
        self.pieces[4][4].toggleToColor(True)
        self.pieces[4][3].toggleToColor(False)
        for i in range(3,5):
            for j in range(3,5):
                self.pieces[i][j].draw(self.win)

        self.whiteScore = 2
        self.blackScore = 2
        self.UpdateScore()

    def ConfigForStart(self):
        self.startPrompt.draw(self.win)
        self.whiteButton.draw(self.win)
        self.blackButton.draw(self.win)
        self.whiteButton.activate()
        self.blackButton.activate()
        self.win.update()
    
    def RemoveConfigForStart(self):
        self.startPrompt.undraw()
        self.whiteButton.undraw()
        self.blackButton.undraw()

    def GetUserColor(self, pt):
        if self.whiteButton.clicked(pt):
            self.prevGameStart = False
            self.gameStart = False
            self.userColor = True
            self.RemoveConfigForStart()
            return
        elif self.blackButton.clicked(pt):
            self.prevGameStart = False
            self.gameStart = False
            self.userColor = False
            self.RemoveConfigForStart()
            return
        



if __name__ == '__main__': 
    test = OthelloGUI()
    while not test.IsDone():
        test.Update()

        


        

    
        

