from flask import Flask, render_template
from main.launch.launchClient import launchClient

app = Flask(__name__)
app.register_blueprint(launchClient, url_prefix='/launch')


@app.route('/')
def index():
    return render_template('base.html')


app.run(host='0.0.0.0', port=80, debug=True)