from main.utils.utils import utilsObj
from flask import Blueprint, json
import requests
import os


ah = Blueprint('ah', __name__)


@ah.route('/getAH')
@ah.route('/')
def getAuction():
    utils = utilsObj(os.path.dirname(__file__))

    token = str(utils.token)[2:][:-3]

    url = "https://us.api.blizzard.com/data/wow/connected-realm/11/auctions?namespace=dynamic-us&locale=en_US" \
          "&access_token=" + token

    response = requests.get(url)
    data = response.json()

    with open(utils.output, "w") as f:
        json.dump(data, f)

    return data
