import curses
import traceback
import time
from contextlib import contextmanager
import locale
# MODULES:
from modules.drawboard import drawboard
from modules.centerui import centercoords
from modules.getvisualdata import  getvisualdata


locale.setlocale(locale.LC_ALL, '')
FPS = 15
FRAME_TIME = 1 / FPS
BLINK_RATE = 0.5

@contextmanager
def section(name=None):
    yield


height = int(input("Board height?\n > "))
width = int(input("Board width?\n > "))
compact = input("Compact? (y/n)\n > ").lower().startswith("y")
gwidth = int(input("Game window width?\n > "))
data = [[" "] * width for _ in range(height)]
brow, bcol = 0, 0 #board row & board column







def main(stdscr):
    global brow, bcol, height, width, data, enter, compact, gwidth
    down, up, left, right = False, False, False, False
    curses.curs_set(0)
    stdscr.clear()
    stdscr.keypad(True)
    stdscr.nodelay(False)
    clear = True
    row, col = 5, 5
    theight, twidth = stdscr.getmaxyx()
    def TEST(text="NONE"):
        stdscr.addstr(5,5,f"[TEST]-[{text}]")

    def cprint(text):
        nonlocal row, col
        stdscr.addstr(row, 0, str(text))
        row += 1
        stdscr.refresh()
        col = 0

    def celltooffset(bx, by, c=False):
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





        #while True:
    #    stdscr.addstr(1,1,"Hello!")
    #    stdscr.refresh()
    last_blink = time.time()
    running = True
    while running:
        start_time = time.time()


        #stdscr.clear()



        with section("Clear conditons"):
            if down or up or right or left: # on user input (likely will move something)
                clear=True
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
            data[brow][bcol] = ("X" if letter else "O") if data[brow][bcol] == " " else data[brow][bcol]
            letter = not letter

        TEST(vdata)
        board = drawboard(height, gwidth, vdata, compact)
        drow, dcol = centercoords(board, [twidth, theight])
        for i in board:

            stdscr.addstr(drow, dcol, i)
            drow += 1
        drow -= len(board)

        offsetcol, offsetrow = celltooffset(bcol, brow, compact)
        stdscr.addch(drow+offsetrow, dcol+offsetcol, data[brow][bcol], curses.A_REVERSE)

        stdscr.refresh()



        elapsed = time.time() - start_time
        sleep_time = max(0, round(FRAME_TIME - elapsed))
        #time.sleep(sleep_time)
        getkeys = True
        while getkeys:
            down, up, left, right, enter = False, False, False, False, False
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
            getkeys = False



try:
    curses.wrapper(main)
except Exception:
    curses.endwin()
    traceback.print_exc()