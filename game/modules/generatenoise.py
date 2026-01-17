from opensimplex import OpenSimplex
import json
from random import randint
import curses

def generatenoise(w, h, scale=20, seed=0, octaves=1):
    shades = [' ', '░', '▒', '▓', '█']
    gen = OpenSimplex(seed)

    def octave_noise(xx, yy):
        value = 0
        amp = 1
        freq = 1
        norm = 0
        for _ in range(octaves):
            value += gen.noise2(xx * freq, yy * freq) * amp
            norm += amp
            amp *= 0.5
            freq *= 2
        return value / norm

    rows = []
    for y in range(h):
        row = ''
        for x in range(w):
            n = octave_noise(x / scale, y / scale)
            n = ((n + 1) / 2) ** 1.3
            idx = min(4, int(n * 5))
            row += shades[idx]
        rows.append(row)
    return rows


def genbg(win):
    theight, twidth = win.getmaxyx()
    ratiow = twidth / 238
    ratioy = theight / 63
    if ratiow > ratioy:
        scalemult = ratioy
    elif ratiow < ratioy:
        scalemult = ratiow
    else:
        scalemult = ratiow
    noiselist = generatenoise(twidth - 1, theight - 1, 20 * scalemult, randint(0, 1000000))
    with open("modules/background.json", "w") as f:
        json.dump({"background": noiselist}, f)


def getbg():
    with open("modules/background.json", "r") as f:
        return json.load(f)["background"]

def drawbg(win, color_pair=7):
    background = getbg()
    for i in range(len(background)):
        win.addstr(i, 0, background[i], curses.color_pair(color_pair))
    win.refresh()