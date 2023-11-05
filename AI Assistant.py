import speech_recognition as sr
import pyttsx3

import os
from dotenv import load_dotenv
load_dotenv
OPENAI_KEY = os.getenv('OPENAI_KEY')

import openai
openai.api_key = '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'

def SpeakText(command):

    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

r = sr.Recognizer()

def record_text():
    while(1):
        try:
            with sr.Microphone() as source2:

                r.adjust_for_ambient_noise(source2, duration = 0.2)

                print("I'm listening")

                audio2 = r.listen(source2)

                MyText = r.recognize_google(audio2)

                return MyText
            

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("Unknown Error Occured")

def send_to_chatGPT(messages, model = "gpt-3.5-turbo"):

    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        max_tokens = 100,
        n = 1,
        stop = None,
        temperature = 0.5,
    )

    message = response.choice[0].message.content
    messages.append(response.choices[0].message)
    return message


messages = [{"role": "user", "content": "Please Act like Jarvis from Iron Man"}]

#pip3 install python-dotenv (possibly)
#pip3 install pyttsx3
#pip3 install openai
#messages = []

while(1):
    text = record_text()
    messages.append({"role": "user", "content": text})
    response = send_to_chatGPT(messages)
    SpeakText(response)

    print(response)