import curses
import traceback
import time
from contextlib import contextmanager
import locale
# MODULES:
from modules.drawboard import drawboard
from modules.centerui import centercoords
from modules.getvisualdata import  getvisualdata
from modules.commands import commandinit
from modules.wincheck import wincheck
from modules.firsttimecheck import firsttimecheck
from modules.tutorial import tutorial
from modules.cleanup import cleanup
from modules.uiscripts.pausemenu import *
from modules.colors import *
locale.setlocale(locale.LC_ALL, '') #sets some locale thing


@contextmanager #idk
def section(name=None):
    yield

def restart():
    global height, width, compact, gwidth, data, brow, bcol
    height = 3#int(input("Board height?\n > "))
    width = 10#int(input("Board width?\n > "))
    compact = False #input("Compact? (y/n)\n > ").lower().startswith("y")
    gwidth = 3#int(input("Game window width?\n > "))
    data = [[" "] * width for _ in range(height)]
    brow, bcol = 0, 0 #board row & board column

restart()

xray = True




def main(stdscr):
    defcolors()
    # CONFIG STUFF:
    global brow, bcol, height, width, data, enter, compact, gwidth, placed, xac
    xac = stdscr
    down, up, left, right = False, False, False, False
    curses.curs_set(0)
    stdscr.clear()
    curses.set_escdelay(25)
    stdscr.keypad(True)
    stdscr.nodelay(False)
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    clear = True
    placed = False
    row, col = 5, 5
    theight, twidth = stdscr.getmaxyx()
    def TEST(text="NONE"):
        stdscr.addstr(5,5,f"[TEST]-[{text}]")

    def cprint(text): #useless function with no purpse
        nonlocal row, col
        stdscr.addstr(row, 0, str(text))
        row += 1
        stdscr.refresh()
        col = 0

    def celltooffset(bx, by, c=False):  #maths, idk how to explain more
        if c:
            x = bx*2+1
            y = (by*2)+1
            return x,y
        else:
            x = bx*4+1
            y = by*2+1
            return x+1,y
    letter = False

    down, up, left, right, enter = False, False, False, False, False



    for y in range(theight-1):
            stdscr.addstr(y, 0, " "*(twidth-1), curses.color_pair(1))
    stdscr.refresh()
        #while True:
    #    stdscr.addstr(1,1,"Hello!")
    #    stdscr.refresh()
    last_blink = time.time()

    tutorialyn = firsttimecheck(stdscr)

    for y in range(theight-1):
            stdscr.addstr(y, 0, " "*(twidth-1), curses.color_pair(1))
    stdscr.refresh()

    running = True
    while running:




        #stdscr.clear()



        with section("Clear conditons"):
            if down or up or right or left: # on user input (likely will move something)
                clear=False  # REMOVING CLEAR REMOVES FLICKER
        clear = False
        if clear:
            stdscr.clear()
            clear = False

        with section("move"):
            if down:
                brow += 1 if brow != height-1 else 0
            if up:
                brow -= 1 if brow != 0 else 0
            if left:
                bcol -= 1 if bcol != 0 else 0
            if right:
                bcol += 1 if bcol != gwidth-1 else 0


        vdata = getvisualdata(data, gwidth)


        if enter:
            placed = (data[brow][bcol] == " ")
            data[brow][bcol] = ("X" if letter else "O") if data[brow][bcol] == " " else data[brow][bcol]
            letter = not letter


        #TEST(vdata)
        def xrayrender():  #render function for seeing the background scrolling
            global data, board2


            board2 = drawboard(height, width, data, compact)           #draws the board
            drow, dcol = centercoords(board2, [twidth, theight])  #centers drawn board on the
            for i in board2:
                stdscr.addstr(drow, dcol, i, curses.color_pair(1))     #displays with color 1
                drow += 1
            drow -= len(board2)                                        #moves display row back to original place






        def render(): #main playable board rendering
            global vdata, xray
            vdata = getvisualdata(data, gwidth)

            board = drawboard(height, gwidth, vdata, compact)                                   #draws board
            drow, dcol = centercoords(board2 if xray else board, [twidth, theight])        #if xray is on, sets board location to be at left side of xray board
            for i in board:

                stdscr.addstr(drow, dcol, i, curses.color_pair(2))                              #displays board
                drow += 1
            drow -= len(board)

            offsetcol, offsetrow = celltooffset(bcol, brow, compact)                            #sets offset for cursor
            stdscr.addch(drow+offsetrow, dcol+offsetcol, data[brow][bcol], curses.A_REVERSE)    #renders the cursor

            stdscr.refresh()
        if xray:
            xrayrender()
        render()
        if placed:
            tmp_data = [list(col) for col in zip(*data)] #converts it from row-based grid to column based grid
            tmp_data.append(tmp_data.pop(0))             #moves rightmost column to left
            data = [list(row) for row in zip(*tmp_data)] #converts back
            placed = False
            #time.sleep(0.2)
            #render()
        wins = wincheck(data)
        #TEST(f"  x:{wins[0]} | o:{wins[1]} | {data}")                                                                                                  # -----------TESTLINE----------
        if tutorialyn:
            tutorial(stdscr)
            for y in range(theight - 1):
                stdscr.addstr(y, 0, " " * (twidth - 1), curses.color_pair(1))
            if xray:
                xrayrender()
            render()
        tutorialyn = False
        getkeys = True
        while getkeys:
            down, up, left, right, enter = False, False, False, False, False #resets inputs before next check
            key = stdscr.getch()
            pressed = False
            # while not pressed:
            #    pressed = bool(stdscr.getch())
            if key == curses.KEY_DOWN:
                down = True
            if key == curses.KEY_UP:
                up = True
            if key == curses.KEY_LEFT:
                left = True
            if key == curses.KEY_RIGHT:
                right = True
            if key in (curses.KEY_ENTER, 10, 13):
                enter = True
            if key == ord(':'):
                exec(commandinit(stdscr), globals())
                fill(stdscr)
            if key == 27:  # escape key
                exec(pausemenu(stdscr), globals())
            getkeys = False



try:
    curses.wrapper(main)
except KeyboardInterrupt:
    cleanup()
except Exception:
    curses.endwin()
    traceback.print_exc()
