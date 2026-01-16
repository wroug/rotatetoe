
def getmessage(msg, variables=None):
    if variables is None:
        variables = {}
    with open(f"assets/messages/{msg}", "r") as f:
        return (f.read()).format(**variables)
