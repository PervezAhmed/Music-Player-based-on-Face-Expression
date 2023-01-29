# Dataset : https://www.kaggle.com/aadityasinghal/facial-expression-dataset

from tensorflow.keras.models import model_from_json
import cv2
import numpy as np
import eel
import os
import subprocess
from playsound import playsound
import random

#path of songs folder of each expresion
folderspath=["D:\Project\Emotion_Based_Music_Player\WD_INNOVATIVE\songs\Angry","D:\Project\Emotion_Based_Music_Player\WD_INNOVATIVE\songs\Happy","D:\Project\Emotion_Based_Music_Player\WD_INNOVATIVE\songs\Sad","D:\Project\Emotion_Based_Music_Player\WD_INNOVATIVE\songs\\Neutral"]


class FacialExpressionModel(object):
    EMOTIONS_LIST = ["Angry", "Disgust",
                    "Fear", "Happy",
                    "Neutral", "Sad",
                    "Surprise"]
    def __init__(self, model_json_file, model_weights_file):
        # load model from JSON file
        with open(model_json_file, "r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)
        # load weights into the new model
        self.loaded_model.load_weights(model_weights_file)
        self.loaded_model.make_predict_function()
    def predict_emotion(self, img):
        self.preds = self.loaded_model.predict(img)
        return FacialExpressionModel.EMOTIONS_LIST[np.argmax(self.preds)]

facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = FacialExpressionModel("model.json", "model_weights.h5")
font = cv2.FONT_HERSHEY_SIMPLEX

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    # returns camera frames along with bounding boxes and predictions
    def get_frame(self):
        _, fr = self.video.read()
        gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        faces = facec.detectMultiScale(gray_fr, 1.3, 5)
        for (x, y, w, h) in faces:
            fc = gray_fr[y:y+h, x:x+w]
            roi = cv2.resize(fc, (48, 48))
            global pred
            pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])
            cv2.putText(fr, pred, (x, y), font, 1, (255, 255, 0), 2)
            cv2.rectangle(fr,(x,y),(x+w,y+h),(255,0,0),2)
        return fr

def gen(camera):
    while True:
        frame = camera.get_frame()
        cv2.imshow('Facial Expression Recognization',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    
camera = VideoCamera()

@eel.expose
def geti():
    gen(camera)
    global i
    i=3
    if pred == "Angry":
        i=0
    elif pred == "Happy":
        i=1
    elif pred == "Sad":
        i=2
    elif pred == "Neutral":
        i=3
    return i


@eel.expose
def playMusic():
    music_dir = folderspath[i]
    songs = os.listdir(music_dir)
    playsong = os.path.join(music_dir,random.choice(songs))
    # os.startfile(playsong)
    songpath = playsong.split('\\')
    songname = songpath[len(songpath)-1]
    print(songname.split('.')[0])
    return songname.split('.')[0]

eel.init('WD_INNOVATIVE')


eel.start('webpage.html')




