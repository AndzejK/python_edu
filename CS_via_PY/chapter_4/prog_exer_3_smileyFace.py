from graphics import *
'''
Write a program that draws some sort of face.
'''

def main():

    win = GraphWin("Programming Exercises - 3. Smiley Face",300,300)
    win.setCoords(0,0,100,100)

    head = Circle(Point(50,50),50)
    head.setFill(color_rgb(232, 190,172))

    left_eye=Circle(Point(38,65),8)
    left_eye.setFill("white")
    pupil_left=Circle(left_eye.getCenter(),1)
    pupil_left.setFill("black")

    right_eye=left_eye.clone()
    right_eye.move(25,0)
    pupil_right=pupil_left.clone()
    pupil_right.move(25,0)

    nose=Circle(head.getCenter(),4) #Point(50,50)
    nose.setFill(color_rgb(199,122,88))
    
    head.draw(win)
    left_eye.draw(win)
    right_eye.draw(win)
    pupil_left.draw(win)
    pupil_right.draw(win)
    nose.draw(win)

    win.getMouse()

main()