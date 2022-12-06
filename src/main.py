from glob import glob
import time
from tkinter import Button
from unittest import case
from forcastIO.forecastIO import Weather
from location.location import UserLocation
from newspaper.NewsFetcher import NewsFetcher
from gui import window
from voice_recognition.music_control import listen_input

import speech_recognition as sr
import pygame
recognizer = sr.Recognizer()

location_flag = False
weather_flag = False
news_flag = False
init_flag = False

window = window

def init_state():
    print(1)


    global location
    location = UserLocation()
    location.get_location()

    global location_flag
    location_flag = True

    global weather 
    lat = location.get_user_lat()
    long = location.get_user_long()
    weather = Weather(lat, long)
    # weather.create_fio()
    
    global news
    news = "Brazil dismantle South Korea to dance into quarter-finals"

    global init_flag 
    init_flag = True

def fetch_data():
    print(2)

    global weather
    # weather.get_current_weatherforecast()
    weather.humidity = 66
    weather.temperature = 30
    global weather_flag 
    weather_flag = True

    global news
    # news.FetchFromBBC()
    news = "Brazil dismantle South Korea to dance into quarter-finals"
    global news_flag
    news_flag = True

def display_data():
    global current_state
    global display_counter
    if display_counter < 10:
        window.update_idletasks()
        window.update()
        time.sleep(1)
        display_counter += 1
    else:
        window.quit()
    with sr.Microphone() as source:
        global result_string 
        result_string = listen_input(recognizer, source)
        if(result_string!=""):
            global voice_received
            voice_received = True


def process_voice():
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
    pass
    pass

def execute_command():
    global result_string


def switch(state):
    return switcher.get(state)()

switcher = {
    1: init_state,
    2: fetch_data,
    3: display_data,
    4: process_voice,
    5: execute_command,
    }

display_counter = 0
def increase_counter():
    global display_counter
    display_counter+=1

def switch_state():
    global location_flag
    global weather_flag
    global news_flag
    global current_state
    global display_counter
    global voice_received
    if init_flag is True and weather_flag is False:
        current_state = 2
    elif location_flag is True and weather_flag is True and news_flag is True and display_counter < 10:
        current_state = 3
    elif display_counter >= 10 and not voice_received:
        weather_flag = False
        news_flag = False
        display_counter = 0
        current_state = 2
    elif voice_received:
        current_state = 4
    


    print(display_counter)
    print(current_state)

def run_state():
    global location_flag
    global weather_flag
    global news_flag
    global current_state
    global display_counter
    if current_state == 1:
        switch(1)
    elif current_state == 2:
        switch(2)
    elif current_state == 3:
        switch(3)
    elif current_state == 4:
        switch(4)
    elif current_state == 5:
        switch(5)

def main_program():
    # location = UserLocation()
    # location.get_location()
    # print(location.get_user_long())
    # print('---')
    # print(location.get_user_lat())
    # lat = location.get_user_lat()
    # long = location.get_user_long()
    # weather = Weather(lat, long)
    # weather.get_current_weatherforecast()
    while True:
        switch_state()
        run_state()

        


current_state=1
switch(state=1)
main_program()