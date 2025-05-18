# A simple program that converts temprature from Celsius to Fahrenheit

from graphics import *

def main():

    win = GraphWin("Investment Growth Chart",400,300)
    win.setCoords(0,0,3,4) 
    win.setBackground("white")

    # Draw the interface/widget
    Text(Point(1,3),"   Celsius Temprature:").draw(win)
    Text(Point(1,1),"Fahrenheit Temprature:").draw(win)
    input_txt=Entry(Point(1.65,3),5)
    input_txt.setText("0,0")
    input_txt.draw(win)

    output_txt=Text(Point(1.55,1),"")
    output_txt.draw(win)

    btn=Text(Point(1.5,2),"Convert it")
    btn.draw(win)
    Rectangle(Point(1,1.5),Point(2,2.5)).draw(win)

    # Wait for a mouse Event click
    win.getMouse()

    # convert input
    celsius = float(input_txt.getText())
    fahrehit = 9.0/5.0*celsius+32

    # display output and change btn
    output_txt.setText(round(fahrehit,2))
    btn.setText("Quit")

    # wait for a mouse click and tehn quit
    win.getMouse()
    win.close()
    # point=win.getMouse()
    # print(point)
main()