from flask import Flask, render_template,request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze")
    emotion_response = emotion_detector(text_to_analyze)
    if emotion_response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    else:
        return f"""For the given statement, the system response is
        'anger': {emotion_response["anger"]}, 'disgust': {emotion_response["disgust"]},
        'fear': {emotion_response["fear"]}, 'joy': {emotion_response["joy"]},
        'sadness': {emotion_response["sadness"]}.  The dominant emotion is {emotion_response["dominant_emotion"]}.
        """

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
