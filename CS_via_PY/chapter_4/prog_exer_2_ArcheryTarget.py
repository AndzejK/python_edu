from graphics import *
def main():
    
    win = GraphWin("Programming Exercises - 2. An archery target")
    r=20

    central_circle=Circle(Point(100,100),r)
    central_circle.setFill("Yellow")

    concentring_ring_blue=Circle(Point(100,100),r*2)
    concentring_ring_blue.setFill("Blue")

    concentring_ring_red=Circle(Point(100,100),r*3)
    concentring_ring_red.setFill("red")

    concentring_ring_black=Circle(Point(100,100),r*4)
    concentring_ring_black.setFill("black")
    concentring_ring_white=Circle(Point(100,100),r*5)
    concentring_ring_white.setFill("white")
    
    # Draw shapes
    concentring_ring_white.draw(win)
    concentring_ring_black.draw(win)
    concentring_ring_red.draw(win)
    concentring_ring_blue.draw(win)
    central_circle.draw(win)

    quit_msg=Text(Point(100,190),"To quit click anywhere...")
    quit_msg.setSize(18)
    quit_msg.setTextColor("red")
    quit_msg.draw(win)
    click=win.getMouse()

main()