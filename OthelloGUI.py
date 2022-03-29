# Alison

from OthelloBoard import Board
from graphics import *
from Button import Button

class OthelloGUI:
    def __init__(self):
        curBoard = Board()
        prevBoard = Board()
        self.win = GraphWin("Othello", 800, 600, autoflush = False)
        self.win.setBackground("white")
        self.win.setCoords(-15,-17,150+2,150*3/4)

        # butotns
        self.quitButton = Button(Point(115,7), 50, 8, "Quit")
        self.quitButton.activate()
        self.quitButton.draw(self.win)
        self.replayButton = Button(Point(115,-5), 50, 8, "Reset")
        self.replayButton.activate()
        self.replayButton.draw(self.win)

        # title
        title = Text(Point(115, 90), "Othello") 
        title.setSize(36)
        title.draw(self.win)

        # choose to be white or black
        self.startPrompt = Text(Point(115, 35), "Choose what color you want\nto play as (black moves first!)") 
        self.startPrompt.setSize(13)
        self.whiteButton = Button(Point(101,25), 22, 8, "White")
        self.blackButton = Button(Point(129,25), 22, 8, "Black")

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

        # draw the text
        for i in range(8):
            Text(Point(10*i, 97.5), chr(i+ord('a'))).draw(self.win)
        for i in range(8):
            Text(Point(77.5, 10*i+20), i+1).draw(self.win)

        self.gameStart = True
        self.prevGameStart = False # state
        self.currentlyGettingColor = False # lol my variable names don't flame me

        self.userColor = True # color that user chooses at thte start of the game
        self.isDone = False

        self.pieces = []
        for yy in range(8):
            row = []
            y = 8-yy
            for x in range(8):
                row.append(Circle(Point(x*10,y*10+10), 3.8))
            self.pieces.append(row)

        for i in range(8):
            for j in range(8):
                self.pieces[i][j].draw(self.win)

        self.whiteScore = 2
        self.blackScore = 2

        self.win.update()

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
        
        if self.gameStart: return
        # otherwise, if done with getting user color at start...

    def IsDone(self):
        return self.isDone

    def UpdateScore(self):
        self.whiteScoreLabel.setText(str(self.whiteScore))
        self.blackScoreLabel.setText(str(self.blackScore))

    def ResetBoard(self):
        for i in range(8):
            for j in range(8):
                self.pieces[i][j].undraw()

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

        


        

    
        

