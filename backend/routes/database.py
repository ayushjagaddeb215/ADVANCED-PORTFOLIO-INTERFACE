import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
PORTFOLIO_FILE = os.path.join(DATA_DIR, "portfolio.json")
MESSAGES_FILE = os.path.join(DATA_DIR, "messages.json")

DEFAULT_PORTFOLIO = {
    "name": "Ayush Jagaddeb",
    "title": "Full Stack AI Developer",
    "email": "ayushjagadev012@gmail.com",
    "bio": "Specialized in the architecture of API-based applications and AI-powered systems.",
    "available": True,
    "socials": {
        "github": "https://github.com/ayushjagaddeb215",
        "linkedin": "https://www.linkedin.com/in/ayush-jagaddeb",
        "twitter": ""
    },
    "skills": [
        "Java",
        "C",
        "JavaScript",
        "React",
        "Next.js",
        "TypeScript",
        "Python",
        "Flask",
        "PostgreSQL",
        "HTML",
        "CSS"
    ],
    "projects": []
}

def ensure_data_files():
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(PORTFOLIO_FILE):
        with open(PORTFOLIO_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_PORTFOLIO, f, indent=2)

    if not os.path.exists(MESSAGES_FILE):
        with open(MESSAGES_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2)

def load_portfolio():
    ensure_data_files()
    with open(PORTFOLIO_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_portfolio(data):
    ensure_data_files()
    with open(PORTFOLIO_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_messages():
    ensure_data_files()
    with open(MESSAGES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_messages(messages):
    ensure_data_files()
    with open(MESSAGES_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2)