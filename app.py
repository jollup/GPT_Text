from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# === Quit date ===
quit_date = datetime(2025, 9, 12)

# === Longer motivational messages (scrolling) ===
normal_messages = [
    "Keep going – you've been vape-free for {days} days!",
    "{days} days clean – that's incredible!",
    "You're smashing it – {days} days no vape!",
    "Still standing strong – {days} days!",
    "Keep your streak alive – {days} days vape-free!",
    "Every day matters – {days} days!",
    "Breathe easy – {days} days strong.",
    "Vape-free and thriving: {days} days!"
]

# === Milestone messages ===
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

# === In-memory cache ===
cached_frame = None
last_hour_checked = None

@app.route('/')
def show_days():
    global cached_frame, last_hour_checked

    now = datetime.now()
    days = (now - quit_date).days
    current_hour = now.strftime('%Y-%m-%d %H')  # e.g., "2025-09-14 15"

    if current_hour != last_hour_checked:
        # Check for milestone message
        if days in milestones:
            message = random.choice(milestones[days])
        else:
            message = random.choice(normal_messages).format(days=days)

        cached_frame = {
            "index": 0,
            "text": message,
            "icon": "a6069",
            "duration": 5000  # show for 5 seconds (scrolling message behaviour)
        }

        last_hour_checked = current_hour

    return jsonify({
        "frames": [cached_frame]
    })

# === For Render deployment ===
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
