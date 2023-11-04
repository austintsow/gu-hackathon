import speech_recognition as sr

recognizer = sr.Recognizer()

source = sr.Microphone()

with source as source:
    print("start speaking")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)


try:
    text = recognizer.recognize_google(audio)
    text = text.lower()
    print(f"you said: {text}")
except sr.UnknownValueError:
    print("unable to understand audio")
except sr.RequestError as e:
    print("could not request reuslts...")
