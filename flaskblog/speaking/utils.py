# IT17158350
from flaskblog.models import Speaking, Speakinganswer
from flask_login import current_user
from datetime import datetime, timedelta
import sqlite3
from PIL import Image
from gtts import gTTS
import secrets
import os
import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io import wavfile
import pyaudio
import speech_recognition as sr
import wavio
import pyttsx3

# see this is the


def Someaudio(form_audio):
    mytext = form_audio
    language = 'en'
    os.chdir('/Users/Bevan/Desktop/New folder (3)/flask/flaskblog/static/audio')
    print(os.listdir())
    engine = pyttsx3.init()
    engine.save_to_file(mytext, 'welcome.mp3')
    engine.runAndWait()

    for f in os.listdir():
        file_name, file_ext = os.path.splitext(f)
        random_hex = secrets.token_hex(8)
        new_name = '{}{}'.format(random_hex, file_ext)
        if(file_name == 'welcome'):
            os.rename(f, new_name)
            return new_name


def record(seconds):
    count = 0
    fs = 44100  # sample rate
    random_file_name = secrets.token_hex(8)
    myrecoding = sd.rec(int(seconds*fs), samplerate=fs, channels=2)
    sd.wait()
    os.chdir('/Users/Bevan/Desktop/New folder (3)/flask/flaskblog/static/')
    wavio.write('data/' + random_file_name +
                '.wav', myrecoding, fs, sampwidth=2)
    count = count+1
    r = sr.Recognizer()
    os.chdir('/Users/Bevan/Desktop/New folder (3)/flask/flaskblog/static/')
    file = sr.AudioFile('data/' + random_file_name + '.wav')

    with file as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio, language='en')
        print(text)
        marks = text
    except sr.UnknownValueError:
        marks = 'none'
        os.chdir(
            '/Users/Bevan/Desktop/New folder (3)/flask/flaskblog/static/data/')
        os.remove(random_file_name + '.wav')
    return marks


# def add(file_name, id, speaking_id, answer):
#     print(answer)
#     speaks = Speakinganswer.query.all()
#     grammar = get_grammar_result(file_name)
#     bonn = sqlite3.connect(
#         'C:\\Users\\Bevan\\Desktop\\New folder (3)\\myflaskapp\\flaskblog\\site.db')
#     b = bonn.cursor()
#     if (file_name != 'none' and answer == "answer03"):
#         b.execute("""UPDATE Speakinganswer SET answer03 = :answer01, answer04 = :answer04, date_posted = :date_posted
#                   WHERE id = :id AND pid = :pid AND user_id = :user_id """,
#                   {'answer01': file_name, 'answer04': grammar, 'id': speaks[-1].id, 'pid': speaking_id, 'user_id': current_user.id, 'date_posted': datetime.now()})
#         bonn.commit()
#     bonn.close()
#     return ("file_name + 1 + speaking_id ")
