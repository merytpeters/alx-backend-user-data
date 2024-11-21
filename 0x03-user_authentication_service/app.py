#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    welcome = jsonify(message="Bienvenue")
    return welcome


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
