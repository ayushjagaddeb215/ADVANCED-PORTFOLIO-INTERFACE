from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from routes.portfolio import portfolio_bp
from routes.upload import upload_bp
from routes.contact import contact_bp
import os

app = Flask(__name__)

CORS(app, origins=["http://localhost:3000"], 
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
     allow_headers=["Content-Type", "Authorization"])

app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB

app.register_blueprint(portfolio_bp, url_prefix="/api")
app.register_blueprint(upload_bp, url_prefix="/api")
app.register_blueprint(contact_bp, url_prefix="/api")

# Serve uploaded files statically
@app.route("/uploads/<path:filename>")
def serve_uploads(filename):
    return send_from_directory("uploads", filename)

# Root health check route
@app.route("/")
def index():
    return jsonify({
        "status": "running",
        "endpoints": [
            "/api/portfolio",
            "/api/upload/profile",
            "/api/upload/resume",
            "/api/upload/project",
            "/api/contact"
        ]
    })

# 404 handler
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Route not found", "available": [
        "GET  /api/portfolio",
        "POST /api/upload/profile",
        "POST /api/upload/resume",
        "POST /api/upload/project",
        "POST /api/contact"
    ]}), 404

if __name__ == "__main__":
    # Create required directories if missing
    for folder in ["uploads/profile", "uploads/resume", "uploads/projects", "data"]:
        os.makedirs(folder, exist_ok=True)

    # Create starter portfolio.json if missing
    portfolio_file = "data/portfolio.json"
    if not os.path.exists(portfolio_file):
        import json
        starter = {
            "name": "Your Name",
            "title": "Your Title",
            "bio": "Your bio here",
            "skills": [],
            "projects": [],
            "social": {}
        }
        with open(portfolio_file, "w") as f:
            json.dump(starter, f, indent=2)
        print(f"Created starter {portfolio_file}")

    print("Flask running on http://localhost:5000")
    print("Test: http://localhost:5000/api/portfolio")
    app.run(debug=True, port=5000, host="0.0.0.0")