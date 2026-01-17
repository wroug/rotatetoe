import time
from modules.uitools import *
from modules.data import *
from modules.bigrestart import restart_program

def settings(win):
    tmp = getdata()
    insettings = True
    while insettings:
        choice = loadmenu(win, "settings.json")
        if choice == 0:
            tmp["xray"] = not tmp["xray"]
            setdata(tmp)
        elif choice == 1:
            choice = loadmenu(win, "needsrestart.json")
            if choice == 1:
                a,b,c=True,True,True
                while a:
                    try:
                        tmp["height"] = int(inputbox(win, "Set conveyor height:",24))
                        setdata(tmp)
                        a = False
                    except ValueError:
                        displayerror(win, "ENTER A NUMBER")
                while b:
                    try:
                        tmp["width"] = int(inputbox(win, "Set conveyor width:",24))
                        setdata(tmp)
                        b = False
                    except ValueError:
                        displayerror(win, "ENTER A NUMBER")
                while c:
                    try:
                        tmp["gameareawidth"] = int(inputbox(win, "Set game area width:", 24))
                        setdata(tmp)
                        c = False
                    except ValueError:
                        displayerror(win, "ENTER A NUMBER")
                restart_program()
        elif choice == 2:
            insettings=False
        elif choice == 3:
            choice = loadmenu(win, "needsrestart.json")
            if choice == 1:
                resetdata()
                fill(win, 7, letter="~")
                drawtextbox(win,text="Done!")
                win.refresh()
                time.sleep(0.9)
            restart_program()