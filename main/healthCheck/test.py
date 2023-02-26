from flask import Blueprint, request, json

healthCheck = Blueprint('healthCheck', __name__)


@healthCheck.route('/test', methods=['POST'])
@healthCheck.route('/')
def check():
    try:
        postthang = request.form['thang']
        poststuff = request.form['stuff']
        response = int(poststuff) + int(postthang)

        return str(poststuff) + " + " + str(postthang) + " = " + str(response)
    except Exception as e:
        if str(e) == "invalid literal for int() with base 10: ''":
            return "You need to post stuff and thangs"

        return json.dumps({'errorMessage': str(e)})

#curl --location --request POST 'http://127.0.0.1:80/healthcheck/test' \
#                               --form 'stuff="3"' \
#                                      --form 'thang="1"'