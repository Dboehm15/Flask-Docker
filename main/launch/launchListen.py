from flask import Blueprint

# from main.launch.launch import stuff

launchListen = Blueprint("launchListen", __name__)


@launchListen.route("/launch", methods=["POST", "GET"])
@launchListen.route("/")
def launch():
    return "The new stuff"


def stuff():
    """The new stuff"""
