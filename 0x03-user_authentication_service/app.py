#!/usr/bin/env python3
"""  Script to host a flask application """
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', strict_slashes=True)
def index() -> jsonify:
    info = {
        "message": "Bienvenue"
    }
    return jsonify(info)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
