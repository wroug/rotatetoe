import copy

def getvisualdata(indata, visible): #visible is amount of rows visible
    data = copy.deepcopy(indata)


    for i in data():
        del i[visible:]

    return data