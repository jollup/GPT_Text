from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# === Quit date ===
quit_date = datetime(2025, 9, 1)

# === Short, non-scrolling motivational messages (≤29 chars) ===
normal_messages = [
    "Keep going – {days}d",
    "Still vape-free: {days}d",
    "You're crushing it!",
    "{days} days clean!",
    "Stay strong! {days}d",
    "Vape-free streak: {days}",
    "One day at a time!",
    "Keep it up – {days}d"
]

# === Milestone messages (longer, scrollable) ===
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

# === In-memory cache to update message only once per hour ===
last_hour_checked = None
cached_frame = None

@app.route('/')
def show_days():
    global last_hour_checked, cached_frame

    now = datetime.now()
    days = (now - quit_date).days
    current_hour = now.strftime('%Y-%m-%d %H')

    if current_hour != last_hour_checked:
        # Check if it's a milestone day
        if days in milestones:
            message = random.choice(milestones[days])
            frame = {
                "index": 0,
                "text": message,
                "icon": "a6069",
                "duration": 5000  # show for 5 seconds
            }
        else:
            message = random.choice(normal_messages).format(days=days)
            frame = {
                "index": 0,
                "text": message,
                "icon": "a6069"
                # No duration = default LaMetric behaviour
            }

        cached_frame = frame
        last_hour_checked = current_hour

    return jsonify({
        "frames": [cached_frame]
    })

# === Render entry point ===
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
