import speech_recognition as sr
from playsound import playsound
recognizer = sr.Recognizer()
def listen_input(recognizer, source):
    result_string = ''
    recognizer.dynamic_energy_threshold = False
    recognizer.adjust_for_ambient_noise(source)
    print('Listening for inputs')
    try:
        #listening to the voice input
        audio = recognizer.listen(source, timeout=2)
        result_string = recognizer.recognize_google(audio, language="vi-VN")
    except Exception as e:
        print(e)
    return result_string
with sr.Microphone() as source:
    while(True):
        result_string = listen_input(recognizer, source)
        if "nhạc" in result_string:
            playsound('./music.mp3')