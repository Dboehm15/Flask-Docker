from flask import Blueprint, request, render_template, json

launchClient = Blueprint('launchListen', __name__)


@launchClient.route('/client', methods=['POST'])
@launchClient.route('/')
def launch():
    try:
        postthang = request.form['thang']
        poststuff = request.form['stuff']
        response = int(poststuff) + int(postthang)

        return str(poststuff) + " + " + str(postthang) + " = " + str(response)
    except Exception as e:
        if str(e) == "invalid literal for int() with base 10: ''":
            return "You need to post stuff and thangs"

        return json.dumps({'errorMessage': str(e)})
