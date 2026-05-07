from flask import Blueprint, request, jsonify
import json, os
from datetime import datetime

contact_bp = Blueprint("contact", __name__)

@contact_bp.route("/contact", methods=["POST"])
def contact():
    d = request.get_json()
    if not d or not all(k in d for k in ["name", "email", "message"]):
        return jsonify({"error": "Missing fields"}), 400
    entry = {**d, "timestamp": datetime.utcnow().isoformat()}
    path = "data/messages.json"
    msgs = []
    if os.path.exists(path):
        with open(path) as f:
            msgs = json.load(f)
    msgs.append(entry)
    with open(path, "w") as f:
        json.dump(msgs, f, indent=2)
    return jsonify({"success": True})