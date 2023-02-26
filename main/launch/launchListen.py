from flask import Blueprint, request, render_template

launchListen = Blueprint('launchListen', __name__)


@launchListen.route('/client', methods=['POST'])
@launchListen.route('/')
def launch():
    pw = request.form['thing']
    return pw
