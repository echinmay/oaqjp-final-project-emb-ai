import requests
import json
    
def process_response(rsp_j):
    result = {} # Result to return
    emotion_d = {} # Place holder dict to hold the emotion values returned in the response

    for d in rsp_j['emotionPredictions']:
        if 'emotion' in d:
            emotion_d = d['emotion']
            break
    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    # Lets populate the result dict
    [result[k] = emotion_d.get(k, 0,0) for k in emotions]
    result['dominant_emotion'] = max(result, key=result.get, default='unknown')
    return result

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(URL, headers=Headers, json=Input)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        rsp_j = response.json()
        result = process_response(rsp_j)
        return result
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


