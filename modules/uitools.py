import curses
import textwrap
import json
from modules.centerui import *


def fill_rect(win, y, x, width, height, color_pair=0):
    for i in range(height):
        try:
            win.addstr(y + i, x, " " * width, curses.color_pair(color_pair)) # fills area with spaces
        except curses.error:
            pass

def writewrapped(win, y, x, text, width, color_pair=0, calc=False):
    linenumber = 0
    for paragraph in text.splitlines():
        lines = textwrap.wrap(paragraph, width) or [""]
        for line in lines:
            if not calc:
                win.addstr(y + linenumber, x, " "+line, curses.color_pair(color_pair))
            linenumber += 1
    return linenumber

def drawtextbox(win, y, x, width, height=-1, text="", color_pair=0):
    if height == -1:
        height = writewrapped(win, y, x, text, width-2, color_pair, True)+2

    win.addstr(y, x, "█"+("▀"*(width-2))+"█", curses.color_pair(color_pair))
    for row in range(height-2):
        win.addstr(
            y+row+1,
            x,
            "█"+(" "*(width-2))+"█",
            curses.color_pair(color_pair)
        )
    win.addstr(y+height-1, x, "█" + ("▄" * (width - 2)) + "█", curses.color_pair(color_pair))
    writewrapped(win, y+1, x+1, text, width, color_pair)
    return height

def loadchoices(win, filename, y, x, color_pair=0, color_pair_selected=2, cursor=">"):

    with open(f"assets/choices/{filename}") as f:
        file = json.load(f)
    cposes=[]
    for choice, data in file.items():

        yo = y+data["yoffset"]    +1          #y offset
        xo = x+data["xoffset"]+1            #x offset
        cposes.append((yo, xo-1, data["id"], choice))
        win.addstr(yo, xo, choice, curses.color_pair(color_pair))
    win.addch(y+1, x, cursor, curses.color_pair(color_pair))
    getchoice=True
    fw, bw, sel = False, False, False
    cursorpos = 0
    win.refresh()
    while getchoice:




        if cursorpos != 0 and bw:
            cursorpos -= 1
        if cursorpos != len(cposes)-1 and fw:
            cursorpos += 1
        if sel:
            return cposes[cursorpos][2]
        for i in cposes:
            win.addstr(i[0], i[1], " "+i[3], curses.color_pair(color_pair))

        win.addstr(cposes[cursorpos][0], cposes[cursorpos][1], cursor+cposes[cursorpos][3], curses.color_pair(color_pair_selected))
        win.refresh()
        getkeys = True
        while getkeys:
            fw, bw, sel = False, False, False
              # resets inputs before next check
            key = win.getch()
            pressed = False
            # while not pressed:
            #    pressed = bool(stdscr.getch())
            if key == curses.KEY_DOWN:
                fw = True  #forwards
            if key == curses.KEY_UP:
                bw = True  #backwards
            if key == curses.KEY_LEFT:
                bw = True
            if key == curses.KEY_RIGHT:
                fw = True
            if key in (curses.KEY_ENTER, 10, 13):
                sel = True
            getkeys = False



def fill(win, color_pair=1, letter=" "):
    theight, twidth = win.getmaxyx()
    for y in range(theight-1):
            win.addstr(y, 0, letter*(twidth-1), curses.color_pair(color_pair))
    win.refresh()





def inputbox(win, title, scale=20, height=5, inputfile="0"):

    fill(win, 7, "~")
    theight, twidth = win.getmaxyx()

    menuwidth = scale


    marginy = centercoords(0, 0, height, theight)
    marginx = centercoords(0, 0, scale, twidth)

    inputx = marginx + 2
    inputy = marginy + 3

    location = centercoords(0, 0, menuwidth, twidth)
    h = theight - 1 - marginy
    h = drawtextbox(win, marginy, location, menuwidth, height, title+"\n\n", 1)

    #curses.curs_set(1)

    fill_rect(win, inputy, inputx, scale-4, 1, 5)
    win.refresh()
    win.attron(curses.color_pair(8))
    curses.echo()
    user_input = win.getstr(inputy, inputx, scale-4)
    curses.noecho()
    win.attroff(curses.color_pair(8))
    user_input = user_input.decode("utf-8")
    curses.curs_set(0)
    return user_input



def loadmenu(win, menufile):

    with open(f"assets/menus/{menufile}") as f:
        file = json.load(f)

    fill(win, 7, "~")
    theight, twidth = win.getmaxyx()

    menuwidth = file["width"]
    menuheight = file["height"]
    title = file["title"]
    choices = file["choices"]

    menuitems = 4

    marginy = centercoords(0, 0, menuheight, theight)
    marginx = centercoords(0, 0, 20, twidth)

    location = centercoords(0, 0, menuwidth, twidth)
    h = theight - 1 - marginy
    h = drawtextbox(win, marginy, location, menuwidth, -1, title + "\n"*(menuheight-3) , 1)
    win.refresh()
    if choices != 0:
        return loadchoices(win, choices, marginy + 2, location + 2, 6)

