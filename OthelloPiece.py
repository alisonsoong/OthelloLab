from graphics import *
class Piece:

    def __init__(self, x, y, color):
        '''x & y should be integers, color should be a boolean '''

        self.x = x
        self.y = y
        self.color = color

        self.circle = Circle(Point(x*10, y*10+10), 3.8)

        if self.color:
            self.circle.setFill('white')
        else:
            self.circle.setFill('black')

    def setColor(self):
        if self.color:
            self.circle.setFill('white')
        else:
            self.circle.setFill('black')
        
    def toggle(self):
        #make toggle also draw
        self.color = not self.color
        
        self.setColor()

    def toggleToColor(self, color):

        self.color = color

        self.setColor()
        
    def undraw(self):
        self.circle.undraw()

    def draw(self, win):
        self.circle.draw(win)
