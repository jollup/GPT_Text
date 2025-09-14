from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# === Quit date ===
quit_date = datetime(2025, 9, 12)

# === Motivational messages ===
normal_messages = [
    "Stay strong – {days} days vape-free!",
    "You're crushing it – {days} days!",
    "Keep going – {days} days clean!",
    "You’ve got this – {days} days without vaping!",
    "Amazing progress – {days} days!",
    "Still standing – {days} days vape-free!",
    "Victory streak: {days} days!",
    "number of vape free days – {days} days"
]

# === Milestone messages (can be a list for each day if you want variety) ===
milestones = {
    1:   ["🎉 Day ONE! You’ve started. Keep going!"],
    3:   ["💪 3 days strong – withdrawal fading!"],
    7:   ["🎊 1 week vape-free – amazing progress!"],
    14:  ["🏆 Two weeks – you're smashing it!"],
    21:  ["🧠 3 weeks – new habits forming!"],
    30:  ["🔥 1 month clean! You legend!"],
    60:  ["💥 Two months – unstoppable!"],
    90:  ["🎖️ 3 months – huge achievement!"],
    180: ["🌟 6 months vape-free – next level!"],
    365: ["🎉 ONE YEAR. You’re a hero!"]
}

# === In-memory cache to only update message once per hour ===
last_hour_checked = None
cached_message = None

@app.route('/')
def show_days():
    global last_hour_checked, cached_message

    now = datetime.now()
    days = (now - quit_date).days
    current_hour = now.strftime('%Y-%m-%d %H')

    if current_hour != last_hour_checked:
        if days in milestones:
            cached_message = random.choice(milestones[days])
        else:
            cached_message = random.choice(normal_messages).format(days=days)

        last_hour_checked = current_hour

    return jsonify({
        "frames": [
            {
                "index": 0,
                "text": cached_message,
                "icon": "a6069"
            }
        ]
    })

# === Render entry point ===
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
