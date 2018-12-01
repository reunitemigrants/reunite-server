import os

from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(data='hello')


if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run()
