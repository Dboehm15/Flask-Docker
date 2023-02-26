from flask import Flask, render_template
from main.healthCheck.test import healthCheck

app = Flask(__name__)
app.register_blueprint(healthCheck, url_prefix='/healthcheck')


@app.route('/')
def index():
    return render_template('base.html')


app.run(host='0.0.0.0', port=80, debug=True)