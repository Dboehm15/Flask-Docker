from flask import Blueprint, request

launchListen = Blueprint("launchListen", __name__)


@launchListen.route("/launch", methods=["POST", "GET"])
@launchListen.route("/")
def launch():
    return "stuff"
