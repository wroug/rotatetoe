from modules.generatenoise import generatenoise
from random import randint
import curses
from modules.uitools import *
from modules.getmessage import *
from time import sleep
import getpass
from modules.uiscripts.settings import *
from modules.cleanup import *


def mainmenu(win):
    username = getpass.getuser()
    theight, twidth = win.getmaxyx()

    ratiow = twidth / 238
    ratioy = theight / 63
    if ratiow > ratioy:
        scalemult = ratioy
    elif ratiow < ratioy:
        scalemult = ratiow
    else:
        scalemult = ratiow

    background = generatenoise(twidth - 1, theight - 1, 20 * scalemult, randint(0, 1000000), 1)
    for i in range(len(background)):
        win.addstr(i, 0, background[i], curses.color_pair(7))
    win.refresh()
    drawtextbox(win, text=getmessage("rotatetoe.txt"), width=49, y=int(theight*0.2))

    win.refresh()
    choice = loadmenu(win, "mainmenu.json", {"username":username})
    if choice == 0:
        return
    elif choice == 1:
        settings(win)

    elif choice == 3:
        cleanup()