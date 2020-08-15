'''
    This module will draw the national flag in inscape
'''
from pyautogui import *
from time import sleep


def draw_rectangle():
    press('s')
    click(568,300)
    location =[[775,-168,167,-775,568,534,"ff6600ff"],[775,-171,171,-775,568,705,"ffffff"],[775,-169,169,-775,568,300,"449900ff"]]

    click(568,367,duration=0.2)  #locate
 
    press('p')
    for item in location:
        
        top,left,right,bottom,x,y, color = item

        sleep(0.5)
        drag(top,0,duration=1)
        # click()
        print("done top")
        drag(0, right,duration=1)
        # click()
        print("done right")
        drag(bottom,0,duration=1) 
        # click()
        print("done bottom")
        drag(0, left,duration=1)
        print("done left")
        # click()

        # press('s')
        # click()
        sleep(1)
        #right click
        hotkey('shift','ctrl','f')
        sleep(1)
        #flat color
        click(1534,223)
        sleep(1)
        #color select
        click(1791,477,clicks=2)
        sleep(1)
        #type color name
        typewrite(color,interval=0.01)
        sleep(1)
        #exit the color pallet
        click(1829,143)

        #for the next rectangle
        click(x,y)


def draw_outer_circle():
    #draw outer circle
    press('e')
    mouseDown(911,561)
    sleep(1)
    drag(126,120)
    press('s')

    # click(955,570)
    #add color
    sleep(1)
    #enter color pallet
    hotkey('shift','ctrl','f')
    sleep(1)
    #  flat color
    click(1517,181)
    sleep(1)
    click(1534,223)
    sleep(1)
    #color select
    click(1791,477,clicks=2)
    sleep(1)
    #type color name
    typewrite("ffffff",interval=0.01)
    sleep(1)
    #stroke - color
    click(1615,183)
    sleep(0.3)
    click(1534,223)
    sleep(1)
    #color select
    click(1791,477,clicks=2)

    sleep(1)
    #type color name
    typewrite("1128fffc",interval=0.01)
    sleep(1)

    #stroke
    click(1763,181)
    sleep(0.2)
    click(1596,225,clicks=2)
    hotkey('ctrl','a')
    typewrite('2.5')

    #exit the color pallet
    click(1829,143)
    sleep(1)
    print("outer circle - done")
    click(568,300)


def draw_lines():
    
    lines = [[(910,624),(1036,623)],[(919,594),(1027,651)],[(940,572),(1008,669)],[(974,562),(974,680)],
    [(1003,569),(945,674)],[(1025,589),(924,656)]]


    click(568,300)
    odd_index,even_index,count = 0,0,0
    for line in lines:
        press('p')
    
        start,end = line
        x1,y1 = start
        x2,y2 = end        
            
        sleep(1)
        move(x1,y1)
        sleep(1)
        click(x1,y1,duration=0.5)
        click(x2,y2,duration=0.4)

        #   enter color pallet
        hotkey('shift','ctrl','f')
        sleep(1)
        #  flat color
        click(1517,181)
        sleep(1)
        click(1534,223)
        sleep(1)
        #color select
        click(1791,477,clicks=2)
        sleep(1)
        #type color name
        typewrite("1128fffc",interval=0.01)
        sleep(1)

        #stroke - color
        click(1615,183)
        sleep(0.3)
        click(1534,223)
        sleep(1)
        #color select
        click(1791,477,clicks=2)
        sleep(1)
        #type color name
        typewrite("1128fffc",interval=0.01)
        sleep(1)


        #   line  - thickness
        click(1763,181)
        sleep(0.2)
        click(1596,225,clicks=2)
        hotkey('ctrl','a')
        typewrite('1.5')

        press('s')
        click(568,300)


def draw_inner_circle():

    #               draw inner circle
    press('s')
    sleep(1)
    press('e')
    mouseDown(966,613)
    sleep(1)
    drag(18,17)
    press('s')

    # click(955,570)
    #add color
    sleep(0.51)
    #enter color pallet
    hotkey('shift','ctrl','f')
    sleep(1)
    #flat color
    click(1517,181)
    sleep(1)
    click(1534,223)
    sleep(1)
    #color select
    click(1791,477,clicks=2)
    sleep(1)
    #type color name
    typewrite("1128ffff",interval=0.01)
    sleep(1)
    #       stroke - color
    click(1615,183)
    sleep(0.3)
    click(1534,223)
    sleep(1)
    #color select
    click(1791,477,clicks=2)
    sleep(1)
    #type color name
    typewrite("1128ffff",interval=0.01)
    sleep(1)

    #exit the color pallet
    click(1829,143)


def main():
    
    sleep(2)

    #open the terminal
    hotkey('winleft')

    sleep(2)

    typewrite("inkscape",interval=0.3)

    press('enter')

    sleep(2)
    hotkey('winleft','up')

    sleep(2)

    draw_rectangle()
    
    draw_outer_circle()
    
    draw_lines()

    draw_inner_circle()

    press('s')
    click(568,300)


if __name__ == "__main__":
    print("Bot Started!!!")
    main()





'''
Created By SanthoshGoku
'''
