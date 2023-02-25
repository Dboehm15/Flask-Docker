from flask import Flask
from main.launch.launchListen import launchListen

app = Flask(__name__)
app.register_blueprint(launchListen, url_prefix="/launch")


@app.route("/")
def index():
    return "Hello world"


app.run(host="0.0.0.0", port=80)