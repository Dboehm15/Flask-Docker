from flask import Blueprint, json
import os
import requests

cseason = Blueprint('cseason', __name__)


@cseason.route('/getseason')
@cseason.route('/')
def season():
    thisDir = os.path.dirname(__file__)
    authDir = thisDir[:55] + "OAuth\\data.json"

    f = open(authDir)
    data = json.load(f)
    token = data["access_token"]

    # TODO make this a post variable sent in the request
    # options are 1=US 2=EU 3=KO and TW 5=CN
    region = "1"

    url = "https://us.api.blizzard.com/sc2/ladder/season/" + str(region) + "?access_token=" + token

    response = requests.get(url)
    data = response.json()

    with open(thisDir + "\data.json", "w") as f:
        json.dump(data, f)

    return data
