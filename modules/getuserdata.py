import json


def getuserdata():

    with open("modules/data.json") as f:
        userdata = json.load(f)
        f.close()
        return userdata