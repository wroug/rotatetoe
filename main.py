import curses
import traceback
import time
from contextlib import contextmanager
import locale
# MODULES:
from modules.drawboard import drawboard




locale.setlocale(locale.LC_ALL, '')
FPS = 15
FRAME_TIME = 1 / FPS
BLINK_RATE = 0.5

@contextmanager
def section(name=None):
    yield


height = int(input("Board height?\n > "))
width = int(input("Board width?\n > "))

data = [[" "]*width]*height









def main(stdscr):
    down, up, left, right = False, False, False, False
    curses.curs_set(0)
    stdscr.clear()
    stdscr.keypad(True)
    stdscr.nodelay(True)
    clear = True
    row, col = 0, 0

    def TEST(text="NONE"):
        stdscr.addstr(5,5,f"[TEST]-[{text}]")

    def cprint(text):
        nonlocal row, col
        stdscr.addstr(row, 0, str(text))
        row += 1
        stdscr.refresh()
        col = 0

    def cellToOffset(bx, by, height, width):
        x = bx*2
        y = by*2
        return (x,y)









        #while True:
    #    stdscr.addstr(1,1,"Hello!")
    #    stdscr.refresh()
    last_blink = time.time()
    running = True
    while running:
        start_time = time.time()

        #stdscr.clear()
        getkeys = True
        while getkeys:
            down, up, left, right, enter = False, False, False, False, False
            key = stdscr.getch()
            pressed = False
            while not pressed:
                pressed = bool(stdscr.getch())
            if key == curses.KEY_DOWN:
                down = True
            if key == curses.KEY_UP:
                up = True
            if key == curses.KEY_LEFT:
                left = True
            if key == curses.KEY_RIGHT:
                right = True
            if key == curses.KEY_ENTER:
                enter = True
            getkeys = False


        with section("Clear conditons"):
            if down or up or right or left: # on user input (likely will move something)
                clear=True
        if clear:
            stdscr.clear()
            clear = False

        with section("move"):
            if down:
                row += 1
            if up:
                row -= 1
            if left:
                col -= 1
            if right:
                col += 1



        for i in drawboard(height, width, data):
            stdscr.addstr(row, col, i)
            row += 1
        row -= len(drawboard(height, width, data))


        stdscr.refresh()



        elapsed = time.time() - start_time
        sleep_time = max(0, round(FRAME_TIME - elapsed))
        #time.sleep(sleep_time)


try:
    curses.wrapper(main)
except Exception:
    curses.endwin()
    traceback.print_exc()