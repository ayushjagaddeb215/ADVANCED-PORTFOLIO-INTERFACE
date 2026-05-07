from flask import Blueprint, jsonify
import json, os

portfolio_bp = Blueprint("portfolio", __name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/portfolio.json")

@portfolio_bp.route("/portfolio", methods=["GET"])
def get_portfolio():
    try:
        with open(DATA_FILE) as f:
            return jsonify(json.load(f))
    except FileNotFoundError:
        return jsonify({"error": "Not found"}), 404