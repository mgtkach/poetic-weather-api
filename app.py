from flask import Flask, request, jsonify
import random
import os

app = Flask(__name__)

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
    ],
    "Drizzle": [
        "A whispering rain, not quite committed.",
        "The air is stitched with silver threads.",
        "Just enough rain to soften the day’s edges.",
        "The sky exhales in mist and mercy.",
        "A light veil falls across the field’s face.",
        "Nothing rushes, and nothing insists.",
        "This is how gentleness arrives.",
        "The world is damp with possibility.",
        "A hush falls, drop by tender drop.",
        "The trees breathe slowly in the hush."
    ],
    "Thunderstorm": [
        "The sky speaks in a furious tongue.",
        "Light splits the dark like prophecy.",
        "Clouds churn with unspoken history.",
        "The rain does not ask permission today.",
        "Thunder rolls like drums in a ritual.",
        "Even the wind bows under the weight.",
        "Power walks the sky in heavy boots.",
        "Lightning sketches warnings in the air.",
        "The earth braces and remembers its strength.",
        "This is no time for silence."
    ],
    "Snow": [
        "The world forgets its name under white silence.",
        "Each flake a note in winter’s lullaby.",
        "Stillness falls in bright abundance.",
        "The earth wears quiet like a garment.",
        "Snow hushes the fields into wonder.",
        "A softness falls that covers every hurry.",
        "Even the wind moves gently through snow’s prayer.",
        "The sky offers stillness, one flake at a time.",
        "The ground dreams in white and waits for spring.",
        "A feathered silence blesses the trees."
    ],
    "Mist": [
        "The morning wears its veil with grace.",
        "Edges soften where mist touches stone.",
        "The world begins in a breath, not a word.",
        "What you seek may be closer than it seems.",
        "Mist rises slowly, like a forgotten thought.",
        "Each blade of grass holds its own ghost.",
        "The field listens with its eyes closed.",
        "You could disappear here, and be found again.",
        "In this moment, the world remembers to pause.",
        "Mist teaches us to move gently, without certainty."
    ],
    "Fog": [
        "The world walks in silence, hooded and barefoot.",
        "A thick quiet braids itself through the trees.",
        "What you cannot see is still breathing.",
        "The road forgets where it was going.",
        "Even the crows speak in whispers.",
        "Fog lays its hands over everything you know.",
        "A slow erasing of distance and edge.",
        "The horizon folds in on itself like paper.",
        "A day wrapped in its own long question.",
        "Step softly — the world is dreaming out loud."
    ],
    "Haze": [
        "The sky carries weight you cannot name.",
        "Light diffused, like memory before sleep.",
        "The day is caught between presence and past.",
        "Colors blur as if painted in regret.",
        "The world dims, but does not vanish.",
        "The sun hides in plain sight.",
        "Haze speaks in the language of delay.",
        "Even the wind seems unsure of its purpose.",
        "It is hard to tell the difference between distance and dream.",
        "You walk slower in this kind of light."
    ]
}

@app.route("/poem")
def get_poem():
    weather = request.args.get("weather", "clear").lower()
    poems = poem_bank.get(weather, poem_bank["clear"])
    return jsonify({"poem": random.choice(poems)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
