#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Home page"""
    welcome = jsonify(message="Bienvenue")
    return welcome


@app.route("/users", methods=["POST"])
def users():
    """User registration"""
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        user = AUTH.register_user(email, password)
        return jsonify(email=user.email, message="user created"), 201

    except Exception as e:
        return jsonify(message="email already registered"), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
