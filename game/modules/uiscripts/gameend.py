from modules.uitools import *
from modules.generatenoise import *
from modules.bigrestart import *

def gameend(win, data):

    theight,twidth = win.getmaxyx()

    text1 = "AN ERROR HAS OCCURED\n PLEASE MAKE AN ISSUE"
    if data[0] > data[1]:
        text1 = "X HAS WON!!"
    elif data[0] < data[1]:
        text1 = "O HAS WON!!"
    elif data[0] == data[1]:
        text1 = "IT'S A DRAW!!"

    text2= f"X had {data[0]} points, O had {data[1]}."

    totaltext = text1 + "\n" + text2 + "\n\n>Return to main menu"

    drawtextbox(win, int(theight*0.2), -1, int(twidth*0.5), -1, totaltext)
    win.getch()
    restart_program()