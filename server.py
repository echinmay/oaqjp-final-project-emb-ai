from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """Render the index.html file."""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """
    Flask API endpoint to analyze emotions in text.
    Expects JSON input: {"text": "some text"}
    Returns: JSON response with emotion analysis.
    """
    data = request.get_json()
    
    if not data or "text" not in data:
        return jsonify({"error": "Invalid input. Expected JSON: {'text': 'some text'}"}), 400
    
    text_to_analyze = data["text"]
    result = emotion_detector(text_to_analyze)  # Call emotion detection function
    if 'dominant_emotion' not in result or result["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)