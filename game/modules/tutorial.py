import json
from modules.uitools import *
from modules.centerui import centercoords
from modules.getmessage import getmessage

def tutorial(disp):
    theight, twidth = disp.getmaxyx()
    marginy = int(theight * 0.05)
    marginx = marginy * 2
    tutorialid = 1
    h=1
    location=1

    while tutorialid != 10:
        fill_rect(disp, marginy, location, twidth - 1 - (marginx * 2), h + 2, 1)
        location = centercoords(0, 0, twidth - 1 - (marginx * 2), twidth)
        h = drawtextbox(disp, marginy, location, twidth - 1 - (marginx * 2), -1, getmessage(f"tutorial{tutorialid}.txt"), 1)

        if tutorialid == 1:
            nav_file = "continue.json"
        elif tutorialid == 9:
            nav_file = "tutorialdone.json"
        else:
            nav_file = "continueorback.json"

        choice = loadchoices(disp, nav_file, marginy + h - 3, 9, 6)

        if choice == 0:
            tutorialid += 1
        else:
            tutorialid -= 1

    disp.clear()
