import speech_recognition as sr
import pygame
recognizer = sr.Recognizer()
def listen_input(recognizer, source):
    result_string = ''
    recognizer.dynamic_energy_threshold = False
    recognizer.adjust_for_ambient_noise(source)
    print('Listening for inputs')
    try:
        #listening to the voice input
        audio = recognizer.listen(source, timeout=5)
        result_string = recognizer.recognize_google(audio, language="vi-VN")
    except Exception as e:
        print(e)
    return result_string
musiclist = ["/home/pi/project/smart_mirror/smart-mirror/src/voice_recognition/AlanWalker_Faded.mp3","./music2.mp3"]
index = 0
with sr.Microphone() as source:
    while(True):
        result_string = listen_input(recognizer, source)
        if ("nhạc" in result_string) or ("music" in result_string):
            pygame.mixer.init()
            pygame.mixer.music.load(musiclist[index])
            pygame.mixer.music.play()
        if ("dừng" in result_string) or ("stop" in result_string):
            pygame.mixer.music.pause()
        if "tiếp theo" in result_string and index < len(musiclist) - 1:
            index = index + 1
            pygame.mixer.init()
            pygame.mixer.music.load(musiclist[index])
            pygame.mixer.music.play()
        if "lùi lại" in result_string and index > 0:
            index = index - 1
            pygame.mixer.init()
            pygame.mixer.music.load(musiclist[index])
            pygame.mixer.music.play()