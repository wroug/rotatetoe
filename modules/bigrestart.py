import os
import sys
import curses

def restart_program():
    curses.endwin()
    python = sys.executable
    os.execv(python, [python] + sys.argv)