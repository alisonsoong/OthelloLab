# Button class (Alison)

from graphics import *

class Button:
        """A button class specifically for Shark Runner Game"""

        def __init__(self, center, w, l, label):
                """Creates a button class."""
                self.width,self.length,self.text = w,l,label
                self.x,self.y = center.getX(),center.getY()

                # create the rectangle
                self.xmax, self.xmin = self.x+w/2, self.x-w/2
                self.ymax, self.ymin = self.y+l/2, self.y-l/2

                # create the rectangle
                p1 = Point(self.xmin, self.ymin)
                p2 = Point(self.xmax, self.ymax)
                self.rect = Rectangle(p1, p2)
                self.rect.setOutline('lightgray')
                self.rect.setFill('lightgray')

                # create the label
                self.label = Text(center, label)

                #start deactivated
                self.active = False
                self.deactivate()

        def draw(self, win):
                self.rect.draw(win) 
                self.label.draw(win)

        def setOutlineFillText(self, outline, fill, text):
                self.rect.setOutline(outline)
                self.rect.setFill(fill)
                self.label.setTextColor(text)

        def clicked(self, pt):
                """Returns true if the point is inside of the button false if not"""
                return (self.active and self.xmin <= pt.getX() <= self.xmax
                        and self.ymin <= pt.getY() <= self.ymax)

        def getLabel(self):
                """Returns the label string of this button"""
                return self.text

        def setLabel(self, newLabel):
                """Sets the button's label"""
                self.text = newLabel
                self.label.setText(self.text)

        def isActive(self):
                """returns if button is active"""
                return self.active

        def activate(self):
                "Sets this button to 'active'. Makes button clickable"
                # self.label.setFill('black')
                self.rect.setWidth(2)
                self.active = True

        def deactivate(self):
                "Sets this button to 'inactive'"
                # self.label.setFill("darkgrey")
                self.rect.setWidth(1)
                self.active = False

        def getComponents(self):
                """Returns components of button to draw"""
                return self.rect, self.label

        def undraw(self):
                """undraws the entire button"""
                self.rect.undraw()
                self.label.undraw()


def main():
        print("I am alive")
        win = GraphWin("Testing button", 200, 200)
        win.setCoords(-100, -100, 100, 100)

        # create the button, and activate
        quitButton = Button()
        quitButton.init(Point(0,0),50,30, "quit")
        quitButton.activate()
        
        # draw the two components
        quitButton.getRectangle().draw(win) 
        quitButton.getLabel().draw(win)

        # while the quit button is not pressed...
        pt = win.getMouse()
        while not(quitButton.clicked(pt)):
                pt = win.getMouse()

        # quit button pressed!
        print("Quit button pressed!")
        quitButton.undraw() # undraw the button

        # click to close graphics window
        print("Click to close")
        win.getMouse()
        win.close()
        
if __name__ == "__main__": main()
