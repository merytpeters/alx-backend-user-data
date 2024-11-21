#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify, request, abort, redirect
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
    except Exception:
        abort(401)


@app.route("/sessions", methods=["DELETE"])
def logout():
    session_id = request.cookies.get("session_id")

    if not session_id:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route("/profile", methods=["GET"])
def profile():
    session_id = request.cookies.get("session_id")

    if not session_id:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)

    return jsonify(email=user.email), 200


@app.route("/reset_password", methods=["POST"])
def get_reset_password_token():
    email = request.form.get("email")

    if not email:
        abort(403)

    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify(email=email, reset_token=reset_token), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
