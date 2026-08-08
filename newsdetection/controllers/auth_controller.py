from flask import request, jsonify
from services.database_service import register_user, login_user


def register():

    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Check if all fields are provided
    if not username or not email or not password:
        return jsonify({
            "status": False,
            "message": "All fields are required."
        }), 400

    # Store user in database
    result = register_user(username, email, password)

    if result:
        return jsonify({
            "status": True,
            "message": "User registered successfully."
        }), 201

    return jsonify({
        "status": False,
        "message": "Email already exists."
    }), 409


def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "status": False,
            "message": "Email and Password are required."
        }), 400

    user = login_user(email, password)

    if user:
        return jsonify({
            "status": True,
            "message": "Login Successful.",
            "user": user
        }), 200

    return jsonify({
        "status": False,
        "message": "Invalid Email or Password."
    }), 401