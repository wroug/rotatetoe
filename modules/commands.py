import curses

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