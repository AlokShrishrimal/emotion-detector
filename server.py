@app.route("/emotionDetector")
def emotion():
    text_to_analyze = request.args.get("textToAnalyze")

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text_to_analyze)
    return str(result)
