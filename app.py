from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# === SET YOUR QUIT DATE HERE ===
quit_date = datetime(2025, 9, 12)

# === MOTIVATIONAL MESSAGES ===
messages = [
    "Stay strong – {days} days vape-free!",
    "You're crushing it – {days} days!",
    "Keep going – {days} days clean!",
    "You’ve got this – {days} days without vaping!",
    "Amazing progress – {days} days!",
    "Still standing – {days} days vape-free!",
    "Victory streak: {days} days!",
    "number of vape free days – {days} days"
]

@app.route('/')
def show_days():
    today = datetime.now()
    days = (today - quit_date).days
    message = random.choice(messages).format(days=days)

    return jsonify({
        "frames": [
            {
                "index": 0,
                "text": message,
                "icon": "a6069"
            }
        ]
    })

# Required for Render – use PORT from environment
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
