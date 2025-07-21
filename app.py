from flask import Flask, request, jsonify
from flask_cors import CORS
import pyttsx3

app = Flask(__name__)
CORS(app)

# Initialize pyttsx3 (TTS engine)
engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)

# Optional: Set voice (change index to your preferred one)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 for default, or try 1, 2...

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Simple reply logic (expand later with AI or intents)
    if "hello" in user_message.lower():
        reply = "Hey there! I'm Alan, your glowing assistant 🤖"
    elif "name" in user_message.lower():
        reply = "My name is Alan. I run on Python and neon vibes!"
    elif "time" in user_message.lower():
        from datetime import datetime
        reply = f"The current time is {datetime.now().strftime('%I:%M %p')}."
    else:
        reply = f"You said: '{user_message}'. I'm still learning!"

    # Speak it aloud locally (optional—browser already speaks via JS)
    try:
        engine.say(reply)
        engine.runAndWait()
    except Exception as e:
        print("Speech error:", e)

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)

