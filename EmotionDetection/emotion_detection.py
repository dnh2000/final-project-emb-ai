import json
import requests 

def emotion_detector(text_to_analyze):
    ''' Analyzes response text and detects dominant emotion using IBM Watson Emotion Detection API 
    '''
    emotions = {}
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input = { "raw_document": { "text": text_to_analyze } } 
    response = requests.post(URL, json = Input, headers=Headers, timeout=5)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        anger = emotions['anger']
        disgust = emotions['disgust']
        joy = emotions['joy']
        fear = emotions['fear']
        sadness = emotions['sadness']
        dominant_emotion = max(emotions, key=emotions.get)
    elif response.status_code == 400:
        anger = None
        disgust = None
        joy = None
        fear = None
        sadness = None
        dominant_emotion = None
    return { 
        'anger': anger,
        'disgust': disgust,
        'joy': joy,
        'fear': fear,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
        }
