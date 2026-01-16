from modules.generatenoise import *
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

    background = getbg()

    running = True
    while running:

        for i in range(len(background)):
            win.addstr(i, 0, background[i], curses.color_pair(7))
        win.refresh()

        heightmult = 0.2 if theight > 38 else 0.05

        drawtextbox(win, text=getmessage("rotatetoe.txt"), width=49, y=int(theight*heightmult))

        win.refresh()
        choice = loadmenu(win, "mainmenu.json", {"username":username})
        if choice == 0:
            running = False
        elif choice == 1:
            for i in range(len(background)):
                win.addstr(i, 0, background[i], curses.color_pair(7))
            win.refresh()

            heightmult = 0.2 if theight > 38 else 0.05

            drawtextbox(win, text=getmessage("rotatetoe.txt"), width=49, y=int(theight * heightmult))

            settings(win)
        elif choice == 2:
            drawtextbox(win, text=getmessage("controls.txt"), width=49, )
            win.getch()

        elif choice == 3:
            cleanup()