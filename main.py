from flask import Flask, render_template
from main.healthCheck.test import healthCheck
from main.blizzard.sc2.ladder.getSeason import cseason
from main.blizzard.wow.getAh import ah

app = Flask(__name__)
app.register_blueprint(healthCheck, url_prefix='/healthcheck')
app.register_blueprint(cseason, url_prefix='/sc2')
app.register_blueprint(ah, url_prefix='/wow')


@app.route('/')
def index():
    return render_template('base.html')


app.run(host='0.0.0.0', port=80, debug=True)