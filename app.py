from flask import Flask, request, jsonify
import random
import os

app = Flask(__name__)

poem_bank = {
    "clear": [
        "Blue skies open wide,\nthe sun dances through the leaves,\nwarmth whispers hello."
    ],
    "rain": [
        "Raindrops stitch the day,\ntap-tapping against still glass,\ndreams drip through puddles."
    ],
    "snow": [
        "White hush on the road,\ntime slows under frozen breath,\npeace beneath the storm."
    ]
}

@app.route("/poem")
def get_poem():
    weather = request.args.get("weather", "clear").lower()
    poems = poem_bank.get(weather, poem_bank["clear"])
    return jsonify({"poem": random.choice(poems)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
