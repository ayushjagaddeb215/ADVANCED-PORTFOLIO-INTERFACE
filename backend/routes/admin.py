from flask import Blueprint, request, jsonify, current_app
from functools import wraps
import jwt
from routes.database import load_portfolio, save_portfolio

admin_bp = Blueprint("admin", __name__)

def require_admin(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        token = request.cookies.get("admin_token")
        if not token:
            return jsonify({"error": "Unauthorized"}), 401

        try:
            jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        except Exception:
            return jsonify({"error": "Unauthorized"}), 401

        return fn(*args, **kwargs)
    return wrapper

@admin_bp.route("/admin/portfolio", methods=["GET"])
@require_admin
def get_admin_portfolio():
    return jsonify(load_portfolio())

@admin_bp.route("/admin/portfolio", methods=["PUT"])
@require_admin
def update_admin_portfolio():
    data = request.get_json() or {}
    current = load_portfolio()

    merged = {
        **current,
        **data,
        "socials": {
            **current.get("socials", {}),
            **data.get("socials", {})
        }
    }

    save_portfolio(merged)
    return jsonify({"success": True, "portfolio": merged})

@admin_bp.route("/admin/projects", methods=["PUT"])
@require_admin
def update_projects():
    data = request.get_json() or []
    current = load_portfolio()
    current["projects"] = data
    save_portfolio(current)
    return jsonify({"success": True, "projects": data})

@admin_bp.route("/admin/skills", methods=["PUT"])
@require_admin
def update_skills():
    data = request.get_json() or []
    current = load_portfolio()
    current["skills"] = data
    save_portfolio(current)
    return jsonify({"success": True, "skills": data})