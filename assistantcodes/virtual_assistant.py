# libraries intalled
# pyaudio,SpeechRecognition,gTTS,wikipedia,pygame,pepwin,bs4,selenium,smtplb,request,socket

import speech_recognition as sr
import os,sys
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import time
import socket
from pygame import mixer
# os.system('cls')
mixer.init()
# Ignore Warnings
warnings.filterwarnings('ignore')


def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 80))
        return True
    except OSError:
        pass
    return False

# function that listens the to user Command and and converts it into text
def listen_speech():
    r=sr.Recognizer() #recogniser Object
    # activate mic
    with sr.Microphone() as source:
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.record(source,duration=6)
    # user Google SR
    data=''
    try:
        print('here')
        data=r.recognize_google(audio)
        print('Text: '+data)
    except sr.UnknownValueError:
        print('Google Cannot Understand')
    except sr.RequestError as e:
        print('print request results from gsr api')
    return data

# function that converts the computed result into speech and plays to user
def talk(text):
    print(text)
    # convert text to speech
    obj=gTTS(text=text, lang='en-uk', slow=False)
    t_stamp=datetime.datetime.now().strftime('%d%m%Y%H%M%S')
    nm="%s.mp3" % os.path.join('responses','assistant'+t_stamp)
    obj.save(nm)
    mixer.music.load(nm)
    mixer.music.play()
    # print('talk')
    # os.system('start assistant_response.mp3')
# command to Wake the Assistant
def wakeWord(text):
    WAKE_WORDS=['hey computer','okay computer','hay computer','ok computer','wassup computer']
    text=text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    return False

# simple function to get the date and time
def getDate():
    now=datetime.datetime.now()
    dt=datetime.datetime.today()
    weekday=calendar.day_name[dt.weekday()]
    monthnum=now.month
    dayNum=now.day
    monthsName=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    return 'Today is {} {} the {}th.'.format(weekday,monthsName[monthnum-1],dayNum)

# Random Greeting
def RandomGreeting(text):
    GREETS=['hi','hola','wassup','hey','hay','ok']
    GREETS_RESPONSE=['hi boss','hello cross']
    for word in text.split():
        if word.lower() in GREETS:
            return random.choice(GREETS_RESPONSE)+'.'
    return ''

# searching wikipedia for querries
def getData(text):
    wordList=text.split()
    i=0
    while wordList[i] not in ['who','what']:
        i+=1
    return wordList[i+2]+' '+wordList[i+3]

# Driver Code
if __name__=='__main__' and is_connected():
    while True:
        print('Say Something')
        text=listen_speech()
        response=''
        if wakeWord(text) is True:
            print('triggered')
            response+=RandomGreeting(text)
            if 'date' in text:
                get_date=getDate()
                response+=' '+get_date

            if 'time' in text:
                now=datetime.datetime.now()
                mer=''
                if now.hour >=12:
                    mer='p.m'
                    hour=now.hour-12
                else:
                    mer='a.m'
                    hour=now.hour
                if now.minute <10:
                    minute='0'+str(now.minute)
                else:
                    minute=str(now.minute)
                response+=' '+'it is {}:{} {}.'.format(hour,minute,mer)

            if 'who is' in text or 'what is' in text:
                data=getData(text)
                print(data)
                wiki=wikipedia.summary(data,sentences=2)
                response+=' '+wiki
            talk(response)
            time.sleep(len(response.split())//2+1)

        if 'thank you' in text or 'bye' in text:
            response += ' ' + 'ok ask me whenever needed'
            talk(response)
            time.sleep(3)
            break
else:
    print('No Internet')