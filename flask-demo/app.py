from flask import Flask
import json


app = Flask(__name__)


@app.route('/hello')
def hello():
    return json.dumps({'hello': 'hi'})


app.run(host='0.0.0.0', port=8090)
