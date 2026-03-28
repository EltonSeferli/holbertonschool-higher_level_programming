#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# boş başla (checker problem etməsin)
users = {}


# Home
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# Status
@app.route("/status")
def status():
    return "OK"


# Bütün username-lər
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


# Tək user
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)


# User əlavə etmək
@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.get_json()

        if data is None:
            return jsonify({"error": "Invalid JSON"}), 400

        username = data.get("username")

        if not username:
            return jsonify({"error": "Username is required"}), 400

        if username in users:
            return jsonify({"error": "Username already exists"}), 409

        # user əlavə et
        users[username] = {
            "username": username,
            "name": data.get("name"),
            "age": data.get("age"),
            "city": data.get("city")
        }

        return jsonify({
            "message": "User added",
            "user": users[username]
        }), 201

    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400


if __name__ == "__main__":
    app.run()
