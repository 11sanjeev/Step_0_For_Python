import speech_recognition as sr
from selenium import webdriver

class voice:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.listenOnMic()

    def listenOnMic(self):
        while True:
            try:
                with sr.Microphone() as source:
                    audio = self.recognizer.listen(source)
                    command = self.recognizer.recognize_google(audio).lower()
                    if "search" in command:
                        driver = webdriver.Chrome()
                        driver.get(f"https://www.google.com/search?channel=trow2&client=firefox-b-d&q={command.split('search ')[-1]}")
            except sr.UnknownValueError:
                pass

listener = voice()
                