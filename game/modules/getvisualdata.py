import copy

def getvisualdata(indata, visible): #visible is amount of rows visible
    data = copy.deepcopy(indata) #makes copy
    for i in data:
        del i[visible:] #filters out not needed data

    return data