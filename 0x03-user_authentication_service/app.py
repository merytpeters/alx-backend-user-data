#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify, request, abort
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

        if not email or not password:
            return jsonify(message="Email and password are required"), 400

        user = AUTH.register_user(email, password)
        return jsonify(email=user.email, message="user created"), 200

    except Exception as e:
        return jsonify(message="email already registered"), 400


@app.route("/sessions", methods=["POST"])
def login():
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        if not email and not password:
            abort(401)

        if not AUTH.valid_login(email, password):
            abort(401)

        session_id = AUTH.create_session(email)

        response = jsonify(email=email, message="logged in")
        response.set_cookie("session_id", session_id)
        return response, 200
    except Exception as e:
        return jsonify(message="An error occured"), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
