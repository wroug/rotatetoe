import json

def getdata():
    with open('modules/data.json', 'r') as f:
        return json.load(f)

def setdata(inp):
    with open('modules/data.json', 'w') as f:
        json.dump(inp, f)


def resetdata():
    with open('modules/defaults.json', 'r') as d:
        with open('modules/data.json', 'w') as f:
            json.dump(json.load(d), f, indent=4)