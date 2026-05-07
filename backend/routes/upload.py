from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os

upload_bp = Blueprint("upload", __name__)
ALLOWED_IMG = {"png", "jpg", "jpeg", "gif", "webp"}

def allowed(filename, allowed_set):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowed_set

@upload_bp.route("/upload/profile", methods=["POST"])
def upload_profile():
    f = request.files.get("file")
    if not f or not allowed(f.filename, ALLOWED_IMG):
        return jsonify({"error": "Invalid file"}), 400
    fname = secure_filename(f.filename)
    f.save(f"uploads/profile/{fname}")
    return jsonify({"url": f"/uploads/profile/{fname}"})

@upload_bp.route("/upload/resume", methods=["POST"])
def upload_resume():
    f = request.files.get("file")
    if not f or not f.filename.lower().endswith(".pdf"):
        return jsonify({"error": "PDF only"}), 400
    fname = secure_filename(f.filename)
    f.save(f"uploads/resume/{fname}")
    return jsonify({"url": f"/uploads/resume/{fname}"})

@upload_bp.route("/upload/project", methods=["POST"])
def upload_project():
    f = request.files.get("file")
    if not f or not allowed(f.filename, ALLOWED_IMG):
        return jsonify({"error": "Invalid file"}), 400
    fname = secure_filename(f.filename)
    f.save(f"uploads/projects/{fname}")
    return jsonify({"url": f"/uploads/projects/{fname}"})