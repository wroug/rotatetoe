
def centercoords(element, tsize, manualpartwidth=0, manualroom=0):#more math that i can't explain
    if not bool(manualpartwidth):
        x = (tsize[0] // 2) - (len(element[0]) // 2)
        y = (tsize[1] // 2) - ((len(element)) // 2)
        return y, x
    else:
        coord = (manualroom // 2) - (manualpartwidth // 2)
        return coord

