import json
from modules.uitools import *
from modules.centerui import centercoords
from modules.getmessage import getmessage
from modules.getuserdata import getuserdata
from modules.generatenoise import *



def firsttimecheck(disp):

    theight, twidth = disp.getmaxyx()
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(6, curses.COLOR_RED, curses.COLOR_BLACK)

    userdata = getuserdata()

    marginy = int(theight * 0.05)
    marginx = marginy * 2

    if userdata["firsttime"]:
        drawbg(disp)
        location = centercoords(0, 0, twidth-1-(marginx*2), twidth)
        h=drawtextbox(disp, marginy, location, twidth-1-(marginx*2), -1, getmessage("tutorialask.txt"), 1)
        choice = loadchoices(disp, "tutorialask.json", marginy+h-3,location+2, 6)
        if choice == 1:
            disp.clear()
            return False
        disp.clear()
        drawtextbox(disp, marginy, location, twidth - 1 - (marginx*2), -1, getmessage("tutorial1.txt"), 1)
        return True


