import json
from pathlib import Path

DB_FILE = Path("expenses.json")

def load_expenses():
    if DB_FILE.exists():
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DB_FILE, "w") as f:
        json.dump(expenses, f, indent=2)