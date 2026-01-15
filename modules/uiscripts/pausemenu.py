from modules.uitools import *
from modules.centerui import *
from modules.getmessage import getmessage
from modules.cleanup import *
from modules.uiscripts.settings import *

def pausemenu(win):
    fill(win, 7, "~")
    theight, twidth = win.getmaxyx()


    menuwidth = 20

    menuitems = 4

    marginy = centercoords(0, 0, menuitems+3, theight)
    marginx = centercoords(0, 0, 20, twidth)

    location = centercoords(0, 0, menuwidth, twidth)
    h = theight-1-marginy
    h=drawtextbox(win, marginy, location, menuwidth, -1, "MENU\n "+"\n."*menuitems, 1)
    win.refresh()
    choice = loadchoices(win, "pausemenu.json", marginy + 2, location+2, 6)
    if choice == 0:
        fill(win)
        return "pass"
    elif choice == 1:
        settings(win)
    elif choice == 2:
        fill(win)
        return 'data = [[" "] * width for _ in range(height)];brow, bcol = 0, 0 #board row & board column'
    elif choice == 3:
        cleanup()
        return "pass"
    return "pass"
