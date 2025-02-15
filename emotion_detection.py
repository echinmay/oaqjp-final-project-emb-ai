import requests
import json

def process_response(rsp_j):
    result = {} # The return dict after parsing the response
    emotion_d = {} # Dict containing the emotion values
    for d in rsp_j['emotionPredictions']:
        if 'emotion' in d:
            emotion_d = d
            break
    allemotions = ['']
    

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(URL, headers=Headers, json=Input)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        rsp_j = response.json()

        return response.text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


