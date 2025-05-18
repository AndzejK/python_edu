# Learning about objects & function in API GraphWin

from graphics import *

def main():
    win=GraphWin("API - GraphWin",500,500)
    win.setCoords(-10,-10,510,510)
    # Graph undertstands the following methods
    # for px in range(50,151):
    #     win.plot(px,100,"red")
    
    # for px in range(50,151):
    #     win.plotPixel(px,100,"green")
    
    click_point=win.checkMouse()
    print(click_point,type(click_point))
    key_string=win.checkKey() 
    print(key_string,type(key_string))

    # Graph undertstands the following objects/Classes
    ## Drawable Objects:
    ### Point, Line, Reectangle, Circle, Oval, Plogon, Text
    ## These graphic objts support following generic fn(s) 
    '''LINES'''
    lineX = Line(Point(0,0),Point(500,0)) # mid point -> Point(250, 0)
    lineX.setFill("pink")
    lineX.setArrow("last")
    lineX.draw(win)
    mid_lineX=Line(lineX.getCenter(),Point(250,500))
    mid_lineX.setFill("pink")
    mid_lineX.draw(win)
    # print(lineX.getP1())
    # print(lineX.getP2())

    lineY = Line(Point(0,0),Point(0,500))
    lineY.setFill("pink")
    lineY.setArrow("last")
    lineY.draw(win)
    mid_lineY=Line(lineY.getCenter(),Point(500,250))
    print("the end of LineY",lineY.getP2())
    mid_lineY.setFill("pink")
    mid_lineY.draw(win)

    find_center_of_LineX=lineX.getCenter()
    
    '''Circle Object'''
    aCircle=Circle(Point(250,250),50)
    aCircle.setFill("red")
    aCircle.draw(win)
    aCircleCenter=aCircle.getCenter()
    aCircleP1=aCircle.getP1()
    aCircleP2=aCircle.getP2()
    print(f"{'-'*15}\n{aCircleP1}\n{aCircleCenter}\n{aCircleP2}")

    '''Rectangle Object'''
    aRectangle=Rectangle(Point(30,30),Point(200,200))
    aRectangle.setOutline("green")
    aRectangle.setWidth(4)
    aRectangle.draw(win)
    center_point_rec=aRectangle.getCenter()
    print(center_point_rec)
    aCircle_within_rec=Circle(center_point_rec,50)
    aCircle_within_rec.setFill("red")
    aCircle_within_rec.draw(win)

    '''Oval Object'''
    aOvel=Oval(Point(320,30),Point(400,200))
    aOvel.setOutline("yellow")
    aOvel.setWidth(4)
    aOvel.draw(win)

    '''Polygon Object'''
    # list_of_random_points=[Point(400,275),Point(300,300),Point(350,450),Point(480,450),Point(335,490)]
    # list_of_random_points = [
    # Point(400, 350),  # right-top
    # Point(300, 300),  # left-top
    # Point(250, 400),  # top vertex
    # Point(280, 480),  # mid-right
    # Point(360, 420)   # bottom-left
    # ]
    from math import sin, cos, pi

    radius = 100
    center_x, center_y = 370, 370
    list_of_random_points = [
        Point(
            center_x + radius * cos(2 * pi * i / 5), # cos(0)=1, sin(0) = 0
            center_y + radius * sin(2 * pi * i / 5)
        ) for i in range(5)
    ]
    print(f"sin(0)={sin(0)}\ncos(0)={cos(0)}")
    aPolygon=Polygon(list_of_random_points)
    aPolygon.setOutline("pink")
    aPolygon.setWidth(4)
    aPolygon.draw(win)
    aPolygon_point_list=aPolygon.getPoints()
    print(aPolygon_point_list)

    # Text, labeling Objects
    aPolygon_txt=Text(Point(375,370),"Regular pentagon")
    aPolygon_txt.setFill("pink")
    aPolygon_txt.setFace("helvetica")
    aPolygon_txt.setSize(18)
    aPolygon_txt.setStyle("bold")
    aPolygon_txt.draw(win)
    win.getMouse()
    aPolygon_txt.setFill("white")
    aCircle_within_rec.undraw()



    key=win.getKey()
    while True:

        if key=='q':
            win.close()

main()