''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package :
# Import the sentiment_analyzer function from the package created:

from  flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze') 
    if text_to_analyze == "":
        return "Empty textfield. Please enter the text to be analyzed."
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)