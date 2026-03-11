from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

# Function to generate chatbot response
def get_response(message):

    msg = message.lower()

    if "stress" in msg or "stressed" in msg:
        return "You seem stressed. Try deep breathing or take a short break.", "Stressed"

    elif "anxious" in msg or "anxiety" in msg:
        return "Anxiety can feel overwhelming. Try slow breathing exercises.", "Anxious"

    elif "sad" in msg or "depressed" in msg:
        return "I'm sorry you're feeling sad. Talking to someone you trust may help.", "Sad"

    elif "happy" in msg:
        return "That's great to hear! Keep doing things that make you happy.", "Happy"

    elif "lonely" in msg:
        return "Feeling lonely happens sometimes. Maybe call a friend or family member.", "Lonely"

    else:
        return "I understand. Would you like to talk more about how you're feeling?", "Neutral"

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    
    user_message = request.json["message"]
    
    bot_reply, mood = get_response(user_message)

    return jsonify({
    "reply": bot_reply,
    "mood": mood
    })


if __name__ == "__main__":
    app.run(debug=True)