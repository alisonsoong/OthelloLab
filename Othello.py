# Alison
from OthelloGUI import OthelloGUI

def main():
    test = OthelloGUI()
    while not test.isDone():
        test.update()


if __name__ == "__main__": main()