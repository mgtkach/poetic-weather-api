from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Poem dictionary (you can expand this further)
poems = {
    "Clear": [
        "The sun spills gold across the quiet field.",
        "All things stretch toward light and call it good.",
        "No curtain today between earth and sky.",
        "A stillness holds the air like a hymn.",
        "Each shadow tells the truth of a bright thing.",
        "Sky without doubt, blue without end.",
        "The day is a bowl of light poured full.",
        "Bare trees reach with ease into the sky.",
        "The morning walks barefoot across the grass.",
        "Light touches even the loneliest stone."
    ],
    "Clouds": [
        "A hush in the sky, soft with remembering.",
        "The sky speaks in softened syllables.",
        "Even the sun bows beneath this gauze.",
        "The day wears a robe of quiet wool.",
        "Clouds drift like thoughts we haven’t named yet.",
        "The air thickens with something unsaid.",
        "All brightness waits behind a curtain.",
        "The world is quilted in pale grey thread.",
        "Today, the sky is thinking deeply.",
        "A pause in the story of light."
    ],
    "Rain": [
        "The sky weeps gently on the earth’s brow.",
        "Each drop a soft question, asked and answered.",
        "Leaves bow under the grace of water.",
        "The world blurs into a kind of prayer.",
        "Puddles gather the sky in quiet bowls.",
        "Rain teaches even stones to listen.",
        "The ground drinks slowly, with reverence.",
        "It is enough to be soaked and still breathing.",
        "The roof hums a lullaby of falling sky.",
        "Even the birds are quiet when the clouds speak."
    ]
    # You can paste more conditions here...
}

@app.route("/poem")
def get_poem():
    weather = request.args.get("weather", "").capitalize()
    # Fallback to "Clear" poems if unknown condition
    poem_list = poems.get(weather, poems["Clear"])
    return jsonify({"poem": random.choice(poem_list)})

# Optional: a root route just to confirm the API is awake
@app.route("/")
def home():
    return "Poetic Weather API is running. Use /poem?weather=Clear"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

