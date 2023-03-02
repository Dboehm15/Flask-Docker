import json

# TODO MAKE DOCUMENTATION FOR THE NEW UTILS OBJECT
class utils:
    def __init__(self, token, output):
        self.token = token,
        self.output = output

    def getToken(self):
        return self.token

    def getOutput(self):
        return self.output


def utilsObj(dir):
    try:
        thisDir = dir
        authDir = thisDir[:55] + "OAuth\\data.json"
        f = open(authDir)
        data = json.load(f)
        token = data["access_token"]
        output = thisDir + "\\data.json"
        return utils(token, output)
    except FileNotFoundError:
        thisDir = dir
        authDir = thisDir[:15] + "/OAuth/data.json"
        f = open(authDir)
        data = json.load(f)
        token = data["access_token"]
        output = thisDir + "/data.json"
        return utils(token, output)
