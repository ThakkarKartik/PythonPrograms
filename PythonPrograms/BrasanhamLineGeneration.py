from graphics import *
from time import *
     
def BresenhamLine(x1,y1,x2,y2):
        """ Bresenham Line Drawing Algorithm For All Kind Of Slopes Of Line """
       
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        slope = dy/float(dx)
        
        x, y = x1, y1   
     
        # creating the window
        win = GraphWin('Brasenham Line', 1000, 1000)
        
        # checking the slope if slope > 1 
        # then interchange the role of x and y
        if slope > 1:
            dx, dy = dy, dx
            x, y = y, x
            x1, y1 = y1, x1
            x2, y2 = y2, x2
     
        # initialization of the inital disision parameter
        p = 2 * dy - dx
        
        PutPixle(win, x, y)
     
        for k in range(2, dx):
            if p > 0:
                y = y + 1 if y < y2 else y - 1
                p = p + 2*(dy - dx)
            else:
                p = p + 2*dy
     
            x = x + 1 if x < x2 else x - 1
            
            # delay for 0.01 secs
           # time.sleep(0.01)
            PutPixle(win, x, y)
     
def PutPixle(win, x, y):
        """ Plot A Pixle In The Windows At Point (x, y) """
        pt = Point(x,y)
        pt.draw(win)
     
def main():
        x1 = int(input("Enter Start X: "))
        y1 = int(input("Enter Start Y: "))
        x2 = int(input("Enter End X: "))
        y2 = int(input("Enter End Y: "))
     
        BresenhamLine(x1, y1, x2, y2)
            
if __name__ == "__main__":
        main()
