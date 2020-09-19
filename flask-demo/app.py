from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
@cross_origin(supports_credentials=True)
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {name}!'


app.run()
