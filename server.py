from flask import Flask, render_template,request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    print(text_to_analyze)
    emotion_response = emotion_detector("I hate job")
    return "For the given statement, the system response is good"

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)