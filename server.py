from flask import Flask, make_response, jsonify
from EmotionDetection import emotion_detector

app = Flask("Emotion Dection")

@app.route("/emotionDetector/<string:text_to_analyze")
def emotion_detector(text_to_analyze):
    emotion_response = emotion_detector(text_to_analyze)
    return "For the given statement, the system response is "

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)