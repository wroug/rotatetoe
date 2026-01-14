
def getmessage(msg):
    with open(f"assets/messages/{msg}", "r") as f:
        return f.read()
