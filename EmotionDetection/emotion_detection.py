import requests, json

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    request_body = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=request_body, headers=header)
    json_response = json.loads(response.text)
    final_response = json_response
    if response.status_code == 200:
        try:
            final_response = json_response["emotionPredictions"]
            emotion_data = final_response[0]['emotion']
            dominant_emotion = max(emotion_data, key=emotion_data.get)
            emotion_data["dominant_emotion"] = dominant_emotion
            final_response = emotion_data
        except Exception as e:
            print("Invalid response")
            print(e)
    elif response.status_code == 400:
        final_response = {"anger" : None, "disgust": None, "fear": None, "joy": None, "sadness":None, "dominant_emotion": None}
    else:
        final_response = {"anger" : "", "disgust": "", "fear": "", "joy": "", "sadness":"", "dominant_emotion": ""}
    return final_response