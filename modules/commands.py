

def commandinit(display):
    h = stdscr.getmaxyx()[0]
    curses.echo()
    s = disp.getstr()
    curses.noecho()
    disp.addch(h, 0, ':')
    disp.move(1,h)
    command = s.decode("utf-8")
