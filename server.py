from flask import Flask, request
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion():
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    return str(result)

@app.route("/")
def home():
    return "Emotion Detector Application"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
