from flask import Blueprint, request, render_template

launchClient = Blueprint('launchListen', __name__)


@launchClient.route('/client', methods=['POST'])
@launchClient.route('/')
def launch():
    pw = request.form['thing']
    return pw
