from flask import Blueprint, request, jsonify, current_app, make_response
import jwt
from datetime import datetime, timedelta

auth_bp = Blueprint("auth", __name__)

def create_token(username):
    payload = {
        "username": username,
        "exp": datetime.utcnow() + timedelta(days=7),
        "iat": datetime.utcnow()
    }
    return jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")

def decode_token(token):
    try:
        return jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
    except Exception:
        return None

@auth_bp.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    username = data.get("username", "").strip()
    password = data.get("password", "")

    admin_username = current_app.config["ADMIN_USERNAME"]
    admin_password = current_app.config["ADMIN_PASSWORD"]

    if username != admin_username or password != admin_password:
        return jsonify({"success": False, "message": "Invalid credentials"}), 401

    token = create_token(username)
    response = make_response(jsonify({
        "success": True,
        "username": username
    }))

    response.set_cookie(
        "admin_token",
        token,
        httponly=True,
        secure=False,
        samesite="Lax",
        max_age=7 * 24 * 60 * 60
    )
    return response

@auth_bp.route("/auth/logout", methods=["POST"])
def logout():
    response = make_response(jsonify({"success": True}))
    response.delete_cookie("admin_token")
    return response

@auth_bp.route("/auth/verify", methods=["GET"])
def verify():
    token = request.cookies.get("admin_token")
    if not token:
        return jsonify({"authenticated": False}), 401

    payload = decode_token(token)
    if not payload:
        return jsonify({"authenticated": False}), 401

    return jsonify({
        "authenticated": True,
        "username": payload["username"]
    })