import curses
from modules.uitools import *
from modules.centerui import *
from modules.getmessage import *


def commandinit(disp):
    disp.attron(curses.A_REVERSE)
    h, w = disp.getmaxyx()
    disp.addstr(h-1, 0, " "*(w-1))
    disp.addch(h-1, 0, ':')
    disp.move(h-1, 1)
    curses.echo()
    command = disp.getstr().decode('utf-8').strip()
    curses.noecho()
    disp.attroff(curses.A_REVERSE)
    disp.addstr(h - 1, 0, " " * (w - 1))
    # stdscr nor disp work in the return-exec thingy so use xac instead
    if command == "xray":
        return "xac.clear(); xray = not xray"
    elif command == "quit":
        return "quit()"
    elif command == "help":
        curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
        curses.init_pair(6, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(7, curses.COLOR_BLUE, curses.COLOR_BLACK)
        fill(disp, 7, "~")
        theight, twidth = disp.getmaxyx()


        marginy = int(theight * 0.05)
        marginx = marginy * 2


        location = centercoords(0, 0, twidth - 1 - (marginx * 2), twidth)
        h = drawtextbox(disp, marginy, location, twidth - 1 - (marginx * 2), -1, getmessage("command-help.txt"), 1)
        choice = loadchoices(disp, "command-help.json", marginy + h - 1, 9, 6)

        fill(disp, 1)
        return "pass"




    else: return "xray = xray"