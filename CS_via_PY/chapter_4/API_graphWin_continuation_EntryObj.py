from graphics import *
from datetime import datetime

def main():
    win=GraphWin("Fasting Calculator",500,250)
    # win.setBackground("Dark Olive Green")
    win.setBackground(color_rgb(164,120,100))
    main_win_llx=0
    main_win_lly=0
    main_win_urx=100
    main_win_ury=50

    win.setCoords(main_win_llx,main_win_lly,main_win_urx,main_win_ury)
    
    # Borders of Main Window
    outline_win_line1_left=Line(Point(main_win_llx,main_win_lly),Point(main_win_llx,main_win_ury))
    outline_win_line1_left.setWidth(5)
    outline_win_line1_left.setFill("pink")
    outline_win_line1_left.draw(win)
    
    outline_win_line2_top=Line(Point(main_win_llx,main_win_ury),Point(main_win_urx,main_win_ury))
    outline_win_line2_top.setWidth(5)
    outline_win_line2_top.setFill("pink")
    outline_win_line2_top.draw(win)

    outline_win_line3_right=Line(Point(main_win_urx,main_win_ury),Point(main_win_urx,main_win_lly))
    outline_win_line3_right.setWidth(5)
    outline_win_line3_right.setFill("pink")
    outline_win_line3_right.draw(win)

    outline_win_line4_bottom=Line(Point(main_win_urx,main_win_lly),Point(main_win_llx,main_win_lly))
    outline_win_line4_bottom.setWidth(5)
    outline_win_line4_bottom.setFill("pink")
    outline_win_line4_bottom.draw(win)

    # center line for main Window
    mid_win=Line(outline_win_line2_top.getCenter(),outline_win_line4_bottom.getCenter())
    mid_win.setWidth(2.5)
    mid_win.setFill("pink")
    mid_win.draw(win)

    inputBoxDate=Entry(Point(62,37),10)
    inputBoxTime=Entry(Point(62,30),10)
    
    # Datetime config
    now_full_date_time=datetime.now()
    # formatted_date=now_full_date_time.strftime('%Y-%m-%d %H:%M %p')
    cur_date=now_full_date_time.date()
    #  %I:%M %p"
    cur_time=now_full_date_time.time()


    inputBoxDate.setText(cur_date)
    inputBoxDate.setTextColor("white")
    inputBoxDate.setSize(15)
    inputBoxDate.draw(win)

    inputBoxTime.setText(cur_time)
    inputBoxTime.setTextColor("white")
    inputBoxTime.setSize(15)
    inputBoxTime.draw(win)
    
    # Image
    # logo=Image(Point(45,25),"fasting-ramadan.gif")
    # logo.getPixel(20,20)
    # print(logo.getPixel(20,20))
    # logo.setPixel(20,20,"red")
    # print(logo.getPixel(20,20))
    # logo.draw(win)
    
    key=win.getKey()
    while True:

        if key=="q":
            break

main()